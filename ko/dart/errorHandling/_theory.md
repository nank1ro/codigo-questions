실행될 수 없는 문장이 있습니다: 숫자가 아닌 텍스트 읽기, 리스트의 끝을 넘어선 요소 가져오기, 빈 리스트의 첫 번째 항목 요구하기. 그런 일이 일어나면 Dart는 실패를 설명하는 객체를 **던집니다**.

`throw` 키워드로 직접 던질 수도 있습니다. `Exception('message')`는 짧은 설명을 담은 미리 만들어진 객체를 만듭니다:

```dart
throw Exception('no fuel');
```

throw는 `return`이 아닙니다. 그 문장과 함수, 그 위에 있는 모든 호출자를 버리고, 그것을 처리하는 무언가를 찾습니다. 아무것도 찾지 못하면 프로그램이 멈추고 실패를 출력합니다:

```
Unhandled exception:
Exception: no fuel
```

throw 뒤의 모든 것은 건너뛰어지므로, 원래 실행됐을 줄들은 결코 실행되지 않습니다. 이 주제가 다루는 것은 바로 그것입니다: 프로그램을 끝내 버리는 대신 실패를 어디서 처리할지 결정하는 것입니다.

---

프로그램을 살아 있게 유지하려면 위험한 문장을 `try` 블록으로 감싸고, 복구 방법을 `catch` 블록에 적습니다:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

텍스트가 정수를 나타내지 않으면 `int.parse`가 예외를 던집니다. Dart는 던지는 첫 번째 문장에서 `try` 블록을 빠져나와 나머지를 건너뛰고, `catch` 블록을 실행한 뒤, 그 뒤에 오는 코드로 계속 나아갑니다. 괄호 안의 변수, 여기서는 `e`, 던져진 객체 그 자체입니다.

`try` 블록 안에서 일어난 일은 되돌려지지 않으므로, 예상하는 실패만큼만 짧게 유지하세요.

---

맨눈의 `catch`는 모든 것을 받아들이므로, 계획하지 못한 실패까지도 감춰 버립니다. 정확히 한 종류만 처리하려면 `on` 절에 그 타입의 이름을 씁니다:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

텍스트가 정수가 아닐 때 `int.parse`는 **`FormatException`**을 던지므로, 입력을 읽을 때는 그 타입의 이름을 쓰는 것이 맞습니다. `on` 절은 그 타입과 그 하위 타입에만 일치하고 그 외의 것에는 아무것도 일치하지 않습니다: 다른 실패는 계속 바깥쪽으로 전파되어 여전히 모습을 드러내고, 그것을 위한 것이 아니었던 복구에 삼켜지지 않습니다.

---

하나의 `try` 블록 뒤에는 **여러 개의** 절을 둘 수 있고, 각각은 서로 다른 실패에서 복구합니다. Dart는 던져진 객체를 위에서부터 아래로 각 절과 비교하여, 일치하는 **첫 번째** 절을 실행합니다:

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

존재하지 않는 인덱스로 리스트를 읽으면 **`RangeError`**가 던져지므로, 그 한 줄의 두 실패는 서로 다른 답을 받습니다.

첫 번째로 일치한 절이 이기므로 순서가 중요합니다: 더 구체적인 절 위에 일반적인 타입의 절을 놓으면 항상 그것이 이겨서 구체적인 절에는 도달할 수 없게 됩니다. 구체적인 절을 먼저 쓰고, 안전망을 원한다면 맨눈의 `catch`를 마지막에 쓰세요.

위의 `on RangeError` 절은 여러 절을 어떻게 나열하는지 보여 주기 위해서만 있는 것입니다. `RangeError`는 프로그램이 통제할 수 없는 상황이 아니라 코드의 실수를 알리는 것이고, 그런 실패는 잡는 대신 막아야 하는 이유는 뒤의 연습문제에서 설명합니다.

---

복구에 던져진 객체가 전혀 필요 없는 경우가 많습니다: 타입이 이미 모든 것을 말해 주기 때문입니다. 그럴 때는 `catch` 부분을 없애고 `on` 절만 남깁니다:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

두 형태의 차이는 변수를 받느냐의 여부뿐입니다:

- `on FormatException catch (e)` — 그 타입에 일치하고 객체를 `e`로 줍니다
- `on FormatException` — 그 타입에 일치하고, 변수는 없습니다
- `catch (e)` — 모든 것에 일치하고 객체를 줍니다

