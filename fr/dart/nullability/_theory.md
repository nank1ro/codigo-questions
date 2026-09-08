Vous savez déjà déclarer une variable avec un type, comme `String name = 'Ada';`. Cependant, il arrive qu'une valeur soit tout simplement **absente** : un utilisateur sans surnom, une recherche qui ne trouve rien, un texte qui ne peut pas être converti en nombre. Dart représente une valeur absente avec `null`.

Depuis Dart 2.12, le langage dispose d'une **null safety** solide : un type normal comme `String` ne peut **jamais** contenir `null`. Tenter de lui en affecter une est une erreur de compilation, si bien que le programme ne s'exécute même pas :

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Pour autoriser une valeur absente, vous ajoutez un point d'interrogation `?` après le type. Une `String?` contient soit une `String`, soit `null`, et afficher `null` montre le mot `null` :

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Les types sans `?` sont dits **non nullables**, les types avec `?` sont **nullables**.

---

Une variable nullable déclarée **sans valeur** commence avec la valeur `null`, donc `= null` peut être omis :

```dart
int? age;
print(age); // null
```

Une variable non nullable n'a pas une telle valeur par défaut : Dart refuse de compiler tout code qui la lit avant qu'une valeur ne lui ait été affectée.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Appeler une méthode ou lire une propriété sur `null` provoquerait un plantage, donc Dart ne vous laisse pas le faire sur une valeur nullable avec le point habituel :

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

L'opérateur d'**accès null-aware** `?.` résout ce problème : si la valeur est `null`, toute l'expression vaut `null` et rien d'autre n'est évalué, sinon il fonctionne comme un `.` normal :

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Comme le résultat peut être `null`, son type est nullable : `text?.length` est un `int?`, pas un `int`.

---

Souvent, une valeur absente doit être remplacée par une valeur **par défaut**. L'opérateur **if-null** `??` retourne l'opérande de gauche lorsqu'il n'est pas `null`, et l'opérande de droite sinon :

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` ne réagit qu'à `null` : une chaîne vide `''` ou le nombre `0` sont de vraies valeurs, donc ils sont conservés.

`??` se combine bien avec `?.`, car `?.` produit un résultat nullable :

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

Le grand avantage de la null safety est que la plupart des erreurs liées à `null` sont détectées par le **compilateur**, et non par vos utilisateurs. Les règles jusqu'ici :

- un type non nullable (`String`, `int`, `List<int>`...) ne peut jamais être `null`
- un type nullable (`String?`, `int?`, `List<int>?`...) le peut, et commence avec la valeur `null` quand il est déclaré sans valeur
- `.` sur une valeur nullable ne compile pas : utilisez `?.` ou fournissez une valeur par défaut avec `??`

---

L'opérateur d'**affectation if-null** `??=` affecte une valeur à une variable **seulement si** cette variable vaut actuellement `null` ; sinon il la laisse intacte :

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

Il fonctionne aussi sur les entrées d'une Map, qui sont nullables car une clé peut être absente :

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

Parfois, **vous** savez qu'une valeur nullable n'est pas `null` à un certain point, même si le compilateur ne peut pas le deviner. L'opérateur d'**assertion non nulle** `!` transforme une `String?` en une `String` en promettant que la valeur est présente :

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Attention : `!` déplace la vérification du moment de la compilation vers le moment de l'exécution. Si la valeur **est** `null`, le programme lève une erreur et s'arrête :

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Utilisez `!` avec parcimonie, et seulement quand un `null` à cet endroit serait de toute façon un bug.

---

Rappelez-vous la différence entre les trois opérateurs que vous avez vus sur une valeur nullable :

- `?.` retourne `null` quand la valeur est `null`, et ne lève jamais d'erreur
- `??` remplace `null` par une valeur par défaut
- `!` suppose que la valeur est présente et **lève une erreur à l'exécution** quand elle ne l'est pas

Aucun d'eux n'est une erreur de compilation : le compilateur vous fait confiance pour votre `!`, et seul le programme en cours d'exécution peut découvrir que la promesse a été rompue.

---

Vérifier une valeur nullable avec `if` est plus sûr que `!`, et Dart vous le rend bien. Après une vérification comme `if (x != null)`, le compilateur sait que `x` ne peut pas être `null` à l'intérieur du bloc, donc il traite `x` comme non nullable à cet endroit. Cela s'appelle la **promotion de type** :

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

La promotion fonctionne aussi après un retour anticipé :

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

La promotion s'applique aux **variables locales et aux paramètres**, dont la valeur ne peut pas changer à votre insu entre la vérification et l'utilisation.

---

La promotion de type ne fonctionne **pas** sur un **champ** de classe qui peut être modifié de l'extérieur, car entre la vérification et l'utilisation, un autre morceau de code (un getter redéfini dans une sous-classe, une autre méthode) pourrait le remettre à `null` :

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

La correction standard consiste à copier le champ dans une **variable locale**, qui est bien promue :

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

Un champ non nullable doit normalement recevoir une valeur dans le constructeur. Quand la valeur n'est connue que **plus tard** (après la lecture d'un fichier, l'ouverture d'une connexion...), vous pouvez marquer le champ `late` : le compilateur accepte l'initialiseur manquant et vous fait confiance pour affecter le champ avant de le lire.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Lire un champ `late` qui n'a pas encore été affecté lève une `LateInitializationError` à l'exécution. Comme `!`, `late` échange une garantie à la compilation contre une vérification à l'exécution, c'est donc une promesse que vous devez tenir.

`late` peut aussi être combiné avec un initialiseur, qui s'exécute alors **paresseusement**, la première fois que la variable est lue :

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

La nullabilité façonne la manière dont vous déclarez les **paramètres nommés**. Un paramètre nommé avec un type nullable est optionnel : quand l'appelant l'omet, il vaut simplement `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Un paramètre nommé avec un type non nullable et sans valeur par défaut n'aurait aucune valeur quand il est omis, donc Dart vous oblige à le marquer `required` ; l'appelant doit alors toujours le passer :

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

