Un **Set** est une collection de valeurs **uniques** : la même valeur ne peut apparaître qu'une seule fois au maximum. Comme une Map, un Set est créé avec la syntaxe littérale `{}`, mais il contient des valeurs simples au lieu de paires `key: value` :

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

L'annotation de type `Set<int>` indique à Dart que chaque élément est un `int`. Comme pour les listes et les Maps, `var` infère le type à partir du littéral :

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Un Set ne stocke jamais la même valeur deux fois. Si un littéral contient des doublons, seule la première occurrence est conservée et les autres sont ignorées à l'exécution sans aucune erreur (l'analyseur vous avertira à propos d'un littéral qui répète une valeur) :

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

La propriété `.length` renvoie le nombre d'éléments **uniques** que contient le Set :

```dart
print(letters.length); // 3
```

---

La méthode `.add(value)` insère une seule valeur. Elle renvoie `true` si la valeur a été ajoutée et `false` si elle était déjà dans le Set, auquel cas rien ne change. La méthode `.addAll(iterable)` insère tous les éléments d'une liste ou d'un autre Set, en ignorant elle aussi ceux déjà présents :

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, déjà présent
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Un littéral `{}` vide est une **Map**, pas un Set. Pour créer un Set vide, donnez-lui un type :

```dart
var empty = <String>{};
Set<int> other = {};
```

---

La méthode `.remove(value)` supprime une valeur du Set. Elle renvoie `true` si la valeur était présente et `false` sinon :

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Pour supprimer tous les éléments à la fois, utilisez `.clear()`.

---

Pour vérifier si une valeur est dans un Set, utilisez `.contains(value)`, qui renvoie un `bool`. La propriété `.isEmpty` vaut `true` quand le Set n'a aucun élément, et `.isNotEmpty` quand il en a au moins un :

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Le Set par défaut en Dart se souvient de l'**ordre d'insertion** : quand vous l'affichez ou le parcourez, les éléments apparaissent dans l'ordre dans lequel ils ont été ajoutés pour la première fois. Ajouter une valeur déjà présente ne la déplace pas :

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Un Set est un `Iterable`, vous pouvez donc parcourir directement ses éléments avec `for-in`, tout comme une liste. Il n'y a pas d'index : les éléments sont visités dans l'ordre d'insertion :

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```

---

Les Sets prennent en charge les opérations classiques sur les ensembles. Chacune renvoie un **nouveau** Set et laisse les originaux inchangés :

- `a.union(b)` contient les éléments qui sont dans `a` **ou** dans `b`
- `a.intersection(b)` contient les éléments qui sont à la fois dans `a` **et** dans `b`
- `a.difference(b)` contient les éléments de `a` qui ne sont **pas** dans `b`

```dart
var a = {1, 2, 3};
var b = {2, 3, 4};
print(a.union(b));        // {1, 2, 3, 4}
print(a.intersection(b)); // {2, 3}
print(a.difference(b));   // {1}
```

---

Convertir une liste en Set est le moyen le plus simple de **supprimer les doublons** : chaque liste possède une méthode `.toSet()` qui renvoie un Set avec ses éléments uniques, dans l'ordre de leur première apparition. Un Set possède une méthode `.toList()` qui fait le chemin inverse, donc enchaîner les deux vous donne une liste sans doublons :

```dart
var votes = ['a', 'b', 'a', 'c', 'b'];
Set<String> unique = votes.toSet();
print(unique); // {a, b, c}
List<String> cleaned = votes.toSet().toList();
print(cleaned); // [a, b, c]
```

---

Les listes et les Sets ont tous deux une méthode `.contains()`, mais ils fonctionnent très différemment. Une liste vérifie ses éléments un par un depuis le début, donc une recherche dans une longue liste devient plus lente à mesure que la liste grandit. Un Set stocke ses éléments selon leur hash, donc `.contains()` trouve une valeur en un temps à peu près constant, quel que soit le nombre d'éléments.

Si vous devez vérifier l'appartenance de nombreuses fois et que l'ordre ou les doublons n'ont pas d'importance, un Set est le bon outil :

```dart
var banned = {'spam', 'scam'};
print(banned.contains('spam')); // rapide, même avec des millions d'éléments
```