쓰이지 않는 변수를 생략하면 핸들러가 실제로 사용하는 것에 대해 정직하게 됩니다.

---

핸들러 뒤에 세 번째 블록이 뒤따를 수 있습니다. `finally`는 **어떤 경우에도** 실행됩니다: `try` 블록이 정상적으로 끝난 뒤에도, 핸들러가 복구한 뒤에도, 그리고 아무것도 일치하지 않아 실패가 여전히 바깥쪽으로 전파되는 중에도요.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

`return`이 값을 돌려주기 전에조차 실행되므로, 위의 메시지는 호출자가 결과를 보기 전에 출력됩니다. 그래서 `finally`는 열었던 것을 닫는 등 어느 쪽이든 반드시 일어나야 할 작업의 자리입니다.

---

여러분의 코드도 라이브러리와 똑같은 방식으로 예외를 던집니다. `Exception('message')`는 짧은 설명을 담은 평범한 예외를 만들고, `throw`가 그것을 보냅니다:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

메시지는 사라지지 않습니다: `toString()`은 `Exception`이라는 단어, 콜론, 메시지를 한데 모으는데, 이는 처리되지 않은 예외 보고서가 출력하는 것과 정확히 같습니다.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

던지는 것은 `-1` 같은 만들어 낸 값을 반환하는 것보다 낫습니다: 호출자가 그것을 확인하는 것을 잊을 수 없고, 이유가 그 값과 함께 전달됩니다.

---

때로는 핸들러가 복구하기에 알맞은 자리가 아닙니다: 실패를 *인지*만 하고, 실제로 처리할 수 있는 호출자에게 계속 진행되게 놔두고 싶을 뿐입니다. `catch` 또는 `on ... catch` 블록 안에서 `rethrow` 키워드가 그 역할을 합니다:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow`는 **같은** 객체를 그대로 앞으로 보내므로, 호출자는 원래의 실패를 봅니다. 대신 `throw e`라고 써도 동작은 하지만, 여정을 처음부터 다시 시작하므로 실패가 처음 어디서 일어났는지가 사라집니다.

같은 문장의 `finally` 블록은 나가는 길 위에서라도 여전히 실행됩니다.

---

`catch` 절은 **두 번째** 매개변수도 받습니다:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

첫 번째는 던져진 객체이고, 두 번째는 `StackTrace`입니다: throw가 일어난 순간 실행되고 있던 호출 사슬입니다. 메시지만으로는 알기 어려운 *어디서* 실패가 왔는지를 알려 줍니다.

스택 트레이스는 파일 이름, 줄 번호, 프레임을 나열하며, 빌드와 호출 경로에 따라 달라집니다. 출력하고, 보고서에 붙이고, 전달하세요 — 하지만 고정된 텍스트와 절대 비교하지 말고, 그 내용 위에 프로그램의 동작을 절대 만들지 마세요. 기록할 때에만 요청하세요.

---

`Exception`은 인터페이스이므로 여러분의 클래스도 그것일 수 있습니다. 직접 만든 예외는 `on` 절이 고를 수 있는 이름을 실패에게 주고, 핸들러가 읽을 수 있는 필드를 줍니다:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

세 가지를 갖추면 좋습니다: 클래스가 다른 실패들과 한데 속하게 해 주는 `implements Exception`, 세부 사항을 담는 `final` 필드, 그리고 처리되지 않은 예외 보고서를 읽을 수 있게 해 주는 재정의된 `toString()`. 그 재정의가 없으면 Dart는 클래스 이름만 출력하고 세부 사항은 사라집니다.

---

Dart는 두 부류의 객체를 던지며, 이 둘은 정반대를 의미합니다.

**`Exception`**은 프로그램이 통제할 수 없는 상황을 설명합니다: 숫자가 아니었던 텍스트, 존재하지 않았던 파일, 아무 대답도 하지 않은 네트워크. `FormatException`이 그중 하나입니다. 이것들은 예상되는 것이고, 그것을 잡는 것이 정상적인 대응입니다.

**`Error`**는 코드 그 자체의 실수를 설명합니다:

- `ArgumentError` — 함수가 자신이 유효하지 않다고 문서화한 값으로 호출되었다
- `StateError` — 객체가 요청받은 일을 할 수 없는 순간에 사용되었다
- `RangeError` — 인덱스나 값이 허용 범위를 벗어났다

`Error`를 잡으면 버그를 고치는 대신 감춥니다. 올바른 대답은 그것이 더 이상 던져지지 않도록 코드를 바꾸는 것입니다: 호출하기 전에 인수를 검사하거나, 던지지 않는 API를 사용하세요. 그래서 `on FormatException` 절은 좋은 관행이지만, `on ArgumentError` 절은 거의 항상 그렇지 않습니다.

---

어떤 라이브러리는 아예 예외를 던지지 않는 버전을 제공합니다. `int.parse` 옆에 Dart는 **`int.tryParse`**를 갖고 있습니다: 같은 변환이지만, 텍스트가 숫자가 아닐 때 예외를 던지는 대신 `null`을 반환합니다.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

결과는 `int?`이므로, `??` 연산자가 그것을 곧바로 기본값으로 바꿉니다:

```dart
final port = int.tryParse(text) ?? 8080;
```

실패가 평범한 일이고 폴백만 원한다면, `try` 블록보다 이것이 더 짧고 명확합니다. 나쁜 텍스트가 정말로 위의 누군가가 들어야 할 실패인 경우에는 `int.parse`를 쓰세요.

---

`firstWhere`는 검사에 일치하는 첫 번째 요소를 반환합니다. 아무것도 일치하지 않으면 반환할 요소가 없으므로 `StateError`를 던집니다:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

`int.tryParse`처럼 라이브러리는 출구를 제공합니다. 이름 있는 매개변수 `orElse`는 아무것도 일치하지 않았을 때 쓸 값을 만들어 내는 함수를 받습니다:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

선택은 앞서와 같습니다: "아무것도 일치하지 않음"이 평범한 결과라면 `orElse`, 그것이 데이터가 망가졌다는 뜻이고 누군가 들어야 한다면 맨눈의 호출입니다.

---

`throw`와 `try`가 같은 함수에 있을 필요는 없습니다. 제 할 일을 할 수 없는 함수는 예외를 던지고, 그것에 대해 무엇을 해야 할지 아는 호출자가 잡습니다:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText`에는 나쁜 나이가 프로그램을 끝내야 하는지, 메시지를 보여야 하는지, 건너뛰어야 하는지에 대한 의견이 없습니다 — 그것은 호출자의 결정이고, `try` 블록이 있어야 할 곳도 호출자입니다. 던지는 것이 `-1`을 반환하는 것보다 가치 있는 이유가 바로 이 분리입니다: 실패가 그것에 답할 수 있는 단 한 곳에 도달합니다.

