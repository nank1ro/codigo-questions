지금까지 작성한 모든 Dart 코드는 **isolate** 안에서 실행됩니다. isolate는 자신만의 메모리와 자신만의 이벤트 루프를 가진 스레드입니다. 프로그램은 하나의 isolate, 즉 *main* isolate로 시작하며, 더 많은 isolate를 시작할 수 있습니다.

isolate를 특별하게 만드는 것은 서로 **아무것도** 공유하지 않는다는 점입니다. 두 isolate는 같은 객체를 결코 보지 못하므로 락도, 데이터 경쟁도, 절반만 갱신된 값도 없습니다. isolate들은 **복사본**인 메시지를 주고받는 방식으로만 서로 통신합니다.

두 번째 isolate를 사용하는 가장 짧은 방법은 **`Isolate.run`**입니다. 함수를 받아 완전히 새로운 isolate에서 실행하고, 그 결과를 담은 `Future`를 돌려줍니다:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate`는 `dart:isolate` 라이브러리에 있으므로 파일은 `import 'dart:isolate';`로 시작해야 합니다. 새 isolate가 계산하는 동안 main isolate는 자유로운 상태를 유지합니다. 이것이 진짜 **병렬성**입니다. 작업이 다른 프로세서 코어에서 일어납니다.

---

`Isolate.run`에 넘기는 함수는 주변의 변수를 **캡처**할 수 있습니다. 그 값들은 함수와 함께 새 isolate로 복사되므로, 계산이 호출자에 의존할 수 있습니다:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run`은 함수가 반환하는 값의 `Future`를 반환하므로 `triple`은 단순히 그것을 반환할 수 있습니다. future를 그대로 전달하기만 할 때는 `async`도 `await`도 필요하지 않습니다.

작업을 다른 isolate로 옮기는 요점은 긴 계산이 더 이상 main isolate를 얼려 먹지 않게 하는 것입니다. 1초 동안 도는 루프는 main isolate에서 실행되면 모든 것을 막지만, `Isolate.run` 안에서는 다른 곳에서 실행되므로 main isolate는 자신의 이벤트를 계속 처리합니다.

---

isolate 사이에서 복사되는 것은 **데이터**뿐이며, **코드**는 복사되지 않습니다. 프로그램의 모든 isolate는 이미 그 프로그램의 모든 최상위 함수와 클래스를 볼 수 있으므로, `Isolate.run`에 주어진 계산은 그것들을 자유롭게 호출할 수 있습니다:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

이동하는 것은 들어가는 길에 캡처된 `text`와 나오는 길에 결과인 `int`이며, 각각은 복사본입니다. 패턴은 항상 같습니다. 무거운 함수는 제자리에 두고 **호출**을 `Isolate.run`으로 감쌉니다.

---

`await`와 `Isolate.run`은 서로 다른 두 문제를 해결하며, 둘을 구분해 두는 것이 좋습니다.

`await`는 하나의 isolate 위에서 **동시성**을 제공합니다. 한 함수가 타이머나 서버를 기다리는 동안 isolate는 대기 중인 다른 코드를 실행합니다. 같은 순간에 실행되는 것은 아무것도 없고, isolate가 놀고 있는 것을 멈출 뿐입니다. 기다림에 맞는 도구입니다.

`Isolate.run`은 **병렬성**을 제공합니다. 두 번째 프로세서 코어의 두 번째 isolate가 첫 번째와 같은 순간에 자신의 코드를 실행합니다. 계산에 맞는 도구입니다.

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

느린 계산을 `await`하는 것은 전혀 도움이 되지 않습니다. `await bigSum()`은 여전히 현재 isolate에서 `bigSum`을 실행하며 마지막 줄까지 막습니다. 그 작업을 옮기는 것은 두 번째 isolate뿐입니다.

---

`Isolate.run`은 하나의 결과를 위한 지름길입니다. 계속 실행되면서 두 번 이상 결과를 보고하는 isolate를 원한다면, **`Isolate.spawn`**으로 직접 시작하고 답변할 방법을 주어야 합니다.

