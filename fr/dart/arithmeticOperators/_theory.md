L'**opérateur d'addition** `+` ajoute deux valeurs ensemble.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Vous pouvez utiliser `+` avec des valeurs `int` ou `double`.

---

L'**opérateur de soustraction** `-` soustrait une valeur d'une autre.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

Le résultat peut être négatif si le deuxième opérande est plus grand que le premier.

---

L'**opérateur de multiplication** `*` multiplie deux valeurs ensemble.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Multiplier un `int` par un autre `int` produit un `int`. Multiplier avec un `double` produit un `double`.

---

L'**opérateur de division** `/` divise une valeur par une autre. En Dart, `/` **renvoie toujours un `double`**, même lorsque le résultat est un nombre entier.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Utilisez toujours une variable `double` pour stocker le résultat de `/`.

---

L'**opérateur de division entière** `~/` divise deux nombres et **tronque** le résultat à un entier (rejette toute partie décimale).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Utilisez `~/` lorsque vous avez besoin d'un quotient entier sans reste.
