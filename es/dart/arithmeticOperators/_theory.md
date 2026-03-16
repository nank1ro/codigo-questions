El **operador de suma** `+` suma dos valores juntos.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Puedes usar `+` con valores `int` o `double`.

---

El **operador de resta** `-` resta un valor de otro.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

El resultado puede ser negativo si el segundo operando es mayor que el primero.

---

El **operador de multiplicación** `*` multiplica dos valores juntos.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Multiplicar un `int` por otro `int` produce un `int`. Multiplicar con un `double` produce un `double`.

---

El **operador de división** `/` divide un valor entre otro. En Dart, `/` **siempre devuelve un `double`**, incluso cuando el resultado es un número entero.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Siempre usa una variable `double` para almacenar el resultado de `/`.

---

El **operador de división entera** `~/` divide dos números y **trunca** el resultado a un entero (descarta cualquier parte decimal).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Usa `~/` cuando necesites un cociente de número entero sin residuo.