La nullabilité s'applique aussi aux **éléments** d'une collection. Une `List<int>` ne contient jamais `null`, tandis qu'une `List<int?>` le peut :

```dart
List<int?> scores = [7, null, 9];
```

Notez la différence avec `List<int>?`, qui est une liste qui peut elle-même être absente mais qui, quand elle est présente, ne contient que de vrais nombres.

Pour se débarrasser des éléments `null`, `nonNulls` retourne un `Iterable` avec seulement les valeurs présentes, typé sans `?` :

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` fait la même chose et fonctionne aussi quand la liste mélange plusieurs types.

---

Beaucoup de fonctions de bibliothèque utilisent `null` pour signaler que quelque chose **n'a pas pu être fait**. Convertir une chaîne en nombre est l'exemple classique : `int.parse` lève une `FormatException` quand le texte n'est pas un nombre, tandis que `int.tryParse` retourne `null` à la place et vous laisse décider quoi faire :

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

Le type de retour de `int.tryParse` est `int?`, donc tout ce que vous avez appris s'applique : `??` pour une valeur par défaut, `?.` pour chaîner, et une vérification `if` pour promouvoir. `double.tryParse` fonctionne de la même manière.

---

Deux autres opérateurs possèdent une variante null-aware.

La **cascade null-aware** `?..` exécute une chaîne d'opérations en cascade seulement quand l'objet n'est pas `null`, et les saute toutes sinon :

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

Le **spread null-aware** `...?` insère les éléments d'une collection nullable dans un littéral, sans rien ajouter quand la collection est `null` :

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Sans le `?`, `...extra` sur une `List<int>?` serait une erreur de compilation.

---

Les données réelles sont pleines de trous : un champ de formulaire laissé vide, une colonne absente d'un fichier, une chaîne qui n'est pas tout à fait un nombre. Les outils de ce chapitre se combinent naturellement pour les gérer : `nonNulls` pour supprimer les éléments manquants, `int.tryParse` pour convertir en toute sécurité, `??` ou une vérification `if` pour traiter ce qui n'a pas pu être converti.
