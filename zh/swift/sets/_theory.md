**Set（集合）**是一种存储相同类型值的集合，没有固定的顺序，最重要的是**没有重复项**：每个值最多出现一次。
当你只关心*哪些*值存在，而不关心出现了多少次或处于什么位置时，集合非常合适。
你使用 `Set<Element>` 类型和数组风格的字面量来声明一个集合：
```swift
let numbers: Set<Int> = [1, 2, 3]
```
类型注解是必需的：没有它，Swift 会创建一个数组。
如果字面量中某个值出现了多次，集合只会保留一份：
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
`count` 属性会告诉你集合中包含多少个不同的值。

---

和数组一样，集合可以是常量（`let`）或变量（`var`）。只有 `var` 集合才能在创建后被修改。
要创建一个空集合，你需要调用该类型的初始化方法，因为仅凭一个空字面量 `[]` 无法告诉 Swift 应该使用哪种元素类型：
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
当集合不包含任何元素时，`isEmpty` 属性为 `true`，这一点和数组完全一样。

---

因为集合永远不会存储同一个值两次，所以它的 `count` 是*不同*值的数量，无论每个值在字面量中被写了多少次。

---

要检查某个值是否在集合中，可以使用 `contains(_:)` 方法，它返回一个 `Bool`：
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
这种检查在集合上非常快，即使有成千上万个元素也是如此，这也是在做成员检查时更倾向于使用集合而不是数组的主要原因之一。

---

`var` 集合可以使用 `insert(_:)` 和 `remove(_:)` 进行修改：
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 已经存在：没有变化
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 不存在：没有变化
```
插入一个已经存在的值不会有任何效果，删除一个不存在的值也不会引发错误。
`remove(_:)` 会把被删除的值作为可选值返回（如果没有删除任何内容则为 `nil`），这样你就可以检查删除是否真的发生了。
要完全清空一个集合，调用 `removeAll()`。

---

你可以用 `for`-`in` 遍历集合，但要记住集合**没有固定的顺序**：元素可能以任意顺序出现，而且这个顺序在每次运行时都可能变化。
当顺序很重要时，先调用 `sorted()`：它会返回一个新的**数组**，其中元素按升序排列，而原集合保持不变。
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 各占一行
}
```

---

集合支持经典的集合论运算。每个运算都会返回一个**新的**集合，原始集合保持不变：
- `a.union(b)` 包含所有在 `a` 中、在 `b` 中，或者两者都在的元素
- `a.intersection(b)` 只包含**同时**在 `a` 和 `b` 中的元素
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

另外两个操作补全了这个体系：
- `a.subtracting(b)` 包含 `a` 中**不在** `b` 中的元素
- `a.symmetricDifference(b)` 包含在 `a` 或 `b` 中，但**不同时在两者中**的元素
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
和 `union`、`intersection` 不同，`subtracting` 不是对称的：`a.subtracting(b)` 和 `b.subtracting(a)` 通常是不同的。

---

集合之间也可以互相比较。这些方法都返回 `Bool`：
- `a.isSubset(of: b)` 在 `a` 的每个元素都在 `b` 中时为 `true`
- `a.isSuperset(of: b)` 在 `a` 包含 `b` 的每个元素时为 `true`
- `a.isDisjoint(with: b)` 在 `a` 和 `b` 没有共同元素时为 `true`
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

集合和数组之间可以很方便地互相转换。
把一个数组传给 `Set(...)` 会用它的元素构建一个集合，这是**去除重复项**最快的方式：
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3}，顺序不定
```
把一个集合传给 `Array(...)` 会得到一个数组，但由于集合没有顺序，元素会以不可预测的顺序出现。
这就是为什么当你需要有序结果时，通常会在集合上调用 `sorted()`，它本身就会返回一个数组：
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
