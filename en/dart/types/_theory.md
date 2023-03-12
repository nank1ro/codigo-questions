Types allow you to categorize all the different data types you use in your code.
In Dart, a __type__ is a way of telling the compiler how you are going to use a given piece of data.
Here's an example of types that Dart supports:
- int
- String
- double
- dynamic
- num

Dart supports many other types. These listed are the main ones you will use.

---

It's okay if you explicitly define the type of a variable, for example:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Variables with explicit type can also be constants, just add the `const` or `final` keyword before the type:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Note: Mutable data allows you to change it whenever you want in an easy way. However, many experienced programmers appreciate the benefits of immutable data. When a value is immutable, you can trust that no one will be able to change the value after you create it. Limiting your data this way prevents many hard-to-find bugs and makes the program easier to think about and test.

---

While it is possible to note the type of a variable, this is redundant. You know that `10` is of type `int` and `3.14` is of type `double`. The Dart compiler is able to infer it thanks to __type inference__. Not all programming languages have _type inference_, and this makes Dart a very powerful programming language.

You can simply remove the type from the variables, for example:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

When the type of a variable is not explicitly noted, Dart will try to infer its type.

---

There is a programmatic way to check the type of a variable, namely with the `is` keyword:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

As you can see Dart has assigned the type `double` to the variable `number`.

---

The `is` keyword allows you to check if a variable is of the type you define. But you can 
 also check if a variable is not of the type defined with the `is!` keyword
```dart
final number = 3.14;
print(number is! int); // true
```

---

Another option you have for seeing the type of a _runtime_ variable is to use the `runtimeType` property which is available to all types.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

Sometimes you will find yourself in the situation of having one type, but needing to convert it to another. You might be tempted to do:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

But Dart will complain and give you the error:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Some programming languages are not that restrictive and will silently convert. Experience shows that this type of silent implicit conversion is a frequent source of bugs and performance problems. Dart has disabled this feature to avoid these problems.

Remember, computers rely on programmers to figure out what to do. In Dart this includes being explicit about the type of conversion.

Instead of expecting an implicit conversion from Dart, you need to explicitly say that you want Dart to convert the type to you. Here's how to convert a `double` number to an `int` one:
```dart
var integer = decimal.toInt();
```

The assignment tells Dart, unequivocally, that you want to convert from the original type `double` to the new type `double`.

> NOTES: In this case, assigning a decimal value to an integer loses precision. The variable `integer` has the value __3__ instead of __3.14__. This is why it's important to be explicit. Dart wants to be sure of what you are doing and lets you know that you will lose information by converting.

---

So far we have seen the operators used independently on integers or decimals. What if you have 
an integer and need to multiply it with a decimal number? Let's see an example:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` is of type `int` while `pi` is of type `double`. What will be the type of `circumference`? Dart will assign the type `double` to the variable `circumference`. This is the safer choice as if I had made it of type `int` it could have caused a loss of precision.

If you want an `int` as a result, you have to do the conversion explicitly:
```dart
const circumference = (2 * pi * radius).toInt();
```

The parentheses tell Dart to multiply first, and then take the result and convert it to an integer value. Unfortunately the analyzer will not like this code:
 > Const variables must be initialized with a constant value.

The problem is that the `toInt` method is a runtime-only method. This means that the `circumference` variable cannot be determined at compile time, so it is not possible for the variable to be constant. To fix replace `const` with `final`:

```dart
final circumference = (2 * pi * radius).toInt();
```

Now `circumference` is a __runtime constant__ variable of type `int`.

---

Sometimes you might have a variable with a generic type, but you need functionality that only exists in a subtype. If you are sure that the type of the variable is the subtype you need, then you can use the `as` keyword to change its type. This prodecure is also known as __type casting__, here is an example:

```dart
num number = 3;
```

Let's say we want to check if the number is even, and the functionality in question is present only on the `int` subtype.
```dart
print(number.isEven);
```

The code above should return you a type error:
> The getter `isEven` isn't defined for the type 'num'.

The `num` type is a too general type to know if a number is even or odd. Only integers can be even or odd.
The problem occurs if `num` contains a `double` value, since `num` includes both `double` and `int` types. In this case, we are sure that __3__ is an integer, so we can cast to `int`

```dart
final integer = number as int;
print(integer.isEven); // false
```

The `as` keyword causes the compiler to recognize the variable `integer` as having the type `int`. This allows you to use the `isEven` property which is present on integers. Since the number __3__ is not an integer, the result is false.

You have to wait when casting. If you incorrectly cast the type you will get a runtime error:
```dart
num numero = 3;
final decimale = numero as double;
```

This will crash the program with the following error:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

The runtime type of `number` is `int` and not `double`. In Dart, you cannot cast with same-level types, such as `int` and `double`. You can only cast sub-types.
