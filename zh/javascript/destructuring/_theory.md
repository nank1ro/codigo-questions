一次一个索引地从数组中读取值非常繁琐：
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**解构**用一行代码完成同样的工作。在 `=` 的左边，你写出一个看起来就像数组本身的模式，其中的每个名字都会接收到相同位置上的元素：
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// 打印 3 7
```
模式不必覆盖整个数组：多余的元素会被直接忽略，而没有匹配元素的名字则会变成 `undefined`。

---

解构最有用的时候正是数组到达的地方：一个函数参数，或者一次调用的结果。与其把数组保存起来然后在各处用索引访问，不如一次性把它解开，并给各个部分起上真正的名字：
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// 打印 5
```
原始数组中不会有任何东西被复制或修改，模式只是从它那里读取。

---

有时只有数组深处的一个元素是重要的。你可以在模式中把一个位置留空，只保留分隔它的逗号：这样的空位置称为**空位**，它会跳过对应的元素而不给它命名：
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// 打印 64
```
数逗号，而不是数名字：每个逗号都会让模式向前移动一个位置，无论它前面有没有名字。

---

数组并不总是和模式期望的一样长。在名字后面写上 `= value` 会给它一个**默认值**，每当数组在对应位置上没有东西时就使用它：
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// 打印 1920 1080
```
默认值只在需要时才会被求值，因此它甚至可以是一次函数调用，而且任何位置都可以有默认值，不只是最后一个。

---

模式也可以出现在普通赋值的左边，前面不加 `const` 或 `let`，这时它会写入已经存在的变量。这样一来，交换两个值就变成了一行代码，而且不需要临时变量：
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// 打印 2 1
```
右边会先被构建，所以当赋值发生时，两个旧值已经安全地待在临时数组里了。注意上一行的分号：否则，以 `[` 开头的一行会被当成对前面内容的索引。

---

对象也可以被解构，只是使用花括号而不是方括号。在这里位置毫无意义：每个名字都会与拼写相同的**键**进行匹配：
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// 打印 Ada 36
```
在模式中调换 `age` 和 `name` 的顺序不会有任何影响，而模式没有提到的键则会被直接留下。没有匹配键的名字会变成 `undefined`。

---

对象模式与默认值的组合方式和数组模式完全一样，这让它成为一种读取键可能存在也可能不存在的配置对象的整洁方式：
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// 打印 dark en
```
由于整个模式就是一条语句，函数可以在它的第一行就从参数中解出它需要的一切。

---

对象模式用键来为变量命名，当键含义模糊或者已经被占用时就会很别扭。写上 `key: newName` 可以**重命名**变量：
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// 打印 Ada 1815
```
把它读作“取出 `n`，叫它 `name`”。冒号并不声明类型，而且 `n` 本身永远不会被创建为变量，只有 `name` 会。被重命名的名字仍然可以有默认值，写在它的后面：`{ n: name = "unknown" }`。

---

默认值有一条让所有人都惊讶的规则：它们**只**对 `undefined` 生效。一个存在并保存着 `null`、`0`、`""` 或 `false` 的键是真实的值，所以模式会取用它，默认值永远不会被使用：
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// 打印 0
```
`null` 在这里的行为和 `0` 一样，尽管在 API 响应中它通常表示“没有值”。当 `null` 也必须被替换时，先解构，之后再用 `??` 回退。

---

当某个键保存的是另一个对象或数组时，模式可以直接继续下去，把那个形状也描述出来：
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// 打印 London
```
注意这一行创建的是什么：`address: { city }` 的意思是“进入 `address`”，而不是“把 `address` 给我”，所以只有 `city` 会成为变量。要两者都拿到，把这个键提到两次即可：`const { address, address: { city } } = user;`。数组模式和对象模式可以自由地互相嵌套，比如 `{ tags: [first] }`。

---

取出数组的头部并保留尾部是一种非常常见的需求，以至于模式为它准备了专门的语法。在最后一个名字前面写上三个点，它就成为一个**剩余元素**，会把剩下的每个元素都收集到一个全新的数组中：
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// 打印 a [ 'b', 'c' ]
```
剩余元素必须放在模式的最后，并且不能有默认值：当没有剩余的东西时，它就是一个空数组。

---

对象模式也有剩余语法，它会把模式没有提到的每个键都收集到一个新对象中：
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// 打印 { name: 'Ada', city: 'London' }
```
这是构建一个去掉某个键的对象副本的最短方式：原始对象永远不会被改动，剩余对象是一个保存着其余值的新对象。

---

在函数声明中，模式可以取代参数名，这样解包就会在调用发生时进行：
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// 打印 12
```
在函数体内部完全没有对象变量，只有 `width` 和 `height`。调用者传入一个对象，但签名清楚地记录了函数读取的是哪些键，而且这些键可以以任意顺序到达。

---

带默认值的解构参数构成了一个整洁的选项对象，但当调用者什么都不传时它仍然会出错：从 `undefined` 中读取键会抛出 `TypeError`。给整个模式一个 `{}` 默认值即可修复：
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// 打印 guest/false
```
由外向内读这一行：`= {}` 在参数缺失时提供一个空对象，然后每个内部默认值再填上各自的键。

---

`Object.entries(obj)` 把一个对象转换为由 `[key, value]` 对组成的数组。把一个数组模式放进 `for...of` 循环的头部，循环运行时每一对都会被解包：
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// 打印 ada is 36
// 打印 bob is 41
```
这是遍历对象最可读的方式：没有索引，没有查找，只有你在乎的那两个名字。`Object.keys` 和 `Object.values` 各自只给出其中一面，`Object.entries` 则两者都给。

---

到目前为止看到的一切都属于同一套语法，所以各个部分可以自由组合：一个对象模式可以嵌套另一个对象模式，后者可以包含一个带默认值的重命名键，旁边还可以放一个以剩余元素结尾的数组模式。于是一行代码就能描述函数期望的整个形状：
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// 打印 Post [js] +2
```
保持可读性：一个不再能放在几行之内的模式，通常说明这个函数想要的东西太多了。
