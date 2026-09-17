L'**operatore di uguaglianza** `==` confronta due valori e restituisce `true` se sono uguali, o `false` se non lo sono.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Il risultato di un confronto è sempre un valore `bool`.

---

L'**operatore di disuguaglianza** `!=` restituisce `true` quando due valori sono **diversi**, e `false` quando sono uguali.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

È il contrario di `==`.

---

L'**operatore maggiore di** `>` restituisce `true` quando il valore a sinistra è strettamente maggiore del valore a destra.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Se il valore a sinistra è uguale o minore di quello a destra, restituisce `false`.

---

L'**operatore minore di** `<` restituisce `true` quando il valore a sinistra è strettamente minore del valore a destra.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Se il valore a sinistra è uguale o maggiore di quello a destra, restituisce `false`.

---

L'**operatore maggiore di o uguale a** `>=` restituisce `true` quando il valore sinistro è più grande che **o uguale a** il valore destro.

```dart
int score = 50;
bool passed = score >= 50; // true
```

A differenza di `>`, questo operatore restituisce anche `true` quando entrambi i valori sono uguali.

---

L'**operatore AND** `&&` combina due espressioni booleane. Restituisce `true` solo quando **entrambi** i lati sono `true`. Se uno dei lati è `false`, il risultato è `false`.

```dart
bool a = true;
bool b = true;
bool result = a && b; // true

bool c = true;
bool d = false;
bool result2 = c && d; // false
```

---

L'**operatore OR** `||` combina due espressioni booleane. Restituisce `true` quando **almeno un** lato è `true`. Restituisce `false` solo quando **entrambi** i lati sono `false`.

```dart
bool a = false;
bool b = true;
bool result = a || b; // true

bool c = false;
bool d = false;
bool result2 = c || d; // false
```
