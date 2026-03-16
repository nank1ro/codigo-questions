**`if` 문**은 조건이 `true`일 때만 코드 블록을 실행합니다.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

중괄호 안의 코드는 조건 `age >= 18`이 `true`로 평가될 때만 실행됩니다.

---

조건이 충족되었을 때 메시지를 표시하기 위해 `if` 블록 안에서 `print()`를 사용할 수 있습니다.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

`isRaining`이 `false`이면 아무것도 출력되지 않습니다.

---

**`if-else` 문**은 조건이 `true`이면 `if` 블록을 실행하고, `false`이면 `else` 블록을 실행합니다.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

두 분기 중 항상 정확히 하나만 실행됩니다.

---

**`else if`**를 사용하면 여러 조건을 순서대로 테스트할 수 있습니다. 조건이 `true`인 첫 번째 분기가 실행되고 나머지는 건너뜁니다.

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

**삼항 연산자** `condition ? expr1 : expr2`는 간단한 `if-else` 표현식을 간결하게 작성하는 방법입니다.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

조건이 `true`이면 `expr1`이 사용되고, 그렇지 않으면 `expr2`가 사용됩니다.
