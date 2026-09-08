非常によくあるタスクは、既存のリストから新しいリストを作ることです。
`for` ループと `append()` を使うと数行かかります。
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Pythonにはまさにこの用途のためのより短い形式があります。**リスト内包表記**で、リスト全体を1つの式で構築します。
```python
doubled = [n * 2 for n in nums]
```
構文は `[expression for item in iterable]` です。`for` の部分が要素をループし、左側の式が各要素に対して評価されます。
結果はループで作ったものとまったく同じ、新しいリストです。

---

左側の式は、値を生み出すものであれば何でも構いません。計算、関数呼び出し、メソッド呼び出しなどです。
ループ変数には好きな名前を付けられ、それは角括弧の中だけに存在します。
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

内包表記は要素を**フィルタリング**することもできます。
`for` の後に `if` 条件を追加すると、条件が `True` になった要素だけが新しいリストに入ります。
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
これは中に `if` を持つループと同じであり、lambdaを使った `filter()` をより読みやすい形で置き換えます。

---

フィルタ条件は、`len()` のような関数呼び出しを含む、ブール値を返す任意の式にできます。
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

イテラブルはリストである必要はありません。ループできるものなら何でも使え、`range()` はその代表例です。
数値のリストを作る最も手早い方法です。
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
`range(start, stop)` は `stop` を含まないことを覚えておいてください。

---

内包表記は**文字列の変換**にも最適です。
各要素に対して文字列メソッドを呼び出したり、f文字列で新しい文字列を組み立てたりできます。
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

内包表記の中では、それより前に定義された変数を、例えば `range()` の上限として使うことができます。

---

要素を取り除くのではなく、一部の要素に**別の値**を選びたいこともあります。
`for` の左側の式として、条件式 `a if condition else b` を使います。
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
位置に注目してください。`if-else` は `for` の**前**にあって必ず値を生成し、フィルタの `if` は `for` の**後**にあって `else` を持ちません。

---

2つの条件を同じ内包表記の中で組み合わせることができます。値を選ぶための `if-else` と、一部の要素を取り除くための末尾のフィルタ `if` です。
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

`if` の 2 つの位置は混同しやすいので、区別して覚えましょう:
```python
values = [n if n > 0 else 0 for n in nums]  # for の前の if-else: 値を選ぶ。else は必須
positives = [n for n in nums if n > 0]      # for の後の if: フィルタする。else は使えない
```
フィルタの `if` の後に `else` を置くと構文エラーになります。

---

内包表記は**複数の `for`** を持つことができます。
これらはネストしたループのように動作し、最初の `for` が外側のループ、2番目が内側のループになります。
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

内側の `for` は外側のものの変数を使うことができます。
これはリストのリストを1つのリストに**平坦化**する定番の方法です。
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
そして `sum()` 関数がリストの数値をすべて合計します。

---

**辞書**に対してもループすることができます。
`.items()` を使うと、`for` の部分が各ペアをキーと値の2つの変数に展開します。
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

同じ考え方は辞書にも通用します。**辞書内包表記**は波括弧と `key: value` の式を使います。
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

`key: value` の部分が**ない**波括弧は、**集合内包表記**になります。
集合（set）は順序を持たず、一意な値だけを保持するコレクションなので、重複は自動的になくなります。
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**いつ内包表記を使うべきでしょうか？**
結果がリスト（または辞書、集合）で、ロジックが読みやすい1行に収まるとき、つまり単純な変換や任意のフィルタのときに最適です。
複数の文が必要だったり、ネストした `for` が2つを超えたり、行が読みにくくなったりする場合は、代わりに普通の `for` ループを書いてください。コードは長くなりますが、より明確になります。
内包表記はまた、lambdaを使った `map()` や `filter()` のほとんどの用途を置き換えます。
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
