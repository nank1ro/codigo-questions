JavaScript では関数は**値**です。変数に入れたり、配列に入れたり、別の関数に引数として渡したりできます。関数を引数として受け取る関数、または関数を返す関数を**高階関数**と呼びます。渡された関数は**コールバック**と呼ばれます。受け取った側が必要になったときに*呼び返す*からです。
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
`shout` は**括弧なし**で渡されていることに注目してください。`twice(shout, "hi")` は関数そのものを渡しますが、`twice(shout("hi"), "hi")` は先に `shout` を呼び出し、その結果である文字列 `"HI!"` を渡すことになり、これは呼び出せません。

---

高階関数を使うと、*各要素に対して何をするか*と*要素をどうたどるか*を分けられます。たどる部分は一度だけ書き、残りはコールバックが決めます。
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
コールバックは要素を 1 つずつ受け取ります。上のようにその場で書いたアロー関数でも、変数に入れた任意の関数でもかまいません。次に学ぶ組み込みの配列メソッドも、内部ではまさにこのように動いています。

---

組み込みの `map` は `transform` と同じことをします。各要素についてコールバックを呼び出し、その結果を**新しい配列**にまとめます。`forEach` も各要素についてコールバックを呼び出しますが、何もまとめず、常に `undefined` を返します。出力のような副作用のためだけに使ってください。
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
よくある間違いは、`forEach` の結果を保存したり、その後ろに別のメソッドをつなげたりすることです。`undefined` を返すので、つなげるものがありません。目安として、新しい値が必要なら `map`、何かを*する*だけなら `forEach` を使います。

---

さらに 2 つの高階メソッドが、日常の用途のほとんどをカバーします。
`filter(callback)` は、コールバックが `true` を返した要素だけを含む新しい配列を返します。このように「はい／いいえ」で答えるコールバックを**述語**と呼びます。
`reduce(callback, initialValue)` はすべての要素を 1 つの値にまとめます。コールバックは**アキュムレータ**（ここまでの結果）と現在の要素を受け取り、新しいアキュムレータを返します。`reduce` の 2 番目の引数が最初のアキュムレータです。
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
`filter` と `map` は配列を返すので、つなげて最後に `reduce` で締めくくれます。`numbers.filter(...).map(...).reduce(...)` のようにです。

---

述語を使って配列について答える 3 つのメソッドがあります。
- `find(predicate)` は述語が `true` になる**最初の**要素を返し、なければ `undefined` を返します
- `some(predicate)` は**少なくとも 1 つ**の要素が述語を満たせば `true` を返します
- `every(predicate)` は**すべての**要素が満たせば `true` を返します（空の配列でも `true`）
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
3 つとも答えが決まった時点で止まるので、必要以上の要素を見ることはありません。

---

`sort(compare)` は、2 つの要素を受け取るコールバックを使って配列を**その場で**並べ替えます。コールバックは、最初の要素を先にすべきときは負の数、2 番目を先にすべきときは正の数、等しいときは `0` を返します。数値なら `(a, b) => a - b` で昇順、`(a, b) => b - a` で降順になります。
比較関数がないと、`sort()` は各要素を**文字列**に変換して 1 文字ずつ比較するので、`"1"` は `"9"` より小さく、`10` が `9` より前に来ます。
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
`sort` は配列を変更するので、元の順序も必要なときはコピーを並べ替えてください。`[...numbers].sort(...)` のようにします。文字列には比較関数として `(a, b) => a.localeCompare(b)` を使うと、テキストをアルファベット順に並べられます。

---

比較関数は要素のどの部分でも見られるので、あるプロパティを比較するだけでオブジェクトの配列をそのプロパティ順に並べ替えられます。
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
コピーを並べ替えれば `items` は元の順序のまま残ります。

---

高階関数は関数を**返す**こともできます。返された関数は、外側の関数が終わった後でも、自分が作られた場所の変数を覚えています。これを**クロージャ**と呼びます。
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
`makeMultiplier` を呼び出すたびに、それぞれ独自の `factor` を持つ新しい関数が作られます。こうして 1 つのひな形から似た関数の一群を作れます。同じものはアロー関数でも書けます。`const makeMultiplier = (factor) => (n) => n * factor;` のようにです。

