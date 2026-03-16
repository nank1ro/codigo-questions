__불리언__은 `true` 또는 `false` 중 2가지 값만을 가질 수 있는 데이터 타입입니다.
Dart에서 불리언 타입은 `bool` 키워드로 선언합니다.

```dart
bool isRaining = true;
```

변수 `isRaining`은 값 `true`를 저장합니다. 이는 현재 비가 오고 있다는 의미입니다.
불리언 값은 항상 소문자로 작성됩니다: `true`와 `false`.

---

다른 변수처럼 `print()`을 사용하여 불리언 값을 출력할 수 있습니다.
불리언을 출력하면 Dart는 `true` 또는 `false` 텍스트를 출력합니다.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

불리언 변수는 값 `false`도 가질 수 있습니다.
어떤 것이 사실이 아닐 때는 `false`를 사용하세요.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

`true`처럼 `false`도 소문자로 작성되어야 합니다.

---

__부정 연산자__ `!`는 ("not"이라고도 함) 불리언 값을 반대로 뒤집습니다.
`true`에 `!`를 적용하면 `false`가 되고, `false`에 `!`를 적용하면 `true`가 됩니다.

```dart
bool isActive = true;
print(!isActive); // false
```

이는 조건의 반대를 확인하고 싶을 때 유용합니다.

---

불리언은 프로그래밍 전반에서 조건을 나타내고 결정을 주도하는 데 사용됩니다.
프로그램이 두 가지 가능성 중에서 선택해야 할 때마다 불리언이 사용됩니다.

예시:
- 사용자가 로그인했나? (`isLoggedIn`)
- 문이 열려 있나? (`isDoorOpen`)
- 주문이 발송되었나? (`isShipped`)
