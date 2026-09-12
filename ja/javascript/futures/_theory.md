すぐには終わらない操作があります。ファイルのダウンロード、データベースの読み込み、タイマーの待機などです。JavaScript はそれらが実行されている間も固まることはありません。代わりに**`Promise`**を渡してきます。これは**後で**利用可能になる値を表すオブジェクトです。

**`async`**を付けた関数は必ずプロミスを返します。関数が返すものは何であれ、そのプロミスの中の値になります：
```javascript
async function fetchNumber() {
  return 42;
}
```
プロミスから値を取り出すには**`await`**を使います。`await`は、プロミスが値を持つまで関数を一時停止し、それから素の値を渡します。`await`を使えるのは`async`関数の中だけです：
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
`await`がないと、`n`はプロミスそのものになり、`console.log(n)`は数値の代わりに`Promise { 42 }`を出力します。

---

関数の前に`async`を付けると、その関数が返すものが変わります。本体は今までどおり普通の値を計算しますが、呼び出し元はその値を包んだプロミスを受け取ります。
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
2つの関数の中身は同じコードで、結果の読み取り方だけが異なります。`shoutLater("hi")`が`"HI"`を返すようにするには、別の`async`関数の中でawaitする必要があります。

待つことが何もない場合、関数に`async`を付けてもコストはかかりません。それでいて、後でその中で`await`を使えるようになります。

---

値が本当に後で届くときは、**`new Promise`**で自分でプロミスを作ります。`new Promise`は関数を1つ受け取り、その関数は**`resolve`**コールバックを受け取ります。値の準備ができたら`resolve(value)`を呼び出すと、プロミスはその値で履行されます。
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)`は`ms`ミリ秒後に`callback`が実行されるようスケジュールし、すぐに返ります。その間、何もブロックされません。

`new Promise`に渡された関数はすぐに実行されますが、`resolve`が呼ばれるまでプロミスは**pending**のままです。awaitすると値が得られます：
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

プロミスは常に3つの状態のどれかにあります：

- **pending**：作業がまだ進行中です
- **fulfilled**：作業が成功し、プロミスが値を保持しています
- **rejected**：作業が失敗し、プロミスがエラーを保持しています

プロミスはpendingの状態で始まり、状態が変わるのは多くても1回だけです。fulfilledかrejectedになったら**settled**（確定）となり、二度と変わることはありません。

`async`関数を呼び出しても待機することはありません。呼び出しは作業を開始し、すぐにpendingのプロミスを渡してくるので、呼び出しの次の行は作業が終わる前に実行されます。そのプロミスは普通のオブジェクトであり、その中の値ではありません。だからこそ`await`を忘れるのはよくある間違いなのです。

---

`await`はプロミスを読み取る唯一の方法ではありません。すべてのプロミスには**`.then(callback)`**メソッドがあります。プロミスが履行されるとすぐに、コールバックが値を受け取ります。
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`**は`value`ですでに履行されたプロミスを作ります。値は手元にあるのにプロミスを返さなければならないときに便利です。

`.then`は、コールバックが返したもので履行される**新しい**プロミスを返します。そのため、呼び出しを**チェーン**でき、各ステップが前のステップの結果を扱えます：
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

`async`関数は、他の関数と同じように上から下へ読めます。`await`は、待機したプロミスが履行されるまで関数を一時停止するだけで、その後は次の行から実行が続きます。
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
最後の行に注目してください。`async`関数でも**呼び出す**必要があります。括弧なしで`main`と書くと、作業を定義するだけで決して開始されず、何も出力されません。

---

非同期の作業は失敗することもあります。`new Promise`に渡す関数は2番目のコールバック**`reject`**を受け取ります。`reject(error)`を呼び出すと、プロミスはfulfilledの代わりにrejectedになります。
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
拒否するときは必ず`Error`オブジェクトを使ってください。`Error`は`message`とスタックトレースを持ちますが、素の文字列にはそれがありません。

拒否は**`.catch(callback)`**で読み取ります。`.then`の鏡像です。**`Promise.reject(error)`**はすでに拒否されたプロミスを作ります。`Promise.resolve`が履行されたプロミスを作るのと同じです：
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
`resolve`と`reject`の両方を呼び出しても、どちらかを2回呼び出しても、何も変わりません。最初の呼び出しだけが意味を持ちます。

---

`.then`、`.catch`、`.finally`は同じチェーンのリンクです。拒否は`.catch`に出会うまですべての`.then`をスキップします。`.catch`のコールバックが値を返すと、チェーンは再び履行され、通常どおり続きます。

