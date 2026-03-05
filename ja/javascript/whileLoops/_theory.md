プログラミングでは、コードブロックを繰り返す必要がよくあります。例えば:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
これは次の出力を生成します:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
当然ながら、長い文の場合、コードを書くのに多くの時間がかかりますが、幸いにもループを使うことができます。
上記と同じ出力を得る`while`ループを学びましょう。
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
まず、初期値として`2`を代入した変数`count`を作成しました。
次に、条件`count <= 5`が`true`である間、コードブロックを実行する`while`文を使いました。
コードブロックの中で、`count += 1`の行を追加することを忘れては**いけません**。
これは`count`の値を増加させます。そうしないと、ループは無限になります

---

`while`ループの繰り返し回数を制御するには、数値に設定された変数から始めます。
この変数をカウンター変数と呼びます

---

次に、条件の中で比較を使い、`counter`変数を数値と比較します。

---

`while`ループを停止するために、コードブロックの中で`counter`変数をインクリメントします。

---

コードを書く順序が出力に影響します。

---

JavaScriptには`while`ループの**do-while**バリエーションもあります。
ループの条件を確認する_前に_、最初にループブロックを1回実行します。
その後、条件が`false`になるまでループを繰り返し続けます。
