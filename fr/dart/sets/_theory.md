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
tags.add('dart');   // false, already there
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
