让我们从**相等** `==` 比较运算符开始。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否相等，例如：
```javascript
console.log(2 == 2);
// 打印 true
console.log(2 == 3);
// 打印 false
```

---

让我们继续学习**不等于** `!=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否**不**相等，例如：
```javascript
console.log(2 != 2);
// 打印 false
console.log(2 != 3);
// 打印 true
```
它与*相等*运算符完全相反

---

让我们继续学习**大于** `>` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于另一个，例如：
```javascript
console.log(2 > 2);
// 打印 false
console.log(3 > 2);
// 打印 true
```

---

让我们继续学习**小于** `<` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于另一个，例如：
```javascript
console.log(2 < 2);
// 打印 false
console.log(2 < 3);
// 打印 true
```

---

让我们继续学习**大于或等于** `>=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于或等于另一个，例如：
```javascript
console.log(2 >= 2);
// 打印 true
console.log(3 >= 2);
// 打印 true
console.log(3 >= 4);
// 打印 false
```

---

让我们继续学习**小于或等于** `<=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于或等于另一个，例如：
```javascript
console.log(2 <= 2);
// 打印 true
console.log(3 <= 2);
// 打印 false
console.log(3 <= 4);
// 打印 true
```

---

现在让我们来看**逻辑**运算符，先从第一个叫做 __AND__（与）`&&` 的开始。
它返回第一个求值为 *false* 的操作数，如果所有操作数都为 *true*，则返回最后一个。
```javascript
console.log(2 == 2 && 2 == 3);
// 打印 false
console.log(1 == 1 && 1 == 1.0);
// 打印 true
```

---

让我们继续学习**或** `||` 逻辑运算符。
它返回第一个求值为 *true* 的操作数，如果所有操作数都为 *false*，则返回最后一个。
```javascript
console.log(2 == 2 || 2 == 3);
// 打印 true
console.log(1 == 2 || 1 == 3);
// 打印 false
```

---

最后让我们学习**非** `!` 逻辑运算符。
它返回一个布尔值，是表达式逻辑状态的反转。
```javascript
console.log(!true);
// 打印 false
console.log(!false);
// 打印 true
console.log(!(2 == 2));
// 打印 false
```

---

`==` 会先把两边的值转换为同一类型，再进行比较，所以 `"5" == 5` 的结果是 `true`。严格运算符 `===` 会跳过这一转换，还要求两边的类型也必须一致。
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

`!=` 和 `==` 一样，会先转换再比较，所以 `"5" != 5` 的结果是 `false`。它的严格版本 `!==` 无论内容是什么，都会把字符串和数字视为不同的值。
```javascript
console.log("5" !== 5); // true
```

---

当两边都是字符串时，`>` 会按字符编码顺序逐字符比较，而不是比较长度，所以 `"b" > "a"` 为 `true`，`"apple" > "ant"` 也同样为 `true`。

---

`>=` 只要满足名字中的任意一半条件即可：`8 >= 8` 为 `true`，因为两个值相等，而更严格的 `8 > 8` 则为 `false`。

---

任何涉及 `NaN` 的比较都会返回 `false`，即使是相反的比较也是如此：`NaN < 3` 和 `NaN >= 3` 都为 `false`，所以 `<` 不成立并不总是意味着左边更大。

---

当一边是字符串、另一边是数字时，`<=` 会先把字符串转换成数字，所以 `"7" <= 8` 的结果是 `true`。
