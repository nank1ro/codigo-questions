---
language: swift
exerciseType: 1
difficulty: 1
title: 빗방울
---

# --description--

여러분의 과제는 숫자를 특정 잠재적 인수에 해당하는 빗방울 소리를 포함하는 문자열로 변환하는 것입니다.
인수는 나머지 없이 다른 숫자를 균등하게 나누는 숫자입니다.
숫자가 다른 숫자의 인수인지 테스트하는 가장 간단한 방법은 나머지 연산을 사용하는 것입니다.
빗방울의 규칙은 주어진 숫자가:

- 3을 인수로 가지면 결과에 'Pling'을 추가합니다.
- 5를 인수로 가지면 결과에 'Plang'을 추가합니다.
- 7을 인수로 가지면 결과에 'Plong'을 추가합니다.
- 3, 5, 7 중 어느 것도 인수로 가지지 않으면 결과는 숫자의 자릿수여야 합니다.

# --instructions--

올바른 문자열을 반환하는 함수를 작성하십시오. 예시:

- 28은 7을 인수로 가지지만 3이나 5는 아니므로, 결과는 `"Plong"`입니다.
- 30은 3과 5를 모두 인수로 가지지만 7은 아니므로, 결과는 `"PlingPlang"`입니다.
- 34는 3, 5, 7 중 어느 것의 인수도 아니므로, 결과는 `"34"`입니다.

> 힌트: `_` (밑줄)로 인수 레이블을 생략하십시오

함수 호출 예시:
```swift
print(raindrops(28))
// prints "Plong"
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func raindrops() {
    
}
```

# --asserts--

1의 소리는 "1"입니다

```swift
tryCatch("1" == raindrops(1))
```

3의 소리는 "Pling"입니다

```swift
tryCatch("Pling" == raindrops(3))
```

5의 소리는 "Plang"입니다

```swift
tryCatch("Plang" == raindrops(5))
```

7의 소리는 "Plong"입니다

```swift
tryCatch("Plong" == raindrops(7))
```

6의 소리는 "Pling"입니다

```swift
tryCatch("Pling" == raindrops(6))
```

8의 소리는 "8"입니다

```swift
tryCatch("8" == raindrops(8))
```

9의 소리는 "Pling"입니다

```swift
tryCatch("Pling" == raindrops(9))
```

10의 소리는 "Plang"입니다

```swift
tryCatch("Plang" == raindrops(10))
```

14의 소리는 "Plong"입니다

```swift
tryCatch("Plong" == raindrops(14))
```

15의 소리는 "PlingPlang"입니다

```swift
tryCatch("PlingPlang" == raindrops(15))
```

21의 소리는 "PlingPlong"입니다

```swift
tryCatch("PlingPlong" == raindrops(21))
```

25의 소리는 "Plang"입니다

```swift
tryCatch("Plang" == raindrops(25))
```

27의 소리는 "Pling"입니다

```swift
tryCatch("Pling" == raindrops(27))
```

35의 소리는 "PlangPlong"입니다

```swift
tryCatch("PlangPlong" == raindrops(35))
```

49의 소리는 "Plong"입니다

```swift
tryCatch("Plong" == raindrops(49))
```

52의 소리는 "52"입니다

```swift
tryCatch("52" == raindrops(52))
```

105의 소리는 "PlingPlangPlong"입니다

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

3125의 소리는 "Plang"입니다

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


