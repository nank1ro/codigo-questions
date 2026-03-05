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

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

1의 소리는 "1"입니다

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

3의 소리는 "Pling"입니다

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

5의 소리는 "Plang"입니다

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

7의 소리는 "Plong"입니다

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

6의 소리는 "Pling"입니다

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

8의 소리는 "8"입니다

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

9의 소리는 "Pling"입니다

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

10의 소리는 "Plang"입니다

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

14의 소리는 "Plong"입니다

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

15의 소리는 "PlingPlang"입니다

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

21의 소리는 "PlingPlong"입니다

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

25의 소리는 "Plang"입니다

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

27의 소리는 "Pling"입니다

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

35의 소리는 "PlangPlong"입니다

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

49의 소리는 "Plong"입니다

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

52의 소리는 "52"입니다

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

105의 소리는 "PlingPlangPlong"입니다

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

3125의 소리는 "Plang"입니다

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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


