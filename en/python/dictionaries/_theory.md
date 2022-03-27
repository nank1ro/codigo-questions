**Dictionaries** are similar to lists and tuples, but you access values by looking up a *key* instead of an index.
A key can be any string or number.
Dictionaries are enclosed in curly braces, like so:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
This is a dictionary called `d` with three *key-value pairs*.
The key `key1` points to the value `1`, `key2` to `2`, and so on.

---

Accessing dictionary values by key is just like accessing list values by index:
```python
user['age']
# gets the age value from the user dictionary
```

---

Like Lists, Dictionaries are _mutable_.
This means they can be changed after they are created.
One advantage of this is that we can add new _key/value pairs_ to the dictionary after it is created like so:
```python
dict_name[new_key_name] = new_value
```

---

The length `len()` of a dictionary is the number of _key-value pairs_ it has.
Each pair counts only once, even if the value is a list. (That's right: you can also put lists inside dictionaries!)

---

Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the `del` command:
```python
del dict_name[key_name]
```
will remove the key `key_name` and its associated value from the dictionary.

---

What if we want to list all the keys of the dictionary?
Well, these's the `keys()` method.

---

What if we want to list all the values of the dictionary?
Well, these's the `values()` method.

---

As for lists, we can loop between dictionary elements using the keywords `for..in`
To get both the key and the value in the loop we can use the `items()` method:
```python
for key, value in dict_name:
	print(key, value)
```

---

We can also use the `in` keyword we used with loops to determine if a dictionary contains certain __key__

---

In order to __add__ or __change__ values to a dictionary, we can also use the `update()` method with the _key-value pairs_ we want to add in braces

---

What if we want to __remove__ a value a dictionary though?
There's the `pop()` method:
```python
dict_name.pop("key_name")
```
