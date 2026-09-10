比較演算子は2つの値を比較し、**ブール値** `True` または `False` を返します。`==` は等しい、`!=` は等しくない、`<` は未満、`>` は超える、`<=` は以下、`>=` は以上を表します:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
結果は変数に格納することも、そのまま出力することもできます。単独の `=` は代入であり、比較ではありません。

---

比較演算子は数値に限りません。文字列はコードポイントを使って1文字ずつ比較されるため、`"apple" < "banana"` は `True` であり、大文字はすべて小文字より前に来るので `"Zoo" < "apple"` も `True` になります。リストとタプルも同じように要素ごとに比較されます:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
比較は式なので、関数は `if` で包まずに直接 `return a < b` と書けます。

---

比較は**連鎖**できます。`1 < x < 10` は `x` が `1` より大きく **かつ** `10` 未満であることを調べ、`1 < x and x < 10` とまったく同じですが、`x` は一度しか評価されません:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
どの比較演算子も連鎖でき、それぞれが両隣に適用されます。`a < b == c` は `a < b and b == c` を意味します。連鎖を範囲 `low < x < high` として読むのが最も一般的な使い方です。

---

論理演算子はブール値を組み合わせます。`and` は両辺が `True` のときだけ `True` になり、`or` は少なくとも一方が `True` のとき、`not` は1つの値を反転します:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
比較は論理演算子より優先順位が高いので、`age >= 18 and member` に括弧は不要です。`and` の中に `or` をまとめるには括弧が必要です: `a and (b or c)`。

---

`not`、`and`、`or` が1つの式に現れると、Python はまず `not`、次に `and`、最後に `or` を適用します。つまり `a or b and c` は `a or (b and c)` を意味し、`not a == b` は `not (a == b)` を意味します:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
別のまとめ方を意図する場合は括弧を追加します。括弧は式を読みやすくもします。

---

すべての値は**真理値**を持ちます。`bool(value)` は `0`、`0.0`、`None`、空文字列 `""`、そして `[]`、`{}`、`set()` のような空のコンテナに対して `False` を返します。それ以外の値はすべて真であり、`"0"` や `[0]` も含まれます:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`、`while`、`and`、`or`、`not` はこの規則を使うので、`if items:` はリストが空でないことを、`not name` は文字列が空であることを調べます。`len(items) > 0` や `name == ""` と書く必要はありません。

---

`if value:` はすでに真理値を適用しているので、`== True` や `== False` との比較は不要であり、誤りにもなり得ます。`2 == True` は `False` ですが、`2` は真です。値そのものを判定してください:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` と `or` は常に `True` や `False` を返すわけではなく、**オペランド**のいずれかを返します。`a and b` は `a` が偽ならば `a` を、そうでなければ `b` を返します。`a or b` は `a` が真ならば `a` を、そうでなければ `b` を返します:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
結果が真か偽かは式全体の真偽とちょうど一致するので、`if a and b:` はそのまま機能します。よくある使い方はデフォルト値です: `name = user_input or "guest"`。

---

論理演算子は**短絡評価**を行います。結果がすでに決まるため、`and` はオペランドが偽になった時点で、`or` は真になった時点で止まります。残りのオペランドは評価されないので、関数呼び出しであれば実行されません:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` は**値**を比較し、`is` は**同一性**、つまり2つの名前がまったく同じオブジェクトを指しているかを比較します。別々に作られた等しい2つのリストは `==` ですが `is` ではありません:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` は `None`、`True`、`False` のようなシングルトン向けです。`value is None` や `value is not None` と書き、`value == None` とは決して書きません。クラスは `==` が何でも返すように定義できるからです。数値や文字列に `is` を使うのは信頼できず、Python は警告を出します。

---

短絡評価は、一部の値で失敗する処理を**ガード**する安全な方法です。`word is not None and len(word) < 4` では、`len(word)` は `word` が `None` でないときにだけ実行されるので、呼び出しが例外を送出することはありません。ガードは先に書かなければなりません:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
`and` はオペランドを返すことに注意してください。`word and len(word) < 4` は `None` に対して `None` を、空文字列に対して `""` を返し、`False` にはなりません。ブール値が必要なときは本物の比較でガードしてください。

---

`in` 演算子は**所属**を調べます。要素がリスト、タプル、集合に含まれるか、部分文字列が文字列に含まれるか、キーが辞書に含まれるかを判定します。`not in` はその否定です:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
どちらもブール値を返し、英語のように読めるため、ループを書く代わりに所属を調べる方法として好まれます。
