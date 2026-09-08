**字符串**是一段文本：用引号括起来的字符序列。
Python 既接受单引号 `'...'`，也接受双引号 `"..."`，它们的工作方式完全相同：
```python
name = 'Ada'
language = "Python"
```
当文本本身包含引号时，选择哪种引号就很重要。
单引号内的撇号会过早地结束字符串，所以这时应改用双引号：
```python
print("It's sunny")  # It's sunny
```

---

内置函数 `len()` 返回字符串的**长度**，也就是它包含多少个字符。
空格和标点符号也算作字符：
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

字符串的每个字符都有一个位置，称为**索引**。
索引从 `0` 开始，而不是从 `1` 开始：第一个字符的索引是 `0`，第二个字符的索引是 `1`，依此类推。
在字符串后面的方括号中写上索引即可读取单个字符：
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
访问一个不存在的索引，比如 `word[6]`，会引发 `IndexError`。

---

索引也可以是**负数**：它们从字符串末尾开始计数。
`-1` 是最后一个字符，`-2` 是它前面的一个，依此类推：
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
这很方便，因为你不需要知道字符串的长度就能到达它的末尾。

---

**切片**（slice）可以提取字符串的一部分。
在方括号中写 `[开始:结束]`：位置为 `开始` 的字符会被包含，位置为 `结束` 的字符会被**排除**：
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
你可以省略 `开始` 来从字符串开头切片，或省略 `结束` 来切片到末尾：
```python
print(word[:2])  # py
print(word[2:])  # thon
```
切片永远不会引发错误：如果 `结束` 大于字符串长度，切片只会在最后一个字符处停止。

---

你已经知道 `+` 可以将两个字符串连接在一起（**拼接**）。
`*` 运算符可以将字符串**重复**指定的次数：
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
重复是绘制分隔符和简单图案的快捷方式。

---

`in` 运算符检查一个字符串是否**包含**另一个字符串。
它返回 `True` 或 `False`，所以很自然地可以放进 `if` 里：
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` 执行相反的检查。

---

字符串自带许多内置**方法**：在字符串后面加一个点来调用的函数。
`upper()` 返回大写形式的文本，`lower()` 返回小写形式：
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
注意，这些方法会**返回一个新的字符串**：原来的 `word` 不会被改变。
`lower()` 常用于忽略大小写比较文本：`"Yes".lower() == "yes"`。

---

字符串是**不可变的**：一旦创建，它的字符就不能被修改。
对索引赋值会引发 `TypeError`：
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
要"修改"一个字符串，你需要构建一个新的字符串，例如使用切片和拼接，然后存储到变量中：
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

用户输入的文本周围经常带有多余的空格。
`strip()` 方法返回一个**去除首尾空白字符**（空格、制表符和换行符）的字符串副本：
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
文本中间的空格会被保留。
`lstrip()` 只去除左侧，`rstrip()` 只去除右侧。

---

`split()` 将字符串拆分成一个**列表**片段。
不带参数时按空白字符拆分；带参数时按该分隔符拆分：
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` 做相反的事：将列表中的元素粘合成一个字符串。
它在**分隔符**上调用，列表作为参数：
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` 返回一个字符串副本，其中**每一处** `old` 都被替换为 `new`：
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
由于字符串是不可变的，如果想保留结果，记得把它存储起来。

---

`find(sub)` 返回 `sub` 第一次出现的**索引**，如果没有找到则返回 `-1`：
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` 返回 `sub` 出现的**次数**：
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` 和 `endswith(suffix)` 会根据字符串的开头或结尾返回 `True` 或 `False`：
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
这是检查文件扩展名、协议或前缀的常用方法。

---

有些字符不能直接输入到字符串中。
**转义序列**是一个反斜杠 `\`，后面跟着一个代表特殊字符的字母或符号：

- `\n` 换行
- `\t` 制表符
- `\"` 双引号字符串中的一个双引号
- `\'` 单引号字符串中的一个单引号
- `\\` 一个字面意义上的反斜杠

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
打印：
```
Line 1
Line 2
She said "hi"
```
每个转义序列都算作**一个**字符，即使你输入了两个。

---

跨越**多行**的字符串可以用**三引号** `"""..."""`（或 `'''...'''`）书写。
引号内的每个换行都会成为字符串的一部分，所以你不需要用 `\n`：
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
打印：
```
Roses are red,
Violets are blue
```
三引号字符串还可以自由包含单引号和双引号。

---

由于每个字符串方法都会返回一个新的字符串，你可以将多个方法**串联**起来依次调用。
每次调用都作用于前一次的结果：
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
切片还可以接受第三个值，即**步长**。
步长 `-1` 会反向遍历字符串，这是反转字符串的经典技巧：
```python
print("abc"[::-1])  # cba
```

---

**slug** 是标题的 URL 友好版本：小写、两端没有空格，单词之间用短横线分隔，例如 `hello-world`。
构建它只需要串联你已经学过的方法：`strip()`、`lower()` 和 `replace()`。
