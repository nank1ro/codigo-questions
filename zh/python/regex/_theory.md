**正则表达式**（regex）是一种描述文本的小型模式语言。Python 在标准库的 `re` 模块中提供了它：
```python
import re
```

`re.search(pattern, text)` 会在文本的任意位置查找该模式。找到内容时它返回一个**匹配对象**，找不到时返回 `None`。`match.group()` 会返回匹配到的那段文本：
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

这个模式里有两处发挥了作用。`\d` 表示*任意数字*，`+` 表示*前一项的一个或多个重复*，所以 `\d+` 可以读作"一个或多个数字"。其他有用的简写还有 `\w`（字母、数字或下划线）和 `\s`（空格、制表符或换行符）。

模式要写成**原始字符串**（raw string），也就是在引号前加一个 `r`。在普通 Python 字符串里，反斜杠用来开始转义序列，所以 `"\d"` 是个迟早会出问题的写法，而 `"\n"` 会变成真正的换行符，而不是正则引擎所期望的那两个字符。`r` 前缀让反斜杠恢复成普通字符，因此 `r"\d"` 正是引擎接收到的内容。编写模式时请始终使用 `r"..."`。

---

`re.search` 会扫描整个文本，而 `re.match` 只在**最开头**尝试匹配模式：
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

两者在没有匹配到内容时都返回 `None`，而匹配对象永远为真，所以判断"是否匹配？"的常用方式就是一个简单的 `if`：
```python
if re.search(r"\d", text):
    print("there is a digit")
```
当需要真正的 `True` 或 `False` 时，可以用 `is not None` 来比较，或者把调用包在 `bool(...)` 里。

---

还有第三个入口函数 `re.fullmatch`，只有当模式从第一个字符到最后一个字符覆盖**整个**文本时它才会成功。它是做校验的合适工具：
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

因此这三个函数的区别只在于模式允许出现的位置：`re.match` 在文本的开头，`re.search` 在文本的任意位置，`re.fullmatch` 则覆盖整个文本。

---

匹配对象携带的信息不止匹配到的文本。除了 `.group()` 之外，它还提供匹配在原始字符串中的位置：
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` 是第一个匹配字符的索引，`.end()` 是最后一个匹配字符之后那个位置的索引，`.span()` 则把两者作为一个元组返回。这意味着 `text[match.start():match.end()]` 总是等于 `match.group()`。

由于 `re.search` 可能返回 `None`，在没有匹配到任何内容时直接读取 `.group()` 会引发 `AttributeError`；请先检查结果。

---

模式中的圆括号会创建一个**捕获组**：匹配中可以单独读取的一部分。各个组从左到右编号，从 `1` 开始：
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` 是整个匹配，与 `match.group()` 完全一样，`match.groups()` 则以元组的形式返回所有的组。请求一个不存在的组编号会引发 `IndexError`。

---

靠数括号来找第 `3` 个组很快就让人厌烦。可以用 `(?P<name>...)` 给组起一个名字，然后用 `match.group("name")` 读取它：
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` 以字典的形式返回所有的命名组。命名组同样保留编号，所以 `match.group(1)` 仍然可用。

这个示例还使用了带花括号的**量词**：`\d{2}` 表示恰好两个数字，`\d{2,4}` 表示两到四个，`\d{2,}` 表示两个或更多。它们是 `+`（一个或多个）、`*`（零个或多个）和 `?`（零个或一个）的精确版本。

---

方括号定义一个**字符类**：一组字符，在该位置上其中任意一个字符都可以被接受。`[aeiou]` 匹配一个元音字母，`[0-9]` 匹配一个数字，`[a-z]` 匹配一个小写字母。紧跟在左方括号后面的 `^` 会翻转含义，所以 `[^0-9]` 匹配任何*不是*数字的字符。

在字符类之外，`^` 和 `$` 是**锚点**：`^` 把模式固定在文本的开头，`$` 固定在文本的末尾。使用 `re.fullmatch` 时锚点是隐含的，这就是用它做校验可读性更好的原因：
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` 在第一个匹配处就停止。`re.findall(pattern, text)` 则会收集**每一个**匹配，并以字符串列表的形式返回它们：
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
没有匹配时列表为空，因此没有 `None` 需要检查：可以直接对它进行循环，或用 `len(...)` 测量长度。注意 `findall` 返回的是普通字符串而不是匹配对象，所以无法获得位置信息。

---

当需要每个匹配的位置或分组时，`re.finditer(pattern, text)` 是正确的选择：它遍历文本，并为每个匹配逐个产生一个**匹配对象**：
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` 产生的是迭代器而不是列表，因此可以用在 `for` 循环或推导式中。`findall` 只给出文本，而 `finditer` 会给出匹配对象所知道的一切。

---

当模式包含捕获组时，`findall` 的行为会改变。恰好只有一个组时，它返回该组的内容而不是整个匹配；有两个或更多组时，它为每个匹配返回一个由各组组成的元组：
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
这一点值得记住：仅仅为了分组而给模式加上括号，就会悄悄改变 `findall` 的返回结果。`re.finditer` 从不这样表现，因为匹配对象总是同时保留完整匹配和各个分组。

---

`re.sub(pattern, replacement, text)` 返回一个新字符串，其中每个匹配都已被替换。字符串是不可变的，所以原始文本不会被动过：
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

替换内容可以用 `\1`、`\2`……（命名组则用 `\g<name>`）来引用捕获组，这让重排文本变成一行代码。出于同样的反斜杠原因，替换内容也要写成原始字符串：
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
`count` 参数限制被替换的匹配数量：`re.sub(r"\d", "#", "1 2 3", count=1)` 得到 `# 2 3`。

---

传给 `re.sub` 的替换内容也可以是一个**函数**。每个匹配会调用它一次，它接收匹配对象，并必须返回用来放在该处的字符串。这样替换结果就可以取决于匹配到了什么：
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
函数按名称传递，不带括号：写成 `shout(match)` 会立刻调用它，而不是把它交给 `re.sub`。

---

`str.split` 只能按固定的分隔符切分。`re.split(pattern, text)` 可以按模式描述的任何内容切分，这正是混乱输入通常需要的：
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
把分隔符写成 `[,;\s]+` 可以让一整串逗号、分号和空格算作一次切分，而不是在它们之间留下空字符串。

`maxsplit` 参数在切分给定的次数后停止，把剩余的文本留在最后一个元素里：`re.split(r"\s+", "a b c", maxsplit=1)` 得到 `['a', 'b c']`。

---

每次调用 `re.search` 或 `re.findall` 都要先在内部缓存中查找模式字符串。`re.compile(pattern)` 跳过这一查找，返回一个带有相同方法的**模式对象**：
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
此时文本成了剩下的唯一参数，因为模式已经固化在对象里。当同一个模式被多次使用时（比如在循环中），编译会带来收益；它还给模式起了一个名字，说明它匹配的是什么。

---

**标志**（flags）会改变模式的应用方式。`re` 中的每个函数都通过 `flags` 参数接受它们，`re.compile` 则把它们存储在模式对象中：
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
最常用的两个是 `re.IGNORECASE`（让字母无论大小写都能匹配）和 `re.MULTILINE`（让 `^` 和 `$` 匹配每一行的开头和末尾，而不是整个文本）。多个标志用 `|` 组合，例如 `re.IGNORECASE | re.MULTILINE`。

标志只改变匹配规则：返回的文本始终是实际存在的那段文本，保留它原本的大小写。
