`Set`s are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
The main difference with `Lists` is that a `Set` allows only one element of each value.

Like `List`s, a `Set` stores multiple values of one or multiple types and uses **indexes** to distinguish these values.
You can assign items to a set with an expression of the form:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` stands for the type of the items inside the set, for example, it can be `Int`, `String`, `Any`...

---

A `Set` is a collection of __unique__ items without a specific order.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

At __[1]__ we're trying to create a set with the number __1__ present twice but as you can see each element must be unique and the second __1__ is automatically discarded.

---

There are two types of `Set`s in Kotlin:

- `Set` cannot be modified after you create it.
- `MutableSet` can be modified after you create it, meaning you can add, remove, or update its elements.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ throws an Error because `Set`s are _read-only_.

To create a modifiable set use the `mutableSetOf` keyword
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

The most common `Set` activity is to test for membership using `in` or `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

As you can see above the `in` and `contains` return a `Bool` telling if the element being passed is present in the set

---

The order of the elements in a `Set` in not important.
In fact if you try to compare two `Set`s with the same element but in different order you get that they are equal.

---

On `Set`s you can perform several operations like checking for union, intersection, difference and subset.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

To convert a `Set` to a `List` we can use the `toList()` function
