Kotlinには`Boolean`と呼ばれる基本的なブール型があります。
ブール値は論理値とも呼ばれ、trueまたはfalseのいずれかしか取れません。
Kotlinでは任意の式を評価し、`true`または`false`の2つの答えのいずれかを得ることができます。

---

数値や文字列と同じように、ブール値`true`を変数に格納することができます。

---

`true`の反対の値は`false`です

---

ブール値は、その前に`!`を付けることで否定することもできます。例:
```kotlin
println(!true) // false を出力
println(!false) // true を出力
```

---

`&&`（_and_）と`||`（_or_）を使ってブール式を作ることもできます:

- `&&`（_and_）: 演算子の左右のブール式がどちらもtrueの場合にのみtrueを返します。
- `||`（_or_）: 演算子の左右のいずれか、または両方の式がtrueの場合にtrueを返します。

```kotlin
println(true && true) // true を出力
println(true && false) // false を出力
println(false && false) // false を出力
println(true || true) // true を出力
println(true || false) // true を出力
println(false || false) // false を出力
```
