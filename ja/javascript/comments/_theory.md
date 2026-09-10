**コメント**とは、ソースコードの中に書かれた、読む人のためのメモです。JavaScript はコメントを完全に無視するので、コメントがプログラムの動作を変えることはありません。

最も単純なコメントは**単一行コメント**です。`//` で始まり、その行の終わりまで続きます。
```javascript
// Greets the user
console.log("Hello");
```
コメントは、そのコードが何のためにあるのか、なぜそう書かれたのかを説明するために使います。他の言語とは違い、JavaScript では `#` はコメントを開始**しない**ことに注意してください。

---

コメントは専用の行である必要はありません。同じ行のコードの後ろに続けることもできます。これが**インラインコメント**（行末コメント）で、その文についての短いメモを書くのに適した場所です。
```javascript
const retries = 3; // give up after three attempts
```
`//` から行末までのすべてが無視され、その前にあるコードはいつもどおり実行されます。

---

コメントは無視されるので、コメントを追加したり削除したりしてもプログラムの動作は決して変わりません。実行されるのは、コメントアウトされて**いない**コードだけです。

そのため `//` は、コードを削除せずに 1 行だけ無効にする手軽な方法になります。これを**コメントアウト**と呼びます。
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
2 行目はコメントになったので、`total` は `10` のままです。`//` を取り除けば、その行はまた生き返ります。

コメントアウトは試行錯誤の間は便利ですが、後片付けを忘れないでください。長期間コメントアウトされたままのコードは、次に読む人を混乱させるだけです。

---

コメントに複数行が必要なとき、JavaScript には**複数行コメント**（ブロックコメントとも呼びます）があります。`/*` で始まり `*/` で終わり、その間にあるものは改行も含めてすべて無視されます。
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
ブロックコメントは短く 1 行に収めることもできます: `/* like this */`。

---

どの種類のコメントを使っても、ルールは同じです。その中のテキストは**コードではありません**。コメントの中の `console.log` は何も出力しませんし、同じ行の `//` より後ろに書かれたコードは、その行が本物のコードで始まっていても決して実行されません。
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
プログラムが何を出力するか分からないときは、まず頭の中ですべてのコメントを消して、残ったものを読んでみましょう。

---

行末で終わる `//` とは違い、`/*` コメントは `*/` に出会うまで終わりません。閉じ忘れると、JavaScript はそれ以降のコードをすべてコメントの一部とみなし、構文エラーを報告します。
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
`//` も `/* */` もインラインコメントとして使えますが、`/*` を使うときは必ず `*/` があることを確認してください。

---

JavaScript のブロックコメントは**入れ子にできません**。コメントは、その前にいくつ `/*` があっても、**最初に**出会った `*/` で終わります。
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
ここではコメントが `inner` の直後で終わるので、`still a comment */` はコードとして読まれ、構文エラーになります。すでに `/* */` コメントを含むブロックをコメントアウトするときは、このことを覚えておいてください。各行に `//` を付けるか、先に内側のコメントを削除しましょう。

---

複数行を一度にコメントアウトするには、各行に `//` を付ける代わりに、それらを 1 つのブロックコメントで囲みます。
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
ブロックの中の行は無視されるので、`total` は変化しません。これはそれらの行に `*/` が含まれていない場合にのみ有効であることを覚えておいてください。

---

JavaScript には 3 つ目の種類のコメント、**ドキュメンテーションコメント**があり、**JSDoc** 形式で書かれます。これは `/**`（アスタリスク 2 つ）で始まるブロックコメントで、関数のすぐ上に置きます。中の行はふつう ` * ` で始まり、`@` で始まる特別な**タグ**が関数を説明します。
- 各パラメータには `@param {type} name description`
- 戻り値には `@returns {type} description`

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
JavaScript にとってはただのコメントですが、エディタはこれを読み取り、`greet` のヘルプテキストとして、波かっこの中に書かれた型（`{number}`、`{string}`、`{boolean}`、`{number[]}` など）とともに表示します。

---

JSDoc コメントの最初の行は**要約**です。関数が何をするのかを述べる短い一文で、関数を説明するように三人称で書きます: "Returns..."、"Adds..."、"Checks..."。その後にタグを 1 行ずつ並べます。
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
コメントは宣言のすぐ上に、間に空行を入れずに置かなければなりません。そうしないとエディタはそれを関数に結び付けません。

---

JSDoc コメントは**契約**でもあります。本体が書かれる前から、関数を呼ぶ人に何を渡し何が返ってくるのかを伝えます。コメントを読むだけで関数を実装できることも少なくありません。
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
各 `@param` は同じ順序で 1 つのパラメータに対応し、`@returns` はあり得るすべての結果を説明します。

---

JSDoc コメントの中の順序はいつも同じです。まず要約、次に宣言された順に各パラメータの `@param`、最後に `@returns` です。開始の `/**` と終了の ` */` が全体を囲み、コメントは説明対象の関数のすぐ上に置かれます。
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

JavaScript ファイルは、**シバン**（ハッシュバン）と呼ばれる特別な行で始めることができます。`#!` に続けて、そのファイルを実行すべきプログラムのパスを書きます。Unix 系のシステムでは、これによって先に `node` と打たずに `./hello.js` のようにターミナルから直接スクリプトを実行できます。
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript はこの行をコメントとまったく同じように無視しますが、それはファイルの**いちばん最初の行**である場合だけです。それ以外の場所では `#!` は構文エラーになります。`/usr/bin/env node` は「このシステム上の `node` を見つけて使う」という意味です。

---

良いコメントは、コードが**何を**するかではなく、**なぜ**そうするのかを説明します。何が起きるかはコード自体が示しています。それを言葉で繰り返すとノイズが増え、コードが変わった途端に古くなります。
```javascript
// set timeout to 30
const timeout = 30;
```
その数字の背後にある理由こそ、読む人には推測できないものです。
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
コメントが下の行を言い換えているだけなら、削除するか、理由に置き換えましょう。

---

エディタが理解する慣習に従うコメントもあります。最もよく使われる**マーカー**は次のとおりです。
- `// TODO: ...` はこれから書く必要があるものを示します
- `// FIXME: ...` は誤りだと分かっていて修正が必要なコードを示します

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
JavaScript にとってはふつうのコメントですが、エディタはこれらを一覧表示するので、残っている作業を見つけやすくなります。`TODO` はたいてい、本当の実装が書かれるまでコードを動かし続けるための仮実装のそばにあります。作業を終えたら、同じ変更の中で仮実装を置き換え、マーカーを削除してください。古くなった `TODO` は誤解を招きます。

---

`FIXME` は `TODO` とは違います。コードはすでに存在しますが、それが誤りだと分かっている場合に使います。良い `FIXME` はバグが何であるかを述べ、可能ならそれを示す例も挙げるので、次の人がすばやく修正できます。`TODO` と同じく、バグを直したらマーカーは削除しますが、今も正しい JSDoc コメントは残してください。