`try` 블록은 첫 번째 실패에서 멈춘다는 것을 기억하세요. 그러므로 실패한 호출 뒤의 문장들도 건너뛰어집니다.

---

`try` 블록이 어디에 놓이는지가 하나의 실패가 파괴하는 작업의 양을 결정합니다. 루프 **바깥**에 있으면 첫 번째 나쁜 요소가 전체 묶음을 끝내지만, 루프 **안**에 있으면 그 요소만 잃고 나머지는 여전히 처리됩니다:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

이것은 파일을 가져오거나, 설정 목록을 읽거나, 메시지 큐를 처리하는 평상시의 모양입니다: 하나의 망가진 행이 좋은 행들을 버리게 해서는 안 됩니다. 규칙은 앞서와 같습니다 — `try` 블록은 실패할 수 있는 문장 주위에, 그보다 크지 않게 유지하세요.

---

마지막 조각은 일부러 `Error`를 던지는 것입니다. 무엇을 받아들이는지 문서화한 함수는 다른 것을 큰 소리로 거부해야 하고, `ArgumentError`가 그 역할의 객체입니다:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

메시지는 `e.message`로 접근할 수 있고, `toString()`은 `Invalid argument(s): ` 뒤에 그것을 붙여 출력합니다.

이것은 앞서의 규칙과 모순되지 않습니다. `ArgumentError`를 던지는 것은 옳고, 그것을 잡는 것은 아닙니다: 그것은 *호출자의* 작성자에게 호출 자체가 잘못되었다고 말해 주는 것이고, 해결은 그 주위의 핸들러가 아니라 호출 전의 검사입니다.
