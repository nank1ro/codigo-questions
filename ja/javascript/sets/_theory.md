**セット**は**ユニークな**値のコレクションです：各値は最大1回だけ現れることができ、位置で値にアクセスするためのインデックスはありません。
セットは、値が*何回*あるいは*どんな順序で*あるかではなく、*どの*値が存在するかだけを気にする場合に最適です。
`new Set()`で空のセットを作成し、`add(value)`で値を追加し、`has(value)`で値が存在するかどうかを確認します：
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
**スプレッド**演算子`...`はその逆で、セットを配列に戻します：
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)`も同じことを行います。

---

セットは値が追加された順序を記憶しており、`for...of`でループすることができます：
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
セットには、すべての値に対して関数を呼び出す`forEach()`メソッドもあります：
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
