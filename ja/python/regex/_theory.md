**正規表現**（regex）は、テキストを記述するための小さなパターン言語です。Pythonでは標準の `re` モジュールで提供されています：
```python
import re
```

`re.search(pattern, text)` はパターンをテキスト内のどこかから探します。何か見つかれば**マッチオブジェクト**を返し、見つからなければ `None` を返します。`match.group()` はマッチしたテキストの断片を返します：
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

ここではパターンの2つの要素が働いています。`\d` は*任意の数字*を意味し、`+` は*直前の項目の1回以上の繰り返し*を意味します。つまり `\d+` は「1つ以上の数字」と読めます。他にも便利な省略記法として `\w`（英字、数字、アンダースコア）や `\s`（空白、タブ、改行）があります。

パターンは、引用符の前に `r` を付けた**raw文字列**として書きます。通常のPython文字列ではバックスラッシュがエスケープシーケンスの始まりを意味するため、`"\d"` は警告のもとになり、`"\n"` は正規表現エンジンが期待する2文字ではなく実際の改行になってしまいます。`r` 接頭辞はバックスラッシュを普通の文字に戻すので、`r"\d"` がそのままエンジンに渡されます。パターンには常に `r"..."` を使用してください。

---

`re.search` はテキスト全体を走査しますが、`re.match` はテキストの**先頭**でだけパターンを試します：
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

どちらもマッチしなければ `None` を返し、マッチオブジェクトは常にtruthyなので、「マッチしたか？」を確かめる一般的な方法はシンプルな `if` です：
```python
if re.search(r"\d", text):
    print("there is a digit")
```
本物の `True` や `False` が必要なときは、`is not None` と比較するか、呼び出しを `bool(...)` で囲みます。

---

3つ目のエントリーポイントとして `re.fullmatch` があります。これは最初の文字から最後の文字までパターンがテキスト**全体**をカバーするときにだけ成功します。バリデーションに適したツールです：
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

つまり3つの関数が違うのは、パターンがどこに置かれることを許すかだけです。`re.match` はテキストの先頭、`re.search` はテキスト内のどこでも、`re.fullmatch` はテキスト全体です。

---

マッチオブジェクトはマッチしたテキスト以上の情報を持っています。`.group()` のほかに、元の文字列の中でのマッチの位置も提供します：
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` はマッチした最初の文字のインデックス、`.end()` は最後の文字の直後のインデックスで、`.span()` はその両方をタプルで返します。つまり `text[match.start():match.end()]` は常に `match.group()` と等しくなります。

`re.search` は `None` を返すことがあるため、何もマッチしなかったときに `.group()` をすぐに読むと `AttributeError` が発生します。まず結果を確認してください。

---

パターン内の丸括弧は**キャプチャグループ**を作成します。これはマッチの一部を、後から単独で読み取れるようにしたものです。グループには左から右へ、`1` から番号が付きます：
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` は `match.group()` とまったく同じくマッチ全体を表し、`match.groups()` はすべてのグループをタプルで返します。存在しないグループ番号を要求すると `IndexError` が発生します。

---

括弧を数えてグループ `3` を探すのはすぐに面倒になります。グループには `(?P<name>...)` で名前を付け、`match.group("name")` で読み取ることができます：
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` はすべての名前付きグループを辞書として返します。名前付きグループも番号を持っているため、`match.group(1)` は依然として機能します。

この例では、波括弧を使った**量指定子**も登場しています。`\d{2}` はちょうど2桁、`\d{2,4}` は2〜4桁、`\d{2,}` は2桁以上を意味します。これらは `+`（1回以上）、`*`（0回以上）、`?`（0回か1回）のより正確なバージョンです。

---

角括弧は**文字クラス**を定義します。文字の集合を表し、その位置でいずれか1文字が受け入れられます。`[aeiou]` は母音1文字、`[0-9]` は数字1文字、`[a-z]` は小文字の英字1文字にマッチします。開き括弧の直後の `^` は意味を反転させ、`[^0-9]` は数字*以外*の任意の文字にマッチします。

文字クラスの外では、`^` と `$` は**アンカー**です。`^` はパターンをテキストの先頭に、`$` は末尾に結び付けます。`re.fullmatch` ではアンカーが暗黙に含まれるため、バリデーションはそちらの方が読みやすくなります：
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` は最初のマッチで止まります。`re.findall(pattern, text)` はその代わりに**すべての**マッチを集め、文字列のリストとして返します：
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
何もマッチしないときリストは空になるため、チェックすべき `None` はありません。そのままループで回したり `len(...)` で測ったりできます。`findall` はマッチオブジェクトではなく普通の文字列を返すため、位置は利用できないことに注意してください。

