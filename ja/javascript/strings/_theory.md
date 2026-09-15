**文字列**は`"hello"`や`'hello'`のように引用符で囲まれた文字の並びです。
すべての文字列には、含まれる文字数を示す`length`プロパティがあります:
```javascript
let greeting = "hello";
console.log(greeting.length);
// 5 を出力
```
スペースや句読点も文字としてカウントされます。

---

文字列内の各文字には`0`から始まる**インデックス**があります。
角括弧または`charAt()`メソッドを使って1文字だけを読み取ることができます:
```javascript
let word = "hello";
console.log(word[0]);
// h を出力
console.log(word.charAt(1));
// e を出力
```
最後の文字はインデックス`length - 1`にあります:
```javascript
console.log(word[word.length - 1]);
// o を出力
```

---

文字列には多くの組み込み**メソッド**が用意されています。最も単純な2つは、すべての文字の大文字・小文字を変換します:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// HELLO を出力
console.log(word.toLowerCase());
// hello を出力
```
どちらのメソッドも引数を取らないので、括弧を忘れないでください。

---

文字列が別の文字列を含んでいるかを調べるには、次のいずれもブール値を返すメソッドを使います:
- `includes(text)`は`text`がどこかに現れれば`true`
- `startsWith(text)`は文字列が`text`で始まれば`true`
- `endsWith(text)`は文字列が`text`で終われば`true`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// true を出力
console.log(file.startsWith("ph"));
// true を出力
console.log(file.endsWith(".jpg"));
// false を出力
```
比較は大文字・小文字を区別します: `"Hello".includes("h")`は`false`です。

---

`indexOf()`メソッドは、指定したテキストが文字列内で**最初**に現れるインデックスを返します。
テキストが見つからない場合は`-1`を返します:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// 2 を出力
console.log(word.indexOf("z"));
// -1 を出力
```

---

`slice(start, end)`メソッドは、インデックス`start`からインデックス`end`の直前まで（`end`は含まない）の部分文字列を取り出します:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// Java を出力
console.log(word.slice(4));
// Script を出力
```
`end`を省略すると、文字列の末尾まで切り出されます。
負のインデックスは末尾から数えます: `word.slice(-3)`は`"ipt"`です。
`substring(start, end)`メソッドも同じように動作しますが、負のインデックスは受け付けません。

---

`indexOf()`と`slice()`はうまく組み合わせて使えます。何かの位置を見つけて、そこで文字列を切り出すのです。
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// 45 を出力
```
