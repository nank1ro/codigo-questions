JavaScriptのすべての値には**型**があります。**プリミティブ**型は7つあります:
- `number`は`42`や`3.14`のような任意の数値
- `string`は`"Ana"`のようなテキスト
- `boolean`は`true`と`false`
- `undefined`は一度も提供されなかった値
- `null`は意図的に空にされた値
- `bigint`は`9007199254740993n`のような任意の大きさの整数
- `symbol`は`Symbol()`で作成される一意の識別子

それ以外のすべて（配列、関数、`{}`で作成されたオブジェクト、日付...）は`object`です。
`typeof`演算子は値の型を文字列として教えてくれます:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// number string boolean を出力
let city;
console.log(typeof city);
// undefined を出力
```

---

JavaScriptは**動的型付け**言語です。変数自体には型がなく、現在保持している値だけが型を持ちます。同じ変数は今は数値を保持し、後で文字列を保持することもでき、`typeof`は値に従います:
```javascript
let data = 10;
console.log(typeof data);
// number を出力
data = "ten";
console.log(typeof data);
// string を出力
```
これは便利ですが、関数が予期しない型の値を受け取る可能性もあるという意味です。そのため、`typeof`でチェックすることはよくある最初のステップです。`typeof`は文字列を返すので、その結果を文字列と比較します:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof`には人を驚かせる答えがいくつかあります。
関数はオブジェクトであるにもかかわらず、独自の答え`"function"`を持ちます:
```javascript
console.log(typeof function () {});
// function を出力
console.log(typeof console.log);
// function を出力
```
配列は独自の答えを持ち**ません**。`{}`と同じく、ただの`"object"`です:
```javascript
console.log(typeof [1, 2, 3]);
// object を出力
```
そして`typeof null`は`"object"`です。これは一度も修正されなかった歴史的なバグです。つまり`typeof`はプリミティブと関数はうまく区別できますが、配列、オブジェクト、`null`を区別することはできません。

---

型を関数として呼び出すことで、値を別の型に**明示的に**変換できます:
- `Number(value)`は数値に変換します: `Number("42")`は`42`
- `String(value)`は文字列に変換します: `String(42)`は`"42"`
- `Boolean(value)`はブーリアンに変換します: `Boolean("")`は`false`

結果はまったく新しい値であり、元の値は変更されません:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// 8 number を出力
console.log(String(count) + "!");
// 8! を出力
```
明示的に変換すると意図がはっきりします。`Number(input)`を読めば、`input`がテキストだったことがわかります。

---

`Number()`は厳密です。文字列全体が数値でなければならず、そうでなければ結果は`NaN`（"Not a Number"）になります:
```javascript
console.log(Number("12px"));
// NaN を出力
```
`parseInt()`と`parseFloat()`はより寛容です。文字列の先頭から数字を読み、先頭の空白をスキップし、数値の一部ではない最初の文字で止まります。`parseInt`は整数部分だけを保持します:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// 12 1.5 を出力
console.log(parseInt("3.9em"), parseInt("-4px"));
// 3 -4 を出力
```
文字列が数値の始まりになり得るもの（任意の符号とその後の数字）で始まっていない場合、これらも`NaN`を返します:
```javascript
console.log(parseInt("auto"));
// NaN を出力
```
`NaN`は自分自身と等しくない唯一の値です。そのため`x === NaN`は常に`false`になります。`NaN`を検出するには`Number.isNaN(x)`を使います。

---

「これは`NaN`か？」と尋ねる方法は2つあり、それぞれ異なる問いに答えます。
古いグローバル関数`isNaN(value)`は、まず`value`を数値に**変換**してからチェックします。そのため、`NaN`ですらないものに対しても、数値になれないものなら何でも`true`を返します:
```javascript
console.log(isNaN("hello"));
// trueを出力、Number("hello") はNaNであるため
console.log(isNaN("42"));
// falseを出力、Number("42") は42であるため
```
`Number.isNaN(value)`は変換し**ません**。`value`が本当に数値の`NaN`であるときにだけ`true`になります:
```javascript
console.log(Number.isNaN("hello"));
// falseを出力、文字列はNaNではない
console.log(Number.isNaN(Number("hello")));
// true を出力
```
`Number.isNaN`を優先して使い、変換が失敗したかどうかを知りたいときは先に変換してください。

---

JavaScriptは**暗黙的**にも変換を行います。そして`+`演算子は、これが最もよくたたる場所です。どちらかの側が文字列なら、`+`は**連結**を行い、もう一方の側は文字列に変換されます:
```javascript
console.log("5" + 3);
// 53 を出力
console.log(1 + 2 + "3");
// 33を出力、1 + 2 が先に計算されるため
```
その他のすべての算術演算子は、両方の側を**数値**に変換します:
```javascript
console.log("6" - 2, "3" * "4");
// 4 12 を出力
```
つまり、テキストから来る値（ユーザー入力、ファイル、URL）を足すと、合計の代わりに黙って文字列が作られてしまうことがあります。安全のために、足す前に`Number()`で変換してください。

