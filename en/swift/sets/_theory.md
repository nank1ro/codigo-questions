A **Set** is a collection that stores values of the same type with no defined order and, most importantly, **no duplicates**: every value appears at most once.
Sets are perfect when you only care about *which* values are present, not how many times or in what position.
You declare a set with the type `Set<Element>` and an array-style literal:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
The type annotation is required: without it Swift would create an array.
If the literal contains a value more than once, the set keeps only one copy:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
The `count` property tells you how many distinct values the set holds.

---

Like arrays, sets can be constants (`let`) or variables (`var`). Only a `var` set can be changed after it is created.
To create an empty set you call the type's initializer, because an empty literal `[]` alone wouldn't tell Swift which element type to use:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
The `isEmpty` property is `true` when the set has no elements, exactly as with arrays.

---

Because a set never stores the same value twice, its `count` is the number of *distinct* values, no matter how many times each one was written in the literal.

---

To check whether a value is in a set use the `contains(_:)` method, which returns a `Bool`:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
This check is very fast on a set, even with thousands of elements, which is one of the main reasons to prefer a set over an array for membership tests.

---

A `var` set can be modified with `insert(_:)` and `remove(_:)`:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
Inserting a value that is already present has no effect, and removing a value that is absent doesn't cause an error.
`remove(_:)` returns the removed value as an optional (`nil` when nothing was removed), so you can check whether the removal actually happened.
To empty a set completely call `removeAll()`.

---

You can loop over a set with `for`-`in`, but remember that a set has **no defined order**: the elements may come out in any order, and that order can change between runs.
When the order matters, call `sorted()` first: it returns a new **array** with the elements in ascending order, leaving the set untouched.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```

---

Sets support the classic operations of set theory. Each one returns a **new** set and leaves the originals unchanged:
- `a.union(b)` contains every element that is in `a`, in `b`, or in both
- `a.intersection(b)` contains only the elements that are in **both** `a` and `b`
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

Two more operations complete the family:
- `a.subtracting(b)` contains the elements of `a` that are **not** in `b`
- `a.symmetricDifference(b)` contains the elements that are in `a` or in `b`, but **not in both**
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
Unlike `union` and `intersection`, `subtracting` is not symmetric: `a.subtracting(b)` and `b.subtracting(a)` are usually different.

---

Sets can also be compared with each other. These methods return a `Bool`:
- `a.isSubset(of: b)` is `true` when every element of `a` is also in `b`
- `a.isSuperset(of: b)` is `true` when `a` contains every element of `b`
- `a.isDisjoint(with: b)` is `true` when `a` and `b` have no element in common
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

Sets and arrays convert easily into each other.
Passing an array to `Set(...)` builds a set from its elements, which is the quickest way to **remove duplicates**:
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} in some order
```
Passing a set to `Array(...)` gives an array back, but since a set has no order the elements come out in an unpredictable sequence.
That's why, when you need an ordered result, you usually call `sorted()` on the set instead, which already returns an array:
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