---

すべてのマッチの位置やグループが必要なときは、`re.finditer(pattern, text)` が適切な呼び出しです。テキストをたどりながら、マッチごとに**マッチオブジェクト**を1つずつ生成します：
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` はリストではなくイテレータを返すため、`for` ループや内包表記で使えます。`findall` がテキストだけを返すのに対し、`finditer` はマッチオブジェクトが知っているすべてを提供します。

---

パターンにキャプチャグループが含まれると、`findall` は動作を変えます。グループがちょうど1つの場合はマッチ全体ではなくそのグループの内容を返し、2つ以上の場合はマッチごとにグループのタプルを返します：
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
これは覚えておく価値があります。グルーピングのためだけにパターンへ括弧を加えると、`findall` の戻り値が静かに変わってしまいます。`re.finditer` はマッチオブジェクトが常にマッチ全体とグループの両方を保持するため、このような動作にはなりません。

---

`re.sub(pattern, replacement, text)` は、すべてのマッチを置き換えた新しい文字列を返します。文字列はイミュータブルなので、元のテキストはそのまま残ります：
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

置換文字列は `\1`、`\2`、... でキャプチャグループを後方参照できます（名前付きグループは `\g<name>`）。これによりテキストの並べ替えが1行で書けます。同じバックスラッシュの理由から、置換文字列もraw文字列にします：
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
`count` 引数は置き換えるマッチの数を制限します。`re.sub(r"\d", "#", "1 2 3", count=1)` は `# 2 3` になります。

---

`re.sub` に渡す置換は**関数**にすることもできます。マッチごとに1回呼び出され、マッチオブジェクトを受け取り、その場所に置く文字列を返す必要があります。これが、置換をマッチした内容に依存させる仕組みです：
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
関数は括弧なしで、名前によって渡されます。`shout(match)` と書くと、`re.sub` に渡す代わりにその場で呼び出されてしまいます。

---

`str.split` は固定のセパレーターでしか分割できません。`re.split(pattern, text)` はパターンが記述する任意のものを区切りとして分割できます。これは乱れた入力で通常必要とされる動作です：
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
セパレーターを `[,;\s]+` と書くと、カンマ、セミコロン、空白の連なり全体が1回の分割として数えられ、それらの間に空文字列が残らなくなります。

`maxsplit` 引数は指定した回数の分割で止まり、テキストの残りを最後の要素に残します。`re.split(r"\s+", "a b c", maxsplit=1)` は `['a', 'b c']` になります。

---

`re.search` や `re.findall` を呼び出すたびに、まず内部キャッシュでパターン文字列を調べる必要があります。`re.compile(pattern)` はその検索を省き、同じメソッドを持つ**パターンオブジェクト**を返します：
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
パターンはすでにオブジェクトに組み込まれているため、残る引数はテキストだけです。コンパイルは、たとえばループの中のように同じパターンを何度も使うときに効果を発揮し、またパターンに何にマッチするのかを説明する名前を与えることもできます。

---

**フラグ**はパターンの適用方法を変えます。`re` のすべての関数は `flags` 引数としてフラグを受け入れ、`re.compile` はフラグをパターンオブジェクトに保存します：
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
最もよく使われる2つは、英字をどの大文字小文字でもマッチさせる `re.IGNORECASE` と、`^` と `$` をテキスト全体ではなく各行の先頭と末尾でマッチさせる `re.MULTILINE` です。複数のフラグは `re.IGNORECASE | re.MULTILINE` のように `|` で組み合わせます。

フラグが変えるのはマッチングのルールだけです。返されるテキストは、常に実際にそこにあった元の大文字小文字のままのテキストです。
