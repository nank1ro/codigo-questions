---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James는 ATM에서 N달러를 인출하고 싶습니다.
현금 인출기는 N이 5의 배수이고, James의 계좌에 인출 거래를 수행할 충분한 잔액이 있는 경우에만 거래를 수락합니다 (은행 수수료 포함).
성공적인 인출마다 은행은 `0.50$`를 수수료로 부과합니다.
인출 시도 후 James의 계좌 잔액을 계산하십시오.
입력은 다음 순서로 제공됩니다:
1. James가 인출하고자 하는 금액은 다음 범위에 있습니다: `0 < N <= 2000`.
2. James의 초기 잔액은 소수점 두 자리로 제공되며 다음 범위에 있습니다: `0 < B <= 2000`.

# --instructions--

인출 시도 후 계좌 잔액을 소수점 두 자리 숫자로 반환하십시오.
계좌에 거래를 완료할 충분한 잔액이 없으면 현재 은행 잔액을 반환하십시오.

> 힌트: `_` (밑줄)로 인수 레이블을 생략하십시오

함수 호출 예시:
```swift
print(accountBalance(10, 20))
// prints 9,5
```

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

성공적인 거래를 수행합니다

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

잔액이 부족합니다

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

거래 거부, 유효하지 않은 금액

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

모든 금액을 성공적으로 인출합니다

```swift
    func testWithdrawAll() {
        let expected: Double = 0.00
        XCTAssertEqual(accountBalance(95, 95.50), expected, "--err-t4--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSuccessfulTransaction", testSuccessfulTransaction),
            ("testInsufficientFunds", testInsufficientFunds),
            ("testNotMultipleOf5", testNotMultipleOf5),
            ("testWithdrawAll", testWithdrawAll),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func accountBalance(_ withdraw: Double,_ balance: Double) -> Double {
    let isMultipleOf5 = withdraw.truncatingRemainder(dividingBy: 5) == 0;
    let isAmountAvailable = balance >= (withdraw + 0.50)
    if isMultipleOf5 && isAmountAvailable {
        return balance - withdraw - 0.50
    }
    return balance
}
```