---

文字列を数値に変換する短い方法が**単項プラス**です。1つの値の前に置かれた`+`は、`Number()`とまったく同じように変換します:
```javascript
console.log(+"5" + 5);
// 10 を出力
console.log(typeof +"5");
// number を出力
```
コンパクトですが足し算と混同しやすいため、明示的な`Number("5")`を好むチームも多くあります。

---

**緩い**等値演算子`==`は、比較の前に2つの側を共通の型に変換します。そのルールは覚えるのが難しいものです:
```javascript
console.log("5" == 5);
// trueを出力、"5" は5になる
console.log(0 == "");
// trueを出力、"" は0になる
console.log(0 == false, "1" == true);
// true true を出力
```
**厳密**等値演算子`===`は決して変換しません。異なる型の値は単純に等しくありません:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// false false false を出力
```
デフォルトでは`===`（と`!==`）を使ってください。唯一のよくある例外は`value == null`で、これは`null`と`undefined`をまとめてチェックします。

---

JavaScriptがブーリアンを必要とするとき、例えば`if`の条件や`Boolean(value)`の中では、値が変換されます。`false`になる値は8つだけで、それらは**falsy**と呼ばれます:
`false`、`0`、`-0`、`0n`、`""`、`null`、`undefined`、`NaN`です。
**それ以外のすべてはtruthyです**。空に見える値もいくつか含まれます:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// false false false を出力
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// true true true true を出力
```
`"0"`は空でない文字列なのでtruthyです。空の配列はオブジェクトなので、これもtruthyです。

---

任意の値をブーリアンに変換するよくある短縮形が**二重否定**`!!`です。最初の`!`がブーリアンに変換して反転し、2番目の`!`がそれを元に戻します:
```javascript
console.log(!!"text", !!0);
// true false を出力
```
`!!value`と`Boolean(value)`はまったく同じ結果になります。明示的な形の方が読みやすいです。

---

JavaScriptには整数と小数のための`number`型が1つだけあります。すべての数値は64ビット浮動小数点値（*double*）です。そのため`5`と`5.0`は同じ値であり、別の整数型は存在しません:
```javascript
console.log(5 === 5.0, 10 / 2);
// true 5 を出力
```
数値に小数部分がないかを調べるには、`Number.isInteger`を使います:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// true false を出力
```
テンプレートリテラルは補間された値を`String()`と同じルールで文字列に変換するので、`${5.0}`は`"5.0"`ではなく`"5"`になります。

---

数値はdoubleであるため、正確に格納できない小数があり、小さな誤差が現れます:
```javascript
console.log(0.1 + 0.2);
// 0.30000000000000004 を出力
console.log(0.1 + 0.2 === 0.3);
// false を出力
```
`toFixed(digits)`メソッドは数値を小数点以下`digits`桁に丸めますが、**文字列**を返します。表示には問題なく、さらなる計算には使えません:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// 0.30 string を出力
```
丸めた**数値**を得るには、結果を`Number()`で変換して戻します:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// 0.3 を出力
```

---

`number`が整数を正確に表せるのは`Number.MAX_SAFE_INTEGER`（`9007199254740991`）までです。それを超えると桁が失われます:
```javascript
console.log(9007199254740993);
// 9007199254740992 を出力
```
より大きい整数には`bigint`を使います。`n`接尾辞を付けてリテラルを書くか、`BigInt()`で変換します:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// bigint 9007199254740994n を出力
```
`console.log`は`n`接尾辞を付けて表示し、`String(big)`は素の数字を返します。
`bigint`と`number`は一緒に計算に使えません。`big + 1`は`TypeError`をスローします。`BigInt(count)`か`Number(big)`で、どちらかの側を明示的に変換してください。

---

`typeof`は配列、オブジェクト、`null`に対して`"object"`と答えるため、これらを区別するには2つの追加チェックが必要です。
`Array.isArray(value)`は配列に対してだけ`true`になります:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// true false を出力
```
`null`については`value === null`と直接比較します。これらを組み合わせると、任意の値の完全な姿がわかります:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
`null`と配列を先にチェックしてください。素の`typeof`ではこれらを区別できないからです。

---

フォーム、ファイル、URLから来るテキストは、それが数値やブーリアンを表していても、常に文字列です。それを正しい型に戻すには、これまでに見てきたことを組み合わせます。ブーリアンは`"true"`や`"false"`と比較し、数値は`Number()`を試します。`Number("")`が`0`になること、そして変換が失敗したときを`Number.isNaN`が教えてくれることを忘れないでください:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// 3.5 0 NaN を出力
```
何にも一致しない場合は、文字列をそのまま返します。
