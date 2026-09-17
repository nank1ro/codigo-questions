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

---

Operator **AND** `&&` łączy dwa wyrażenia logiczne. Zwraca `true` tylko wtedy, gdy **obie** strony są `true`. Jeśli choćby jedna strona jest `false`, wynik to `false`.

```dart
bool a = true;
bool b = true;
bool result = a && b; // true

bool c = true;
bool d = false;
bool result2 = c && d; // false
```

---

Operator **OR** `||` łączy dwa wyrażenia logiczne. Zwraca `true` jeśli **co najmniej jedna** strona jest `true`. Zwraca `false` tylko wtedy, gdy obie strony są `false`.

```dart
bool a = true;
bool b = false;
bool result = a || b; // true

bool c = false;
bool d = false;
bool result2 = c || d; // false
```
