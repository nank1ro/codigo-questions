**Objects** are similar to arrays, but you access values by looking up a *key* instead of an index
A key can be any string or number.
Objects are enclosed in curly brackets, like so:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
This is a dictionary called `objectName` with three *key-value pairs*.
The key `key1` points to the value `1`, `key2` to `2`, and so on.

---

Accessing dictionary values by key is just like accessing array values by index:
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Like Arrays, Dictionaries are _mutable_.
This means they can be changed after they are created (if are not declared constant).
One advantage of this is that we can add new _key/value pairs_ to the dictionary after it is created like so:
```javascript
dictName[newKeyName] = newValue;
```

---

Because dictionaries variables are mutable, they can be changed in many ways.
Items can be removed from a dictionary with the 'delete' keyword:
```javascript
delete dictName[keyName];
```
will remove the key `keyName` and its associated value from the dictionary.

---

What if we want to list all the keys of the dictionary?
Well, these's the `Object.keys()` method.

---

What if we want to list all the values of the dictionary?
Well, these's the `Object.values()` method.

---

As for arrays, we can loop between dictionary elements using the `Object.entries()` method.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
