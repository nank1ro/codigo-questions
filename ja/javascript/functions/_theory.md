コードの一部を少しだけ異なる値で再利用したい場面を考えたことがあるかもしれません。
コード全体を書き直す代わりに、関数を定義すれば、繰り返し使用できるのでずっとすっきりします。
JavaScriptでは、`function`キーワードの後に関数名を記述します：
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

パラメータを指定したい場合、__関数定義__の括弧は空でなくてもよいです

---

関数に値を__返して__もらいたい場合があります。
そのためには`return`キーワードを使います。

---

関数は複数の入力パラメータを持つことができ、関数の括弧内にカンマで区切って記述します。
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

関数のパラメータに値を代入することで、任意のパラメータに_デフォルト_値を定義できます。
デフォルト値が定義されている場合、関数を呼び出す際にそのパラメータを省略できます
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

__残余パラメータ__構文を使うと、不定数の引数を配列として表現できます。
パラメータ名の前に3つのピリオド`...`を付けて残余パラメータを記述します。
残余パラメータに渡された値は、関数本体内で配列として利用できます。
例えば、`numbers`という名前の残余パラメータは、関数本体内でnumbersという定数配列として利用できます

---

関数には、関数の動作を説明する_オプションのコメント_を追加できます：
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
単一行コメントには`//`を、複数行コメントには`/** */`を使用できます
