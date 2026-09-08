Un **String** est un morceau de texte : une séquence de caractères entourée de guillemets. En Dart, vous pouvez utiliser des guillemets simples `'...'` ou des guillemets doubles `"..."`, ils fonctionnent exactement de la même manière :

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Choisir un type de guillemets vous permet d'utiliser l'autre type à l'intérieur du texte sans avoir besoin de l'échapper :

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Si vous avez besoin du même guillemet à l'intérieur, échappez-le avec une barre oblique inverse : `'It\'s sunny'`.

---

Deux chaînes peuvent être jointes en une nouvelle avec l'opérateur `+`, appelé **concaténation** :

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart joint également deux **littéraux** de chaîne écrits l'un à côté de l'autre, sans aucun opérateur. C'est pratique pour répartir un long texte sur plusieurs lignes :

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Seules les chaînes peuvent être concaténées avec `+` : `'Age: ' + 30` est une erreur de compilation, car `30` est un `int`.

---

Au lieu de concaténer, vous pouvez insérer des valeurs directement dans une chaîne avec l'**interpolation**. Écrivez `$name` pour insérer la valeur d'une variable, et `${expression}` pour insérer le résultat de n'importe quelle expression :

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

L'interpolation fonctionne avec n'importe quel type : les nombres, les booléens et les listes sont automatiquement convertis en texte, donc `'Age: $age'` fonctionne même si `age` est un `int`.

---

Chaque chaîne connaît le nombre de caractères qu'elle contient grâce à sa propriété `.length`. Les espaces et la ponctuation comptent aussi comme des caractères :

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Vous pouvez lire un seul caractère avec des crochets et son **index**, en commençant à `0`. Le résultat est un `String` d'un seul caractère :

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Lire un index en dehors de la chaîne (comme `word[5]`) lève une erreur.

---

Les chaînes sont **immuables** en Dart : une fois créée, une chaîne ne change jamais. Des méthodes comme `.toUpperCase()` et `.toLowerCase()` ne modifient pas la chaîne d'origine, elles **en renvoient une nouvelle** :

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Si vous voulez que la variable contienne la nouvelle valeur, réassignez le résultat : `word = word.toUpperCase();`.

---

Le texte saisi par un utilisateur a souvent des espaces supplémentaires autour de lui. La méthode `.trim()` renvoie une copie de la chaîne sans les espaces en début et en fin (espaces, tabulations et retours à la ligne). `.trimLeft()` et `.trimRight()` ne les suppriment que d'un côté :

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

La méthode `.substring(start, end)` renvoie la partie d'une chaîne allant de l'index `start` jusqu'à, **sans l'inclure**, l'index `end`. Si vous omettez `end`, elle prend tout jusqu'à la fin de la chaîne :

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Plusieurs méthodes permettent de rechercher à l'intérieur d'une chaîne :

- `.contains(other)` renvoie `true` si `other` apparaît n'importe où dans la chaîne
- `.startsWith(other)` et `.endsWith(other)` vérifient le début et la fin
- `.indexOf(other)` renvoie l'index de la première occurrence, ou `-1` si elle n'est pas trouvée

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Toutes sont sensibles à la casse : `'Dart'.contains('dart')` vaut `false`.

---

La méthode `.replaceAll(from, to)` renvoie une nouvelle chaîne où **chaque** occurrence de `from` est remplacée par `to`. `.replaceFirst(from, to)` ne remplace que la première :

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

La méthode `.split(separator)` découpe une chaîne en une `List<String>` à chaque occurrence du séparateur. L'opposé est `.join(separator)`, une méthode des listes qui assemble les éléments en une seule chaîne :

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Appeler `.split('')` avec un séparateur vide vous donne une liste avec chaque caractère individuel.
