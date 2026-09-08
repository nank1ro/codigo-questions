**String**(문자열)은 인용부호로 둘러싸인 문자의 나열, 즉 텍스트 조각입니다. Dart에서는 작은따옴표 `'...'`나 큰따옴표 `"..."`를 사용할 수 있으며, 둘은 완전히 동일하게 동작합니다:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

한쪽 종류의 따옴표를 선택하면, 이스케이프 없이 텍스트 안에서 다른 종류의 따옴표를 사용할 수 있습니다:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

내부에서 같은 따옴표가 필요하다면, 백슬래시로 이스케이프하세요: `'It\'s sunny'`.

---

두 문자열은 `+` 연산자로 새로운 문자열로 합칠 수 있으며, 이를 **연결**(concatenation)이라고 합니다:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart는 연산자 없이 나란히 작성된 두 문자열 **리터럴**도 이어 붙입니다. 이는 긴 텍스트를 여러 줄로 나눌 때 유용합니다:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

`+`로 연결할 수 있는 것은 문자열끼리뿐입니다. `'Age: ' + 30`은 컴파일 오류가 됩니다. `30`이 `int`이기 때문입니다.

---

문자열을 연결하는 대신, **보간**(interpolation)을 사용해 값을 문자열에 직접 삽입할 수 있습니다. 변수의 값을 삽입하려면 `$name`을, 임의의 식의 결과를 삽입하려면 `${expression}`을 작성하세요:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

보간은 어떤 타입에도 사용할 수 있습니다. 숫자, 불리언, 리스트는 자동으로 텍스트로 변환되므로, `age`가 `int`라 하더라도 `'Age: $age'`처럼 써도 됩니다.

---

모든 문자열은 `.length` 프로퍼티를 통해 자신이 담고 있는 문자 수를 알고 있습니다. 공백과 문장 부호도 문자로 셉니다:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

대괄호와 `0`부터 시작하는 **인덱스**를 사용해 문자 하나를 읽을 수 있습니다. 결과는 한 글자짜리 `String`입니다:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

문자열 범위를 벗어난 인덱스(예: `word[5]`)를 읽으면 오류가 발생합니다.

---

Dart의 문자열은 **불변**입니다: 한 번 만들어진 문자열은 절대 변경되지 않습니다. `.toUpperCase()`나 `.toLowerCase()` 같은 메서드는 원본 문자열을 수정하지 않고 **새로운 문자열을 반환**합니다:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

변수가 새 값을 갖도록 하려면 결과를 다시 대입하세요: `word = word.toUpperCase();`.

---

사용자가 입력한 텍스트에는 앞뒤로 불필요한 공백이 들어있는 경우가 많습니다. `.trim()` 메서드는 앞뒤 공백(스페이스, 탭, 줄바꿈)을 제거한 사본을 반환합니다. `.trimLeft()`와 `.trimRight()`는 한쪽만 제거합니다:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

`.substring(start, end)` 메서드는 인덱스 `start`부터 인덱스 `end` 직전까지(`end`는 **포함하지 않음**)의 부분 문자열을 반환합니다. `end`를 생략하면 문자열 끝까지 모두 가져옵니다:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

문자열 안을 검색할 수 있는 여러 메서드가 있습니다:

- `.contains(other)`는 `other`가 문자열 어디든 나타나면 `true`를 반환합니다
- `.startsWith(other)`와 `.endsWith(other)`는 시작과 끝을 확인합니다
- `.indexOf(other)`는 처음 나타난 위치의 인덱스를 반환하며, 찾지 못하면 `-1`을 반환합니다

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

이들은 모두 대소문자를 구분합니다. `'Dart'.contains('dart')`는 `false`입니다.

---

`.replaceAll(from, to)` 메서드는 `from`이 나타나는 **모든** 부분을 `to`로 바꾼 새 문자열을 반환합니다. `.replaceFirst(from, to)`는 첫 번째 것만 바꿉니다:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

`.split(separator)` 메서드는 구분자가 나타날 때마다 문자열을 잘라서 `List<String>`으로 만듭니다. 그 반대는 리스트의 메서드인 `.join(separator)`로, 요소들을 하나의 문자열로 이어붙입니다:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

빈 구분자로 `.split('')`을 호출하면 문자 하나하나로 이루어진 리스트를 얻습니다.
