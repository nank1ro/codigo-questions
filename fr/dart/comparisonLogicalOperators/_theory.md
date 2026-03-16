L'**opérateur d'égalité** `==` compare deux valeurs et retourne `true` si elles sont égales, ou `false` sinon.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Le résultat d'une comparaison est toujours une valeur `bool`.

---

L'**opérateur de différence** `!=` renvoie `true` lorsque deux valeurs sont **différentes**, et `false` lorsqu'elles sont identiques.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

Il est l'opposé de `==`.

---

L'**opérateur supérieur à** `>` renvoie `true` lorsque la valeur de gauche est strictement plus grande que la valeur de droite.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Si la valeur de gauche est égale ou inférieure à celle de droite, il renvoie `false`.

---

L'**opérateur inférieur à** `<` renvoie `true` lorsque la valeur de gauche est strictement plus petite que la valeur de droite.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Si la valeur de gauche est égale ou supérieure à celle de droite, il renvoie `false`.

---

L'**opérateur supérieur ou égal à** `>=` retourne `true` quand la valeur de gauche est plus grande que **ou égale à** la valeur de droite.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Contrairement à `>`, cet opérateur retourne aussi `true` quand les deux valeurs sont égales.
