Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
A list stores multiple values of any type and uses **indexes** to distinguish these values.
You can assign items to a list with an expression of the form:
```python
list_name = [item1, item2]
```

---

You can access an individual item of the list by its index.
An index is like an address that identifies the item's place in the list.
The index appears directly after the list name, in between brackets, like this:
```python
list_name[index]
```

List indices begin with `0`, **not** `1`! You access the first item in a list like this: `list_name[0]`.
The second item in a list is at index 1: `list_name[1]`.

---

A list index behaves like any other variable name! It can be used to access as well as assign values.
You saw how to access a list index like this:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
This is how an assignment works:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

Just like strings, lists have a **length**.
A list's length is the number of items it contains

---

A list doesn't have to have a fixed length.
You can add items to the end of a list any time you like!
To add an item to a list we use the `append` keyword:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Sometimes, you only want to access a portion of a list.
Consider the following code:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
First, we create a list called `numbers`.
Then, we take a subsection of the list and store it in the slice list.
We do this by defining the indices we want to include after the name of the list: `numbers[1:3]`.
In Python, when we specify a portion of a list in this manner, we include the element with the first index, `1`, but we exclude the element with the second index, `3`.

---

You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index `0`.
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included.

---

List elements could be of any type:
```python
list_name = ["one", 2, True]
```
In fact, above we have, in order, a string, an integer and a boolean.
But we can also have lists with lists as well!

---

Sometimes you need to search for an item in a list.
In Python we can use the `index()` method:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
The code above prints the first index that contains the string `"Zac"`, `1` in this case.
We can also insert items into a list in a specific index, using the `insert()` method:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1

---

In Python we can loop through a list in a very simple way using the `for..in` keywords:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
A variable name follows the `for` keyword, it will be assigned the value of each list item in turn.

---

**Tuples** are like lists but are much faster.
However, tuple values cannot be changed.
We tend to use tuples for **read-only** data that remains constant while the program is running.
To create a tuple we use the round brackets `()`

---

There may be times when we want to change our tuple into a list.
In order to do this, we can use the `list()` function

---

Likewise, we can convert a list into a tuple
