```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` stands for the type of the items inside the array, for example, it can be `Int`, `String`, `Any`...

 Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. An array stores multiple values of one or multiple types and uses **indexes** to distinguish these values. You can assign items to an array with an expression of the form:

---

You can access an individual item of the array by its index.
An index is like an address that identifies the item's place in the array.
The index appears directly after the array name, in between brackets, like this:
```swift
arrayName[index]
```

Array indices begin with `0`, **not** `1`! You access the first item of an array like this: `arrayName[0]`.
The second item in an array is at index 1: `arrayName[1]`.

---

An array index behaves like any other variable name.
It can be used to access as well as assign values.
You saw how to access an array index like this:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
This is how an assignment works:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

Just like strings, arrays have a **length** `count`.
An arrays's length is the number of items it contains

---

```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

 An array doesn't have to have a fixed length. You can add items to the end of an array any time you like! To add an item to an array we use the `append` function:

---

Sometimes, you only want to access a portion of an array.
Consider the following code:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
First, we create an array called `numbers`.
Then, we take a subsection of the array and store it in the slice array.
We do this by defining the indices we want to include after the name of the array: `numbers[1...2]`.
In Swift we can include the last index using `...`, but we can also exclude the last index using `..<`

---

In Swift we puede slice un arreglo como we querer!
```swift
// Grabs el primero two elementos
listName[..<2]
// Grabs the fourth through ultimo elementos
listName[3...]
```
si your arreglo slice incluye el muy primero o ultimo elemento en un arreglo, el indice para ese elemento doesn't tiene un ser included

---

arreglo elements podria ser de cualquier tipo, si we specify el `Any` tipo:
```swift
var arrayName: [Any] = ["one", 2, true]
```
In fact, encima de we tiene, en order, un cadena, un integer y un booleano.
pero we puede tambien tiene arreglos con arreglos como well!

---

```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
The code above prints the first index that contains the string `"Zac"`, `1` in this case.
We can also insert items into an array in a specific index, using the `insert()` method:
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1

 Sometimes you need to search for an item in an array. In Swift we can use the `firstIndex()` method:

---

In Swift we can loop through an array in a very simple way using the `for..in` keywords:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3 
```
A variable name follows the `for` keyword, it will be assigned the value of each array item in turn.

---

**Tuples** son like arreglos pero you puede nombre el elements y usar esos nombres un refer un them
a Crea un tuple we usar el round brackets `()` 
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
