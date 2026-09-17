`String`は二重引用符で囲んで書かれた文字の並びです。
`length`プロパティは、スペースを含めて文字列に何文字含まれているかを示します:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

文字列の各文字には**インデックス**があり、最初の文字は`0`から始まります。
角括弧または`get`関数を使って1文字を読み取ることができ、結果は`Char`になります:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
最後の文字はインデックス`length - 1`にあります。`first()`と`last()`関数は便利なショートカットです:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()`は文字列のすべての文字を大文字にしたコピーを返し、`lowercase()`はその逆を行います。
元の文字列は変更されません:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

文字列に特定のテキストが含まれているかどうかを調べるには、`contains`、`startsWith`、`endsWith`を使います。これらはすべて`Boolean`を返します:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
この比較は大文字・小文字を区別しますが、`ignoreCase = true`を渡すと区別しなくなります:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf`は、あるテキストが**最初**に現れるインデックスを返します。まったく現れない場合は`-1`を返します。
`lastIndexOf`は代わりに末尾から検索します:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring`は文字列の一部を取り出します。2つの引数を渡すと、開始インデックスから終了インデックスの直前まで（終了インデックスを**含みません**）の文字を取得します。
引数が1つの場合は、そのインデックスから末尾までのすべてを取得します:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
`indexOf`と`substring`を組み合わせると、マーカーを基準に文字列を切り出せます:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split`は区切り文字を基準に文字列を`List`の断片に分割し、`joinToString`はその逆で、コレクションの要素を選んだ区切り文字で1つの文字列につなぎ合わせます:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

`split`は`List`を返すので、他のリストと同じようにその要素をループ処理できます:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// a、続けて b を出力
```

---

ユーザーの入力には余分なスペースが含まれていることがよくあります。`trim()`は先頭と末尾のスペースを取り除いた文字列を返し、`trimStart()`と`trimEnd()`は片側だけ取り除きます:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()`は`""`のとき`true`になりますが、`isBlank()`はスペースだけでできた文字列でも`true`になります:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)`は、`old`の**すべて**の出現箇所を`new`に置き換えたコピーを返します:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)`は文字列を`n`回連結したものを返します:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)`は、文字列が`width`文字になるまで先頭に`char`を追加します。`padEnd`は末尾に追加します。
文字列がすでに十分な長さであれば、変更されずにそのまま返されます:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
数値は文字列ではないので、`42.toString().padStart(4, '0')`のように、まず`toString()`を呼び出してください。

---

2つの文字列は、同じ文字が同じ順序で含まれているとき等しくなります。Kotlinでは`==`は文字列の**内容**を比較するので、通常はこれを使って比較します。
`equals`も同じことをしますが、大文字と小文字の違いを無視するための`ignoreCase = true`も受け付けます:
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===`は、2つの変数がメモリ上でまったく同じオブジェクトを指しているかどうかを調べるもので、文字列に対してこれを使いたい場面はほとんどありません。

---

`reversed()`は文字の順序を逆にした文字列を返します:
```kotlin
println("stressed".reversed()) // desserts
```
`"level"`のように前から読んでも後ろから読んでも同じ単語は、**回文**と呼ばれます。

---

文字列は**イミュータブル**です。つまり、一度作られると決して変化しません。ここまでに見てきた`uppercase()`や`replace()`のような関数はすべて、**新しい**文字列を返し、元の文字列には手を加えません。
結果を保持するには、それを保存する必要があります。例えば`var`に再代入する方法があります:
```kotlin
var name = "kotlin"
name.uppercase()        // 結果が捨てられる
println(name)           // kotlin
name = name.uppercase() // 結果が保存される
println(name)           // KOTLIN
```

---

`+`を使って長い文字列を1つずつ組み立てると、その都度新しい文字列が作られます。`StringBuilder`はこの作業のために作られた、変更可能なテキストバッファです。`append`は末尾にテキストを追加し（ビルダー自身を返すので呼び出しを連結できます）、`toString()`は最終的な`String`を返します:
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append`は文字列、文字、数値を受け付けます。
