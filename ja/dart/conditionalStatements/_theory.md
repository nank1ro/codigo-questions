**`if` 文**は条件が `true` のときだけコードブロックを実行します。

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

波括弧の中のコードは、条件 `age >= 18` が `true` と評価された場合にのみ実行されます。

---

条件が満たされたときにメッセージを表示するために、`if` ブロック内で `print()` を使用できます。

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

`isRaining` が `false` の場合、何も出力されません。

---

**`if-else` 文**は条件が `true` のとき `if` ブロックを実行し、`false` のとき `else` ブロックを実行します。

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

二つの分岐のうち必ずどちらか一方が実行されます。

---

**`else if`** を使うと複数の条件を順番にテストできます。条件が `true` になる最初の分岐が実行され、残りはスキップされます。

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

**三項演算子** `condition ? expr1 : expr2` は、シンプルな `if-else` 式をコンパクトに書く方法です。

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

条件が `true` なら `expr1` が使われ、そうでなければ `expr2` が使われます。
