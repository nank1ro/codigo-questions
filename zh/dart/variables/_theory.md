Variables are containers for storing values.
Every variable in Dart is an object (`Object`).
To create a variable, we have to give it a __name__ taking into account the fact that it must not contain spaces.
Take a look at the following:

```dart
int number = 1;
```

This statement declares a variable called `number` of type `int`.
It then sets the value of the variable to number `1`.
The `int` part of the declaration is known as __type annotation__, and tells Dart explicitly the type of the variable.

---

In the previous example, we saw the creation of a variable:

```dart
int number = 1;
```

Do not be fooled by the symbol `=`.
It is not the equality symbol as in mathematics, but is known as the __assignment operator__ because it assigns a value to the variable.
The equality sign, on the other hand, is `==`.

---

If you want to change the value of a variable, simply assign it a different value of the same type:

```dart
int number = 1;
number = 2;
```

---

The `int` type allows whole numbers to be stored.
To save decimal numbers instead, we can use the `double` type:

```dart
double pi = 3.14159;
```

This example is similar to the previous one. This time, however, the variable is of type `double`, a type which allows decimal numbers to be stored with high precision.

---

Dart is a __type-safe__ language.
This means that when you assign a type to a variable, you cannot change it afterwards. Here is an example:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

3.14159` is of type `double`, but you've already defined `integerNumber` with type `int`.

Of course, occasionally it might be useful to assign related types to the same variable. For example you might want a variable `integerNumber` which accepts both `int` and `double` numbers, like here:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Both `int` and `double` extend `num`, so both types are accepted.
However, if we try to assign a `String` the compiler returns an error.

---

If you like to live by risk, we can completely ignore the __type-safety__ of the language by using the `dynamic` type.
This allows you to assign any type of value to the variable.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

This approach is strongly discouraged as errors are no longer intercepted by the code's _analyzer_, but only _runtime_ (when the programme is running).

---

Dart supports __type inference__.
It is not necessary to indicate the type of a variable as Dart can infer its type.
The `var` keyword tells Dart to use the most appropriate type.

```dart
var number = 5;
```

It is not necessary to tell Dart that the number `5` is of type `int`.
Dart infers the type and makes `number` of type `int`.

---

Dart supports two different types of "_variables_" whose value never changes. They are declared with the keywords `const` and `final`.
Let's start by seeing what is meant by `const`.

## const (constants)

Variables whose value you can change are known as __mutable_data__. Mutable data is often overused and can present problems. It is easy to lose track of all the points in the code that can change the value of a variable.

For this reason, you should use `const`ants instead of `var`iables whenever possible. These variables that cannot change value are also called __immutable data__.

To create a constant in Dart we use the `const` keyword:

```dart
const number = 5;
```

Just like `var`, Dart with the __type inference__ determines that `number` is of type `int`.

---

When you have declared a constant variable, you can no longer change its value. For example:

```dart
const number = 2;
number = 3; // Error
```

This code produces the error:
> Constant variables can't be assigned a value.

That is, it is not possible to change the value of a constant variable.

---

You will often find yourself in the situation of wanting to use a constant but not knowing the value at compile time. You will only know the value after the program has started execution.
This type of constant is known as a __runtime constant__.

In Dart `const` is only used for __compile-time constants__ for values that can be determined by the compiler before the programme is executed.

If you cannot create a constant variable because you do not know its compile-time value, then you must use the `final` keyword to make the variable a __runtime constant__.

There are many reasons why you cannot know the value of a variable before running the program. For example, you would have to get the value from the server, or ask the user for it.

---

Here is an example of a value that can only be obtained at runtime:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` is a function to get the current date and time of when the code is executed.
With the `hour` field we access the number of hours that have passed since the start of the day.

Since the value of `hour` is different depending on when the code is executed, this can be defined as the _runtime_ value.

If you try to change the value of a `final` variable, you get an error.
