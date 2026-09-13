你已经知道 `extends` 会让一个类成为另一个类的子类。这个关键字真正带给你的是**继承**：子类免费获得父类的每一个属性和方法，并且还可以在此基础上添加自己的内容。

让继承真正有用的是 **`super`**。在子类的构造函数中，`super(...)` 会调用父类的构造函数，这样父类就能设置它所拥有的那部分对象：
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
这里 `super(name)` 把 `name` 交给 `Animal`，由它来存储，而 `Dog` 只需要关心 `breed`。

---

子类不必重新定义父类已经提供的任何内容。方法也会被继承，所以子类的实例可以像调用自己的方法一样调用它们：
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
当子类声明了自己的构造函数时，在其中调用 `super(...)` 是**强制性的**：没有它，对象就永远不会被初始化，JavaScript 会抛出 `ReferenceError`。完全没有构造函数的子类也没有问题，因为 JavaScript 会自动写一个把所有参数转发给父类的构造函数。

---

关于 `super()` 的规则比"在某处调用它"要严格得多。在子类的构造函数中，在 `super()` 运行之前 `this` 这个词并不存在，因为创建对象的是父类构造函数。在这一行之前触碰 `this` 会抛出错误：
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
所以 `super(...)` 应该是任何使用 `this` 的子类构造函数的**第一条语句**。

---

当子类定义了父类已经拥有的方法时，子类的版本会获胜。这被称为**重写（overriding）**：
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
重写并不会删除父类的版本，只是把它隐藏起来。在子类方法内部，`super.methodName(...)` 仍然可以访问到它，这让你可以扩展父类的行为而不是完全替换它：
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
注意区别：`super(...)` 调用的是父类的**构造函数**，`super.name(...)` 调用的是父类的**方法**。

---

到目前为止，每个属性都是在构造函数内部创建的。**类字段（class field）**让你可以直接在类体中声明它，并可以带一个可选的初始值：
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
字段会在构造函数体运行之前赋给每个新实例，所以构造函数已经可以依赖它们。没有值的字段也依然是已声明的，只是以 `undefined` 作为起始值：
```javascript
class Task {
    done = false;
    title;
}
```
注意语法：声明中没有 `let`，没有 `const`，没有 `this`，并且这一行以分号结尾。

---

当类相互继承时，顺序很重要。`class` 声明**不会**像 `function` 那样被提升：这个名字只从类被书写的那一行开始才存在。所以子类必须出现在它所继承的父类*之后*，否则 `extends` 子句会因 `ReferenceError` 而失败。

---

有些行为属于类本身，而不是属于任何单个实例。例如，两个单位之间的转换就不需要一个对象来操作。给方法标记 **`static`** 会把它放到类上：
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
静态方法通过类名调用，绝不能通过实例调用：`new MathUtils().double(4)` 会抛出 `TypeError`，因为实例不会获得静态成员。在静态方法内部，`this` 指向类本身，所以一个静态方法可以用 `this.otherStatic(...)` 调用另一个静态方法。

---

`static` 对字段也有效。**静态属性**只在类上存储一次，而不是每个实例各存一份，这使它成为共享计数器或常量的自然归宿：
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
因为只有一份副本，更新它的每个实例更新的都是同一个值。在构造函数内部，你要通过类名 `Circle.PI` 来访问它，而不是通过 `this`：`this.PI` 会在实例上查找属性，什么也找不到，然后给你 `undefined`。

---

静态方法一个非常常见的用途是**工厂（factory）**：一种从其他形状的数据构建实例并返回它的方法。它把 `new` 集中在一个地方，并给这个构建过程起了一个能说明其用途的名字：
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
工厂可以在任何实例存在之前被调用，这是普通方法做不到的。

---

**getter** 是一种像属性一样被读取的方法。在它前面写上 `get`，并在调用处去掉括号：
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area` 会运行该方法并返回它的结果，所以它是一个数字。再加上括号就会试图调用这个数字，而这会失败。

与之对应的是 **setter**，用 `set` 声明，在对属性赋值时运行。它只接收一个参数：
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

setter 的真正价值在于它可以拒绝。在赋值和存储的值之间，你有机会检查、限制或拒绝传进来的内容：
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
同名的 getter 和 setter 共同构成一个属性，所以它们不能同时也是一个普通字段：存储的值存放在另一个名字下，按照惯例就是同名但前面加一个下划线。

---

`_temperature` 的前导下划线只是一种惯例：没有什么能阻止外部世界写下 `v._level = 999` 并直接绕过你的 setter。**私有字段（private field）**则是由语言强制执行的。它的名字以 `#` 开头，必须在类体中声明，并且只能在该类的内部读取或写入：
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
有两个细节容易踩坑。`#` 是名字的一部分，所以你总是写 `this.#code`，永远不要写 `this.code`。而且私有字段不会出现在 `Object.keys` 中，也不会出现在实例的 `console.log` 输出里。

---

方法也可以是私有的。在名字前加上 `#`，这个方法就会从类的公开表面消失，同时仍然可以被任何其他方法通过 `this.#name(...)` 调用：
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
这就是你把辅助步骤挡在 API 之外的方式：调用者看到的是 `print`，而不是它背后的格式化细节。私有字段和私有方法一起让类有了清晰的内部与外部之分。

---

打印一个对象通常会得到没什么用的东西。每当 JavaScript 需要一个字符串却得到一个对象时，它会调用该对象的 **`toString`** 方法，而默认实现返回 `[object Object]`。定义你自己的版本即可替换它：
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
字符串拼接和 `String(value)` 使用的也是同一个方法。如果你还想得到一个有意义的**数字**，可以定义 `[Symbol.toPrimitive](hint)`，它会接收 `"string"`、`"number"` 或 `"default"` 并决定返回什么；当它存在时，它的优先级高于 `toString`。

---

**`instanceof`** 运算符询问一个对象是否由某个类构建，或者由继承自它的任何类构建：
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript 没有 `abstract` 关键字，但同样的思想可以手写出来：基类定义形状，而子类*必须*提供的每个方法直接抛出错误：
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
忘记重写 `area` 的子类会在第一次被使用时就大声地失败，而不是悄悄地返回 `undefined`。

---

`for...of` 和展开运算符 `...` 并不是对任何对象都有效：它们作用于**可迭代对象（iterable）**，即提供了存储在特殊键 `Symbol.iterator` 下的方法的对象。给你的类加上这个方法，它就加入了这个俱乐部：
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
名字前面的 `*` 使它成为一个**生成器（generator）**：一种用 `yield` 逐个交出值并在其间暂停的函数。这是满足迭代协议的最简短方式，而且它也适用于那些被计算出来而非存储起来的值。
