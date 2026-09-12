**正则表达式**（或 **regex**）是一个描述文本形状的小模式："四个数字"、"后面跟着 `@` 的单词"、"引号之间的任何内容"。在 Kotlin 中，模式是一个 `Regex` 对象，有两种等价的构建方式：
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
模式中的大多数字符代表它们自己，但有几个是**简写**：
- `\d` 表示任意数字，在 Kotlin 字符串中写作 `"\\d"`，因为 `\` 必须转义
- `[a-z]` 表示任意小写字母，`[abc]` 表示 `a`、`b` 或 `c` 中的任意一个
- 元素后面的 `+` 表示"一个或多个它"，所以 `\d+` 是一串数字

你能提出的最简单的问题是 `matches`，只有当模式描述**整个**字符串时它才为 `true`：
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` 通常过于严格：通常你只想知道模式是否出现在文本的**某个地方**。这就是 `containsMatchIn`：
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
除了 `\d`，还有两个你会经常用到的简写：`\w` 表示单词字符（字母、数字或 `_`），`\s` 表示空白字符。它们每一个都可以用**量词**重复：
- `+` 一个或多个
- `*` 零个或多个
- `?` 零个或一个
- `{3}` 恰好三个，`{2,4}` 两个到四个

把每个反斜杠都加倍会变得很混乱，所以模式通常写成三引号的**原始字符串**，其中 `\` 只是一个普通字符：
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` 只能说明模式*是否*存在。`find` 还能说明是**什么**以及在**哪里**：它把第一个匹配作为 `MatchResult` 返回，当没有东西可找时返回 `null`。
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` 是匹配到的文本，`range` 是它在原字符串中覆盖的索引。因为结果是可空的，你要用安全调用 `?.` 来访问它，当没有找到匹配时它会给出 `null` 而不是崩溃：
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

模式中的圆括号创建一个**捕获组**：匹配中你想单独读取的一部分。`MatchResult.groupValues` 保存着这些组，索引 `0` 是整个匹配，`1`、`2`……是各个组，从左到右排列：
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
当完全没有匹配时，`find` 返回 `null`，没有什么可读取的，所以提取组的函数通常要决定在这种情况下返回什么：
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

数括号来弄清楚主机是第 `2` 个组，一旦模式变大就会变得脆弱。可以用 `(?<name>...)` 给组起一个**名字**，然后通过该名字从 `groups` 中读取：
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` 把组作为 `MatchGroup?` 返回，所以你仍要请求它的 `.value`。命名组也像往常一样有编号，所以 `groupValues[1]` 在它旁边仍然有效。

---

`find` 在第一个匹配处停止。`findAll` 返回**每一个**匹配，作为一个 `Sequence<MatchResult>`：一条惰性链，你可以像列表一样用 `map`、`filter`、`count` 和 `toList` 来处理它。
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
当没有匹配时，`findAll` 返回一个空序列而不是 `null`，所以不需要写安全调用。打印序列本身没有用，它显示的是对象而不是匹配：先把它转换成列表。

---

`replace` 重写文本：它返回一个**新**字符串，其中每个匹配都被替换内容换掉，而原始字符串保持不变。
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
在替换字符串中，`$1`、`$2`……代表该匹配捕获的组，所以你可以重新排列或复用匹配到的部分：
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` 是整个匹配。如果你需要在替换中出现字面意义上的 `$`，把它转义为 `\$`。
`replace` 重写**每一个**匹配，所以当只想重写完整的字符串时，用**锚点** `^`（文本开头）和 `$`（文本结尾）来固定模式：
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

替换字符串只能重新排列交给它的那些部分。当新文本需要**计算**得出时，改为向 `replace` 传递一个 lambda：它接收 `MatchResult` 并返回替代该匹配的字符串。
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
在 lambda 内部你可以使用完整的 `MatchResult`，所以 `m.value`、`m.range` 和 `m.groupValues` 都可用。注意 `$1` 在这里没有任何含义：它只是你返回的字符串中的一个普通字符。

---

`split` 在模式匹配到的每一处切割字符串，并把各部分作为 `List<String>` 返回。与在固定的分隔符字符串上分割不同，正则分隔符可以描述一整类分隔符：
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
匹配到的分隔符不是结果的一部分。如果文本以分隔符开头或结尾，紧挨着它的那部分是空字符串：
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` 接受一个 `limit` 作为第二个参数，在生成给定数量的部分后停止，把剩下的内容原封不动地保留在最后一部分中。

---

模式区分大小写：`Regex("kotlin")` 不匹配 `"Kotlin"`。与其写 `[kK][oO]...`，不如把一个选项作为第二个参数传入：
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
选项属于 `Regex`，所以该对象的每个方法都遵守它：`matches`、`find`、`findAll`、`replace` 和 `split` 都一样。其他有用的选项还有 `RegexOption.MULTILINE`（它让 `^` 和 `$` 在每一行都匹配）和 `RegexOption.DOT_MATCHES_ALL`。要组合它们，传入一个集合：`Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`。

---

`Regex("cat")` 也会匹配 `catalog` 中的 `cat`。要要求整个单词，使用**单词边界** `\b`：它匹配单词字符与其他任何内容之间的空位置，包括文本的开头和结尾。
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
模式是一个普通字符串，所以它可以在运行时由多个部分拼接而成：
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

字符 `. * + ? ( ) [ ] { } | ^ $ \` 在模式中有特殊含义。其中最狡猾的是 `.`，它匹配**任意**字符，而不是一个点。要表示字符本身，用反斜杠转义它：
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
当要查找的文本来自变量且必须按字面处理时，让库用 `Regex.escape` 来做转义：
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` 和组一起把一行文本变成结构化数据。序列中的每个 `MatchResult` 都带有自己的 `groupValues`，所以一条链就能构建列表、映射或总和：
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` 用 lambda 返回的 `key to value` 对构建一个映射。当模式有固定数量的组时，`destructured` 让你把它们解包到命名变量中，而不用按索引读取：
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

方括号定义一个**字符类**：从列出的集合中选出一个字符。在其中可以使用范围，开头的 `^` 会对整个类取反：
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
字符类只能在单个字符之间选择。要在整个备选项之间选择，使用 `|`，通常把它包在一个组里，以免它吞掉模式的其余部分：
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

因为 `findAll` 给出的是一个序列，你已经知道的聚合方法也可以用在匹配上：`sumOf`、`maxOfOrNull`、`filter`、`sortedBy`。从自由文本中提取数字是一个两步工作：先匹配它们，再把文本转换成数字。
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

一个实际的模式通常同时混合所有内容：用组保留你需要的部分，用转义的 `\.` 表示字面上的点，再用 lambda 替换来围绕它们重建文本。
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
让模式保持任务允许范围内的简单：一个试图描述每一个合法电子邮件地址的模式是难以阅读的，而 `\w+@\w+\.\w+` 足以在句子中找到地址。
