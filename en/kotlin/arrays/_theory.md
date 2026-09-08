An **array** stores a fixed number of values of the same type under a single variable name.
You create one with `arrayOf`, read an element with square brackets and an **index** starting from `0`, and get the number of elements with `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
The last element is at index `size - 1`.

---

`arrayOf(1, 2, 3)` creates an `Array<Int>` where every element is a boxed object.
For primitive types Kotlin offers dedicated, more efficient types such as `IntArray`, `DoubleArray` and `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
You can also build an array of a given size with an **init** lambda that receives each index, or a zero-filled `IntArray`:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Every array has two handy properties for working with indexes:
- `indices` is the range of valid indexes, from `0` to the last one
- `lastIndex` is the index of the last element, that is `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Even when an array is declared with `val`, its **elements** can be replaced by assigning to an index:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
To visit every element you can use a `for` loop or `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Note that `n` and `it` are read-only copies of the values and cannot be reassigned, so to modify elements you need their index.

---

To check whether an array holds a value use `in` or `contains`, both return a `Boolean`.
`indexOf` returns the index of the first occurrence, or `-1` when the value is not present:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Printing an array directly does not show its elements, it prints something like `[Ljava.lang.String;@1b6d3586`.
Use `joinToString` to build a readable string, optionally with a custom separator (the default is `", "`), or `contentToString` to get the elements between square brackets:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Arrays can be sorted **in place** or copied into a new sorted collection:
- `sort()` and `sortDescending()` reorder the array itself and return nothing
- `reverse()` flips the order of the array itself
- `sorted()`, `sortedDescending()` and `reversed()` leave the array untouched and return a new `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Numeric arrays come with aggregate functions:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` and `min()` throw an exception on an empty array, use `maxOrNull()` and `minOrNull()` when the array may be empty.

---

The main difference between an array and a `MutableList` is that an array has a **fixed size**: once created you can replace its elements but you can never add or remove one, there is no `add` function.
Expressions like `nums + 4` do not grow `nums`, they build a brand new array:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Prefer a `MutableList` when the number of elements changes over time, and an array when it is known up front or when you need primitive performance.

---

Arrays support the same transformation functions as lists. `filter` keeps the elements matching a condition and `map` transforms every element.
Both return a new `List`, not an array:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Since the result is a list, printing it directly shows its elements.

---

When you need both the index and the value while looping, use `withIndex()` and destructure each pair, or `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Arrays and lists convert into each other easily:
- `toList()` and `toMutableList()` copy an array into a list
- `toTypedArray()` copies a list into an `Array<T>`
- `toIntArray()` copies a list of `Int` into an `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Every conversion creates a **copy**, so changing the result does not affect the original.

---

Unlike lists, two arrays with the same elements are **not** equal with `==`: arrays are compared by reference, so `==` is `true` only for the very same array object.
To compare the contents use `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Since arrays have a fixed size, taking a part of one means creating a new array:
- `copyOf()` copies the whole array, `copyOf(n)` copies the first `n` elements
- `copyOfRange(from, to)` copies the elements from index `from` up to `to` **excluded**
- `sliceArray(range)` copies the elements at the indexes of the range, both ends included
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
