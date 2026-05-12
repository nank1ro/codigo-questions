---
language: swift
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

달력의 1년은 정확히 365.25일입니다. 하지만 결국 이것은 혼란을 초래할 수 있는데, 인간은 보통 소수점이 아닌 1의 정확한 나눗셈으로 계산하기 때문입니다. 따라서 이를 피하기 위해 4년 주기마다 0.25일을 모두 합산하여 그 해를 366일로 만들고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 3년은 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 도전에서는 한 단계 더 나아가, `Date` 클래스, `switch` 문, __if 블록__, __if-else 블록__ 또는 __삼항 연산__ (`x ? a : b`)을 사용하지 않고, 또한 논리 연산자 __AND__ (`&&`)와 __OR__ (`||`)도 사용하지 않고 (단, __NOT__ (`!`) 연산자는 예외) 윤년인지 아닌지를 판별해야 합니다.

윤년이면 `true`를, 그렇지 않으면 `false`를 반환하십시오.

함수 호출 예시:
```swift
print(leapYear(2000))
// prints true
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

`Date`, `switch`, `if`, `else`, `&&`, `||` 또는 `?`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```swift
tryCatch(leapYear(2016) == true)
```

`1996`년은 윤년입니다.

```swift
tryCatch(leapYear(1996) == true)
```

`1600`년은 윤년입니다.

```swift
tryCatch(leapYear(1600) == true)
```

`2020`년은 윤년입니다.

```swift
tryCatch(leapYear(2020) == true)
```

`2000`년은 윤년입니다.

```swift
tryCatch(leapYear(2000) == true)
```

`2008`년은 윤년입니다.

```swift
tryCatch(leapYear(2008) == true)
```

`1521`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(1521) == false)
```

`1800`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(1800) == false)
```

`2007`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(2007) == false)
```

`2002`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(2002) == false)
```

`1979`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(1979) == false)
```

`2006`년은 윤년이 아닙니다.

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
