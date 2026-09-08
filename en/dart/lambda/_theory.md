You already know how to declare a function with a name, such as `void sayHello() { ... }`. Dart also lets you write a function **without a name**: an **anonymous function**. It has the same parts as a named function (parameters in parentheses and a body in curly braces) but no return type and no name:

```dart
(String name) {
  print('Hello, $name!');
}
```

Since it has no name, the usual way to use it is to store it in a variable and then call the variable like a function:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Note the `;` after the closing brace: the assignment is a normal statement.

---

An anonymous function can take parameters and `return` a value, exactly like a named one. The return type is not written: Dart **infers** it from the `return` statements in the body.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

When the body is a single expression, an anonymous function can use the **arrow syntax** `=>`, just like a named function. The arrow replaces the curly braces and the `return` keyword:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

This short form is by far the most common way to write anonymous functions in Dart.

---

Functions are values, so they have a type. The type of a function is written as the **return type**, then the keyword `Function`, then the **parameter types** in parentheses:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

When the variable is typed this way, the parameter types can be omitted from the anonymous function, because Dart infers them from the declared type:

```dart
int Function(int, int) add = (a, b) => a + b;
```

The bare type `Function` accepts any function, whatever its parameters and return type, but it tells Dart nothing about how to call it.

---

Because a function type is a normal type, a function can take **another function as a parameter**. Inside the body, the parameter is called like any function:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Here the caller decides what `apply` does by passing an anonymous function as the second argument.

---

Many methods of Dart collections take a function as an argument, and anonymous functions are the natural way to pass one. The simplest is `forEach`, which calls the given function once for every element of a list:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

The parameter type is inferred from the list, so `fruit` is a `String` without writing it.

---

Two other very common methods that take an anonymous function are `map` and `where`:

- `map` transforms every element with the function and returns the new values
- `where` keeps only the elements for which the function returns `true`

Both return a lazy `Iterable`; call `toList()` to turn the result into a `List`:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Since `map` and `where` both return an `Iterable`, their calls can be **chained** one after the other. Each step receives the result of the previous one, and `toList()` is called once at the end:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` reorders a list in place. By default it uses the natural order of the elements, but you can pass an anonymous function that **compares two elements** and returns a negative number, zero or a positive number. `compareTo` gives exactly such a number, so it is the usual building block:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Swapping `a` and `b` in the comparison reverses the order.

---

`reduce` combines all the elements of a list into a single value. Its anonymous function takes two parameters: the value **accumulated so far** and the **next element**, and returns the new accumulated value. The first element is used as the starting point:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` throws an error on an empty list, since there is no first element to start from.

---

A function can also **return a function**. The return type is then a function type, and the body returns an anonymous function:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Notice that the returned function still uses `amount`, a parameter of `makeAdder`, even after `makeAdder` has finished. A function that remembers the variables around it like this is called a **closure**.

---

A closure does not just read the variables it captures: it can also **modify** them, and the changes are kept between calls. This makes it possible to keep private state without a class:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Each call to `makeTimer()` creates a brand new `seconds` variable, so two timers never share their count.
