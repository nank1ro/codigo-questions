変数はデータ値を格納するためのコンテナです。
JavaScriptのすべての変数はオブジェクトです。
変数を作成するには、スペースを含まない**名前**を付ける必要があります。
変数は、最初に値を代入した時点で作成されます。
JavaScriptでは、`let`や`const`キーワードで定数を宣言し、`var`キーワードで変数を宣言します。
定数の値は一度設定すると変更できませんが、変数は将来別の値に設定できます。
`x`という名前の変数を作成する例は次のとおりです:
```javascript
var x = 1;
```
このようにして、`x`という名前の変数に値`1`を代入しました。
変数`x`を表示すると、数値`1`が返されます:
```javascript
console.log(x);
// prints 1
```

---

変数は、格納している値が変更できるため、このように呼ばれています。
`=`を使って`x`に新しい値を与えることで更新できます。
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

他の変数の値を変数に代入することもできます。
ここでは、変数`y`に`x`の値を代入できます。
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

変数を更新すると、以前の値は忘れられます。
ここでは、変数`x`を2回表示して、値がどのように更新されるかを確認できます。
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

JavaScriptでは、文字列変数はダブルクォートとシングルクォートの両方を使って宣言できます:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

複数の単語からなる変数名を付けたい場合は、**キャメルケース**を使います。
フレーズの途中にある各単語の先頭を大文字にする書き方です。
