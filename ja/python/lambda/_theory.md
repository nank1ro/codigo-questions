数値を2倍にするような、一度きりしか使わない小さな関数が必要になることがあります。
そのために完全な `def` ブロックを書くのは大げさに感じます。
Pythonにはもっと短い形式があります。**lambda** 式で、1行で書かれる _無名_ 関数です。
```python
lambda x: x * 2
```
構文は `lambda parameters: expression` です。
lambdaには名前がありませんが、変数に格納して他の関数と同じように呼び出すことができます。
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

lambdaの本体には `return` キーワードがないことに注目してください。
本体は**単一の式**であり、その値は自動的に返されます。
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

lambdaは**複数のパラメータ**を取ることができます。
`def` 関数の場合とまったく同じように、カンマで区切ります。
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

本体は単一の式でなければならないため、lambdaは**文を含むことができません**。
`return` も `if` ブロックも、ループも代入もありません。
```python
# SyntaxError
increment = lambda x: return x + 1
```
これらが必要な場合は、代わりに通常の `def` 関数を書いてください。

---

lambdaのパラメータも**デフォルト値**をサポートします。
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

lambdaを格納する必要すらありません。**即座に呼び出す**こともできます。
lambdaを括弧で囲み、その後に引数を追加します。
```python
print((lambda x: x + 1)(4))  # 5
```

---

lambdaが本当に輝くのは**他の関数への引数**として使われるときです。
`sorted()` は `key` パラメータを受け取ります。これは各アイテムに対して呼び出される関数で、その結果が順序を決定します。
lambdaはまさにぴったりです。
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

`key` に渡すlambdaは、アイテムのどの部分でも選ぶことができます。
リストのリストの場合、`lambda p: p[1]` は各内側のリストの2番目の要素でソートします。

---

`map()` はリストの**すべてのアイテム**に関数を適用します。
これは特別な _mapオブジェクト_ を返すので、値を見るには `list()` で包んでください。
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` は関数が `True` を返すアイテムだけを残します。
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

`map` オブジェクトをそのまま出力しても値は表示されず、`<map object at 0x7f2b1c>` のような結果になります。
`list()`（またはループ）を使って初めて期待した値が得られます。

---

lambdaは組み込み関数だけに限られません。**あなた自身の関数**も関数をパラメータとして受け取り、それを呼び出すことができます。
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` と `min()` も、`sorted()` と同じように `key` 関数を受け取ることができます。
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**では、いつ `def` を使うべきでしょうか？**
lambdaは、引数として渡す短い使い捨ての関数に最適です。
ロジックに名前、複数行、docstring が必要な場合や、多くの場所で再利用される場合は、`def` 関数の方が明確です。
最後にもう一つ：`sorted()` は `reverse=True` も受け取ることができ、最大の値から先に取得できます。
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
