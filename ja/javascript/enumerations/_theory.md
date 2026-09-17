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

---

列挙型は`switch`文と自然に組み合わせられます。`switch`文は1つの値をいくつかの`case`ラベルのリストと比較し、最初に一致したもののコードを実行します。
各分岐は`return`または`break`で終わり、任意の`default`分岐はどれにも一致しなかった場合に実行されます。
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// go を出力
```
常に生の値（`"red"`）ではなくメンバー（`Light.RED`）と比較してください。そうすれば、値が変わっても`switch`は機能し続けます。

---

値からメンバー名に戻すことは**逆引き**と呼ばれます。`Object.keys()`で名前をループし、配列メソッド`find()`を使って値が一致する最初の名前を選びます。`find()`はコールバックが`true`になる最初の要素を返します（該当するものがなければ`undefined`を返します）。
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// HIGH を出力
```
`Priority[key]`は、変数`key`に格納された名前を持つメンバーを読み取ります。これはどんなオブジェクトに対しても使えるのと同じブラケット記法です。

---

文字列メンバーには1つの弱点があります。同じテキストを持つ任意の文字列がメンバーとして受け入れられてしまうことです。
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// true を出力
```
自分自身とだけ等しいメンバーが欲しい場合は、`Symbol`を使います。`Symbol(description)`は、同じ説明文で作成されたものであっても他のどのシンボルとも異なる、まったく新しい値を作成します。
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// true を出力
console.log(Suit.HEARTS === Symbol("hearts"));
// false を出力
console.log(typeof Suit.HEARTS);
// symbol を出力
```
渡すテキストはデバッグ用のラベルにすぎず、`description`プロパティで読み取ることができます（`Suit.HEARTS.description`は`"hearts"`です）。

---

列挙型の値は、例えばすべてのメンバーをラベルや価格に対応させるために、別のオブジェクトの**キー**としてよく使われます。オブジェクトリテラルの中でキーを角括弧`[ ]`で囲むと、式が評価されてその結果がキーとして使われます（**計算されたキー**）。これは文字列メンバーでもシンボルメンバーでも機能します。
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// Completed を出力
```
角括弧がなければ、`Status.DONE: "Completed"`は構文エラーになり、`"Status.DONE"`は単なる文字列のキーになってしまいます。

---

各メンバーが複数のデータや独自のメソッドを必要とする場合は、**クラス**が列挙型の役割を果たすことができます。すべてのメンバーはそのクラスのインスタンスであり、`static`プロパティ、つまり各インスタンスではなくクラス自体に属するプロパティに格納されます。
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// Earth を出力
```
クラスの後に`Object.freeze(Planet)`を呼び出すことで、誰もメンバーを追加したり置き換えたりできないようにし、コンストラクタの中で`Object.freeze(this)`を使って各インスタンスを凍結することで、メンバー自体を読み取り専用に保ちます。
