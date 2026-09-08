**文字列（string）**とは、引用符で囲まれた文字の並び、つまりテキストの一部です。
Pythonではシングルクォート `'...'` とダブルクォート `"..."` のどちらも使え、両者は全く同じように動作します：
```python
name = 'Ada'
language = "Python"
```
テキスト自体に引用符が含まれる場合は、どちらを選ぶかが重要になります。
シングルクォートの中にアポストロフィがあると、そこで文字列が早く終わってしまうので、その場合はダブルクォートで囲みましょう：
```python
print("It's sunny")  # It's sunny
```

---

組み込み関数 `len()` は文字列の**長さ**、つまりそれが含む文字数を返します。
スペースや句読点も文字として数えられます：
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

文字列の各文字には**インデックス**と呼ばれる位置があります。
インデックスは `1` からではなく `0` から始まります：最初の文字はインデックス `0`、2番目はインデックス `1`、というように続きます。
文字列の後に角括弧でインデックスを書くと、1文字だけを読み取れます：
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
`word[6]` のように存在しないインデックスを指定すると、`IndexError` が発生します。

---

インデックスは**負の数**にもできます：その場合は文字列の末尾から数えます。
`-1` は最後の文字、`-2` はその1つ前の文字、というように続きます：
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
これは文字列の長さを知らなくても末尾に到達できるので便利です。

---

**スライス**は文字列の一部を取り出します。
角括弧の中に `[start:end]` と書くと、`start` の位置の文字は含まれ、`end` の位置の文字は含まれません：
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
`start` を省略すると先頭から、`end` を省略すると末尾までスライスできます：
```python
print(word[:2])  # py
print(word[2:])  # thon
```
スライスはエラーを起こしません。`end` が文字列の長さより大きい場合は、単に最後の文字で止まります。

---

`+` が2つの文字列を連結する（**concatenation**）ことはすでに知っています。
`*` 演算子は文字列を指定した回数だけ**繰り返し**ます：
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
繰り返しは、区切り線や簡単なパターンをすばやく描く方法です。

---

`in` 演算子は、ある文字列が別の文字列を**含んでいる**かどうかを調べます。
`True` か `False` を返すので、`if` の中で自然に使えます：
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` は逆の確認を行います。

---

文字列には多くの組み込み**メソッド**が用意されています：文字列の後にドットを付けて呼び出す関数です。
`upper()` はテキストを大文字にして返し、`lower()` は小文字にして返します：
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
これらのメソッドは**新しい文字列を返す**ことに注意してください：元の `word` は変更されません。
`lower()` は大文字小文字を無視してテキストを比較するのによく使われます：`"Yes".lower() == "yes"`。

---

文字列は**イミュータブル（不変）**です：一度作られると、その文字を変更することはできません。
インデックスへの代入は `TypeError` を発生させます：
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
文字列を「変更」するには、たとえばスライスと連結を使って新しい文字列を作り、それを変数に格納します：
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

ユーザーが入力したテキストには、前後に余分なスペースが含まれていることがよくあります。
`strip()` メソッドは、**先頭と末尾の空白**（スペース、タブ、改行）を取り除いた文字列のコピーを返します：
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
テキストの途中にあるスペースはそのまま残ります。
`lstrip()` は左側のみ、`rstrip()` は右側のみを取り除きます。

---

`split()` は文字列を分割して断片の**リスト**にします。
引数がない場合は空白で分割し、引数がある場合はその区切り文字で分割します：
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` はその逆で、リストの要素を1つの文字列にくっつけます。
これは**区切り文字**に対して呼び出され、リストは引数として渡されます：
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` は、`old` の**すべて**の出現箇所を `new` に置き換えた文字列のコピーを返します：
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
文字列はイミュータブルなので、結果を残しておきたい場合は忘れずに保存してください。

---

`find(sub)` は `sub` が最初に出現する位置の**インデックス**を返し、見つからない場合は `-1` を返します：
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` は `sub` が**何回**現れるかを返します：
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` と `endswith(suffix)` は、文字列の始まり方や終わり方に応じて `True` か `False` を返します：
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
これらは、ファイル拡張子やプロトコル、接頭辞をチェックする一般的な方法です。

---

一部の文字は文字列の中に直接入力できません。
**エスケープシーケンス**とは、バックスラッシュ `\` の後に文字や記号を続けて、特殊な文字を表すものです：

- `\n` 改行
- `\t` タブ
- `\"` ダブルクォート文字列の中のダブルクォート
- `\'` シングルクォート文字列の中のシングルクォート
- `\\` 文字としてのバックスラッシュ

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
これは次のように表示されます：
```
Line 1
Line 2
She said "hi"
```
2文字入力しても、それぞれのエスケープシーケンスは**1文字**として数えられます。

---

**複数行**にまたがる文字列は、**トリプルクォート** `"""..."""`（または `'''...'''`）で書くことができます。
引用符の中の改行はすべて文字列の一部になるので、`\n` を使う必要はありません：
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
これは次のように表示されます：
```
Roses are red,
Violets are blue
```
トリプルクォート文字列には、シングルクォートやダブルクォートを自由に含めることもできます。

---

すべての文字列メソッドは新しい文字列を返すので、メソッドを次々に**チェーン**させることができます。
各呼び出しは、その前の結果に対して作用します：
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
スライスは3つ目の値、**ステップ**も受け取れます。
ステップ `-1` は文字列を逆向きにたどるもので、これは文字列を反転させる定番のテクニックです：
```python
print("abc"[::-1])  # cba
```

---

**スラッグ（slug）**とは、タイトルをURLに使いやすい形式にしたものです：小文字で、前後にスペースがなく、単語はダッシュで区切られます。例：`hello-world`。
スラッグを作るのは、これまで学んだメソッド `strip()`、`lower()`、`replace()` をつなげるだけです。
