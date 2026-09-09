Pythonでは関数は**値**であり、数値や文字列と同じものです。変数に格納したり、リストに入れたり、別の関数に渡したりできます。呼び出すのは丸括弧だけで、`shout` は関数そのもの、`shout("hi")` はその結果です：
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
別の関数をパラメータとして受け取る、または返す関数は**高階関数**と呼ばれます。その内部では、パラメータは他の関数と同じように丸括弧を付けて呼び出されます：
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

関数を引数として渡すと、呼び出し側が**何を**するかを決め、高階関数が**何回**、**何に対して**行うかを決められます。関数パラメータは必要な回数だけ呼び出すことができ、その結果を関数自身に戻すこともできます：
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
どんな呼び出し可能オブジェクトでも使えます。`def` で定義した関数、`len` のような組み込み関数、`lambda` などです。

---

組み込みの `map(func, iterable)` はすべての要素に対して `func` を呼び出し、要素ごとに1つの結果を生成します。*mapオブジェクト* という遅延オブジェクトを返すので、値を見るには `list()` で包みます：
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
lambdaだけでなく、どんな呼び出し可能オブジェクトでも渡せます。`len` のような組み込み関数や、そのクラスから取り出したメソッド、たとえば文字列を最初の引数として取る `str.upper` などです：
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

組み込みの `filter(func, iterable)` は、`func` が真の値を返す要素だけを残します。`map` と同じように、リストに変換する必要がある遅延オブジェクトを返します：
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
`filter` に渡す関数は**述語**と呼ばれます。1つの要素を受け取り、その要素についてのはい/いいえの質問に答えます。関数の代わりに `None` を渡すと、それ自体が真の要素だけが残り、`0`、`""`、`None` は捨てられます。

---

`sorted(iterable, key=func)` は、各要素に対して `func` が返す値に基づいて要素を並べ替えます。要素そのものは変わりません。`reverse=True` を追加すると、大きいものから順になります：
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
ソートは**安定**です。キーが等しい要素は元の順序を保ちます。`key` 関数は要素ごとに1回呼び出され、その結果は比較にのみ使われるので、出力には元の単語がそのまま含まれ、長さにはなりません。

---

`key` 関数は要素の**任意の部分**を取り出せます。タプルのリストでは `lambda s: s[1]` が各タプルの2番目の項目で並べ替え、辞書のリストでは `lambda d: d["age"]` がある値で並べ替えます：
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` と `max` は同じ `key` パラメータを受け取るので、`max(pairs, key=lambda p: p[1])` は `('a', 3)` を返します。数値だけではなくタプル全体です。

---

関数は関数を**返す**こともできます。`def` で内部関数を定義し、呼び出さずに返します：
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
内部関数は、`make_greeter` が終了した後も `greeting` を使い続けます。自分が作られたスコープの変数を**覚えて**いるのです。このような関数は**クロージャ**と呼ばれます。`make_greeter` を呼び出すたびに、それぞれ独自の `greeting` を持つ新しい独立したクロージャが作られます。

---

クロージャは外側の関数の変数を読むことはできますが、その変数に代入すると代わりに**新しいローカル**変数が作られます。外側の変数を更新するには、内部関数の中で `nonlocal` を付けて宣言します：
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` はモジュールレベルで `count` を探しますが、そこには存在しません。`nonlocal` を使うと、返された関数を呼び出すたびに同じ `count` が更新されるので、クロージャは小さなオブジェクトのように呼び出しの間で状態を持ち運びます。

---

`functools` モジュールの `reduce(func, iterable, initial)` は、シーケンスを**1つの値**に畳み込みます。`initial` から始めて、それまでの結果と次の要素を引数に `func` を呼び出します：
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
ステップは `0 + 1`、次に `1 + 2`、次に `3 + 3` と進みます。`initial` を省略すると最初の要素が開始値として使われますが、その場合、空のシーケンスは `TypeError` を発生させるので、シーケンスが空かもしれないときは必ず初期値を渡してください。

---

`functools` の `partial(func, *fixed)` は、一部の引数が**すでに埋められた**新しい関数を作ります。結果の関数を呼び出すと、残りの引数を渡します：
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
`partial` に渡した位置引数は最初のパラメータを埋めます。キーワード引数は名前でパラメータを固定しますが、呼び出し時に上書きすることもできます。partialは普通の呼び出し可能オブジェクトなので、`map`、`sorted`、その他の高階関数に渡せます。

---

`partial` はオプションを取る組み込み関数と相性が良いです。`int(text, base=16)` は16進数の文字列を解析します。baseを固定すると、`map` にぴったりの1引数の変換関数が得られます：
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
partialオブジェクトは包んでいるものを覚えています。`hex_to_int.func` は `int` で、`hex_to_int.keywords` は `{'base': 16}` です。

---

**デコレータ**は、関数を受け取ってそれを包む新しい関数を返す高階関数です。通常は元の呼び出しの前後に振る舞いを追加します：
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` は関数が定義されたときの名前です。デコレータの適用は単なる呼び出しです。`greet = announce(greet)` のように書きます。`def` の**上**の行に置く `@` 構文は、まさにそれを行います：
```python
@announce
def greet(name):
    return "Hello, " + name
```
デコレータは `@` で使う前に定義されていなければなりません。置き換えは `def` が実行されるとすぐに起きるからです。

---

1つの引数しか受け取れないデコレータはほとんど役に立ちません。**どんな**関数でも包めるように、ラッパーはすべての位置引数を `*args` に、すべてのキーワード引数を `**kwargs` に集め、そのまま転送します：
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
ラッパーの中では、`args` はタプル、`kwargs` は辞書です。呼び出しのときの `*` と `**` が、それらを個別の引数に展開し直します。

---

`any(iterable)` は**少なくとも1つ**の要素が真なら `True` を返し、`all(iterable)` は**すべての**要素が真なら `True` を返します。これらは**ジェネレータ式**と自然に組み合わせられます。ジェネレータ式は角括弧を書かないリスト内包表記で、リストを作る代わりに値を1つずつ生成します：
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
値は遅延的に生成されるので、`any` は最初の `True` で、`all` は最初の `False` で停止し、残りを評価しません。`sum` もジェネレータ式を受け取ります。`sum(1 for age in ages if age >= 18)` は大人の人数を数えます。
