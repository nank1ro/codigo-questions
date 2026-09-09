`Future`는 나중에 도착하는 **하나의** 값을 나타냅니다. **Stream**은 시간에 걸쳐 도착하는 값들의 **연속**을 나타냅니다. 키 입력, 파일의 조각, 서버에서 오는 메시지 같은 것들이죠. 각 값을 **이벤트**라고 부르며, 마지막 이벤트 이후 스트림은 **완료**됩니다.

스트림을 만드는 가장 간단한 방법은 `Stream.fromIterable`로, 리스트의 모든 요소를 하나씩 차례로 내보냅니다:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

이벤트를 하나씩 소비하려면 **`await for`** 루프를 사용합니다. `await`처럼 `async`로 표시된 함수 안에서만 허용되므로, `main`은 `Future<void> main() async`가 됩니다. 루프 본문은 이벤트마다 한 번씩 실행되고, 스트림이 완료되면 루프가 끝납니다:

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

여기서는 평범한 `for` 루프가 동작하지 않습니다. `Stream`은 `Iterable`이 아니며, 그 값들은 한꺼번에 사용할 수 있는 것이 아니기 때문입니다.

---

`Stream.fromIterable`은 모든 값을 미리 필요로 합니다. 값을 하나씩 **생산**하려면 **비동기 제너레이터**를 작성하세요. 본문이 `async*`로 표시되고 반환 타입이 `Stream<T>`인 함수입니다. 그 안에서 `yield`가 스트림에 이벤트 하나를 보냅니다:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

`countTo(3)`을 호출해도 본문은 실행되지 않습니다. 리스너가 값을 요청하는 대로 지연 실행되며, 본문이 끝나면 스트림은 완료됩니다.

모든 이벤트를 `List`로 모으려면 `toList()`를 호출하세요. 이는 `Future<List<T>>`를 반환하므로 `await`로 기다립니다:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

`await for` 루프는 출력하는 것 이상을 할 수 있습니다. 루프 앞에서 선언한 변수를 갱신할 수 있죠. 스트림을 소비해 결과를 계산하는 함수는 `async`로 표시해야 하며, 그 결과의 `Future`를 반환합니다:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

이 함수는 스트림이 완료된 뒤에야 `return`에 도달하므로, 호출자는 future를 기다릴 때 최종 값을 받습니다:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

모든 스트림은 결국 끝납니다. `async*` 제너레이터의 경우, 함수 본문이 끝나는 순간 스트림은 **완료**됩니다. 끝까지 도달했든 `return`을 만났든 마찬가지입니다. 완료된 스트림에 대한 `await for` 루프는 빠져나오고, `toList()`의 future는 모두 완료됩니다.

스트림은 다시 시작하거나 값을 반복하지 않습니다. 한 번 완료되면 계속 완료된 상태로 남습니다.

---

`await for`는 스트림이 완료될 때까지 현재 함수를 멈춥니다. **기다리지 않고** 이벤트에 반응하고 싶을 때는 `listen`을 호출하고 콜백을 넘기세요. 콜백은 이벤트마다 한 번씩 호출되고, `listen` 다음 코드는 곧바로 실행됩니다.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen`은 이름 있는 매개변수 `onDone`도 받습니다. 스트림이 끝날 때 호출되는, 인자가 없는 함수입니다:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

`async*` 제너레이터는 `yield*`(yield-star)로 **다른 스트림의 모든 이벤트**를 전달할 수 있습니다. 각 값을 yield하는 `await for` 루프를 한 줄로 쓴 것과 같습니다:

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

내부 스트림이 완료되면 바깥 스트림은 자신의 `yield`를 이어갑니다.

---

`Iterable`처럼 `Stream`에도 기존 스트림으로부터 **새 스트림**을 만드는 메서드가 있습니다:

- `map`은 각 이벤트를 변환합니다
- `where`는 조건을 만족하는 이벤트만 남깁니다
- `take`는 주어진 개수의 이벤트 후에 멈춥니다

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

이 메서드들은 **지연 평가**됩니다. 누군가 결과 스트림을 구독하기 전까지는 아무것도 실행되지 않습니다. 체이닝할 수 있고, 원본 스트림은 절대 변경되지 않습니다.

---

`where`, `map`, `take`가 각각 스트림을 반환하므로, 이들을 체이닝하고 마지막에 `toList()`를 붙여 결과를 리스트로 얻을 수 있습니다. `Future`를 반환하는 유일한 호출이 마지막 `toList()`이므로, `await`가 필요한 곳도 거기뿐입니다:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

`toList()` 외에도 스트림에는 모든 이벤트를 **소비**하고 하나의 `Future`를 반환하는 메서드들이 있습니다:

- `first`와 `last`는 첫 번째 또는 마지막 이벤트로 완료됩니다
- `length`는 이벤트 개수로 완료됩니다
- `join(separator)`는 모든 이벤트를 하나의 `String`으로 이어 붙인 값으로 완료됩니다
- `reduce(combine)`은 이벤트를 두 개씩 묶어 하나의 값으로 만듭니다

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce`는 지금까지의 결과와 다음 이벤트를 `combine`에 전달합니다. 스트림이 비어 있으면 예외를 던지므로, 이벤트가 최소 하나 보장될 때만 사용하세요.

