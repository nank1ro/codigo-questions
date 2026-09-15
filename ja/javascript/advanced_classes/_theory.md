すでに学んだように、`extends` を使うとあるクラスが別のクラスの子になります。このキーワードが実際に与えてくれるのは**継承**です。子クラスは親のすべてのプロパティとメソッドを無料で受け取り、その上に自分のものを追加できます。

継承を便利にする鍵となるのが **`super`** です。子のコンストラクタ内で `super(...)` と書くと親のコンストラクタが呼ばれ、親は自分が担当する部分のオブジェクトをセットアップできます：
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
ここでは `super(name)` が `name` を `Animal` に渡して格納させ、`Dog` は `breed` だけを考えればよいことになります。

---

子クラスは、親がすでに提供しているものを再定義する必要はありません。メソッドも継承されるので、子のインスタンスはそれを自分のものとして呼び出せます：
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// Max makes a sound を出力
```
子が独自のコンストラクタを宣言するとき、その中で `super(...)` を呼ぶことは**必須**です。呼ばないとオブジェクトが初期化されず、JavaScript は `ReferenceError` を投げます。コンストラクタをまったく持たない子クラスは問題ありません。JavaScript がすべての引数を親に転送するコンストラクタを自動で書いてくれるからです。

---

`super()` についてのルールは「どこかで呼べばよい」よりも厳密です。子のコンストラクタ内では、`super()` が実行されるまで `this` という言葉は存在しません。オブジェクトを作るのは親のコンストラクタだからです。その行より前に `this` に触れると例外が投げられます：
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
したがって、`this` を使う子のコンストラクタでは、`super(...)` を**最初の文**にすべきです。

---

子が親がすでに持っているメソッドを定義すると、子のバージョンが優先されます。これを**オーバーライド**と呼びます：
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// Woof を出力
```
オーバーライドしても親のバージョンが消えるわけではなく、隠れるだけです。子のメソッド内では `super.methodName(...)` で親のバージョンに届くので、親の振る舞いを置き換えるのではなく拡張できます：
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// Woof! を出力
```
違いに注意してください。`super(...)` は親の**コンストラクタ**を呼び、`super.name(...)` は親の**メソッド**を呼びます。

---

これまではプロパティはすべてコンストラクタの中で作成していました。**クラスフィールド**を使うと、クラスの本体に直接宣言でき、初期値も任意で指定できます：
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// 0 を出力
```
フィールドはコンストラクタの本体が実行される前にそれぞれの新しいインスタンスに代入されるので、コンストラクタはそれらをすでに当てにできます。値のないフィールドも宣言はされており、単に `undefined` として始まります：
```javascript
class Task {
    done = false;
    title;
}
```
構文に注意してください。宣言には `let` も `const` も `this` も不要で、行はセミコロンで終わります。

---

クラスが互いを継承するときは順序が重要です。`class` 宣言は `function` のように巻き上げられ**ません**。名前はクラスが書かれた行以降でのみ存在します。そのため、子クラスは継承する親より*後*に現れなければなりません。そうしないと `extends` 節が `ReferenceError` で失敗します。

---

インスタンスではなくクラスそのものに属する振る舞いがあります。例えば、2つの単位の間の変換は、操作対象のオブジェクトを必要としません。メソッドに **`static`** を付けると、そのメソッドはクラス上に置かれます：
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// 8 を出力
```
静的メソッドはインスタンスではなくクラス名に対して呼び出します。`new MathUtils().double(4)` は `TypeError` を投げます。インスタンスは静的メンバーを受け取らないからです。静的メソッドの中では `this` はクラスを指すので、`this.otherStatic(...)` で別の静的メソッドを呼び出せます。

---

`static` はフィールドにも使えます。**静的プロパティ**はインスタンスごとではなくクラスに1つだけ格納されるので、共有カウンターや定数の自然な置き場所になります：
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// 3.14 を出力
```
コピーは1つしかないので、それを更新するインスタンスはすべて同じ値を更新することになります。コンストラクタの中では `this` ではなくクラス名を通して `Circle.PI` にアクセスします。`this.PI` はインスタンス上のプロパティを探し、何も見つからず `undefined` を返してしまいます。