**`.finally(callback)`**は、チェーンが確定したときに実行されます。履行されたか拒否されたかは関係ありません。コールバックは引数を取らず、戻り値は無視されるので、値は次の`.then`へ流れ続けます。スピナーを隠すような後片付けの場所です：
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

`async`関数の中では`.catch`は必要ありません。拒否されたプロミスをawaitするとエラーが**スロー**されるので、普通の`try` / `catch` / `finally`文で処理できます：
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
逆方向も成り立ちます。`async`関数の中の`throw`は呼び出し元をクラッシュさせず、関数が返したプロミスを拒否します。
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
どの`try`ブロックとも同じように、失敗した`await`の後の行はスキップされ、`catch`ブロックが実行され、どちらの場合でも`finally`ブロックが実行されます。

---

`await`の周りの`try` / `catch`のよくある使い方は、失敗を適切なデフォルト値に置き換えることです。そうすれば、呼び出し元はエラーを扱う必要がありません：
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
値をすぐに返す場合でも、`measure(path)`の前の`await`は残してください。`await`がないと、プロミスは`try`ブロックを通らずに関数の外へ出てしまい、拒否が`catch`から逃げてしまいます。

---

複数の結果が必要なとき、1つずつawaitしていては時間の無駄です。それぞれが前のものが終わってからでないと始まらないからです。**`Promise.all(promises)`**は、すでに実行中のプロミスの配列を受け取り、すべての値の配列で履行される1つのプロミスを返します：
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
覚えておく価値のある2つのルールがあります：

- 値は終わった順ではなく、**配列の順序どおり**に返ってきます
- どれかのプロミスが拒否されると、`Promise.all`が返すプロミスはその最初のエラーですぐに拒否され、他の値は失われます

---

`Promise.all`は、空の配列を含む任意の長さの配列で動作します。`Promise.all([])`をawaitすると、すぐに空の配列が返ってきます。これにより、「待つべきものが何もない」場合の特別扱いをせずに、実行時に作られたリストを安全に渡せます。
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
返ってくる配列は、受け取った配列と常に同じ数の要素を同じ位置に持つので、他の配列と同じようにループできます。

---

**逐次**と**並列**の待機の違いは、`await`を*どこに*置くかで決まります：
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
最初のバージョンでは、`await`がその行で関数を一時停止するため、2番目のダウンロードは1番目が終わってから始まります。2番目のバージョンでは、何かをawaitする前に両方の呼び出しが行われるので、`Promise.all`が待っている間に、両方のダウンロードはすでに実行されています。

2番目のタスクが本当に1番目の結果を必要とするときだけ、逐次のawaitを使ってください。そうでなければ、まずすべてを開始してからまとめてawaitします。

---

`Promise.all`は、1つでもプロミスが拒否されると諦めます。それでもすべての結果が欲しいときは、**`Promise.allSettled(promises)`**を使ってください。`Promise.allSettled`は決して拒否されず、プロミスごとに1つの小さなオブジェクトを同じ順序で入れて履行されます：

- 成功したものは `{ status: "fulfilled", value: ... }`
- 失敗したものは `{ status: "rejected", reason: ... }`

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
`status`が`"fulfilled"`のときだけ`value`を、`"rejected"`のときだけ`reason`を読んでください。もう片方のプロパティは単に存在しません。

---

**`Promise.race(promises)`**は、プロミスのうち**最初**に確定したものと同じタイミングで確定し、その結果をそのままコピーします。最初の値で履行されるか、最初のエラーで拒否されます。他のプロミスはキャンセルされず実行し続けますが、それが何を生成しても無視されます。
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
典型的な使い方は締め切りです。実際の作業を、しばらくしたら失敗するプロミスと競わせると、結果かタイムアウトエラーのどちらかが得られます。

空の配列には注意してください。`Promise.race([])`は、確定させるものが何もないため、永遠にpendingのままです。

---

最後のピースを組み合わせると、ほとんどすべての実際のアプリケーションで使われる小さなツールができます。締め切りです。`ms`ミリ秒後に拒否されるプロミスを作り、それを実際の作業と競わせると、先に確定したほうが結果を決めます：
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
`async`関数からプロミスを返すのも問題ありません。関数が返すプロミスはそれに追従するので、呼び出し元がawaitするのは、プロミスの中のプロミスではなく最終的な値です。
