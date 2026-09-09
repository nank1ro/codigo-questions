ときどき、変数がまだ保持する**値を持たない**ことがあります：ログインしていないユーザー、何も見つからなかった検索、一度も選択されていない設定。Python はこれを特別な値 `None` で表します。
`None` は他の値と同じように扱える値です：代入も、printも、関数に渡すこともできます。その型は `NoneType` で、プログラム全体に `None` は**1つ**しか存在しないため、書いたすべての `None` は同じオブジェクトを参照します：
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` は `0` でも、空文字列でも、`False` でもありません：「ここには何もない」ことを意味する独立した値です。

---

すべての関数呼び出しは値を生み出します。たとえ関数が何も返していないように見えてもです。`return` 文が**ない**関数や、裸の `return` だけの関数は `None` を返します：
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
これが `print(my_list.append(3))` が `None` と表示される理由です：`append` はリストをその場で変更し、何も返しません。
動作だけを行う関数（print、保存、リストの変更）は通常 `None` を返し、何かを計算する関数は明示的に `return` しなければなりません。

---

変数が `None` を保持しているかを調べるときは、`==` ではなく `is` と `is not` を使います：
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` は「これらの値は*等しいか*？」を尋ねます。そしてどのクラスも `__eq__` メソッドを定義することで、その問いに独自の方法で答えることができます。`is` は「これらは*同じオブジェクト*か？」を尋ねます。その答えを変えることは誰にもできません。
`None` は1つしか存在しないので、`is None` は常に正しく、少し速くなります。一方、`== None` はカスタムの `__eq__` を持つオブジェクトに対して驚くような答えを返すことがあります。

---

`None` は条件の中で**偽**として扱われるため、`value` が `None` なら `if not value:` は `True` になります。これを `None` チェックとして使いたくなりますが、同じテストは `0`、`""`、`[]` およびその他のすべての空の値に対しても `True` になります：
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
「値がない」ことと「値が空である」ことを別々に扱わなければならないときは、まず `is None` をチェックし、それから真偽値を調べます：
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
`if not value:` を使うのは、`None` と空の値を本当に同じように扱いたいときだけにしてください。

---

引数には**デフォルト値**を持たせることができます。これは呼び出し側が引数を省略したときに使われます。「提供されなかった」ことのデフォルトとしては、通常 `None` が使われます：
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
これはリストや辞書で問題になります。デフォルト値は関数が定義されるときに**一度だけ**評価されるため、`def add(item, items=[])` は `items` を省略したすべての呼び出しで同じリストを共有し、アイテムが蓄積していきます。解決策は、デフォルトを `None` にして、関数の中で新しいリストを作ることです：
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

`[]` で辞書から存在しないキーを読もうとすると、`KeyError` が発生します。`get` メソッドは安全な代替手段です。キーが存在すればその値を返し、存在しなければ `None` を返します：
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` は第2引数を受け取ります。キーが見つからないときに `None` の**代わりに**返す値です：
```python
print(ages.get("Grace", 0))  # 0
```
これは、日常のコードで `None` が現れる最も一般的なケースです。何も見つからなかった検索です。

---

数値**または** `None` を返す関数は、シグネチャでそれを明示すべきです。**型ヒント**は、期待される型を文書化する注釈です。パラメータには `name: str`、戻り値には `-> int` のように書きます。Python はヒントを強制しませんが、エディタや読み手はそれを頼りにします：
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` は「`int` または `None`」と読みます。古い書き方である `typing` モジュールの `Optional[int]` はまったく同じ意味で、既存のコードではまだ出会うことになります。
シグネチャに `| None` を見つけたら、その結果を使う前に必ずチェックすることを忘れないでください。

---

`None` を受け取る可能性のある関数は、しばしば**ガード**から始まります。これは、作業すべきものがないときに早く返す `if` です。こうすることで、関数の残りの部分では、すべてを `else` の中に入れ子にせずに、値が存在すると仮定できます：
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
ガードは最初に、チェックが行われなければならない順序で置きます。`text` が `None` でないと分かる前に `text.split()` を呼ぶことはできません。

---

`or` 演算子は `True` や `False` を返すのではありません。左のオペランドが真であればそれを返し、そうでなければ右のオペランドを返します。これにより、フォールバックを提供する1行の方法が得られます：
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
落とし穴は、`or` が `None` ではなく真偽値を見ることです：`0`、`""`、`[]` もフォールバックに置き換えられます。`x or fallback` を使うのは、すべての空の値もフォールバックになってよいときだけにしてください。

---

`0` や `""` を保持し、`None` だけを置き換えなければならないとき、フォールバックには明示的な `is None` チェックが必要です。コンパクトな形が**条件式**です。`a if condition else b` は、条件が真のとき `a` に、そうでなければ `b` に評価されます：
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

リストには、実際の値の隣に `None` が含まれることがあります。たとえば、失敗した測定値やスキップされた回答です。ほとんどの操作は `None` を受け付けません：`sum([8, None])` は `TypeError` を発生させます。
条件が `is not None` のリスト内包表記で、`None` の値を取り除きます：
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
代わりに `if r` を使うと、すべての `0` も取り除かれてしまいます。ゼロが有効な測定値であるときは、明示的に書いてください。

---

検索の後に `None` チェックが続くとき、通常は2行必要です。結果を保存する1行と、それをテストする1行です。**代入式**の演算子 `:=` は*セイウチ*と呼ばれ、式の**中**で値を代入するので、両方のステップが `if` に収まります：
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
括弧は必須です。括弧がないと、`:=` は比較全体を代入しようとしてしまいます。`if` の後も、`age` は他の変数と同じように使えます。

---

すべての「見つからない」が `None` で報告されるわけではありません。古い関数の一部は、代わりに**センチネル**値を返します。これは特別な意味を与えられた通常の値です。文字列メソッドの `find` は部分文字列のインデックスを返し、見つからなければ `-1` を返します：
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
`re` モジュールの `re.match(pattern, text)` 関数は、`text` が `pattern` で始まるかをチェックし、マッチオブジェクトを返します。マッチしなければ `None` を返します。
`None` の方が安全な規約です：`-1` は有効なインデックスなので、`text[text.find("x")]` は失敗する代わりに黙って最後の文字を返してしまいます。一方、`None` をインデックスとして使うとすぐにエラーが発生します。

---

`None` は順序付けできません：`None < 1` は `TypeError` を発生させます。Python には「無」が数値より小さいか大きいかを見当もつかないからです。
これが問題になるのは、`None` が検索の開始値として使われるときです。たとえば「これまでに見つけた最良の値（もしあれば）」です。すべての比較は、**最初に**置かれた `is None` チェックで保護されなければなりません。そうすることで `or` が短絡し、まだ比較すべきものがないときは比較がスキップされます：
```python
if best is None or value > best:
    best = value
```
逆の順序で書いた `value > best or best is None` は、最初の繰り返しで `None` との比較を行い、クラッシュしてしまいます。
