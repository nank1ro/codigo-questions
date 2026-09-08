`void sayHello() { ... }` のような名前付き関数の宣言方法はすでに知っていますね。Dartでは**名前のない**関数、つまり**無名関数**を書くこともできます。無名関数は名前付き関数と同じ要素（括弧の中のパラメータと波括弧の中の本体）を持ちますが、戻り値の型と名前がありません：

```dart
(String name) {
  print('Hello, $name!');
}
```

名前がないため、通常は変数に格納し、その変数を関数のように呼び出して使います：

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

閉じ波括弧の後の `;` に注目してください。代入は通常の文です。

---

無名関数は、名前付き関数とまったく同じように、パラメータを取り `return` で値を返すことができます。戻り値の型は書きません。Dartが本体の `return` 文から**推論**します：

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

本体が単一の式である場合、無名関数も名前付き関数と同じように**アロー構文** `=>` を使えます。アローは波括弧と `return` キーワードの両方を置き換えます：

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

この短い形式は、Dartで無名関数を書く最も一般的な方法です。

---

関数は値であるため、型を持ちます。関数の型は、**戻り値の型**、キーワード `Function`、括弧の中の**パラメータの型**の順に書きます：

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

変数をこのように型付けすると、Dartが宣言された型からパラメータの型を推論するため、無名関数側ではパラメータの型を省略できます：

```dart
int Function(int, int) add = (a, b) => a + b;
```

型を `Function` だけとすると、パラメータや戻り値の型が何であれ任意の関数を受け入れますが、その呼び出し方についてはDartに何も伝えません。

---

関数型も普通の型であるため、関数は**別の関数をパラメータとして**受け取れます。本体の中では、そのパラメータを他の関数と同じように呼び出します：

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

ここでは、呼び出し元が2番目の引数として無名関数を渡すことで、`apply` の動作を決めています。

---

Dartのコレクションには引数として関数を受け取るメソッドが多くあり、それを渡す自然な方法が無名関数です。最も単純なのは `forEach` で、リストの各要素に対して渡された関数を1回ずつ呼び出します：

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

パラメータの型はリストから推論されるため、`fruit` が `String` であることは書く必要がありません。

---

無名関数を受け取る、その他の非常に一般的なメソッドが `map` と `where` です：

- `map` は関数で各要素を変換し、新しい値を返します
- `where` は関数が `true` を返す要素だけを残します

どちらも遅延評価される `Iterable` を返します。結果を `List` に変換するには `toList()` を呼びます：

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

`map` と `where` はどちらも `Iterable` を返すため、その呼び出しは次々と**チェーン**できます。各ステップは前のステップの結果を受け取り、最後に一度だけ `toList()` を呼びます：

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` はリストをその場で並べ替えます。デフォルトでは要素の自然な順序が使われますが、**2つの要素を比較**して負の数、ゼロ、正の数のいずれかを返す無名関数を渡すこともできます。`compareTo` はまさにそのような数を返すため、通常はこれが構成要素として使われます：

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

比較の中で `a` と `b` を入れ替えると、順序が逆になります。

---

`reduce` はリストのすべての要素を1つの値にまとめます。その無名関数は2つのパラメータ、つまり**これまでに蓄積された値**と**次の要素**を受け取り、新しい蓄積値を返します。最初の要素が出発点として使われます：

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

出発点となる最初の要素がないため、`reduce` は空のリストに対してエラーをスローします。

---

関数は**関数を返す**こともできます。この場合、戻り値の型は関数型になり、本体は無名関数を返します：

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

返された関数は、`makeAdder` が終了した後でも、`makeAdder` のパラメータである `amount` を使い続けます。このように自分を取り囲む変数を覚えている関数は**クロージャ**と呼ばれます。

---

クロージャはキャプチャした変数を読むだけでなく、それらを**変更**することもでき、その変更は呼び出しの間も保持されます。これにより、クラスを使わずにプライベートな状態を保持できます：

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

`makeTimer()` を呼び出すたびにまったく新しい `seconds` 変数が作られるため、2つのタイマーがカウントを共有することはありません。