---

`Stream`의 메서드는 두 그룹으로 나뉩니다:

- `map`, `where`, `take`, `skip` 같은 **변환** 메서드는 **새 `Stream`**을 반환하며 지연 평가됩니다. 새 스트림을 구독하기 전까지는 어떤 이벤트도 처리되지 않습니다
- `toList`, `reduce`, `join`, `first`, `last`, `length` 같은 **소비** 메서드는 스트림을 구독하고 최종 결과를 담은 **`Future`**를 반환합니다

따라서 체인은 0개 이상의 변환 호출 뒤에 최대 하나의 소비 호출이 오는 모양입니다.

---

제너레이터는 하나의 함수 안에서 이벤트를 만들어 냅니다. 이벤트가 **다른 곳**(버튼, 네트워크 콜백, 다른 객체)에서 올 때는 **`StreamController`**가 필요합니다. 이는 `dart:async` 라이브러리에 있으므로 파일은 `import 'dart:async';`로 시작해야 합니다.

컨트롤러는 스트림을 소유하고, 거기에 이벤트를 밀어 넣게 해 줍니다:

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)`는 이벤트 하나를 보냅니다
- `close()`는 스트림을 끝냅니다. 이를 잊으면 리스너는 영원히 기다립니다
- `stream`은 리스너가 소비하는 `Stream`입니다

아무도 구독하기 전에 추가된 이벤트는 버퍼에 보관되므로 위 코드는 안전합니다. 나중에 도착한 리스너도 `4`와 `2`를 받습니다.

---

`StreamController`는 흔히 같은 자리에서 만들어지고 소비됩니다. `listen`으로 `controller.stream`을 구독한 다음, `add`로 이벤트를 추가하고 `close`로 컨트롤러를 닫습니다. `listen`은 기다리지 않으므로 이벤트는 현재 코드가 끝난 뒤에 전달되지만, 언제나 추가된 순서대로 전달됩니다:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

지금까지 본 스트림은 **단일 구독** 스트림입니다. 리스너를 정확히 하나만 허용하죠. `listen`, `await for` 또는 소비 메서드를 두 번째로 호출하면 `StateError`("Stream has already been listened to")가 던져집니다.

스트림을 여러 리스너가 공유하려면 `asBroadcastStream()`으로 **브로드캐스트** 스트림으로 변환하세요:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

브로드캐스트 스트림은 버퍼링하지 않습니다. 리스너는 구독한 **이후**에 내보내진 이벤트만 받습니다. 예시에서는 두 리스너 모두 첫 `await` 전에 구독하므로, 둘 다 모든 이벤트를 받습니다.

---

컨트롤러는 이름 있는 생성자 `StreamController<T>.broadcast()`로 브로드캐스트 스트림을 바로 만들 수 있습니다. 그 `stream`은 리스너를 몇 개든 받아들이고, 각 이벤트는 구독한 순서대로 그들 모두에게 전달됩니다:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

모든 브로드캐스트 스트림처럼 버퍼링하지 않습니다. 리스너가 구독하기 전에 추가된 이벤트는 그 리스너에게는 사라집니다.

---

스트림은 값뿐 아니라 **오류**도 전달할 수 있습니다. `async*` 제너레이터 안에서 `throw`는 오류 이벤트를 보내고 스트림을 끝냅니다. `StreamController`는 `addError`로 오류를 보낼 수 있습니다.

소비하는 쪽에서는 `await for` 루프가 루프가 있는 자리에서 오류를 다시 던지므로, 루프를 평범한 `try`/`catch`로 감싸 처리합니다:

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

`listen`에서는 대신 `onError` 콜백을 넘기세요: `stream.listen(print, onError: (e) => print('caught: $e'));`
