O **operador de adição** `+` soma dois valores juntos.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Você pode usar `+` com valores `int` ou `double`.

---

O **operador de subtração** `-` subtrai um valor do outro.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

O resultado pode ser negativo se o segundo operando for maior que o primeiro.

---

O **operador de multiplicação** `*` multiplica dois valores juntos.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Multiplicar um `int` por outro `int` produz um `int`. Multiplicar com um `double` produz um `double`.

---

O **operador de divisão** `/` divide um valor por outro. Em Dart, `/` **sempre retorna um `double`**, mesmo quando o resultado é um número inteiro.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Sempre use uma variável `double` para armazenar o resultado de `/`.

---

O **operador de divisão inteira** `~/` divide dois números e **trunca** o resultado para um inteiro (descarta qualquer parte decimal).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Use `~/` quando você precisar de um quociente de número inteiro sem resto.