그 방법은 한 쌍의 포트입니다. **`ReceivePort`**는 우편함입니다. 여러분 쪽에서 만들고 도착하는 메시지를 읽습니다. 그것의 **`sendPort`**는 그 우편함의 주소이며, 다른 isolate가 답장하기 위해 필요한 유일한 것입니다.

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn`은 실행할 함수와 그 함수에 전달할 단 하나의 메시지를 받습니다. 여기서는 `SendPort`입니다. 반대쪽에서는 `send`가 값을 우편함에 넣고, `await receivePort.first`는 첫 번째 메시지를 기다린 뒤 포트를 닫습니다.

---

`Isolate.spawn`에 주어지는 함수는 **진입점**이라고 부릅니다. 정확히 하나의 매개변수, 즉 `Isolate.spawn`이 전달하는 메시지를 받는 최상위(또는 static) 함수여야 합니다.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

`ReceivePort`에 도착하는 메시지는 어떤 값이든 보내졌을 수 있으므로 static 타입이 `dynamic`입니다. 다른 isolate가 무엇을 보내는지 알 때는 캐스팅하세요:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

생성된 isolate는 항상 같은 네 단계를 따릅니다. 우편함을 열고, 주소와 함께 워커를 생성하고, 답을 기다리고, 그것을 사용합니다.

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

`Isolate.spawn` 앞의 `await`는 isolate가 작업을 끝내기를 기다리는 것이 아니라 *시작*되기를 기다립니다. 결과는 나중에 포트를 통해 도착합니다.

---

`Isolate.spawn`은 진입점에 정확히 **하나의** 메시지를 전달하며, 워커는 보통 답장할 `SendPort`와 작업할 데이터 둘 다 필요로 합니다. 흔한 요령은 모든 것을 하나의 `List`로 묶어 반대쪽에서 풀어내는 것입니다:

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

리스트는 들어가는 길에 복사되므로 워커는 자신만의 값을 읽습니다. `SendPort`는 복사되지 않고 공유되는 몇 안 되는 것 중 하나입니다. 자신을 만든 isolate의 우편함을 계속 가리키며, 바로 그 이유로 반송 주소로 쓸 수 있습니다.

---

`first`는 하나의 메시지를 읽고 우편함을 닫습니다. `ReceivePort`는 **`Stream`**이기도 하므로, 많은 메시지를 읽으려면 `await for`로 반복합니다.

루프는 스스로 끝나지 않습니다. 포트는 절대 오지 않을 수도 있는 메시지를 기다리며 열려 있습니다. 그래서 워커는 신호로 마지막 값, 보통 `null`을 보내고, 리스너는 **`close()`**를 호출해 반응합니다. 이것이 스트림과 루프를 끝냅니다:

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

일련의 메시지 전체를 모으는 것은 하나의 레시피를 따릅니다. 루프 전에 빈 리스트를 만들고, 진짜 메시지마다 한 번 `add`하고, 스트림을 끝내는 신호에서 `close()`를 호출합니다. 포트가 닫히면 `await for`가 끝나고 함수는 반환할 수 있습니다:

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

메시지는 보내진 순서를 유지하므로, 여러분이 만든 리스트는 다른 isolate의 작업을 단계별로 반영합니다.

---

열려 있는 `ReceivePort`는 대기 중인 작업으로 셉니다. 하나라도 존재하는 한, 그것을 소유한 isolate는 살아 있을 이유가 있고 이벤트 루프는 메시지를 계속 기다립니다. 커맨드 라인 프로그램에서 열린 포트를 가진 main isolate는 그냥 **끝나지 않으며**, 직접 멈춰야 합니다.

따라서 포트를 닫는 것은 최적화가 아니라 작업의 일부입니다:

- `await port.first`는 하나의 메시지 후에 자동으로 닫아 줍니다
- `port.close()`는 명시적으로 닫으며, `await for` 루프 뒤에 필요한 것입니다

`Isolate.run`에는 이런 관리가 전혀 없습니다. 포트를 만들고, 닫고, isolate를 종료하는 것을 여러분 대신 해 줍니다. 하나의 결과만 필요하다면 언제든 이것을 선호하세요.

---

isolate 안에서 던져진 예외는 다른 isolate로 건너갈 수 없습니다. 둘은 별개의 스택을 가집니다. `Isolate.run`은 에러를 잡아 되돌려 보내고 반환된 future를 그 에러로 실패하게 만들어 그 간극을 메워 줍니다. 따라서 여러분 쪽에서는 `await`를 `try`/`catch`로 감싸 잡는 평범한 비동기 에러입니다:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

`try` 안의 `await`는 다른 어떤 future와 마찬가지로 중요합니다. 그것이 없으면 future가 `try` 블록을 미완성인 채로 빠져나가고 `catch`는 절대 실행되지 않습니다.

`Isolate.spawn`에는 이런 다리가 없습니다. 잡히지 않은 에러는 생성된 isolate를 조용히 죽이고 부모는 절대 도착하지 않을 메시지를 계속 기다립니다. 이것이 `Isolate.run`을 먼저 손대는 또 하나의 이유입니다.

---

`Isolate.run`에서 돌아오는 에러는 반대쪽에서 던져진 것의 **복사본**이므로, 평소의 확인 방법이 그대로 동작합니다. `catch (e)`는 객체를 주고, `e is FormatException`은 어떤 종류의 실패였는지 알려 줍니다.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

의존할 수 없는 것은 자신의 isolate를 가리키는 스택 트레이스입니다. 에러는 이동했지만 스택은 그렇지 않습니다.

---

조합해 보면 `Isolate.run` 프로그램은 평범한 순차 코드처럼 읽힙니다. 호출 전의 줄은 main isolate에서 실행되고, 계산은 다른 곳에서 실행되며, `await` 뒤의 줄은 결과를 손에 든 채 main isolate로 돌아와 실행됩니다.

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

isolate는 메모리를 공유하지 않으므로, 모든 메시지는 건너갈 때 **복사**됩니다. 숫자, 불리언, 문자열, `null`, 리스트, 맵과 대부분의 평범한 객체는 그 여정을 갈 수 있습니다. 열린 소켓 같은 몇 가지는 전혀 복사될 수 없으며, 그것을 보내려고 하면 `ArgumentError`가 던져집니다.

그 결과가 isolate를 안전하게 만드는 규칙입니다. 보낸 뒤에는 두 쪽이 **두 개의 독립적인 객체**를 가집니다. 한 isolate가 자신의 복사본에 하는 어떤 일도 다른 쪽에는 보이지 않습니다.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort`는 그 규칙을 증명하는 예외입니다. 원래의 우편함을 계속 가리킬 수 있도록 정확히 그 이유로, 복사되는 것이 아니라 공유됩니다.

---

각 `Isolate.run`은 자신만의 isolate를 시작하므로, 그중 여러 개는 실제로 기계가 가진 코어 수만큼 같은 순간에 실행됩니다. 패턴은 여러분이 future에서 이미 알고 있는 것입니다. 모든 계산을 먼저 시작한 다음, `Future.wait`로 그 전부를 기다립니다. 결과는 입력의 순서를 유지합니다.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

isolate를 시작하는 것은 공짜가 아닙니다. 메모리와 몇 밀리초가 듭니다. 하나의 긴 계산을 몇 개의 isolate에 나누는 것은 값어치가 있지만, 천 개의 사소한 덧셈을 천 개의 isolate에 보내는 것은 그렇지 않습니다.
