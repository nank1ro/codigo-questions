一个类只能 `extend` 一个超类，但很多时候，彼此毫无关联的类却需要相同的行为。**mixin** 是一段可复用的行为，任意数量的类都可以把它混入进来。

使用 **`mixin`** 关键字声明一个 mixin，类则通过 **`with`** 关键字使用它：

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` 自身没有声明任何成员，但每个 `Fish` 都拥有 `swim`，因为 mixin 的成员会成为类的成员。一个 mixin 可以被任意多个类使用，无论这些类是否相关。

---

mixin 的主体看起来和类的主体一样：方法、getter 和字段，写法完全相同。区别在于你能对声明本身做什么。

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

mixin 的名字也是一个**类型**，因此 `Server() is Timestamped` 为 `true`，变量可以声明为 `Timestamped t = Server();`。两个毫无关联的类就这样共享同一份实现，而无须一方继承另一方。

---

mixin 不局限于方法：它也可以声明**字段**，使用该 mixin 的每个类的每个对象都拥有自己的一份副本。

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

这正是 mixin 胜过接口的地方：它既带来数据，也带来操作这些数据的代码。

---

`mixin` 声明**不是**类。它存在的意义只是被混入其他类，因此它没有自己的构造函数，不能被实例化也不能被继承：

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

它的名字仍然可以作为类型使用，因此 `Team() is Scored` 和 `Scored s = Team();` 都没有问题。mixin 没有构造函数，所以非空字段必须在声明处初始化（或标记为 `late`），就像上面的 `int score = 0;`。

---

mixin 可以声明**没有主体**的成员。这样的成员是抽象的：mixin 使用它，而混入该 mixin 的类必须提供它。

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

mixin 带来行为，类带来数据。类中的一个字段，比如 `final String name;`，就足以满足同名的抽象 getter。

---

把各个部分组合起来，一个使用 mixin 的程序有三部分：`mixin` 声明、一个或多个用 `with` 混入它的类，以及调用共享成员的代码。

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

在 Dart 中，顶层声明可以按任意顺序编写，但当 mixin 出现在使用它的类之前时，从上到下阅读文件会更容易。

---

一个类可以**同时使用多个 mixin**，把它们列在 `with` 之后并用逗号分隔。Dart 按**从左到右**的顺序应用它们，把每个 mixin 依次叠加在前一个之上，因此当两个 mixin 声明了同一个成员时，列表中**最后**一个获胜：

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

这种叠加称为**线性化（linearization）**：`with A, B` 构建出链条 `Object` → `A` → `B` → 类本身。

---

由于最后一个 mixin 获胜，`with` 列表的顺序是类含义的一部分，而不是风格细节。改变顺序会改变对象最终得到的实现：

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

只有一个 mixin 声明的成员永远不存在竞争：无论顺序如何，它们都可用。把 `with X, Y` 读作“从 `X` 开始，然后让 `Y` 覆盖它”。

---

mixin 和 `extends` 可以协同工作。一个类可以既有超类**又有**一列 mixin，而 mixin 总是应用在超类**之上**：

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

这里的链条是 `Object` → `Document` → `Timestamped` → `Report`。成员查找从链条的末端开始，所以 `Report().header()` 会先找到 `Timestamped` 的版本。在超类和 mixin 中声明同一个成员是完全合法的：这正是 mixin 替换或包装继承行为的方式。

---

类主体位于链条的最末端，所以类中声明的成员会**覆盖**来自任何 mixin 的同名成员。在覆盖内部，**`super`** 可以到达 mixin 提供的版本：

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

mixin 本身不受影响：`Guest` 仍然得到原始的 `greet`。`super.greet()` 让 `Host` 在共享行为之上构建，而不是复制它。

---

有些行为只有在某个特定类之上才有意义，并且需要那个类的成员才能完成工作。**`on`** 子句声明了这一要求：

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` 做两件事：它让 mixin 可以使用 `Animal` 的成员，比如上面的 `name`；同时它限制了谁可以使用这个 mixin。`class Rock with Noisy {}` 是编译错误，因为 `Rock` 不是 `Animal`。

---

带 `on` 子句的 mixin 可以把超类的成员当作自己的成员来使用，这正是它适合承载装饰现有类型之行为的原因：

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` 覆盖了 `kind`，而 `show` 会自动采用覆盖后的版本：mixin 总是在真实对象上调用成员。

---

一旦 mixin 有了 `on` 子句，它就可以**覆盖**该类型的成员，并调用 **`super`** 到达链条中位于它下方的版本：

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` 不是 mixin 自己的 `log`，而是它下方的那一个，因此不会无限递归。用 `with A, B` 叠放多个这样的 mixin 时，每一个都包装前一个：调用先进入**最后**一个 mixin，再向下传递到超类。

---

`mixin` 声明不能被实例化或继承，而普通 `class` 不能用在 `with` 之后。当你需要一份**两种**方式都可行的声明时，写 **`mixin class`**：

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

`mixin class` 为这种灵活性付出两个限制的代价：它必须继承自 `Object`，因此不能有自己的 `extends` 子句；它不能声明构造函数，因为 mixin 永远不会运行构造函数。

---

mixin、继承和接口解决三个不同的问题：

- **`extends`** 给一个类一个超类，用于“是一种”的关系。这个位置只有一个，所以应该留给最强的关系。
- **`with`** 添加许多互不相关的类都需要的行为。数量没有限制，而且实现是共享的，不是复制的。
- **`implements`** 承诺一组成员，但**不带**任何实现：每个类都必须自己编写方法体。

当你想把某个方法复制到没有天然共同父类的多个类中时，比如 `Duck`、`Plane` 和 `Kite` 都需要同样的 `fly`，这就是你需要 mixin 的明显信号。

---

叠放的 mixin 是把小的、独立的规则组合进一个类的方式。每个 mixin 覆盖同一个成员，完成自己那一部分，然后调用 `super` 把工作继续传递下去。由于调用先进入**最后**一个 mixin，`with` 列表的顺序决定了哪条规则先于哪条运行：

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` 会把每一笔存款翻倍。在 `Doubled` 之后再加一个 mixin，那个 mixin 会先拿到这笔存款，`Doubled` 之后才看到它。
