Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
A list stores multiple values of one or multiple types and uses **indexes** to distinguish these values.
You can assign items to an list with an expression of the form:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` stands for the type of the items inside the list, for example, it can be `Int`, `String`, `Any`...

---

A list is a collection of items with a specific order. There are two types of lists in Kotlin:

- `List` cannot be modified after you create it.
- `MutableList` can be modified after you create it, meaning you can add, remove, or update its elements.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ throws an Error because `List`s are _read-only_.

To create a modifiable list use the `mutableListOf` keyword
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

You can access an individual item of the list by its index.
An index is like an address that identifies the item's place in the list.
The index appears directly after the list name, in between brackets, like this:
```kotlin
listName[index]
```

List indices begin with `0`, **not** `1`! You access the first item of an list like this: `listName[0]` or `listName.get(0)` or even `listName.first()`.
The second item in an list is at index __1__: `listName[1]`.

---

The index is actually an offset from the first element. For example, when you say `list[2]` you are not asking for the second element of the list, but for the element that is 2 positions offset from the first element. Hence `list[0]` is the first element (zero offset), `list[1]` is the second element (offset of 1), `list[2]` is the third element (offset of 2), and so on.

A list index can be used to access as well as assign values.
You saw how to access a list index like this:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
This is how an assignment works:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

Just like strings, lists have a **length** retrieved with the `size` getter.
A list length is the number of items it contains

---

Another useful list operation is the `contains` method to find out if a given element is in the list.
For example, if you have a list of names, you can use the `contains` method to find out if a given name is present in the list.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

A mutable list doesn't have to have a fixed length.
You can add items to the end of a list any time you like!
To add an item to a mutable list we use the `add` function or the `+=` shortcut:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

As we've seen in the previous example, we can add items ony by one using the `add` function.
But if we've to add all the elements of another list at once we can simply use the `addAll` function, or the `+=` shortcut:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e") 
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

Sometimes, you only want to access a portion of a list.
Consider the following code:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: first, we create a _read-only_ list called `numbers`.
__[2]__: then, we take a subsection of the list using the `slice` function and store it in the slice list.
We do this by defining the indices we want to include inside the `slide` function.

In Kotlin we can include the last index using `..`, but we can also exclude the last index using `until`

---

Lists elements could be of any type, if we specify the `Any` type:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
In fact, above we have, in order, a `String`, an `Integer` and a `Boolean`.
But we can also have lists with lists as well!

---

Sometimes you need to search for an item in a list.
In Kotlin we can use the `indexOfFirst` method:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

The `indexOfFirst` method takes a __predicate__ function that will be evaluated for each item in the list until it's true, returning the _index_ of the element.
The code above prints the first index that contains the string `"Zac"`, `1` in this case.

We can also insert items into a modifiable list in a specific index, using the `add(index, element)` method:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1

---

In Kotlin we can loop through a list in a very simple way using the `for..in` keywords:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3 
```
A variable name follows the `for` keyword, it will be assigned the value of each list item in turn.
