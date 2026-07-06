**函数**是一个可重复使用的代码块，用于执行特定任务。在 Dart 中，定义函数时需要指定返回类型、名称和一对括号 `()`。

当函数不返回任何值时，其返回类型为 `void`：

```dart
void sayHello() {
  print("Hello!");
}
```

通过写出函数名称加 `()` 来调用函数：

```dart
sayHello(); // prints Hello!
```

---

函数可以**返回一个值**给调用方。在函数名前声明返回类型，并使用 `return` 关键字将值传回：

```dart
int getAge() {
  return 25;
}
```

函数名前的类型（`int`）告诉 Dart 该函数将返回什么类型的值。可以使用 `String`、`int`、`double`、`bool` 等。

---

函数可以接受**参数**——在调用函数时传入的值。参数在括号内声明，包含其类型和名称：

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

每个参数都有类型（`int`）和名称（`n`）。多个参数之间用逗号分隔。

---

Dart 支持使用 `=>` 语法的**箭头函数**。当函数体是单个表达式时，可以用 `=>` 代替 `{ return ...; }` 来简化：

```dart
// 普通函数
int double(int n) {
  return n * 2;
}

// 箭头函数——结果相同
int double(int n) => n * 2;
```

箭头函数使代码更简洁。`=>` 同时替代了花括号和 `return` 关键字。

---

Dart 支持**命名参数**——用花括号 `{}` 包裹的参数。命名参数必须通过名称调用，可以有默认值或标记为 `required`：

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

命名参数提高了代码的可读性，尤其是当函数有多个参数时。
