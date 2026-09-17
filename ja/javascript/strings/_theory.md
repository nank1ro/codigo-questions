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

---

`split(separator)`メソッドは、`separator`が現れるたびに区切って、文字列を断片の**配列**に分割します:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// [ 'I', 'like', 'JavaScript' ] を出力
```
その逆が配列メソッドの`join(separator)`で、断片を再び1つの文字列につなぎ合わせます:
```javascript
console.log(words.join("-"));
// I-like-JavaScript を出力
```

---

ユーザーの入力には、前後に余分なスペースが入っていることがよくあります。`trim()`メソッドは、文字列の**両端**から空白を取り除いたコピーを返します:
```javascript
let input = "   hello   ";
console.log(input.trim());
// hello を出力
```
`trimStart()`は先頭の空白だけを、`trimEnd()`は末尾の空白だけを取り除きます。
文字列の途中にあるスペースは決して変更されません。

---

`replace(search, replacement)`メソッドは、`search`が**最初**に現れた箇所を`replacement`に置き換えた新しい文字列を返します:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// blue red を出力
```
**すべて**の出現箇所を置き換えるには`replaceAll()`を使います:
```javascript
console.log(text.replaceAll("red", "blue"));
// blue blue を出力
```

---

`repeat(count)`メソッドは、文字列を`count`回繰り返した結果を返します:
```javascript
console.log("ab".repeat(3));
// ababab を出力
console.log("ab".repeat(0));
// 空の文字列を出力
```

---

`padStart(targetLength, padString)`メソッドは、文字列が`targetLength`文字に達するまで**先頭**に`padString`を追加します。`padEnd()`は末尾に対して同じことを行います:
```javascript
console.log("7".padStart(3, "0"));
// 007 を出力
console.log("Tea".padEnd(6, "."));
// Tea... を出力
```
文字列がすでに十分な長さであれば、変更されずにそのまま返されます。
数値には文字列メソッドがないため、まず`String(number)`で文字列に変換してください。

---

2つの文字列が`===`で等しいのは、まったく同じ文字が同じ大文字・小文字で並んでいる場合だけです:
```javascript
console.log("hello" === "hello");
// true を出力
console.log("hello" === "Hello");
// false を出力
```
`<`と`>`演算子は、文字列を1文字ずつアルファベット順に比較します。
大文字は小文字より前に来るため、`"Zoo" < "apple"`は`true`になります。

---

文字列は**イミュータブル**です。つまり、一度作成された文字列は決して変更できません。
インデックスへの代入は何も起こさず、すべての文字列メソッドは元の文字列を変更するのではなく、**新しい**文字列を返します:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// hello を出力
word.toUpperCase();
console.log(word);
// hello を出力
```
結果を保持するには、変数に代入し直してください:
```javascript
word = word.toUpperCase();
```

---

空の区切り文字で`split("")`を呼び出すと、文字列は1文字ずつの配列に変換されます。
配列には`reverse()`メソッドがあるので、分割・反転・結合することで文字列を反転できます:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// cba を出力
```
