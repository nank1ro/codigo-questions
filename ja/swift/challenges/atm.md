---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

ジェームズはATMからNドルを引き出したいと考えています。
ATMは、Nが5の倍数であり、ジェームズの口座に引き出し取引を行うのに十分な残高がある場合（銀行手数料を含む）にのみ取引を受け付けます。
引き出しが成功するたびに、銀行は`0.50$`の手数料を請求します。
取引を試みた後のジェームズの口座残高を計算してください。
入力は以下の順序です:
1. ジェームズが引き出したい金額は次の範囲です: `0 < N <= 2000`。
2. ジェームズの初期残高は小数点以下2桁で与えられ、次の範囲です: `0 < B <= 2000`。

# --instructions--

取引を試みた後の口座残高を小数点以下2桁の数値として返してください。
口座に取引を完了するのに十分なお金がない場合は、現在の銀行残高を返してください。

> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
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

取引が成功する場合

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

残高不足の場合

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

取引拒否、無効な金額

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

全額を正常に引き出す

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
