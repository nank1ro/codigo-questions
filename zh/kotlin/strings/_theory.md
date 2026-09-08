`String` 是写在双引号之间的字符序列。
`length` 属性表示字符串包含多少个字符，包括空格：
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

字符串的每个字符都有一个**索引**，第一个字符从 `0` 开始。
你可以用方括号或 `get` 函数读取单个字符，结果是一个 `Char`：
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
最后一个字符的索引是 `length - 1`。`first()` 和 `last()` 函数是方便的快捷方式：
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` 返回一个所有字母都变为大写的字符串副本，`lowercase()` 则相反。
原字符串不会被修改：
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

要检查字符串是否包含某段文本，可以使用 `contains`、`startsWith` 和 `endsWith`。它们都返回 `Boolean`：
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
这种检查区分大小写，除非你传入 `ignoreCase = true`：
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` 返回一段文本**第一次**出现的索引，如果完全没有出现则返回 `-1`。
`lastIndexOf` 则从末尾开始查找：
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` 提取字符串的一部分。使用两个参数时，它获取从起始索引到结束索引（**不包括**结束索引）之间的字符。
使用一个参数时，它获取从该索引到末尾的所有内容：
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
结合使用 `indexOf` 和 `substring` 可以围绕某个标记截取字符串：
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` 将字符串按分隔符拆分为一个 `List`，而 `joinToString` 则相反：它用你选择的分隔符把集合中的元素拼接成一个字符串：
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

由于 `split` 返回一个 `List`，你可以像遍历任何其他列表一样遍历它的元素：
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

用户输入常常带有多余的空格。`trim()` 返回去掉首尾空格的字符串，`trimStart()` 和 `trimEnd()` 只去掉一侧的空格：
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` 对 `""` 返回 `true`，而 `isBlank()` 对仅由空格组成的字符串也返回 `true`：
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` 返回一个字符串副本，其中 `old` 的**每一次**出现都被替换为 `new`：
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` 返回重复拼接 `n` 次的字符串：
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` 在字符串开头添加 `char`，直到字符串达到 `width` 个字符；`padEnd` 则在末尾添加。
如果字符串已经足够长，则原样返回：
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
数字不是字符串：先调用 `toString()`，例如 `42.toString().padStart(4, '0')`。
