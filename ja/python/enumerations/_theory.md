**列挙型**（*enum*）は、曜日や信号機の色のような、関連する固定値のグループに共通の型を定義します。
バラバラの文字列や数値をやり取りする代わりに、各値に**名前**を付けることで、コードが読みやすくなり、打ち間違いはエラーになります。
Pythonでは、`enum` モジュールから `Enum` をインポートし、それを継承するクラスを宣言することで列挙型を作成します。
各クラス属性は、名前と値を持つ列挙型の**メンバー**です：
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
慣例により、メンバー名は大文字で書きます。メンバーにはクラスを通じてアクセスし、printするとクラス名とメンバー名が表示されます：
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

列挙型のすべてのメンバーには2つの属性があります：クラスに書いた識別子である `name` と、代入した値である `value` です：
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
値は整数に限らず、どんな型でも構いません：文字列、タプル、浮動小数点数がよく使われます。
メンバーは普通のオブジェクトなので、変数に格納して後からその属性を読み取ることができます：
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

各列挙型のメンバーは**一度だけ**存在します：`Color.RED` と書くたびに、常にまったく同じオブジェクトが得られます。
そのため、メンバーは `==` だけでなく `is`（同一性）でも比較でき、どちらも同じ結果になります：
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
メンバーはその生の値と**等しくはありません**。メンバーとただの数値は別物だからです：
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
これが列挙型を安全にしている点です：プログラムの他の場所から来た `1` が `Color.RED` と誤認されることはありません。

---

列挙型のクラスは**反復可能**です：クラスに対する `for` ループは、宣言された順序ですべてのメンバーを訪れます：
```python
for color in Color:
    print(color.name, color.value)
```
`len()` は列挙型が持つメンバーの数を返し、`list(Color)` はそれらのリストを作成します：
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
リストの中では、メンバーは `repr()` で表示され、山括弧の間に値が含まれます。

---

クラスを関数のように呼び出せば**値**から、角括弧を使えば**名前**からメンバーを取得できます：
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
どちらも、値や名前がファイルやユーザー入力のようにプログラムの外部から来る場合に便利です。
何も一致しない場合、`Color(9)` は `ValueError` を発生させ、`Color["PINK"]` は `KeyError` を発生させます。

---

多くの場合、具体的な値は重要ではありません：メンバー同士が異なっていればそれで十分です。
その場合は、同じく `enum` モジュールからインポートする `auto()` で、Pythonに値を選ばせることができます。
最初のメンバーに `1` を割り当て、その後1ずつ数え上げていきます：
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

通常の `Enum` のメンバーは `<` で比較したり、数値に加算したりすることはできません。
メンバーが順序付けが必要な**レベル**を表す場合は、代わりに `IntEnum` を継承します：そのメンバーは整数でもあるため、比較、算術演算、ソートに対応しています：
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
`IntEnum` のメンバーはその整数値とも等しくなります：`Priority.LOW == 1` は `True` です。

---

`StrEnum`（Python 3.11以降で利用可能）は `IntEnum` の文字列版です：そのメンバーは文字列でもあり、自分の値と等しくなります。
そのため、設定キーやAPIパラメータのように、プレーンな文字列が期待される場所ならどこでも便利に使えます：
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
通常の `Enum` とは異なり、`StrEnum` のメンバーを `str()` やf文字列の中でテキストに変換すると、`Mode.DARK` ではなくその**値**になります。

---

列挙型はクラスなので、他のクラスと同じように**メソッド**や**プロパティ**を持つことができます。
その中では、`self` はメソッドが呼び出されたメンバーなので、`self.name` や `self.value` を参照したり、`self` を他のメンバーと比較したりできます：
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
クラス本体で代入されたプレーンな値はすべてメンバーになりますが、関数やプロパティはどこに現れても決してメンバーにはなりません。

---

2つのメンバーが同じ値を持つ場合、2つ目は新しいメンバーではなく、1つ目の**エイリアス**になります：
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
エイリアスは反復時にはスキップされ、`len()` でも数えられません。
通常、重複した値は間違いです。`enum` からインポートする `unique` デコレータを使うと、エイリアスを含む列挙型が宣言された時点でPythonが `ValueError` を発生させます：
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

`Flag` はメンバーを**組み合わせる**ことができる列挙型です：1つの値が、オプションの集合のように複数のメンバーを同時に保持できます。
メンバーは `auto()` で宣言します。`Flag` の場合、`auto()` は2の累乗（`1`、`2`、`4`、...）を割り当てるため、すべての組み合わせが一意な値を持ちます：
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
メンバーの組み合わせには `|` を、メンバーが組み合わせに含まれているかの確認には `in` を、結果の数値を見るには `value` を使います：
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

列挙型は `match` 文（Python 3.10以降で利用可能）と自然に組み合わせられます。`match` 文は値を一連の `case` パターンと比較し、最初に一致したものを実行します：
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
メンバーは必ず `Light.RED` のようにクラスと一緒に書いてください：`case RED:` のような裸の名前は何も比較せず、単に値を新しい変数 `RED` に捕捉してすべてに一致してしまいます。
ワイルドカードの `case _:` がデフォルトであり、その後のパターンには決して到達できないため、最後に置かなければなりません。

---

列挙型のメンバーは**ハッシュ可能**なので、辞書のキーやセットの要素として使うことができます。
列挙型をキーとする辞書は、各メンバーにデータを結び付けるきれいな方法です。また、メンバーで検索する方は、打ち間違いのおそれがある生の文字列を使うよりも安全です：
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
メンバーはどのコレクションにも現れることができるので、リスト、セット、内包表記について知っていることはすべてそのまま使えます：
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

メンバーの値は**タプル**にすることができ、各メンバーに複数のデータを持たせることができます。
列挙型が `__init__` メソッドを定義していると、Pythonはメンバーごとに1回それを呼び出し、タプルを引数に展開します。そのため、各データを個々の属性に保存できます：
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
メンバーの `value` はタプル全体のままです。

---

クラスの反復と名前によるメンバー検索は、ログ行やファイルのように外部から来るデータを処理する際に、うまく連携します。
クラスに対する辞書内包表記でメンバーごとに1つのエントリを用意し、次に `Level[name]` が入力される各文字列を対応するメンバーに変換します：
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
列挙型は宣言順を保持するため、後で `counts` を反復すると、メンバーが同じ順序で得られます。

---

通常のメソッドに加えて、列挙型は `@classmethod` で**クラスメソッド**を定義できます。クラスメソッドは列挙型のクラスそのものを `cls` として受け取るので、メンバーを見つける別の方法を置くのに適した場所です：
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
`auto()`、メソッド、プロパティ、検索と組み合わせれば、独自の振る舞いを備えた列挙型を作れます。
