**对象**与数组类似，但你通过查找*键*而不是索引来访问值。
键可以是任何字符串或数字。
对象用花括号括起来，如下所示：
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
这是一个名为 `objectName` 的字典，包含三个*键值对*。
键 `key1` 指向值 `1`，`key2` 指向 `2`，以此类推。

---

通过键访问字典值就像通过索引访问数组值一样：
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

与数组一样，字典是_可变的_。
这意味着它们在创建后可以被修改（如果没有声明为常量）。
这样做的一个好处是，我们可以在字典创建后向其中添加新的_键/值对_，如下所示：
```javascript
dictName[newKeyName] = newValue;
```

---

因为字典变量是可变的，所以可以通过多种方式进行修改。
可以使用 'delete' 关键字从字典中删除项目：
```javascript
delete dictName[keyName];
```
这将从字典中删除键 `keyName` 及其关联的值。

---

如果我们想列出字典中所有的键怎么办？
可以使用 `Object.keys()` 方法。

---

如果我们想列出字典中所有的值怎么办？
可以使用 `Object.values()` 方法。

---

与数组一样，我们可以使用 `Object.entries()` 方法遍历字典元素。
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
