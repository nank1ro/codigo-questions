**正規表現**（**regex**）は、テキストの形を記述する小さなパターンです。「4桁の数字」「`@`の後に単語が続くもの」「引用符の間にある任意の文字」のようなものです。Kotlinではパターンは`Regex`オブジェクトで、2つの等価な方法で作れます:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
パターンの中のほとんどの文字はその文字自身を表しますが、いくつかは**省略記法**になっています:
- `\d`は任意の数字です。`\`はエスケープが必要なため、Kotlinの文字列では`"\\d"`と書きます
- `[a-z]`は任意の小文字、`[abc]`は`a`、`b`、`c`のいずれかです
- 要素の後の`+`は「それが1個以上」を意味し、`\d+`は数字の連続になります

最も基本的な質問は`matches`で、パターンが文字列**全体**に一致するときだけ`true`になります:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches`はしばしば厳しすぎます。通常は、パターンがテキストの**どこかに**現れているかどうかを知りたいだけです。それが`containsMatchIn`です:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
`\d`のほかに、頻繁に使う2つの省略記法があります。`\w`は単語文字（英字、数字、`_`）、`\s`は空白文字です。それぞれに**量指定子**で繰り返しを指定できます:
- `+` 1個以上
- `*` 0個以上
- `?` 0個か1個
- `{3}` ちょうど3個、`{2,4}` 2個から4個

すべてのバックスラッシュを2重にするのは読みにくいので、パターンは通常、三重引用符の**raw文字列**で書きます。そこでは`\`は単なる1文字です:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn`は、パターンが*あるかどうか*だけを教えます。`find`は**何が**どこにあるかも教えてくれます。最初に一致したものを`MatchResult`として返し、見つからなければ`null`を返します:
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value`は一致したテキストで、`range`は元の文字列の中でそれが占めるインデックスの範囲です。結果はnull許容なので、安全な呼び出し`?.`でアクセスします。一致が見つからなかったときもクラッシュせずに`null`になります:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

パターンの中の丸括弧は**キャプチャグループ**を作ります。一致のうち、後で別々に読み取りたい部分のことです。`MatchResult.groupValues`がそれらを保持していて、インデックス`0`は一致全体、`1`、`2`、...は左から右の順でグループに対応します:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
一致がまったくないとき、`find`は`null`を返し、読み取るものもありません。そこで、グループを取り出す関数は通常、その場合に何を返すかを決めておきます:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

パターンが複雑になるにつれ、ホストがグループ`2`だと数えて確認する方法は壊れやすくなります。グループには`(?<name>...)`で**名前**を付けられ、その名前で`groups`から読み取れます:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups`はグループを`MatchGroup?`として返すので、その`.value`を尋ねる必要があります。名前付きグループも通常どおり番号が付くので、`groupValues[1]`も引き続き使えます。

---

`find`は最初の一致で止まります。`findAll`は**すべての**一致を`Sequence<MatchResult>`として返します。`map`、`filter`、`count`、`toList`でリストのように扱える遅延評価のチェーンです:
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
何も一致しないとき、`findAll`は`null`の代わりに空のシーケンスを返すので、安全な呼び出しを書く必要はありません。シーケンスそのものを出力しても役に立ちません。表示されるのは一致ではなくオブジェクトです。まずリストに変換してください。

---

`replace`はテキストを書き換えます。すべての一致を置換内容と入れ替えた**新しい**文字列を返し、元の文字列はそのまま残ります:
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
置換文字列の中では、`$1`、`$2`、...がその一致でキャプチャされたグループを表します。一致させた部分を並べ替えたり再利用したりできます:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0`は一致全体です。置換の中でリテラルの`$`が必要なときは、`\$`とエスケープします。
`replace`は**すべての**一致を書き換えるので、完全な文字列だけを書き換えたいときは、**アンカー**の`^`（テキストの先頭）と`$`（テキストの末尾）でパターンを固定します:
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

置換文字列でできるのは、受け取った部品の組み合わせ替えだけです。新しいテキストを**計算**して作る必要があるときは、代わりにラムダを`replace`に渡します。ラムダは`MatchResult`を受け取り、その代わりになる文字列を返します:
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
ラムダの中では`MatchResult`全体にアクセスできるので、`m.value`、`m.range`、`m.groupValues`はすべて使えます。ここで`$1`には特別な意味がないことに注意してください。返す文字列の中では普通の文字にすぎません。

---

`split`はパターンが一致する場所で文字列を切り分け、その断片を`List<String>`として返します。固定の区切り文字列で分割するのとは違い、正規表現の区切りは区切り文字の一族まるごとを記述できます:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
一致した区切りは結果には含まれません。テキストの先頭や末尾が区切りのときは、その隣の断片は空になります:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split`は第2引数に`limit`を受け付けます。指定した個数の断片で止まり、残りは最後の断片にそのまま残ります。

---

パターンは大文字と小文字を区別します。`Regex("kotlin")`は`"Kotlin"`に一致しません。`[kK][oO]...`と書く代わりに、第2引数でオプションを渡します:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
オプションは`Regex`に属するので、そのオブジェクトのすべてのメソッドが従います。`matches`、`find`、`findAll`、`replace`、`split`のいずれも同じです。その他に便利なオプションとして、`^`と`$`をどの行でも一致させる`RegexOption.MULTILINE`や、`RegexOption.DOT_MATCHES_ALL`があります。組み合わせるときはsetを渡します: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`

---

`Regex("cat")`は`catalog`の中の`cat`にも一致します。単語全体を要求するには、**単語境界**の`\b`を使います。これは単語文字とそれ以外の間にある空の位置に一致し、テキストの先頭と末尾も含まれます:
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
パターンは普通の文字列なので、実行時に部品から組み立てられます:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

`. * + ? ( ) [ ] { } | ^ $ \` の各文字は、パターンの中では特別な意味を持ちます。最も落とし穴になりやすいのは`.`で、ドットではなく**任意の**1文字に一致します。文字そのものを表したいときは、バックスラッシュでエスケープします:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
探すテキストが変数から来ていて、リテラルとして扱う必要があるときは、`Regex.escape`でエスケープをライブラリに任せます:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll`とグループを組み合わせると、1行のテキストを構造化されたデータに変換できます。シーケンスの各`MatchResult`はそれぞれ自分の`groupValues`を持っているので、1つのチェーンでリスト、マップ、合計を作れます:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate`は、ラムダが返す`key to value`のペアからマップを作ります。パターンのグループの数が決まっているときは、インデックスで読み取る代わりに`destructured`で名前付きの変数に展開できます:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

角括弧は**文字クラス**を定義します。リストされた集合の中から1文字に一致します。その中では範囲も使え、先頭の`^`はクラス全体を否定します:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
文字クラスで選べるのは1文字だけです。完全な選択肢の中から選ぶには`|`を使います。通常はグループで囲み、パターンの残りの部分を飲み込まないようにします:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

`findAll`はシーケンスを返すので、すでに知っている集約メソッドは一致にも使えます: `sumOf`、`maxOfOrNull`、`filter`、`sortedBy`。自由なテキストから数値を取り出すのは2段階の作業です。まず一致させ、次にテキストを数値に変換します。
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

実用的なパターンは通常、すべてを一度に組み合わせます。必要な部分を取り出すグループ、リテラルのドットのためのエスケープされた`\.`、そしてその周囲からテキストを組み立て直すラムダ置換です。
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
パターンは仕事が許すかぎりシンプルに保ちましょう。あらゆる正しいメールアドレスを記述しようとするパターンは読みにくくなりますが、`\w+@\w+\.\w+`で十分に文中のアドレスを見つけられます。
