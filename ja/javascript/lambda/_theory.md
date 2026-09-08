関数には名前は必要ありません。**関数式**は関数を値として作成するので、変数に格納してその変数経由で呼び出せます：
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
**アロー関数**は同じものをより短く書く方法です。`function`キーワードを省き、パラメータリストと本体の間に「ファットアロー」`=>`を置きます：
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
アロー関数は通常`const`に格納されるため、名前が誤って再代入されることはなく、他の関数とまったく同じように呼び出されます。

---

よくある2つの場合に、アロー関数はさらに短くできます。
本体が**単一の式**である場合は、波括弧と`return`キーワードを省略でき、式の値が自動的に返されます（**暗黙のreturn**）：
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
**パラメータが1つだけ**の場合は、その周りの括弧も省略できます：
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
パラメータが0個、または2個以上の場合は括弧が必要です：`() => 42`と`(a, b) => a + b`。

---

暗黙のreturnには1つの罠があります。本体が`{`で始まるアロー関数は、オブジェクトリテラルとしてではなく**ブロック本体**として解釈されます：
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
ここで`{ name: name }`は、ラベル`name:`とその後の式`name`を含むブロックです。何も返されないため、呼び出しは`undefined`になります。
1行でオブジェクトリテラルを返すには、**括弧**で囲んでJavaScriptに式として扱わせます：
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

オブジェクトリテラルを括弧で囲むことは、1行のアロー関数でオブジェクトを作る標準的な方法です。例えば、いくつかの値を1つのレコードにまとめるときに使います：
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
パラメータを持たないアロー関数は、空の括弧`()`で始まります：
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

アロー関数が真価を発揮するのは**コールバック**です。コールバックとは、他の関数に引数として渡される関数のことです。配列メソッドが最も一般的な例です。
`map(callback)`は各要素に対するコールバックの結果を含む新しい配列を返し、`filter(callback)`はコールバックが`true`を返す要素だけを含む新しい配列を返します：
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
どちらも新しい配列を返し、元の配列はそのままなので、`numbers.filter(...).map(...)`のようにチェーンできます。

---

コールバックを取る配列メソッドがもう2つあります。
`forEach(callback)`は要素ごとにコールバックを1回呼び出し、何も返しません。出力などの副作用のために使います。
`reduce(callback, initialValue)`は配列を1つの値に畳み込みます。コールバックはこれまでの累積値と現在の要素を受け取り、新しい累積値を返します：
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)`は、2つの要素を受け取り、1つ目を先にすべきなら負の数、2つ目を先にすべきなら正の数、等しいなら`0`を返すコールバックを使って、配列をその場で並べ替えます。数値の場合、`(a, b) => a - b`は昇順に、`(a, b) => b - a`は降順に並べ替えます。
`find(callback)`はコールバックが`true`を返す最初の要素を返し、なければ`undefined`を返します：
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

アロー関数のパラメータは、通常の関数のパラメータと同じ機能をサポートしています。
引数が省略されたり`undefined`だったりする場合は、**デフォルト値**が使われます：
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
デフォルト値を持つパラメータは、それが唯一のパラメータであっても必ず括弧が必要です：`name = "World" => ...`は構文エラーです。

---

**レストパラメータ**`...name`は任意の数の引数を1つの配列にまとめます。アロー関数でも使えます：
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
通常の関数には、受け取ったすべての引数を保持する隠れた配列風の`arguments`オブジェクトもあります。アロー関数には**ありません**。アロー関数の中では、`arguments`は外側の関数の`arguments`を参照するか、まったく存在しません。アロー関数で「すべての引数」が必要なときは、レストパラメータを使いましょう。

---

関数は、**作成された**スコープの変数を、そのスコープの実行が終わった後でも覚えています。これを**クロージャ**と呼びます。
典型的な例はカウンター生成関数です。`makeCounter`を呼び出すたびに新しい`count`が作られ、その同じ`count`を使い続けるアロー関数が返されます：
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
他の誰も`count`を読んだりリセットしたりできません。`count`は返された関数の中にだけ存在します。2回目の`makeCounter()`の呼び出しは、独自の`count`を持つ独立したカウンターを作ります。

---

関数は値なので、アロー関数は**別のアロー関数を返す**ことができます。2つのアローをチェーンすることは、関数を作る関数を書くためのコンパクトな方法です：
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
左から右に読みます。`makeAdder`は`amount`を受け取り、`(n) => n + amount`（クロージャを通して`amount`をキャプチャするアロー関数）を返します。`makeAdder(1)(5)`は返された関数をすぐに呼び出します。
