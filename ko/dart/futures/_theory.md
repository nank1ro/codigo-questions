어떤 작업은 시간이 걸립니다. 파일 읽기, 서버 호출, 타이머 대기 같은 것들입니다. Dart는 그런 작업이 진행되는 동안 프로그램을 멈추지 않습니다. 대신 그런 함수는 **`Future<T>`**를 반환합니다. `T` 타입의 값이 **나중에** 준비된다는 약속입니다.

가장 단순한 future는 이미 값을 가지고 있는 것으로, `Future.value`로 만듭니다:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

future에서 값을 꺼내려면 **`await`**를 사용합니다. `await`는 future가 완료될 때까지 현재 함수를 멈췄다가, 그 뒤에 순수한 값을 돌려줍니다. **`async`**가 붙은 함수 안에서만 쓸 수 있으므로 `main`은 `Future<void> main() async`가 됩니다:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

`await`가 없으면 `n`은 `Future` 자체가 되고, `print(n)`은 숫자 대신 `Instance of 'Future<int>'`를 보여줍니다.

---

함수에 `async`를 붙이면 두 가지 일이 일어납니다. 본문 안에서 `await`를 쓸 수 있게 되고, 함수가 **`Future`를 반환**하게 됩니다. `return`으로 돌려주는 값이 곧 future가 완료되는 값이 되므로, 본문이 순수한 `T`를 반환해도 선언하는 반환 타입은 `Future<T>`입니다:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

여기서는 `Future.value`가 필요 없습니다. `async` 키워드가 반환값을 대신 감싸 줍니다.

---

`Future.value`는 곧바로 완료됩니다. 시간이 걸리는 작업을 흉내 내려면 **`Future.delayed`**를 사용하세요. `Duration`과 함수를 받아 그 시간만큼 기다린 뒤, 함수가 반환한 값으로 완료됩니다:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration`은 `seconds`, `milliseconds`, `minutes` 같은 이름 있는 매개변수로 만듭니다. `async` 함수 안에서는 값 없이 지연만 await 해서 잠시 멈출 수도 있습니다:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

두 방식 모두 흔합니다. 두 번째는 평범한 순차 코드처럼 읽힙니다.

---

future의 두 방향을 머릿속에서 분명히 구분하세요:

- `async` 함수는 `Future<T>`를 **선언**하고 순수한 `T`를 **반환**합니다: 감싸는 일은 자동입니다
- `Future<T>`를 `await` 하는 호출자는 순수한 `T`를 **받습니다**: 벗겨내는 일은 자동입니다

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

`int count() async`라고 쓰면 오류입니다. `async` 함수는 `Future`(또는 `void`) 반환 타입을 선언해야 합니다.

---

future를 쓰는 방법이 `await`만 있는 것은 아닙니다. **`then`**으로 **콜백**을 등록할 수도 있습니다. 넘긴 함수는 future가 완료되면 그 값과 함께 호출됩니다. `await`와 달리 `then`은 현재 함수를 멈추지 **않으므로**, 그 뒤의 코드가 먼저 실행됩니다:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

`Future.value`로 만든 future조차 현재 코드가 끝난 뒤에야 값을 전달합니다. 그래서 `waiting`이 먼저 출력됩니다. `then`은 `async`든 아니든 어떤 함수에서나 동작합니다.

---

`async` 함수 안에서 `await`는 비동기 단계를 평범한 순차 코드처럼 쓸 수 있게 해 줍니다. 각 `await`는 자신의 future를 기다리고, 다음 줄은 값이 준비된 뒤에야 실행됩니다:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await`는 식 안에서 바로 쓸 수도 있습니다. `return await width() * await height();`도 같은 결과를 줍니다.

---

함수가 `await`를 만나면 그 줄에서 **멈추고**, 프로그램의 나머지는 계속 진행됩니다. `await` 뒤의 줄들은 future가 완료된 뒤에야 실행됩니다. 그래서 `async` 함수를 위에서 아래로 읽으면 그 효과가 일어나는 정확한 순서를 알 수 있습니다:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

future는 **오류**로 완료될 수도 있습니다. `async` 함수가 예외를 던지면 예외가 곧바로 빠져나가지 않고, 반환된 future의 오류가 됩니다. 그 future를 `await` 하는 쪽은 `await` 지점에서 오류가 던져진 것으로 보게 되므로, 평범한 `try`/`catch`로 처리할 수 있습니다:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

`try` 안의 `await`가 핵심입니다. `return parseLater(s);`는 future를 **기다리지 않고** 호출자에게 넘겨 버리므로, 오류는 `try` 블록이 이미 끝난 뒤에 도착하고 `catch`는 절대 실행되지 않습니다.

