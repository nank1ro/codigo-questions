---
language: swift
exerciseType: 1
difficulty: 1
title: 100のドア
---

# --description--

100個のドアが一列に並んでおり、すべて最初は閉まっています。
あなたはドアの前を100回通過します。
1回目は、すべてのドアを訪れてドアを「切り替え」ます（ドアが閉まっていれば開け、開いていれば閉めます）。
2回目は、2番目ごとのドア（つまり、ドア#2、#4、#6、...）だけを訪れて切り替えます。
3回目は、3番目ごとのドア（つまり、ドア#3、#6、#9、...）を訪れ、100番目のドアだけを訪れるまで続けます。

# --instructions--

最後の通過後のドアの状態を判定する関数を実装してください。
最終結果を配列で返し、開いているドアの番号のみを配列に含めてください。
> このメソッドは可変数のドアで動作できなければなりません。

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

100個のドアが与えられた場合、開いているドアの正しいリストを返す

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

10個のドアが与えられた場合、開いているドアの正しいリストを返す

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

950個のドアが与えられた場合、開いているドアの正しいリストを返す

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
