配列は、1つの変数名の下に、異なる情報の集まりを順序付きで格納するために使用できるデータ型です。
配列は1つまたは複数の型の値を格納し、**インデックス**を使用してこれらの値を区別します。
次のような式で配列に要素を代入できます:
```javascript
var arrayName = [item1, item2];
```

---

配列の個々の要素にはインデックスを使ってアクセスできます。
インデックスは、配列内の要素の位置を特定するアドレスのようなものです。
インデックスは配列名の直後に、角括弧の中に記述します:
```javascript
arrayName[index];
```
配列のインデックスは`0`から始まります。`1`では**ありません**！配列の最初の要素には次のようにアクセスします: `arrayName[0]`。
配列の2番目の要素はインデックス1にあります: `arrayName[1]`。

---

配列のインデックスは他の変数名と同じように動作します。
値のアクセスだけでなく、値の代入にも使用できます。
配列のインデックスにアクセスする方法は次のとおりです:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
代入は次のように行います:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

文字列と同様に、配列にも**長さ**があります。
配列の長さは、配列に含まれる要素の数です

---

配列は固定長である必要はありません。
いつでも配列の末尾に要素を追加できます！
配列に要素を追加するには`push`関数を使用します:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

配列の一部分だけにアクセスしたい場合があります。
次のコードを見てください:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
まず、`numbers`という配列を作成します。
次に、配列の一部を取り出して`slice`配列に格納します。
これは配列名の後にインデックスを指定することで行います: `numbers.slice(1, 3)`。
右側のインデックスは含まれないことに注意してください

---

JavaScriptでは配列を自由にスライスできます！
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
配列のスライスに最初の要素や最後の要素が含まれる場合、その要素のインデックスを含める必要はありません

---

配列の要素は任意の型にすることができます。
```javascript
var arrayName = ["one", 2, true];
```
実際、上記には順に文字列、整数、ブール値が含まれています。
さらに、配列の中に配列を含めることもできます！

---

配列内の要素を検索する必要がある場合があります。
JavaScriptでは`indexOf()`メソッドを使用できます:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
上記のコードは、文字列`"Zac"`を含む最初のインデックス（この場合は`1`）を出力します。
また、`splice()`メソッドを使用して、特定のインデックスに要素を挿入することもできます:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
上記のコードは`"Ali"`をインデックス`1`に挿入し、このインデックス以降のすべての要素を1つ後ろにずらします。
2番目の値`0`は_deleteCount_（削除数）を意味します。この場合、配列からどの要素も削除しません。しかし`1`を指定した場合、`Zac`が配列から削除されます

---

JavaScriptでは`for..of`キーワードを使用して、配列を非常に簡単にループ処理できます:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
`for`キーワードの後に変数名を指定すると、その変数に配列の各要素の値が順番に代入されます。
