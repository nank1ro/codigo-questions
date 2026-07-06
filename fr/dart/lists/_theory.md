En Dart, une **liste** est une collection ordonnée d'éléments. La façon la plus simple de créer une liste est d'utiliser la syntaxe littérale `[]` :

```dart
List<int> numbers = [1, 2, 3];
```

Vous pouvez également utiliser l'inférence de type avec `var` :

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

L'annotation de type `List<String>` indique à Dart que chaque élément de la liste doit être un `String`.

---

Les listes en Dart sont **indexées à partir de zéro**, ce qui signifie que le premier élément est à l'index `0`, le second à l'index `1`, et ainsi de suite.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

L'accès à un élément par index se fait avec la syntaxe `list[index]`.

---

La méthode `.add()` ajoute un seul élément à la **fin** d'une liste :

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Notez que `.add()` modifie la liste **en place** et retourne `void`.

---

La propriété `.length` retourne le nombre d'éléments d'une liste :

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Une liste vide a une longueur de `0` :

```dart
var empty = [];
print(empty.length); // 0
```

---

La méthode `.contains()` vérifie si une liste contient une valeur donnée. Elle retourne `true` si elle est trouvée, `false` sinon :

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Cela est utile pour les vérifications d'appartenance sans avoir besoin d'une boucle.
