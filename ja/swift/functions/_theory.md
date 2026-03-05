コードの一部を、少しだけ異なる値で再利用したいと思う場面を考えたことがあるかもしれません。
コード全体を書き直す代わりに、関数を定義する方がはるかにすっきりしており、繰り返し使用できます。
Swiftでは、`func`キーワードの後に関数名を書いて関数を定義します:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

パラメータを指定したい場合、__関数定義__の括弧は空である必要はありません

---

関数に値を__返して__もらいたい場合があります。
そのためには`return`キーワードを使います。

---

関数は複数の入力パラメータを持つことができ、関数の括弧内にカンマで区切って記述します。
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

タプル型を関数の戻り値の型として使用すると、1つの複合的な戻り値の一部として複数の値を返すことができます。

---

パラメータの引数ラベルが不要な場合は、明示的な引数ラベルの代わりにアンダースコア`_`を書きます

---

関数の任意のパラメータに_デフォルト_値を定義するには、パラメータの型の後に値を代入します。
デフォルト値が定義されている場合、関数を呼び出すときにそのパラメータを省略できます
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

_可変長パラメータ_は、指定された型の0個以上の値を受け取ります。
可変長パラメータを使用すると、関数が呼び出されたときにさまざまな数の入力値を渡せることを指定できます。
可変長パラメータは、パラメータの型名の後に3つのピリオド`...`を挿入して記述します。
可変長パラメータに渡された値は、関数本体内で適切な型の配列として利用できます。
例えば、名前が`numbers`で型が`Double...`の可変長パラメータは、関数本体内で`[Double]`型の定数配列numbersとして利用できます

---

関数には、関数の動作を説明する_オプションのコメント_を追加できます:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
1行コメントには`///`を、複数行コメントには`/** */`を使用できます
