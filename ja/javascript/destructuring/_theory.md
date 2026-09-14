配列から値を 1 つずつインデックスで取り出すのは冗長です:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**分割代入**は同じ仕事を 1 行で行います。`=` の左側には配列そのものに似たパターンを書き、その中のすべての名前が同じ位置の要素を受け取ります:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
パターンが配列全体をカバーする必要はありません。余分な要素は単に無視され、対応する要素のない名前は `undefined` になります。

---

分割代入は、関数の引数や呼び出しの結果のように、配列が現れるその場で最も役立ちます。配列をそのまま保持してあちこちでインデックスで参照する代わりに、一度展開して各部分に実際の名前を付けられます:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
元の配列はコピーも変更もされず、パターンはそこから読み取るだけです。

---

配列の奥深くにある 1 つの要素だけが重要なことがあります。パターンでは位置を空のままにして、区切るカンマだけを残せます。このような空の位置は**ホール**と呼ばれ、名前を付けずに要素をスキップします:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
数えるのは名前ではなくカンマです。各カンマは、手前に名前があるかどうかにかかわらず、パターンを 1 位置前に進めます。

---

配列がパターンの期待どおりの長さとは限りません。名前の後に `= value` と書くと**デフォルト値**が与えられ、配列にその位置の要素がないときに使われます:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
デフォルト値は必要なときにだけ評価されるので、関数呼び出しであってもかまいません。また、デフォルト値は最後の位置だけでなく任意の位置に付けられます。

---

パターンは、`const` や `let` を手前に付けずに通常の代入の左側に置くこともでき、その場合はすでに存在する変数に書き込みます。これにより、2 つの値の入れ替えが一時変数なしの 1 行になります:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
右辺が先に作られるので、代入が行われるときには両方の古い値がすでに一時配列の中に安全に収まっています。前の行のセミコロンに注意してください。そうしないと、`[` で始まる行は直前のものに対するインデックスとして読まれてしまいます。

---

オブジェクトも、角括弧の代わりに波括弧を使って分割代入できます。ここでは位置は何の意味も持ちません。各名前は、同じつづりの**キー**と照合されます:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
パターン内で `age` と `name` を入れ替えても結果は変わらず、パターンが言及しないキーは単にそのまま残されます。対応するキーのない名前は `undefined` になります。

---

オブジェクトのパターンとデフォルト値は、配列の場合とまったく同じように組み合わせられます。これにより、キーがあるかどうか分からない設定オブジェクトを読むための整った方法になります:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
パターン全体が 1 つの文なので、関数は最初の行で引数から必要なものをすべて展開できます。

---

オブジェクトのパターンはキーの名前に合わせて変数を命名しますが、キーが暗号のようだったりすでに使われていたりすると不便です。`key: newName` と書くと変数の**名前を変更**できます:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
「`n` を取り、それを `name` と呼ぶ」と読みます。コロンは型を宣言するものではなく、`n` 自身は変数として作られず、作られるのは `name` だけです。名前を変更した変数にもデフォルト値を後ろに書いて付けられます: `{ n: name = "unknown" }`。

---

デフォルト値には誰もが驚くルールが 1 つあります。適用されるのは `undefined` に対して**だけ**です。存在していて `null`、`0`、`""`、`false` を持つキーは実際の値なので、パターンはそれを採用し、デフォルト値は決して使われません:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` は API レスポンスではよく「値なし」を意味しますが、ここでは `0` と同じように振る舞います。`null` も置き換えたい場合は、まず分割代入し、その後で `??` によるフォールバックを使ってください。

---

キーが別のオブジェクトや配列を保持している場合も、パターンはそのまま続けてその形を記述できます:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
その行が何を作るかに注意してください。`address: { city }` は「`address` の中に入る」ことを意味し、「`address` を渡して」ではないので、変数になるのは `city` だけです。両方を得るにはキーを 2 回書きます: `const { address, address: { city } } = user;`。配列とオブジェクトのパターンは、`{ tags: [first] }` のように互いに自由に入れ子にできます。

---

配列の先頭を取り出して残りを保持するのは非常によくある需要なので、パターンにはそれ専用の構文があります。最後の名前の前にドットを 3 つ付けると**rest 要素**になり、残りのすべての要素をまったく新しい配列に集めます:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
rest 要素はパターンの最後に来なければならず、デフォルト値を持てません。何も残っていないときは単に空の配列になります。

---

オブジェクトのパターンにも rest があり、その場合はパターンが言及しなかったすべてのキーを新しいオブジェクトに集めます:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
これは、あるキーを除いたオブジェクトのコピーを作る最も短い方法です。元のオブジェクトは決して変更されず、rest オブジェクトは残りの値を保持する新しいオブジェクトになります。

---

関数宣言では、パターンをパラメータ名の代わりに置けます。そのため、呼び出しのときに展開が行われます:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
本体の中にはオブジェクト変数はまったくなく、`width` と `height` だけがあります。呼び出し側は 1 つのオブジェクトを渡しますが、シグネチャは関数がどのキーを読むかを正確に文書化し、キーはどんな順序で到達してもかまいません。

---

デフォルト値付きの分割代入パラメータはきれいな options オブジェクトを作りますが、呼び出し側が何も渡さないときにはやはり壊れます。`undefined` からキーを読むと `TypeError` がスローされるからです。パターン全体に `{}` というデフォルト値を与えると修正できます:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
この行は外側から読みます。`= {}` は引数がないときに空のオブジェクトを供給し、その後、内側の各デフォルト値がそれぞれのキーを埋めます。

---

`Object.entries(obj)` はオブジェクトを `[key, value]` ペアの配列に変換します。`for...of` ループのヘッドに配列パターンを置くと、ループが回るたびに各ペアが展開されます:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
これはオブジェクトをたどる読みやすい方法です。インデックスもルックアップもなく、関心のある 2 つの名前だけがあります。`Object.keys` と `Object.values` はそれぞれ片側だけを返し、`Object.entries` は両方を返します。

---

これまでに見たすべては 1 つの構文に属するので、部品は自由に組み合わさります。オブジェクトのパターンは別のオブジェクトのパターンを入れ子にでき、その中ではデフォルト値付きでキーの名前を変更でき、さらに rest 要素で終わる配列のパターンを並べられます。こうして 1 行で関数が期待する形全体を記述できます:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
読みやすさを保ってください。2、3 行に収まらなくなったパターンは、通常、関数が要求しすぎているサインです。
