**字典**与数组和元组类似，但你通过查找*键*而不是索引来访问值。
键可以是任何字符串或数字。
字典用方括号括起来，如下所示：
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
这是一个名为 `dictionaryName` 的字典，包含三个*键值对*。
键 `key1` 指向值 `1`，`key2` 指向 `2`，依此类推。

---

通过键访问字典值就像通过索引访问数组值一样：
```swift
// gets the age value from the user dictionary
user['age']
```

---

与数组一样，字典是_可变的_。
这意味着它们在创建后可以被修改（如果没有被声明为常量）。
这样做的一个好处是，我们可以在字典创建后向其中添加新的_键/值对_，如下所示：
```swift
dictName[newKeyName] = newValue
```

---

字典的长度 `count` 是它拥有的_键值对_的数量。
每对只计算一次，即使值是一个数组。（没错：你也可以把数组放在字典里！）

---

因为字典是可变的，所以它们可以通过多种方式进行修改。可以使用 `removeValue(forKey:)` 方法从字典中删除项目：
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
这将从字典中删除键 `keyName` 及其关联的值。

---

如果我们想列出字典的所有键怎么办？
可以使用 `keys` 属性。

---

如果我们想列出字典的所有值怎么办？
可以使用 `values` 属性。

---

与数组一样，我们可以使用 `for..in` 关键字在字典元素之间循环。
要在循环中同时获取键和值，我们不需要指定任何属性：
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

我们也可以使用数组中用过的 `isEmpty` 属性来判断字典是否为空

---

为了向字典__添加__或__修改__值，我们也可以使用 `updateValue(_:forKey:)` 方法

---

之前我们了解了如何使用 `removeValue()` 方法从字典中删除_键值对_。
我们也可以通过将键的值赋为 `nil` 来删除元素
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
