型を使うと、コードで使用するさまざまなデータの種類を分類することができます。
Dartでは、__型__はコンパイラに対して、あるデータをどのように使用するかを伝える方法です。
Dartがサポートする型の例を以下に示します：
- int
- String
- double
- dynamic
- num

Dartは他にも多くの型をサポートしています。ここに挙げたものは、主に使用するものです。

---

変数の型を明示的に定義しても問題ありません。例えば：
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

明示的な型を持つ変数も定数にすることができます。型の前に`const`または`final`キーワードを追加するだけです：
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> 注意：ミュータブルなデータは、いつでも簡単に変更することができます。しかし、多くの経験豊富なプログラマーは、イミュータブルなデータの利点を高く評価しています。値がイミュータブルであれば、作成後に誰も値を変更できないと信頼できます。このようにデータを制限することで、発見しにくいバグを防ぎ、プログラムについて考えたりテストしたりすることが容易になります。

---

変数の型を記述することは可能ですが、冗長です。`10`が`int`型で、`3.14`が`double`型であることはわかります。Dartコンパイラは__型推論__のおかげでそれを推測することができます。すべてのプログラミング言語に_型推論_があるわけではなく、これがDartを非常に強力なプログラミング言語にしています。

変数から型を単純に削除することができます。例えば：
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

変数の型が明示的に記述されていない場合、Dartはその型を推論しようとします。

---

変数の型をプログラムで確認する方法があります。それは`is`キーワードを使うことです：
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

ご覧の通り、Dartは変数`number`に`double`型を割り当てています。

---

`is`キーワードを使うと、変数が指定した型かどうかを確認できます。しかし、`is!`キーワードを使って、
変数が指定した型でないかどうかも確認できます。
```dart
final number = 3.14;
print(number is! int); // true
```

---

_ランタイム_変数の型を確認するもう一つの方法は、すべての型で利用可能な`runtimeType`プロパティを使用することです。
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

ある型を持っているが、別の型に変換する必要がある場合があります。次のようにしたくなるかもしれません：

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

しかし、Dartはエラーを出します：
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

一部のプログラミング言語はそれほど厳しくなく、暗黙的に変換します。経験上、このような暗黙的な変換はバグやパフォーマンスの問題の原因になりがちです。Dartはこれらの問題を避けるために、この機能を無効にしています。

コンピュータはプログラマーに何をすべきか教えてもらう必要があることを覚えておいてください。Dartでは、型変換について明示的であることも含まれます。

Dartに暗黙的な変換を期待する代わりに、Dartに型を変換してほしいことを明示的に伝える必要があります。`double`の数値を`int`に変換する方法は次の通りです：
```dart
var integer = decimal.toInt();
```

この代入はDartに対して、元の型`double`から新しい型`double`に変換したいことを明確に伝えます。

> 注意：この場合、小数値を整数に代入すると精度が失われます。変数`integer`の値は__3.14__ではなく__3__になります。だからこそ明示的であることが重要です。Dartは、あなたが何をしているかを確認し、変換によって情報が失われることを知らせてくれます。

---

これまで、整数や小数に対して個別に演算子を使う方法を見てきました。整数を小数と掛け算する必要がある場合はどうでしょうか？例を見てみましょう：
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius`は`int`型で、`pi`は`double`型です。`circumference`の型は何になるでしょうか？Dartは変数`circumference`に`double`型を割り当てます。これはより安全な選択です。`int`型にすると精度が失われる可能性があるからです。

結果を`int`にしたい場合は、明示的に変換する必要があります：
```dart
const circumference = (2 * pi * radius).toInt();
```

括弧はDartにまず掛け算を行い、その結果を整数値に変換するよう指示します。残念ながら、アナライザーはこのコードを好みません：
 > Const variables must be initialized with a constant value.

問題は、`toInt`メソッドがランタイム専用のメソッドであることです。つまり、`circumference`変数はコンパイル時に決定できないため、定数にすることができません。修正するには`const`を`final`に置き換えます：

```dart
final circumference = (2 * pi * radius).toInt();
```

これで`circumference`は`int`型の__ランタイム定数__変数になります。

---

汎用的な型の変数を持っているが、サブタイプにしか存在しない機能が必要な場合があります。変数の型が必要なサブタイプであると確信している場合は、`as`キーワードを使って型を変更できます。この手順は__型キャスト__とも呼ばれます。以下に例を示します：

```dart
num number = 3;
```

数値が偶数かどうかを確認したいとしましょう。この機能は`int`サブタイプにのみ存在します。
```dart
print(number.isEven);
```

上記のコードは型エラーを返すはずです：
> The getter `isEven` isn't defined for the type 'num'.

`num`型は、数値が偶数か奇数かを判断するには一般的すぎる型です。整数のみが偶数または奇数になり得ます。
`num`に`double`値が含まれている場合に問題が発生します。`num`は`double`と`int`の両方の型を含むためです。この場合、__3__は整数であると確信しているので、`int`にキャストできます。

```dart
final integer = number as int;
print(integer.isEven); // false
```

`as`キーワードにより、コンパイラは変数`integer`を`int`型として認識します。これにより、整数に存在する`isEven`プロパティを使用できます。数値__3__は偶数ではないため、結果はfalseです。

キャストする際は注意が必要です。型を誤ってキャストすると、ランタイムエラーが発生します：
```dart
num numero = 3;
final decimale = numero as double;
```

これにより、プログラムは次のエラーでクラッシュします：
> CastError (type 'int' is not a subtype of type 'double' in type cast)

`number`のランタイム型は`int`であり、`double`ではありません。Dartでは、`int`と`double`のような同レベルの型でキャストすることはできません。サブタイプのみキャストできます。