---

クロージャは変数の値のコピーではなく、変数への**生きた**つながりを保ちます。同じ呼び出しの中で複数の関数が作られると、それらは同じ変数を共有し、一方を通した変更は他方からも見えます。
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
それら 2 つの関数を通す以外に、外部から `count` を読んだりリセットしたりすることは誰にもできません。この変数は**プライベート**です。`makeCounter()` を 2 回目に呼び出すと、まったく別の `count` が作られます。

---

関数は値なので、2 つの関数を新しい 1 つの関数に**組み合わせる**高階関数を書けます。`compose(f, g)` は、先に `g` を適用し、その結果に `f` を適用する関数を返します。数学の記法 *f(g(x))* と同じです。
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
順序が重要です。`compose(f, g)` は先に `g`、次に `f` を実行します。このように小さな関数をつなぎ合わせてプログラムを組み立てることを**関数合成**と呼びます。

---

関数を返す関数は、コールバックを**適合させる**自然な方法でもあります。ある述語があり、`filter` にはその反対が必要だとします。書き直す代わりに、包んでしまいましょう。
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
汎用の `not(predicate)` は、どんな述語に対してもこれを行います。同じ引数で `predicate` を呼び出し、結果を `!` で反転する新しい関数を返します。`filter`、`find`、`some`、`every` の述語は要素を第 1 引数として受け取るので、ラッパーはその 1 つの値だけを渡せば十分です。

---

`reduce` のアキュムレータは数値である必要はありません。文字列、配列、オブジェクトでもかまいません。空のオブジェクト `{}` から始めれば、一度の走査で数えたりグループ分けしたりできます。コールバックからは必ず**アキュムレータを返す**ようにしてください。そうしないと次のステップは `undefined` を受け取ります。
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` は現在のカウントを読み取り、そのキーがまだ存在しない場合は `0` を読み取ります。

---

すべての関数は `bind` メソッドを持ち、いくつかのものをあらかじめ固定した**新しい**関数を返します。最初の引数は新しい関数の `this` になり、残りの引数は、新しい関数を呼び出すときに渡す引数の前に置かれます（**部分適用**）。
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
`this` を固定することはメソッドで重要です。メソッドをオブジェクトから取り出して単独で呼び出すと、`this` はもうそのオブジェクトを指さないので、`this.name` は `undefined` になります。`bind` はそれをオブジェクトに固定します。
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
元の関数は決して変更されません。`bind` は常に新しい関数を作り、その `name` は元の名前の前に `bound ` が付いたものになります。

---

実際のプログラムでは、これらのメソッドを**パイプライン**として組み合わせます。必要な要素を絞り込み、必要な値に変換し、1 つの結果にまとめます。途中の配列を定数に入れておくと各ステップが読みやすくなり、再利用もできます。
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` は文字列の配列を、要素をカンマと空白で区切った 1 つの文字列に変えます。

---

クロージャを使うと、返された関数が呼び出しをまたいで**プライベートな状態**を保てます。こうして作られる定番のヘルパーが `once(fn)` です。返された関数は最初に呼ばれたときだけ `fn` を実行し、その結果を覚えておき、以降の呼び出しでは `fn` を再実行せずに同じ結果を返します。
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
ラッパーには 2 つのプライベート変数が必要です。`fn` をすでに実行したかどうかと、保存した結果です。どちらもクロージャの中にあり、外からは見えません。ラッパーのすべての引数を `fn` に渡すには、残余引数 `(...args)` を使ってラッパーを宣言し、`fn(...args)` を呼び出します。

---

すべてが `groupBy(items, keyFn)` に集約されます。これは、各要素の**グループキー**を決めるコールバックを受け取り、各キーにそのキーを持つ要素の配列を対応させたオブジェクトを返す高階関数です。オブジェクトをアキュムレータにした `reduce` がすべてを行います。
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
各要素についてキーを求め、そのキーの配列がまだなければ作り（`acc[key] ?? []`）、要素を追加してアキュムレータを返します。`keyFn` は呼び出す側が選ぶので、同じ関数で単語を頭文字ごとに、人を都市ごとに、数値を偶奇ごとにグループ分けできます。