---

오류는 호출 스택이 아니라 future와 함께 이동합니다. 예외를 던지는 `async` 함수를 호출한 것만으로 호출자가 죽는 일은 없습니다. 오류는 반환된 future에 저장되었다가, 그 future를 기다리는 지점에서 나중에 드러납니다. 그래서 `try`/`catch`는 future를 만든 호출이 아니라 **`await`**를 감싸야 합니다.

실패한 future를 아무도 await 하거나 처리하지 않으면, Dart는 *unhandled exception*을 보고하고 명령줄 프로그램에서는 오류로 종료합니다.

---

콜백을 쓸 때 오류는 `then`의 짝인 **`catchError`**가 처리합니다. 둘 다 새로운 future를 반환하므로 보통 이어 붙여서 씁니다. future가 성공하면 `then`이 값을 받고, 실패하면 `catchError`가 오류를 받으며, 두 콜백 중 하나만 실행됩니다:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

`then` 뒤에 놓인 `catchError`는 `then` 콜백 안에서 던져진 오류도 잡습니다. `then`과 마찬가지로 체인 뒤의 코드가 먼저 실행됩니다. 콜백은 현재 코드가 끝난 뒤에야 호출되기 때문입니다.

---

여러 future가 서로 의존하지 않을 때는 모두 **`Future.wait`**에 넘기세요. `List<Future<T>>`를 받아 동시에 실행시키고, **전부** 끝났을 때 완료되는 하나의 `Future<List<T>>`를 반환합니다. 어떤 future가 먼저 끝났는지와 상관없이 결과는 입력 리스트의 순서를 유지합니다:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();`는 `25` 밀리초가 걸립니다. `fast()`가 `slow()`가 완료된 뒤에야 호출되기 때문입니다. `await Future.wait([slow(), fast()])`는 가장 긴 쪽의 시간인 약 `20` 밀리초가 걸립니다.

---

`Future.wait`는 "여러 개를 불러온 다음 계속하기"를 위한 도구입니다. 전형적인 형태는 future 리스트를 만들고, 거기에 `await Future.wait`를 적용한 뒤, 나온 리스트를 사용하는 것입니다:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()`가 먼저 완료되지만, 리스트는 여전히 호출 순서를 따릅니다. `stock()`이 첫 번째, `orders()`가 두 번째입니다.

---

두 future를 동시에 실행하는 데 `Future.wait`가 꼭 필요한 것은 아닙니다. `async` 함수는 **호출되는** 순간부터 첫 `await`까지 실행되기 시작합니다. 돌려받는 future는 이미 진행 중인 작업입니다. 그래서 요령은 **먼저 호출하고, 나중에 await 하기**입니다:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

`return await words() / await pages();`와 비교해 보세요. 여기서는 `pages()`가 `words()`가 완료된 뒤에야 호출됩니다. 결과는 같지만 시간은 두 배입니다. 두 번째 호출이 첫 번째의 결과를 필요로 하지 않는다면 언제나 동시 실행 형태를 택하세요.

---

오류는 그것을 잡지 않는 모든 `await`를 거쳐 **전파**됩니다. `load()`가 실패하면 `loadTwice()` 안의 `await load()`가 예외를 던지고, `loadTwice`에는 `try`/`catch`가 없으므로 그 future도 같은 오류로 실패합니다. 이런 식으로 어떤 `await`가 `try`/`catch`로 감싸질 때까지 사슬을 따라 올라갑니다:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

이는 동기 호출에서 예외가 전파되는 방식과 같습니다. 무엇을 해야 할지 아는 계층에서 한 번만 처리하면 됩니다.

---

`Future.wait`도 같은 규칙을 따릅니다. future 중 **하나라도** 실패하면 합쳐진 future는 그 오류로 완료되고 `await Future.wait(...)`는 예외를 던집니다. 성공한 값들만 담긴 부분 리스트를 받는 일은 결코 없습니다. 나머지를 살리려면 `Future.wait`에 넘기기 전에 각 future 안에서 오류를 처리하세요. 예를 들어 `catchError`를 사용합니다.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

`await`가 future의 오류를 평범한 예외로 바꿔 주기 때문에, 재시도 루프를 포함한 익숙한 `try`/`catch` 패턴이 모두 비동기 코드에도 그대로 적용됩니다. `catch` 블록 안에서 **`rethrow`**는 같은 오류를 다시 던지며, 마지막 시도 뒤에 포기하는 방법이 바로 이것입니다:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

`Future<String> Function() task` 같은 함수 타입 매개변수는 future가 아니라 **함수** 자체를 받습니다. `task()`를 호출할 때마다 새로운 시도가 시작됩니다.
