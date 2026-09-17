**セット**は**ユニークな**値のコレクションです：各値は最大1回だけ現れることができ、位置で値にアクセスするためのインデックスはありません。
セットは、値が*何回*あるいは*どんな順序で*あるかではなく、*どの*値が存在するかだけを気にする場合に最適です。
`new Set()`で空のセットを作成し、`add(value)`で値を追加し、`has(value)`で値が存在するかどうかを確認します：
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// true を出力
console.log(colors.has("green"));
// false を出力
```

---

すでにセットに存在する値を追加しても**何も起こりません**：重複は単純に無視されます。
さらに2つの重要な機能があります：
- `delete(value)`はセットから値を削除します
- `size`は格納されている値の数です（プロパティなので括弧は不要です）

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// 2 を出力
tags.delete("css");
console.log(tags.size);
// 1 を出力
```

---

`add()`はセット自体を返すため、複数の呼び出しをチェーンできます：
```javascript
let letters = new Set();
letters.add("a").add("b");
```
チェーンするかどうかにかかわらず、すでに存在する値が2回目に追加されることはないため、`size`は各値を1回だけカウントします。

---

配列を`new Set()`に渡すことで、一度にセットを作ることができます。配列内の重複は取り除かれるため、これは配列の異なる値を見つける最も手っ取り早い方法です：
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// 3 を出力
```
**スプレッド**演算子`...`はその逆で、セットを配列に戻します：
```javascript
let unique = [...distinct];
console.log(unique);
// [ 1, 2, 3 ] を出力
```
`Array.from(distinct)`も同じことを行います。

---

セットは値が追加された順序を記憶しており、`for...of`でループすることができます：
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// 3 を出力
// 1 を出力
// 2 を出力
```
セットには、すべての値に対して関数を呼び出す`forEach()`メソッドもあります：
```javascript
nums.forEach((n) => console.log(n * 10));
// 30 を出力
// 10 を出力
// 20 を出力
```

---

`delete(value)`は、値が削除された場合は`true`を、セットに存在しなかった場合は`false`を返します。
**すべて**の値を一度に削除するには、`clear()`を呼び出します：
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// true を出力
console.log(cart.delete("pen"));
// false を出力
cart.clear();
console.log(cart.size);
// 0 を出力
```

---

セットは、`===`とほぼ同じルールで2つの値が「同じ」かどうかを判断します（ただし`NaN`は自分自身と等しいとみなされます）。文字列や数値の場合はその内容を比較しますが、**オブジェクトは参照によって比較されます**：同じフィールドを持つ2つのオブジェクトリテラルは、異なる2つの値として扱われます。
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// 1 を出力
people.add({ name: "Alice" });
console.log(people.size);
// 2 を出力
```
まったく同じオブジェクトを再度追加した場合のみ無視されます。

---

スプレッドと`filter()`を組み合わせることで、集合論の古典的な演算を行うことができます。それぞれが**新しい**コレクションを作り、元のセットは変更されません：
- **和集合**：`a`、`b`、またはその両方にある値すべて：`new Set([...a, ...b])`
- **積集合**：**両方**にある値だけ：`[...a].filter((x) => b.has(x))`
- **差集合**：`a`の値のうち`b`に**ない**もの：`[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// [ 1, 2, 3, 4 ] を出力
console.log([...a].filter((x) => b.has(x)));
// [ 3 ] を出力
console.log([...a].filter((x) => !b.has(x)));
// [ 1, 2 ] を出力
```
最近のJavaScriptエンジンでは、セットに直接`a.union(b)`、`a.intersection(b)`、`a.difference(b)`も用意されていますが、スプレッドとfilterによる方法はどこでも使えます。

---

`Map`と同じインターフェースを保つため、セットにもイテレーターメソッド`values()`、`keys()`、`entries()`が用意されています。
セットにはキーがないため、`keys()`は`values()`の別名にすぎず、`entries()`は各値を`[value, value]`というペアとして**2回**返します：
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// [ 'a', 'b' ] を出力
console.log([...letters.entries()]);
// [ [ 'a', 'a' ], [ 'b', 'b' ] ] を出力
```
実際にはこれらを使う必要はほとんどありません：`for...of`とスプレッドはすでに値を直接ループしてくれます。

---

`new Set()`は配列だけでなく、あらゆる**イテラブル**を受け取ります。文字列も1文字ずつイテラブルなので、テキストの異なる文字を取得できます：
```javascript
let letters = new Set("hello");
console.log([...letters]);
// [ 'h', 'e', 'l', 'o' ] を出力
```
