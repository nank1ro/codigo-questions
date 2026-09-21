---
language: swift
exerciseType: 1
difficulty: 2
title: 시계
---

# --description--

24시간 시계는 하루의 시각을 `HH:MM` 형태로 표시하며, 자정이 지나자마자 `00:00`에서 시작해 다음 자정 1분 전인 `23:59`에서 끝납니다. 두 부분은 항상 두 자리로 쓰이므로, 오전 11시 9분은 `11:09`로 표시됩니다.

하루 전체는 1440분입니다. 시계가 `23:59`를 지나면 `00:00`으로 넘어가 하루를 다시 시작하고, `00:00`에서 거꾸로 돌리면 `23:59`에 도착합니다.

# --instructions--

두 정수 `hours`와 `minutes`를 받아, 두 부분을 모두 두 자리로 채운 24시간 시계의 시각을 문자열 `"HH:MM"`으로 반환하는 함수 `clockTime`을 작성하세요.

예시:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- 두 숫자 중 하나는 음수이거나 실제 시계가 허용하는 값보다 클 수 있습니다.
- `hours * 60 + minutes`로 총 분 수를 구한 다음, 그 총합을 `0`부터 `1439` 범위로 감싸서 시계가 양방향으로 넘어가도록 하세요.
- `clockTime(24, 0)`은 정확히 하루이므로 `"00:00"`이 표시됩니다.

> 힌트: `_`(언더스코어)를 사용해 인수 레이블을 생략하세요

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
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    
}
```

# --asserts--

오전 8시는 `08:00`으로 표시됩니다

```swift
tryCatch(clockTime(8, 0) == "08:00")
```

한 자리 숫자는 두 자리로 채워지므로, 오전 11시 9분은 `11:09`로 표시됩니다

```swift
tryCatch(clockTime(11, 9) == "11:09")
```

정확히 하루 분의 시간이 지나면 `00:00`으로 넘어갑니다

```swift
tryCatch(clockTime(24, 0) == "00:00")
```

60이 넘는 분은 시간으로 넘어갑니다

```swift
tryCatch(clockTime(25, 160) == "03:40")
```

음수 시간은 시계를 자정 너머로 거꾸로 돌립니다

```swift
tryCatch(clockTime(-1, 15) == "23:15")
```

음수 분 수도 시계를 거꾸로 돌립니다

```swift
tryCatch(clockTime(0, -90) == "22:30")
```

하루 이상 거꾸로 돌아도 계속 넘어갑니다

```swift
tryCatch(clockTime(-25, 0) == "23:00")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    // %는 왼쪽 피연산자의 부호를 유지하므로, 0..1439 범위에 들어오도록
    // 하루를 더한 뒤 다시 한번 넘깁니다.
    let total = (((hours * 60 + minutes) % 1440) + 1440) % 1440

    return String(format: "%02d:%02d", total / 60, total % 60)
}
```
