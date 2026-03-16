`for` 반복문은 코드 블록을 정해진 횟수만큼 반복합니다. 기본 구문은 다음과 같습니다:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: 반복문이 시작되기 전에 한 번 실행됩니다 (예: `int i = 0`)

**condition**: 각 반복 전에 확인됩니다. 거짓이 되면 반복문이 멈춥니다

**update**: 각 반복 후에 실행됩니다 (예: `i++`)

---

현재 카운트를 추적하기 위해 반복문 본체 안에서 반복 변수를 사용할 수 있습니다. 예를 들어, 합계를 누적하는 경우:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

반복문 후에 `total`은 15가 됩니다.

---

`for` 반복문은 감소 연산자(`i--`)와 `>=` 조건을 사용하여 **아래로** 카운트할 수 있습니다:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

이것은 카운트다운이나 역순 반복에 유용합니다.

---

`for-in` 반복문은 인덱스 없이 컬렉션의 모든 요소를 반복 처리합니다:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

각 반복에서 다음 요소가 반복 변수（여기서는 `fruit`）에 할당됩니다.

---

`break` 문은 조건이 충족되면 즉시 반복문을 종료합니다:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

이것은 값을 검색할 때 찾으면 즉시 멈추고 싶은 경우에 유용합니다.
