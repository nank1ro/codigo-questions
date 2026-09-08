Une **Map** est une collection de **paires clé-valeur** : chaque valeur est stockée sous une clé unique, et vous utilisez la clé pour retrouver la valeur. Une Map est créée avec la syntaxe littérale `{}`, en écrivant chaque paire comme `key: value` :

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

L'annotation de type `Map<String, int>` indique à Dart que chaque clé est un `String` et chaque valeur est un `int`. Comme pour les listes, `var` infère le type à partir du littéral :

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Pour lire une valeur, vous utilisez la clé entre crochets, tout comme un index dans une liste :

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Si la clé n'est pas dans la Map, la recherche ne lève **pas** d'erreur : elle renvoie `null`. C'est pourquoi le type de `ages['Ann']` est `int?` (un `int` nullable), et non `int` :

```dart
print(ages['Zed']); // null
```

---

Une affectation avec `map[key] = value` **ajoute** une nouvelle paire, quand la clé n'est pas encore dans la Map, ou **met à jour** la valeur stockée sous une clé existante :

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // ajoute Bob
ages['Ann'] = 31; // met à jour Ann
print(ages); // {Ann: 31, Bob: 25}
```

Les nouvelles clés sont ajoutées après les clés existantes, donc une Map se souvient de l'ordre d'insertion.

---

La méthode `.remove(key)` supprime une clé et sa valeur de la Map. Elle renvoie la valeur supprimée, ou `null` si la clé n'était pas présente :

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

La propriété `.length` renvoie le nombre de paires clé-valeur :

```dart
print(ages.length); // 1
```

---

Pour vérifier si une Map contient une clé donnée, utilisez `.containsKey(key)`. Pour vérifier si une paire quelconque stocke une valeur donnée, utilisez `.containsValue(value)`. Les deux renvoient un `bool` :

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Lire une clé manquante ne lève jamais d'erreur, alors gardez toujours à l'esprit qu'une recherche peut vous donner `null`. Un schéma sûr consiste à fournir une valeur de secours avec l'opérateur `??` :

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

La propriété `.keys` donne toutes les clés d'une Map et `.values` donne toutes les valeurs, dans l'ordre d'insertion. Ce sont des `Iterable`s paresseux, donc appelez `.toList()` quand vous avez besoin d'une vraie `List` :

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
