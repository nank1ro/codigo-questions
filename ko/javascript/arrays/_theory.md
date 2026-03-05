Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
An array stores multiple values of one or multiple types and uses **indexes** to distinguish these values.
You can assign items to an array with an expression of the form:
```javascript
var arrayName = [item1, item2];
```

---

You can access an individual item of the array by its index.
An index is like an address that identifies the item's place in the array.
The index appears directly after the array name, in between brackets, like this:
```javascript
arrayName[index];
```
Array indices begin with `0`, **not** `1`! You access the first item of an array like this: `arrayName[0]`.
The second item in an array is at index 1: `arrayName[1]`.

---

An array index behaves like any other variable name.
It can be used to access as well as assign values.
You saw how to access an array index like this:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
This is how an assignment works:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Just like strings, arrays have a **length**.
An arrays's length is the number of items it contains

---

An array doesn't have to have a fixed length.
You can add items to the end of an array any time you like!
To add an item to an array we use the `push` function:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

Sometimes, you only want to access a portion of an array.
Consider the following code:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
First, we create an array called `numbers`.
Then, we take a subsection of the array and store it in the slice array.
We do this by defining the indices we want to include after the name of the array: `numbers.slice(1, 3)`.
Keep in mind that the right index is excluded

---

In JavaScript we can slice an array as we want!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
If your array slice includes the very first or last item in an array, the index for that item doesn't have to be included

---

Array elements could be of any type.
```javascript
var arrayName = ["one", 2, true];
```
In fact, above we have, in order, a string, an integer and a boolean.
But we can also have arrays with arrays as well!

---

Sometimes you need to search for an item in an array.
In JavaScript we can use the `indexOf()` method:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
The code above prints the first index that contains the string `"Zac"`, `1` in this case.
We can also insert items into an array in a specific index, using the `splice()` method:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1.
The second value `0` means _deleteCount_, in this case, we don't delete any item in the array; but if we had specified `1` the value `Zac` would have been removed from the array

---

In JavaScript we can loop through an array in a very simple way using the `for..of` keywords:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3 
```
A variable name follows the `for` keyword, it will be assigned the value of each array item in turn.
