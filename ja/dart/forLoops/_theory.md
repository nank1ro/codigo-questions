`for` ループはコードブロックを決まった回数繰り返します。基本的な構文は次の通りです：

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: ループが始まる前に一度実行されます（例：`int i = 0`）

**condition**: 各反復の前にチェックされます。偽になるとループが停止します

**update**: 各反復の後に実行されます（例：`i++`）

---

現在のカウントを追跡するために、ループ変数をボディの中で使うことができます。例えば、合計を累積する場合：

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

ループの後、`total` は 15 になります。

---

`for` ループはデクリメント（`i--`）と `>=` 条件を使って**下向きに**カウントできます：

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

これはカウントダウンや逆順の反復に役立ちます。

---

`for-in` ループはインデックスを使わずにコレクションのすべての要素を反復処理します：

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

各反復で次の要素がループ変数（ここでは `fruit`）に代入されます。

---

`break` 文は条件が満たされたときにループをすぐに終了します：

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

これは値を検索していて、見つかったらすぐに停止したい場合に役立ちます。
