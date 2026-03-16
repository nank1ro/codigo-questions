A **function** is a reusable block of code that performs a specific task. In Dart, you define a function with a return type, a name, and a pair of parentheses `()`.

When a function does not return any value, its return type is `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

You call the function by writing its name followed by `()`:

```dart
sayHello(); // prints Hello!
```

---

Functions can **return a value** back to the caller. You declare the return type before the function name, and use the `return` keyword to send the value back:

```dart
int getAge() {
  return 25;
}
```

The type before the function name (`int`) tells Dart what kind of value the function will return. You can use `String`, `int`, `double`, `bool`, and more.

---

Functions can accept **parameters** — values passed in when calling the function. Parameters are declared inside the parentheses with their type and name:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Each parameter has a type (`int`) and a name (`n`). Multiple parameters are separated by commas.

---

Dart supports **arrow functions** using the `=>` syntax. When a function body is a single expression, you can shorten it with `=>` instead of `{ return ...; }`:

```dart
// Regular function
int double(int n) {
  return n * 2;
}

// Arrow function — same result
int double(int n) => n * 2;
```

Arrow functions make code more concise. The `=>` replaces both the curly braces and the `return` keyword.

---

Dart supports **named parameters** — parameters wrapped in curly braces `{}`. Named parameters must be called by name and can have default values or be marked `required`:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Named parameters improve readability, especially when a function has many parameters.
