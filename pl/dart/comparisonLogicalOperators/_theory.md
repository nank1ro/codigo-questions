Operator **równości** `==` porównuje dwie wartości i zwraca `true`, jeśli są równe, lub `false`, jeśli nie.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Wynik porównania jest zawsze wartością `bool`.

---

Operator **nierówności** `!=` zwraca `true`, gdy dwie wartości są **różne**, i `false`, gdy są takie same.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

Jest to przeciwieństwo `==`.

---

Operator **większości** `>` zwraca `true`, gdy lewa wartość jest ściśle większa niż prawa wartość.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Jeśli lewa wartość jest równa lub mniejsza od prawej, zwraca `false`.

---

Operator **mniejszości** `<` zwraca `true`, gdy lewa wartość jest ściśle mniejsza niż prawa wartość.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Jeśli lewa wartość jest równa lub większa od prawej, zwraca `false`.

---

Operator **większy lub równy** `>=` zwraca `true`, gdy lewa wartość jest większa **lub równa** prawej wartości.

```dart
int score = 50;
bool passed = score >= 50; // true
```

W przeciwieństwie do `>`, ten operator zwraca również `true`, gdy obie wartości są równe.
