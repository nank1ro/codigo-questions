**列挙型**（*enum*）とは、曜日、トランプのスート、注文の状態のように、関連する値の小さな固定グループのための共通の型です。
多くの言語と異なり、JavaScriptには`enum`キーワードが**存在しません**。慣用的な代替手段は、メンバーをプロパティとして持つ通常のオブジェクトを`Object.freeze()`に渡し、後から誰も変更できないようにすることです。
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// red を出力
```
慣習として、このオブジェクトは`const`で宣言され、名前は大文字で始まり、メンバー名は他の定数と同じように`UPPER_CASE`で書かれます。

---

各メンバーに格納する値は自由に選べます。**文字列**は、出力・ログ・ファイル保存の際に読みやすいため最も一般的な選択肢です。
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// done を出力
```
一度凍結されたオブジェクトには新しいプロパティを追加することもできず、`Object.isFrozen(obj)`でオブジェクトが凍結されているかどうかを確認できます。
```javascript
console.log(Object.isFrozen(Status));
// true を出力
```

---

そもそもなぜオブジェクトを凍結するのでしょうか？凍結されたオブジェクトはあらゆる変更を拒否します。既存のメンバーへの代入、新しいメンバーの追加、削除のいずれも効果がありません。
この拒否がどのように現れるかは、コードが実行されるモードによって異なります。
- **スロッピーモード**（通常のスクリプトのデフォルト）では、代入は**黙って無視されます**
- **strictモード**（`"use strict"`で始まるファイル、ESモジュール、クラス本体）では、`TypeError`が**送出されます**

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// s を出力
console.log(Size.MEDIUM);
// undefined を出力
```
どちらのモードでも、列挙型は定義した値をそのまま保持します。これはまさに定数の集合に求められる性質です。

---

メンバーは**数値**を保持することもできます。数値は、メンバー同士に自然な順序がある場合に、通常の演算子で比較できるため便利です。
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// true を出力
```
トレードオフは可読性です。`Priority.HIGH`を出力すると`3`と表示され、文字列`"high"`ほど多くの情報を伝えません。

---

列挙型は単なるオブジェクトなので、通常のオブジェクト用ヘルパーを使って中身を調べることができます。
- `Object.keys(Enum)`はメンバーの**名前**の配列を返します
- `Object.values(Enum)`はメンバーの**値**の配列を返します
- `Object.entries(Enum)`は`[名前, 値]`のペアの配列を返します

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// [ 'RED', 'BLUE' ] を出力
console.log(Object.values(Color));
// [ 'red', 'blue' ] を出力
```
`Object.values()`と配列メソッドの`includes()`を組み合わせることは、例えばユーザー入力から読み取った値のような任意の値が、有効なメンバーかどうかを確認する標準的な方法です。
```javascript
console.log(Object.values(Color).includes("red"));
// true を出力
console.log(Object.values(Color).includes("pink"));
// false を出力
```
