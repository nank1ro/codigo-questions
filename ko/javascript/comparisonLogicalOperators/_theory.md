**동등** `==` 비교 연산자부터 시작하겠습니다.
이 연산자는 두 표현식이 같은지 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 == 2);
// true 출력
console.log(2 == 3);
// false 출력
```

---

**부등** `!=` 비교 연산자를 계속 살펴보겠습니다.
이 연산자는 두 표현식이 같지 **않은지** 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 != 2);
// false 출력
console.log(2 != 3);
// true 출력
```
이것은 *동등* 연산자와 정확히 반대입니다

---

**초과** `>` 비교 연산자를 계속 살펴보겠습니다.
이 연산자는 하나의 표현식이 다른 표현식보다 큰지 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 > 2);
// false 출력
console.log(3 > 2);
// true 출력
```

---

**미만** `<` 비교 연산자를 계속 살펴보겠습니다.
이 연산자는 하나의 표현식이 다른 표현식보다 작은지 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 < 2);
// false 출력
console.log(2 < 3);
// true 출력
```

---

**이상** `>=` 비교 연산자를 계속 살펴보겠습니다.
이 연산자는 하나의 표현식이 다른 표현식보다 크거나 같은지 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 >= 2);
// true 출력
console.log(3 >= 2);
// true 출력
console.log(3 >= 4);
// false 출력
```

---

**이하** `<=` 비교 연산자를 계속 살펴보겠습니다.
이 연산자는 하나의 표현식이 다른 표현식보다 작거나 같은지 여부를 나타내는 **불리언** (`true` 또는 `false`)을 반환합니다. 예를 들면:
```javascript
console.log(2 <= 2);
// true 출력
console.log(3 <= 2);
// false 출력
console.log(3 <= 4);
// true 출력
```

---

이제 **논리** 연산자를 살펴보겠습니다. 먼저 __AND__ `&&`부터 시작합니다.
이 연산자는 *false*로 평가되는 첫 번째 피연산자를 반환하거나, 모두 *true*이면 마지막 피연산자를 반환합니다.
```javascript
console.log(2 == 2 && 2 == 3);
// false 출력
console.log(1 == 1 && 1 == 1.0);
// true 출력
```

---

**or** `||` 논리 연산자를 계속 살펴보겠습니다.
이 연산자는 *true*로 평가되는 첫 번째 피연산자를 반환하거나, 모두 *false*이면 마지막 피연산자를 반환합니다.
```javascript
console.log(2 == 2 || 2 == 3);
// true 출력
console.log(1 == 2 || 1 == 3);
// false 출력
```

---

마지막으로 **not** `!` 논리 연산자를 살펴보겠습니다.
이 연산자는 표현식의 논리 상태를 반전시킨 불리언을 반환합니다.
```javascript
console.log(!true);
// false 출력
console.log(!false);
// true 출력
console.log(!(2 == 2));
// false 출력
```
