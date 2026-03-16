Un __booléen__ est un type de données qui ne peut contenir que l'une de deux valeurs : `true` ou `false`.
En Dart, le type booléen est déclaré avec le mot-clé `bool`.

```dart
bool isRaining = true;
```

La variable `isRaining` stocke la valeur `true`, ce qui signifie qu'il pleut actuellement.
Les valeurs booléennes sont toujours écrites en minuscules : `true` et `false`.

---

Comme n'importe quelle autre variable, vous pouvez afficher une valeur booléenne avec `print()`.
Lorsque vous affichez un booléen, Dart génère le texte `true` ou `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Une variable booléenne peut également contenir la valeur `false`.
Utilisez `false` quand quelque chose n'est pas le cas.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Comme `true`, `false` doit être écrit en minuscules.

---

L'__opérateur de négation__ `!` (aussi appelé "non") inverse une valeur booléenne.
Appliquer `!` à `true` donne `false`, et appliquer `!` à `false` donne `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

C'est utile quand vous voulez vérifier le contraire d'une condition.

---

Les booléens sont utilisés partout dans la programmation pour représenter des conditions et orienter les décisions.
Chaque fois que votre programme doit choisir entre deux possibilités, un booléen est impliqué.

Exemples :
- L'utilisateur est-il connecté ? (`isLoggedIn`)
- La porte est-elle ouverte ? (`isDoorOpen`)
- La commande a-t-elle été expédiée ? (`isShipped`)
