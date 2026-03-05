**等価** `==` 比較演算子から始めましょう。
この演算子は、2つの式が等しいかどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 == 2);
// true を出力
console.log(2 == 3);
// false を出力
```

---

**不等価** `!=` 比較演算子に進みましょう。
この演算子は、2つの式が等しく**ない**かどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 != 2);
// false を出力
console.log(2 != 3);
// true を出力
```
これは*等価*演算子の正反対です

---

**より大きい** `>` 比較演算子に進みましょう。
この演算子は、一方の式がもう一方より大きいかどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 > 2);
// false を出力
console.log(3 > 2);
// true を出力
```

---

**より小さい** `<` 比較演算子に進みましょう。
この演算子は、一方の式がもう一方より小さいかどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 < 2);
// false を出力
console.log(2 < 3);
// true を出力
```

---

**以上** `>=` 比較演算子に進みましょう。
この演算子は、一方の式がもう一方以上かどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 >= 2);
// true を出力
console.log(3 >= 2);
// true を出力
console.log(3 >= 4);
// false を出力
```

---

**以下** `<=` 比較演算子に進みましょう。
この演算子は、一方の式がもう一方以下かどうかを示す**ブール値**（`true` または `false`）を返します。例えば：
```javascript
console.log(2 <= 2);
// true を出力
console.log(3 <= 2);
// false を出力
console.log(3 <= 4);
// true を出力
```

---

次に**論理**演算子を見てみましょう。まず__AND__ `&&`から始めます。
この演算子は、*false*と評価される最初のオペランドを返し、すべてが*true*の場合は最後のオペランドを返します。
```javascript
console.log(2 == 2 && 2 == 3);
// false を出力
console.log(1 == 1 && 1 == 1.0);
// true を出力
```

---

**or** `||` 論理演算子に進みましょう。
この演算子は、*true*と評価される最初のオペランドを返し、すべてが*false*の場合は最後のオペランドを返します。
```javascript
console.log(2 == 2 || 2 == 3);
// true を出力
console.log(1 == 2 || 1 == 3);
// false を出力
```

---

最後に**not** `!` 論理演算子を見てみましょう。
この演算子は、式の論理状態を反転したブール値を返します。
```javascript
console.log(!true);
// false を出力
console.log(!false);
// true を出力
console.log(!(2 == 2));
// false を出力
```
