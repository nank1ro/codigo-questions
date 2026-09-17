**例外**は、文を実行できないことをPythonが伝えるための方法です。ゼロによる除算、`"abc"`の整数への変換、存在しない辞書キーの読み取りは、すべて例外を発生させます。どの処理も行われないと、プログラムはその場で停止し、**トレースバック**を出力します：
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
トレースバックには実行されていた行が一覧表示され、最後の行には**例外の型**（`ZeroDivisionError`）とそのメッセージ（`division by zero`）が示されます。この最後の行を最初に読むべきです。

プログラムを動かし続けるには、危険が伴う文を`try`ブロックに置き、回復の処理を`except`ブロックに記述します：
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Pythonは`try`ブロックを実行します。指定した例外が発生すると、一致する`except`ブロックへ直接ジャンプし、プログラムの残りを続行します。

---

`try`ブロックは例外を発生させる**最初の**文で停止し、それ以降の行はスキップされて制御が`except`ブロックに移ります。`try`ブロック内の処理は何も元に戻されないため、できるだけ短く保ちましょう：
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
`except`内の`return`は他の`return`と同じように機能するため、`try`/`except`はクラッシュする代わりにフォールバック値を返す自然な方法になります。

---

どの`except`ブロックにも一致しない例外は、外側へ伝わり続けます：その行の外、その行を実行した関数の外、さらにその呼び出し元の外、という具合です。プログラムの最上部に達するまでに何も捕捉しないと、Pythonはトレースバックを出力し、プロセスはゼロ以外の終了ステータスで終了します。失敗した文の後の行が実行されることはありません。

---

`except`節は、指定した型とそのサブクラスだけを捕捉します。これが重要な点です：それ以外の例外は外側へ伝わり続けるため、予期していなかったバグは飲み込まれる代わりにトレースバックとして現れます。

`int(text)` はテキストが整数を表していないときに**`ValueError`**を発生させるため、ユーザー入力を読み取るときに指定すべき型はこれです：
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
ここで`ValueError`を指定するのは形式的なことではなく、意図的な決断です：`int(None)`は`TypeError`を発生させますが、この関数はそれを**意図的に**捕捉しません。`None`を渡すのはプログラミングのミスであり、見えるべきだからです。

---

予期する失敗をカバーする最も狭い型を選ぶことが、信頼できるエラー処理の鍵です。テキストを読み取る関数は不正なテキストから回復すべきですが（`ValueError`）、間違った種類の引数で呼び出されることを隠してはいけません（`TypeError`）。そのエラーは呼び出し元に属するものなので、そのまま通しましょう。

---

1つの`try`ブロックの後に**複数の**`except`節を続けることができ、それぞれが異なる失敗を異なる回復処理で扱います。Pythonは発生した例外を上から下へ順に比較し、一致する**最初の**節を実行します。それ以外の節はスキップされます：
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
最初に一致した節が採用されるため、型同士に関係がある場合は順序が重要です。より具体的な型の節の上に一般的な型の節を置くと、常に一般の節が採用され、具体的な節に到達できなくなります。

---

複数の失敗に**同じ**回復処理がふさわしいときは、ブロックを繰り返す代わりに、1つの節にタプルとして並べる方が簡潔です：
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
括弧は必須です：`except ValueError, ZeroDivisionError:` はPython 3では構文エラーになります。タプルであっても、明示的な型のリストであることに変わりありません。

---

後ろに型を書かない `except:` は**裸のexcept（bare except）**です。これはすべてに一致するため、守ろうとしていた操作とは無関係な例外まで捕捉されます。ルールは単純です：実際に回復できる型だけを必ず指定しましょう。

---

