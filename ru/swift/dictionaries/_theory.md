**Dictionaries** are similar to arrays and tuples, but you access values by looking up a *key* instead of an index
A key can be any string or number.
Dictionaries are enclosed in square brackets, like so:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
This is a dictionary called `dictionaryName` with three *key-value pairs*.
The key `key1` points to the value `1`, `key2` to `2`, and so on.

---

Accessing dictionary values by key is just like accessing array values by index:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Like Arrays, Dictionaries are _mutable_.
This means they can be changed after they are created (if are not declared constant).
One advantage of this is that we can add new _key/value pairs_ to the dictionary after it is created like so:
```swift
dictName[newKeyName] = newValue
```

---

The length `count` of a dictionary is the number of _key-value pairs_ it has.
Each pair counts only once, even if the value is an array. (That's right: you can also put arrays inside dictionaries!)

---

Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the `removeValue(forKey:)` method:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
will remove the key `keyName` and its associated value from the dictionary.

---

What if we want to list all the keys of the dictionary?
Well, these's the `keys` property.

---

What if we want to list all the values of the dictionary?
Well, these's the `values` property.

---

As for arrays, we can loop between dictionary elements using the keywords `for..in`.
To get both the key and the value in the loop we don't have to specify any property:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

We can also use the `isEmpty` property we used with arrays to determine if a dictionary is empty

---

In order to __add__ or __change__ values to a dictionary, we can also use the `updateValue(_:forKey:)` method

---

Previously we saw how to remove a _key-value pair_ from the dictionary with the `removeValue()` method.
We can also remove an element by assigning to the key the value `nil`
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
