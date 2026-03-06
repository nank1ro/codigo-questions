让我们从**相等** `==` 比较运算符开始。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否相等，例如：
```javascript
console.log(2 == 2);
// prints true
console.log(2 == 3);
// prints false
```

---

让我们继续学习**不等于** `!=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否**不**相等，例如：
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3);
// prints true
```
它与*相等*运算符完全相反

---

让我们继续学习**大于** `>` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于另一个，例如：
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

让我们继续学习**小于** `<` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于另一个，例如：
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

让我们继续学习**大于或等于** `>=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于或等于另一个，例如：
```javascript
console.log(2 >= 2);
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

让我们继续学习**小于或等于** `<=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于或等于另一个，例如：
```javascript
console.log(2 <= 2);
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

现在让我们来看**逻辑**运算符，先从第一个叫做 __AND__（与）`&&` 的开始。
它返回第一个求值为 *false* 的操作数，如果所有操作数都为 *true*，则返回最后一个。
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

让我们继续学习**或** `||` 逻辑运算符。
它返回第一个求值为 *true* 的操作数，如果所有操作数都为 *false*，则返回最后一个。
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

最后让我们学习**非** `!` 逻辑运算符。
它返回一个布尔值，是表达式逻辑状态的反转。
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
