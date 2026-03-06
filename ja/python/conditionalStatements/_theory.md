特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良いときだけ外で遊びたいとしましょう。
プログラミングでは、ブール変数 `nice_weather` を保存し、この変数が `True` の場合に外で遊ぶというアクションを `if` で実行できます。例えば：
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

前の例の続きを見てみましょう。
```python
nice_weather = True
if (nice_weather):
    # play outside
```
`if` 文は条件が `True` の場合にのみコードブロックを実行することがわかりました。
もう一つ重要なことは、**コロン** `:` と**インデント**です。これらはコードブロックの開始を示します。
インデントとは、コード行の先頭にあるスペースのことです。
他のプログラミング言語ではインデントは読みやすさのためだけですが、Pythonではインデントは不可欠です。
お好みのスペース数（2、4、6、8）を使用できますが、4が推奨されています。
このアプリでは、コード行をインデントするために**TAB**キーを使用することをお勧めします

---

条件が成立した場合にコードブロックを実行する方法を見ました。次に、最初の条件が偽の場合に別のコードブロックを実行する方法を見てみましょう。
天気が良ければ外で遊びます。そうでなければ、家にいます。
Pythonでは、`else` 文を使用できます。例えば：
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

もう一つの条件をチェックしたい場合を考えてみましょう。次の例のように：
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
このコードの出力は `the number is 3` です。
まず、数値が2に等しいかチェックします。これは偽です。
次に、2番目の文に進み、`num` が3に等しいかチェックします。これは真なので、`the number is 3` を出力するコードブロックを実行します

---

`elif` 文はいくつでも追加できます。制限はありません
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
このコードの出力は `the number is 4` です。

---

条件文（`if`、`elif`、`else`）を別の条件文の中にネストして、より複雑な構造を作ることもできます。
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
このコードの出力は `the number is 4` です。
