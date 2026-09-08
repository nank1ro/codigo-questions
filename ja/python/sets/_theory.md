**セット（set）**は**一意**な要素のコレクションです：同じ値は何回書いても一度しか現れません。
セットはまた**順序を持たず**：最初や最後の要素というものがないため、インデックスで要素を読み取ることはできません。
セットは、値が*何回*あるか、*どの位置*にあるかではなく、*どの*値が存在するかだけが重要な場合に最適です。
波括弧 `{...}` の間に要素を書くことでセットを作成します：
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
重複した `"red"` は削除されるため、`len()` は個別の要素だけを数えます。

---

組み込み関数 `set()` は、リストや文字列など任意のコレクションからセットを構築します。
セットは各値を一度しか保持しないため、これは**重複を取り除く**ための定番の方法です：
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
値が含まれているかどうかを確認するには `in` 演算子を使います。これは `True` か `False` を返します：
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
セットに対するメンバーシップの確認は、要素が数千個あっても非常に高速です。

---

**空のセット**を作成する際には落とし穴があります。
波括弧は辞書の構文でもあるため、`{}` は空の**辞書**を作成し、セットにはなりません：
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
空のセットを得るには、引数なしで `set()` を呼び出す必要があります：
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

セットは**ミュータブル（変更可能）**です：作成した後でも要素を追加したり削除したりできます。
`add(value)` は値を挿入します。すでに存在する値を追加しても何も変わりません：
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
要素を削除する方法は2つあります：
- `remove(value)` は要素を削除しますが、その値がセットに存在しない場合は `KeyError` を発生させます
- `discard(value)` は存在すれば削除し、存在しなくても**何もせず**エラーになりません
```python
letters.remove("a")
letters.discard("z")  # "z" is not there, but no error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` はセットから**任意の要素**を削除し、それを返します。
セットには順序がないため、どの要素が削除されるかを選ぶことはできません。空のセットに対して `pop()` を呼び出すと `KeyError` が発生します：
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` は**すべて**の要素を削除し、空のセットを残します：
```python
tickets.clear()
print(len(tickets))  # 0
```

---

リストとまったく同じように、`for` を使ってセットをループ処理できます：
```python
for color in {"red", "blue"}:
    print(color)
```
セットは順序を持たないため、要素は**任意の順序**で出てくる可能性があり、その順序は実行のたびに変わることさえあります。
決まった順序が必要な場合は、セットを `sorted()` に渡してください。これは要素を並べ替えた**リスト**を返します：
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

2つのセットの**和集合（union）**は、**両方**の要素を重複なく含む新しいセットです。
`|` 演算子または `union()` メソッドを使います：
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
`a` も `b` も変更されません：セット演算は常に新しいセットを返します。

---

2つのセットの**積集合（intersection）**は、**両方**に存在する要素だけを含みます。
`&` 演算子または `intersection()` メソッドを使います：
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
セットに共通の要素がない場合、結果は空のセットになります。

---

**差集合（difference）** `a - b` は、`a` の要素のうち `b` に**含まれない**ものです。
順序が重要です：`a - b` と `b - a` は通常異なります：
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
**対称差（symmetric difference）** `a ^ b` は、2つのセットの**どちらか一方だけ**に含まれる要素です：
```python
print(a ^ b)  # {1, 4}
```
メソッド形式は `difference()` と `symmetric_difference()` です。

---

演算子とメソッドは完全に同等というわけではありません。
`|`、`&`、`-`、`^` 演算子は、**両方**のオペランドがセットである場合にのみ機能します。
`union()`、`intersection()`、`difference()`、`symmetric_difference()` メソッドは、リストや文字列のような**任意のイテラブル**を受け付けます：
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

セット同士は**比較**することもできます。
`a.issubset(b)`、または `a <= b` は、`a` のすべての要素が `b` にも含まれる場合に `True` になります。
`a.issuperset(b)`、または `a >= b` は、`a` が `b` のすべての要素を含む場合に `True` になります。
`a.isdisjoint(b)` は、2つのセットに共通する要素が**1つもない**場合に `True` になります：
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

セットには**ハッシュ可能**な要素、つまり変更できない値しか含められません：数値、文字列、`True`/`False`、そして**タプル**です。
リスト、辞書、または別のセットを追加しようとすると `TypeError` が発生します：
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
タプルのセットは、座標や (name, age) のような一意なペアを管理するのに便利です：
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

**frozenset** は**イミュータブル（不変）**なセットです：一度作成すると、要素を追加したり削除したりできません。
任意のコレクションから `frozenset()` を使って作成します：
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
frozenset を出力すると、`frozenset({'sat', 'sun'})` のように要素の周りに型名が表示されます。
変更できないため、frozenset はハッシュ可能です：通常のセットと違い、別のセットの要素や辞書のキーになれます。
読み取り専用の操作（`in`、`len()`、`|`、`&`、`-`、`^`、比較）はすべて通常どおり動作します。

---

**集合内包表記（set comprehension）**は、リスト内包表記と同じ構文で波括弧を使い、1つの式でセットを構築します：
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
オプションの `if` で要素をフィルタリングでき、式によって生成された重複は自動的に取り除かれます：
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

セット演算は、新しいセットを返す代わりに**その場で（in place）**セットを変更することもできます。
`update(iterable)` は、任意のコレクションのすべての要素を追加します。`add()` に似ていますが、一度に多くの値を追加できます：
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
複合代入演算子もその場で動作します：`|=` は別のセットの要素を追加し、`&=` は共通の要素だけを残し、`-=` は別のセットの要素を削除します：
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

2つのセットは、書かれた順序に関係なく同じ要素を含んでいれば**等しい**とみなされます：
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
コレクションの長さとそのセットの長さを比較するのは、重複を検出する手早い方法です：セットの方が**小さい**場合、何らかの値が複数回出現しています：
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
リストのメソッド `count(value)` は、ある値が何回出現するかを教えてくれるので、*どの*値が重複しているかを見つけるのに役立ちます。
