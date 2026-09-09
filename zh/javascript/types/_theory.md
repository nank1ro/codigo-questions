JavaScript 中的每个值都有一个**类型**。共有七种**原始**类型：
- `number` 表示任何数字，比如 `42` 或 `3.14`
- `string` 表示文本，比如 `"Ana"`
- `boolean` 表示 `true` 和 `false`
- `undefined` 表示从未提供的值
- `null` 表示有意为空的值
- `bigint` 表示任意大小的整数，比如 `9007199254740993n`
- `symbol` 表示用 `Symbol()` 创建的唯一标识符

其他所有东西（数组、函数、用 `{}` 创建的对象、日期……）都是 `object`。
`typeof` 运算符以字符串的形式告诉你一个值的类型：
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript 是**动态类型**的：变量本身没有类型，只有它当前存放的值才有类型。同一个变量可以先存放数字，之后再存放字符串，`typeof` 会跟随值：
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
这很方便，但也意味着函数可能收到意外类型的值，因此用 `typeof` 做检查是常见的第一步。由于 `typeof` 返回字符串，你需要把它的结果与字符串比较：
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` 有几个让人意外的答案。
函数有自己专属的答案 `"function"`，尽管它们是对象：
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
数组**没有**自己专属的答案：它们就是普通的 `"object"`，和 `{}` 一样：
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
而 `typeof null` 是 `"object"`，这是一个从未修复的历史遗留问题。所以 `typeof` 能很好地区分原始值和函数，但它无法区分数组、对象和 `null`。

---

你可以通过把类型当作函数来调用，从而**显式**地把一个值转换为另一种类型：
- `Number(value)` 转换为数字：`Number("42")` 是 `42`
- `String(value)` 转换为字符串：`String(42)` 是 `"42"`
- `Boolean(value)` 转换为布尔值：`Boolean("")` 是 `false`

结果是一个全新的值；原值不会被改变：
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
显式转换能让你的意图一目了然：任何读到 `Number(input)` 的人都知道 `input` 原本是文本。

---

`Number()` 是严格的：整个字符串必须是一个数字，否则结果是 `NaN`（"Not a Number"）：
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` 和 `parseFloat()` 更宽容：它们从字符串开头读取数字，跳过开头的空格，并在第一个不属于数字的字符处停止。`parseInt` 只保留整数部分：
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
当字符串不是以能构成数字开头的内容（可选的正负号，然后是一位数字）开始时，它们同样返回 `NaN`：
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` 是唯一不等于自身的值，所以 `x === NaN` 总是 `false`；要检测它，请使用 `Number.isNaN(x)`。

---

有两种方式可以询问"这是 `NaN` 吗？"，而它们回答的是不同的问题。
旧的全局函数 `isNaN(value)` 会先把 `value` **转换**为数字，然后再检查。因此对任何无法变成数字的值它都返回 `true`，即使它根本不是 `NaN`：
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` **不会**转换：只有当 `value` 确实是数字 `NaN` 时它才返回 `true`：
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
优先使用 `Number.isNaN`；如果你想知道一次转换是否失败，请先做转换。

---

JavaScript 也会进行**隐式**转换，而 `+` 运算符是最常出问题的地方。只要任意一侧是字符串，`+` 就会进行**拼接**，并把另一侧转换为字符串：
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
其他所有算术运算符都会把两侧转换为**数字**：
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
因此，把来自文本的值（用户输入、文件、URL）相加可能会在不知不觉中拼出字符串而不是求出和。为了安全起见，请在相加前用 `Number()` 进行转换。

---

把字符串转换为数字的一种简写方式是**一元加号**：放在单个值前面的 `+` 会完全按照 `Number()` 的方式转换它：
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
它很简洁，但容易与加法混淆，所以很多团队更喜欢显式的 `Number("5")`。

---

**宽松**相等 `==` 在比较前会把两侧转换为同一种类型，其规则很难记住：
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
**严格**相等 `===` 从不转换：不同类型的值就是不相等：
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
默认使用 `===`（以及 `!==`）。唯一常见的例外是 `value == null`，它把 `null` 和 `undefined` 一起检查。

---

当 JavaScript 需要一个布尔值时，比如在 `if` 条件中或 `Boolean(value)` 中，它会对值进行转换。只有八个值会变成 `false`，它们被称为**假值**（falsy）：
`false`、`0`、`-0`、`0n`、`""`、`null`、`undefined` 和 `NaN`。
**其他所有值都是真值（truthy）**，包括一些看起来为空的值：
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` 是非空字符串，所以它是真值；空数组是对象，所以它也是真值。

---

把任意值转换为布尔值的一个常见捷径是**双重取反** `!!`：第一个 `!` 把值转换为布尔值并取反，第二个再把它取反回来：
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` 和 `Boolean(value)` 给出的结果完全相同；显式的写法更易读。

---

JavaScript 只有一个 `number` 类型，同时用于整数和小数：每个数字都是 64 位浮点值（*双精度*）。所以 `5` 和 `5.0` 是同一个值，也不存在单独的整数类型：
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
要判断一个数字没有小数部分，请使用 `Number.isInteger`：
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
模板字面量会按照与 `String()` 相同的规则把插值转换为字符串，所以 `${5.0}` 会变成 `"5"`，而不是 `"5.0"`。

---

因为数字是双精度数，有些小数无法被精确存储，于是会出现微小的误差：
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
`toFixed(digits)` 方法把一个数字四舍五入到 `digits` 位小数，但它返回的是**字符串**，用于显示没问题，用于继续计算就错了：
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
要得到四舍五入后的**数字**，请用 `Number()` 把结果转换回来：
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

`number` 只能精确表示不超过 `Number.MAX_SAFE_INTEGER`（即 `9007199254740991`）的整数。超过这个范围，数字位就会丢失：
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
更大的整数请使用 `bigint`：书写字面量时加上 `n` 后缀，或者用 `BigInt()` 进行转换：
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` 会显示 `n` 后缀；`String(big)` 给出纯数字。
`bigint` 和 `number` 不能在算术运算中混用：`big + 1` 会抛出 `TypeError`。请显式转换其中一侧，使用 `BigInt(count)` 或 `Number(big)`。

---

由于 `typeof` 对数组、对象和 `null` 都返回 `"object"`，要区分它们就需要两个额外的检查。
`Array.isArray(value)` 只对数组返回 `true`：
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
对于 `null` 则直接比较，`value === null`。把它们结合起来就能完整判断任何值：
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
先检查 `null` 和数组，因为普通的 `typeof` 无法区分它们。

---

来自表单、文件或 URL 的文本总是字符串，即使它表示的是数字或布尔值。把它转换回正确的类型需要综合运用你已见过的内容：对布尔值与 `"true"` 和 `"false"` 比较，对数字尝试 `Number()`，并记住 `Number("")` 是 `0`，而 `Number.isNaN` 会告诉你转换何时失败：
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
当什么都不匹配时，就让字符串保持原样。