---

静的メソッドの非常に一般的な使い方は**ファクトリー**です。ファクトリーとは、別の形のデータからインスタンスを組み立てて返すメソッドのことです。`new` を1か所にまとめ、何をするのかがわかる名前を構築に与えます：
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// 120 を出力
```
ファクトリーはインスタンスが1つも存在しない前に呼び出せます。通常のメソッドではこれはできません。

---

**ゲッター**はプロパティのように読み取られるメソッドです。名前の前に `get` を書き、呼び出し側では括弧を省きます：
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// 12 を出力
```
`r.area` はメソッドを実行してその結果を返すので、数値です。括弧を付けるとその数値を呼び出そうとして、失敗します。

その逆が**セッター**です。`set` で宣言し、プロパティに代入されると実行されます。パラメーターはちょうど1つ受け取ります：
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

セッターの真の価値は、拒否できることにあります。代入と格納される値の間で、届いた値を確認したり、範囲内に収めたり、拒否したりする機会が得られます：
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// 3を出力、セッターは50を拒否した
```
同じ名前のゲッターとセッターは1つのプロパティを形作るので、同時に通常のフィールドにはなれません。格納される値は別の名前の下に置きます。慣習としては、先頭にアンダースコアを付けた同じ名前です。

---

`_temperature` の先頭のアンダースコアは単なる慣習にすぎません。外の世界が `v._level = 999` と書いてセッターを素通りすることを妨げるものは何もありません。**プライベートフィールド**は言語によって強制されます。名前は `#` で始まり、クラスの本体で宣言しなければならず、そのクラスの内側からのみ読み書きできます：
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// 1234 を出力
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
つまずきやすい詳細が2つあります。`#` は名前の一部なので、常に `this.#code` と書き、決して `this.code` とは書きません。また、プライベートフィールドは `Object.keys` やインスタンスの `console.log` には現れません。

---

メソッドもプライベートにできます。名前の前に `#` を付けると、そのメソッドはクラスの公開部分から消えますが、他のどのメソッドからでも `this.#name(...)` で呼び出せます：
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// $7 を出力
```
これが、ヘルパーの処理を API の外に追いやる方法です。呼び出し側に見えるのは `print` で、その背後にある整形の詳細は見えません。プライベートフィールドとプライベートメソッドを合わせれば、クラスには明確な内側と外側ができます。

---

オブジェクトを出力すると、通常は役に立たないものが表示されます。JavaScript が文字列を必要としてオブジェクトを受け取ると、そのオブジェクトの **`toString`** メソッドを呼び出します。デフォルトの実装は `[object Object]` を返します。自分で定義すればそれを置き換えられます：
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// $7 を出力
```
同じメソッドは文字列の連結や `String(value)` でも使われます。適切な**数値**も欲しい場合は、`[Symbol.toPrimitive](hint)` を定義します。これは `"string"`、`"number"`、`"default"` のいずれかを受け取って返す値を決定し、存在すれば `toString` よりも優先されます。

---

**`instanceof`** 演算子は、オブジェクトがあるクラス、あるいはそれを継承する任意のクラスから作られたかどうかを調べます：
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript には `abstract` キーワードがありませんが、同じ考え方を手で書けます。基底クラスが形を定義し、子が*必ず*提供しなければならないメソッドは単に例外を投げるのです：
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
`area` のオーバーライドを忘れた子は、黙って `undefined` を返す代わりに、最初に使われた時点で大きな音を立てて失敗します。

---

`for...of` やスプレッド演算子 `...` は任意のオブジェクトに対して動作するわけではありません。これらが動くのは**イテラブル**、つまり特殊なキー `Symbol.iterator` の下に格納されたメソッドを提供するオブジェクトです。自分のクラスにそのメソッドを与えれば、仲間入りです：
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// [ 'a', 'b' ] を出力
```
名前の前の `*` はそれを**ジェネレーター**にします。ジェネレーターとは、`yield` で値を1つずつ渡し、その間で一時停止する関数です。これが反復プロトコルを満たす最も短い方法で、格納されているのではなく計算される値に対しても機能します。
