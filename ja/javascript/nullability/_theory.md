JavaScriptには「ここには値がない」ことを表す方法が2つあります。
`undefined`は値が**一度も提供されていない**ことを意味します。値なしで宣言された変数は`undefined`を持ち、オブジェクトに存在しないプロパティも同様です:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null`は「空であることを、自分はわかっている」と意図的にあなたが代入する値です:
```javascript
let owner = null;
console.log(owner);
// prints null
```
つまり`undefined`は通常、何かが欠けていることを言語が伝えているものであり、`null`はプログラマーが何かを意図的に空にしていることを示すものです。

---

関数はさらに2つの場面で`undefined`を生み出します。
宣言されているより**少ない引数**で関数を呼び出すと、欠けている引数は`undefined`になります:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
関数が**`return`なしで**(または`return;`のみで)終わると、呼び出しの結果は`undefined`になります:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
`null`を明示的に渡すことは引数を省略することと同じではないことに注意してください: `greet(null)`は`null`を出力します。`null`は関数に渡された実際の値だからです。

---

`typeof`演算子は値の型を文字列として返します。`undefined`に対しては期待どおり`"undefined"`と答えます:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
しかし`null`に対しては`"object"`と答えます。これはJavaScriptの最初のバージョンからのバグで、あまりに多くのコードがそれに依存しているため修正されることはありませんでした:
```javascript
console.log(typeof null);
// prints object
```
したがって`typeof`は`undefined`を検出する確実な方法ですが、`null`の検出には使えません。`null`を調べるには、直接比較します: `value === null`。

---

`null`と`undefined`は互いにどのように比較されるのでしょうか？ それは演算子によります。
**緩い**等価演算子`==`は両者を同じものとして扱い、`0`、`""`、`false`を含む他のどの値とも異なるものとみなします:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
**厳密**等価演算子`===`は型も比較しますが、`null`と`undefined`は型が異なります:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

ほとんどの場合、2つの「値なし」マーカーの*どちら*を受け取ったかは気にしません: 値が存在するかどうかだけを知りたいはずです。
`null == undefined`は`true`であり、`null`と緩く等しいものは他にないため、`value == null`という比較は**両方**を一度にキャッチする標準的なイディオムです:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
これは`===`よりも`==`が好まれる唯一のケースです: `value === null || value === undefined`と書いてもまったく同じ働きをしますが、より長くなるだけです。
`0`、`""`、`false`などの値は`null`では*ありません*: それらはたまたまfalsyな実際の値です。

---

`null`または`undefined`のプロパティを読むと、プログラムを停止させるエラーになります:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address`は`undefined`であり、`undefined`にはプロパティがありません。**オプショナルチェーン**演算子`?.`がこれを解決します: 左側の値が`null`または`undefined`の場合、式全体がそこで止まり、スローする代わりに`undefined`と評価されます:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
左側に値がある場合、`?.`は通常の`.`とまったく同じように動作します。いくつでも連鎖できます: `user.address?.street?.name`は、どこかのリンクが欠けている時点で`undefined`を返します。

---

オプショナルチェーンはドットによるプロパティアクセスに限られません。さらに2つの形式があります。
`?.[]`は左側に値がある場合にのみ、要素または計算されたキーを読みます:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()`は関数が存在する場合にのみ呼び出します。これはオプションのコールバックに便利です:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
どの形式でも、チェックは`?.`の**直前の**値に適用されます: `post?.tags?.[0]`は`post`自体が`null`や`undefined`でも安全です。

---

値が欠けているかもしれないとわかったら、通常はその代わりに**デフォルト**値を用意したくなります。それを行う演算子が2つあり、「欠けている」とみなす基準が異なります。
`a || b`は`a`が**falsy**なときは常に`b`を返します: `null`と`undefined`だけでなく、`0`、`""`、`false`、`NaN`も対象です。
**null 合体**演算子`a ?? b`は`a`が`null`または`undefined`のときにのみ`b`を返し、それ以外の値はそのまま保持します:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
`0`、`""`、`false`が保持すべき正当な値である場合は`??`を使い、すべてのfalsyな値を本当に置き換えたい場合は`||`を使ってください。

---

非常によくあるパターンは「このプロパティがまだ設定されていない場合にのみ埋める」というものです。`??`で書くと名前を繰り返すことになります:
```javascript
options.timeout = options.timeout ?? 1000;
```
**null 合体代入**演算子`??=`は同じことを1ステップで行います: 左側が現在`null`または`undefined`である場合にのみ右側を代入し、それ以外の値はそのまま残します:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries`は`0`がnullishではないため`0`のままです; `timeout`は存在しなかったので`1000`を受け取ります。同じ考え方は`||`に対する`||=`にも存在し、こちらはすべてのfalsyな値を上書きします。

---

**デフォルト引数**は、呼び出し側が値を提供しなかった場合に引数へ値を与えます。そのルールは正確です: デフォルトが使われるのは引数が`undefined`のときだけです。これは引数の省略も含みます。`null`を渡してもデフォルトは発動**しません**。`null`は値だからです:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
デフォルト引数は`undefined`のルールに従いますが、`??`は`null`と`undefined`の両方をカバーします: 関数がどのように呼ばれるかに合わせて選んでください。

---

オプショナルチェーンと`== null`によるガードはうまく連携します: チェーンはネストした値をスローせずに読み、ガードは結果が欠けている場合の対処を決めます:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
最後の`return`の中ではプレーンな`.`が安全です。ガードがすべてのリンクの存在をすでに証明しているからです。

---

多くの組み込みメソッドは「何も見つからなかった」ことを`undefined`を返すことで報告します。配列メソッド`find(callback)`が典型的な例です: コールバックが`true`になる最初の要素を返し、一致する要素がない場合は`undefined`を返します:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
ここで`found.price`を読むとスローしてしまうため、`?.`と`??`は`find`の自然な相棒です:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null`と`undefined`は、`JSON.stringify()`でオブジェクトをJSONに変換するときに異なる動作をします。
JSONには`null`という値はありますが`undefined`はありません。そのため、値が`undefined`のプロパティは単に**省かれ**、`null`のプロパティは保持されます:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
配列の中では位置を消すことができないため、そこでは`undefined`は`null`になります:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

`obj.key === undefined`のチェックでは、2つの場面を区別できません: プロパティが存在しないのか、存在するが値として`undefined`を持っているのかです。
`Object.hasOwn(obj, key)`は最初の疑問にのみ答えます: オブジェクトが`key`という名前の**自身の**プロパティを持っていれば、その値が何であれ`true`を返します:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
「自身の」とは、オブジェクト自体に宣言されたことを意味します: `toString`のような継承されたメンバーはすべてのオブジェクトで利用できますが、`Object.hasOwn(config, "toString")`は`false`です。
