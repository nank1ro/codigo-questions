__ブーリアン__は、`true`または`false`のいずれか2つの値のみを保持できるデータ型です。
Dartでは、ブーリアン型は`bool`キーワードで宣言します。

```dart
bool isRaining = true;
```

変数`isRaining`は値`true`を格納します。これは現在雨が降っていることを意味します。
ブーリアン値は常に小文字で書きます：`true`と`false`。

---

他の変数と同じように、`print()`を使用してブーリアン値を出力できます。
ブーリアンを出力すると、Dartは`true`または`false`というテキストを出力します。

```dart
bool isSunny = true;
print(isSunny); // true
```

---

ブーリアン変数は値`false`も保持できます。
何かが成立しない場合は`false`を使用します。

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

`true`と同じように、`false`は小文字で書かなければなりません。

---

__否定演算子__`!`（「not」とも呼ばれる）はブーリアン値を反転します。
`!`を`true`に適用すると`false`になり、`!`を`false`に適用すると`true`になります。

```dart
bool isActive = true;
print(!isActive); // false
```

これは条件の反対をチェックしたい場合に便利です。

---

ブーリアンはプログラミング全体で条件を表し、決定を駆動するために使用されます。
プログラムが2つの可能性の間で決定する必要があるときはいつでも、ブーリアンが関与しています。

例：
- ユーザーはログインしていますか？（`isLoggedIn`）
- ドアは開いていますか？（`isDoorOpen`）
- 注文は発送されましたか？（`isShipped`）
