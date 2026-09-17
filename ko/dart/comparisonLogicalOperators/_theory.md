**같음 연산자** `==` 는 두 값을 비교하며 같으면 `true`, 다르면 `false`를 반환합니다.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

비교의 결과는 항상 `bool` 값입니다.

---

**다름 연산자** `!=` 는 두 값이 **다르면** `true`, 같으면 `false`를 반환합니다.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

`==` 의 반대입니다.

---

**보다 큼 연산자** `>` 는 왼쪽 값이 오른쪽 값보다 엄격히 크면 `true`를 반환합니다.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

왼쪽 값이 오른쪽 값 이하이면 `false`를 반환합니다.

---

**보다 작음 연산자** `<` 는 왼쪽 값이 오른쪽 값보다 엄격히 작으면 `true`를 반환합니다.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

왼쪽 값이 오른쪽 값 이상이면 `false`를 반환합니다.

---

**이상 연산자** `>=` 는 왼쪽 값이 오른쪽 값보다 크거나 **같으면** `true`를 반환합니다.

```dart
int score = 50;
bool passed = score >= 50; // true
```

`>` 와는 달리 이 연산자는 두 값이 같을 때도 `true`를 반환합니다.

---

**AND 연산자** `&&` 는 두 개의 부울 식을 결합합니다. **두 쪽 모두** `true`일 때만 `true`를 반환합니다. 어느 한쪽이라도 `false`이면 결과는 `false`입니다.

```dart
bool a = true;
bool b = true;
bool result = a && b; // true

bool c = true;
bool d = false;
bool result2 = c && d; // false
```

---

**OR 연산자** `||` 는 두 개의 부울 식을 결합합니다. **최소한 하나**의 쪽이 `true`일 때 `true`를 반환합니다. **두 쪽 모두** `false`일 때만 `false`를 반환합니다.

```dart
bool a = false;
bool b = true;
bool result = a || b; // true

bool c = false;
bool d = false;
bool result2 = c || d; // false
```