例外はオブジェクトであり、`as` はそれを名前に束縛するので、ハンドラからその内容を調べられます：
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)`（`print(e)` やf文字列のスロットが使うもの）は例外が構築されたときのメッセージを返し、`type(e).__name__` はクラス名をテキストとして返します。`as` で束縛された名前は `except` ブロックの中でのみ存在し、ブロックが終わるとPythonはその名前を削除します。

---

`try` ブロックの後に `else` ブロックを続けることができます。これは**`try` ブロックが例外を発生させずに終わったときにだけ**実行されます：
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
`print(number * 2)` を `try` ブロックの中に置いても動作しますが、その場合、出力自体が発生させた `ValueError` が変換の失敗と誤解される可能性があります。`else` は `try` ブロックを守る対象の1文だけに保ち、成功時に起こるべき処理をすべてそこに収めます。

---

`finally` ブロックは**何が起こっても**実行されます：問題なく終わった `try` ブロックの後でも、`except` ブロックの後でも、誰にも捕捉されない例外が外側へ伝わっている最中でも、そして `try` や `except` ブロックが `return` を実行するときでも実行されます：
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
どちらの経路でも、値が関数から出る前に `done` が出力されます。この保証のために `finally` があります：ファイルを閉じる、ロックを解放する、設定を元に戻す、といった処理です。完全な形は `try` / `except` / `else` / `finally` です。`try` には少なくとも1つの `except` か `finally` が必要で、`else` は `except` と一緒のときにしか使えません。

---

自分のコードでも例外を発生させられます。`raise` 文の後に例外オブジェクトを続けます：
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` は組み込みの失敗とまったく同じように、関数を即座に停止させます。代わりにエラー値を返す方法（`-1`、`None`、`False`）は、呼び出し元が忘れやすいものです。例外はうっかり無視されることがありません。

問題を表す型を選びましょう：引数の型は正しいが値が不可能なときは `ValueError`、型自体が間違っているときは `TypeError` です。例外に渡したテキストがそのメッセージになります。

---

ほんの一握りの組み込み例外が、日常的な失敗のほとんどをカバーしています：

| 例外 | 発生する状況 | 例 |
|---|---|---|
| `ValueError` | 型は正しいが値が不可能 | `int("abc")` |
| `TypeError` | 型自体が間違っている | `"x" + 1` |
| `ZeroDivisionError` | 除算や剰余算の除数がゼロ | `1 / 0` |
| `KeyError` | 辞書にそのキーが存在しない | `{"a": 1}["b"]` |
| `IndexError` | シーケンスのインデックスが範囲外 | `[1, 2][5]` |

新しい型をでっち上げる代わりにこれらの1つを使えば、Pythonを知っている人なら誰でもエラーを読みやすくなります。

---

ハンドラは、失敗の責任を負うことなく反応すべきときがあります：ログに記録し、カウントし、何かを閉じる — その後、呼び出し元に任せます。`except` ブロックの中で単独の `raise` は、処理中の例外を元の型、メッセージ、トレースバックをそのままにして**再発生（re-raise）**させます：
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
代わりに `raise ValueError(...)` と書くと、新しいトレースバックを持つ別の例外が作られます——それはもう捕まえたのと同じ失敗ではなくなり、単独の `raise` はまさにその同一性を保持します。

---

組み込みの型がどれも合わないときは、`Exception` のサブクラスを作って独自の型を定義します。空の本体で通常は十分です。名前自体が読み手へのメッセージです：
```python
class ConfigError(Exception):
    pass
```
他の例外と同じように振る舞います：`raise ConfigError("bad port")` と発生させ、`except ConfigError:` で捕捉できます。

低レベルの失敗を自分の型に変換することはよくありますが、その過程で元のエラーを失ってはいけません。`raise NewError(...) from original` は2つを**チェーン（連鎖）**させます：`original` を新しい例外の `__cause__` 属性に格納し、トレースバックには *The above exception was the direct cause of the following exception* の下に両方が表示されます：
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
`from e` がなくても2つは暗黙的にリンクされますが、`from` は最初のエラーが2番目を引き起こしたことをはっきり述べます。
