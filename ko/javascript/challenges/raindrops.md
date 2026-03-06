---
language: javascript
exerciseType: 1
difficulty: 1
title: 빗방울
---

# --description--

숫자를 특정 잠재적 인수에 해당하는 빗방울 소리가 포함된 문자열로 변환하는 것이 과제입니다.
인수는 나머지 없이 다른 숫자를 균등하게 나누는 숫자입니다.
숫자가 다른 숫자의 인수인지 테스트하는 가장 간단한 방법은 나머지 연산을 사용하는 것입니다.
빗방울의 규칙은 다음과 같습니다:

- 3을 인수로 가지면 결과에 'Pling'을 추가합니다.
- 5를 인수로 가지면 결과에 'Plang'을 추가합니다.
- 7을 인수로 가지면 결과에 'Plong'을 추가합니다.
- 3, 5, 7 중 어느 것도 인수로 가지지 않으면 결과는 해당 숫자의 자릿수여야 합니다.

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

- 28은 7을 인수로 가지지만 3이나 5는 아니므로 결과는 `"Plong"`입니다.
- 30은 3과 5를 인수로 가지지만 7은 아니므로 결과는 `"PlingPlang"`입니다.
- 34는 3, 5, 7 중 어느 것의 인수도 아니므로 결과는 `"34"`입니다.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function convert(number) {
  
}
```

# --asserts--

1의 소리는 "1"입니다

```javascript
tryCatch(convert(1) === "1");
```

3의 소리는 "Pling"입니다

```javascript
tryCatch(convert(3) === "Pling");
```

5의 소리는 "Plang"입니다

```javascript
tryCatch(convert(5) === "Plang");
```

7의 소리는 "Plong"입니다

```javascript
tryCatch(convert(7) === "Plong");
```

6의 소리는 "Pling"입니다

```javascript
tryCatch(convert(6) === "Pling");
```

8의 소리는 "8"입니다

```javascript
tryCatch(convert(8) === "8");
```

9의 소리는 "Pling"입니다

```javascript
tryCatch(convert(9) === "Pling");
```

10의 소리는 "Plang"입니다

```javascript
tryCatch(convert(10) === "Plang");
```

14의 소리는 "Plong"입니다

```javascript
tryCatch(convert(14) === "Plong");
```

15의 소리는 "PlingPlang"입니다

```javascript
tryCatch(convert(15) === "PlingPlang");
```

21의 소리는 "PlingPlong"입니다

```javascript
tryCatch(convert(21) === "PlingPlong");
```

25의 소리는 "Plang"입니다

```javascript
tryCatch(convert(25) === "Plang");
```

27의 소리는 "Pling"입니다

```javascript
tryCatch(convert(27) === "Pling");
```

35의 소리는 "PlangPlong"입니다

```javascript
tryCatch(convert(35) === "PlangPlong");
```

49의 소리는 "Plong"입니다

```javascript
tryCatch(convert(49) === "Plong");
```

52의 소리는 "52"입니다

```javascript
tryCatch(convert(52) === "52");
```

105의 소리는 "PlingPlangPlong"입니다

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

3125의 소리는 "Plang"입니다

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
