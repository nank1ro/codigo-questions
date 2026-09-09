Vous savez déjà ajouter des méthodes à une classe que vous avez écrite vous-même. Mais qu'en est-il de `String`, `int` ou `List`, dont le code vit dans le SDK Dart ? Vous ne pouvez pas les modifier, et pourtant vous souhaiteriez souvent qu'ils aient une méthode de plus.

Une **extension** résout ce problème : elle ajoute de nouveaux membres à un type **existant**, sans toucher à son code source et sans créer de sous-classe. La syntaxe est :

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

À l'intérieur de l'extension, `this` désigne la valeur sur laquelle le membre est appelé. Une fois l'extension déclarée, ses membres s'appellent exactement comme ceux du type lui-même :

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Les extensions se déclarent au **niveau supérieur** d'un fichier, à côté des classes et des fonctions, jamais à l'intérieur de `main`.

---

Les extensions fonctionnent sur n'importe quel type, y compris les nombres. Cette extension donne à chaque `int` une méthode qui le double :

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Comme l'extension s'applique au **type**, vous pouvez appeler la méthode sur une variable ou directement sur un **littéral**. Les littéraux négatifs ont besoin de parenthèses, sinon le point est lu avant le signe moins :

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Une extension peut aussi déclarer des **getters**, qui se lisent comme des propriétés, sans parenthèses. À l'intérieur d'une extension, vous pouvez appeler directement les membres propres du type : `this.` est optionnel, exactement comme dans une classe.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

Choisissez un getter quand le membre se contente de **lire** une valeur et ne prend aucun paramètre ; choisissez une méthode quand il effectue un travail ou a besoin d'arguments.

---

Le type après `on` peut être un type **paramétré** tel que `List<int>`. L'extension ne s'applique alors qu'aux listes de ce type d'élément : `[1, 2].total()` fonctionne, `['a', 'b'].total()` ne compile pas.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

À l'intérieur de l'extension, `this` est la liste, vous pouvez donc la parcourir, l'indexer ou appeler `length` comme d'habitude.

---

Une extension sur `List<int>` ne peut pas être utilisée sur une `List<String>`. Pour écrire une extension qui fonctionne pour **tous** les types d'éléments, donnez à l'extension un **paramètre de type**, écrit entre chevrons après son nom, et utilisez-le dans le type du `on` :

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` est un espace réservé pour « quel que soit le type de l'élément » : sur une `List<int>` il devient `int`, sur une `List<String>` il devient `String`, si bien que le getter ci-dessus retourne un `int` ou une `String` en conséquence. Le compilateur remplit `T` pour vous à chaque appel.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Une extension sur `String` ne peut pas être appelée sur une `String?` : la valeur pourrait être `null`, et le compilateur refuse l'appel. Si vous déclarez plutôt l'extension sur le type **nullable**, la méthode peut être appelée directement sur une `String?`, et à l'intérieur `this` a le type `String?`, vous devez donc gérer vous-même le cas `null`, par exemple avec `??` :

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

Un `int` non nullable peut être passé là où un `int?` est attendu, l'extension fonctionne donc sur les deux.

---

Une extension peut ajouter des méthodes, des getters, des setters et des opérateurs, mais elle **ne peut pas ajouter de champs d'instance**. Une valeur `int` a une disposition fixe en mémoire, et une extension n'est qu'un ensemble de fonctions que le compilateur vous permet d'appeler avec la syntaxe point : il n'y a aucun endroit où stocker des données supplémentaires pour chaque valeur.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Les getters et les setters d'une extension peuvent uniquement calculer des valeurs à partir de `this` ou déléguer aux membres existants : ils ne peuvent rien retenir entre les appels.

---

Une extension peut déclarer des membres **statiques**. Comme dans une classe, ils appartiennent à l'extension elle-même, et non à une valeur, et on y accède par le **nom de l'extension**, et non par le type qu'elle étend :

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

Les membres statiques sont un endroit pratique pour les constantes et les fonctions utilitaires liées au type étendu.

---

Les extensions ne sont pas réservées aux types du SDK : vous pouvez aussi étendre **vos propres classes**. C'est utile lorsque la classe provient d'un paquet que vous ne contrôlez pas, ou lorsque vous voulez garder la classe petite et ajouter des aides optionnelles à côté du code qui en a besoin.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

L'extension voit les champs et les méthodes publics de la classe, exactement comme du code écrit à l'extérieur de la classe.

---

Dart permet à un type de définir la signification d'opérateurs comme `+`, `*` ou `==` pour ses valeurs, au moyen d'une méthode dont le nom est le mot-clé `operator` suivi du symbole. Le membre de droite de l'opérateur est le paramètre de la méthode :

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Comme les extensions peuvent déclarer des opérateurs, vous pouvez donner à un type existant un nouvel opérateur qu'il n'a pas déjà. `String` possède `+` et `*`, mais pas `-`, une extension peut donc définir ce que signifie `'hello world' - 'o'`.

---

Que se passe-t-il si une extension déclare un membre que le type possède **déjà** ? Le membre propre du type gagne toujours : les membres d'extension ne sont pris en compte que lorsque le type lui-même n'a aucun membre avec ce nom. Le membre de l'extension est ignoré silencieusement, sans erreur et sans redéfinition.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Une extension peut donc ajouter des membres et combler des manques, mais elle ne peut jamais **modifier** le comportement des membres existants.

---

Le nom d'une extension est optionnel. Une extension **sans nom** fonctionne de la même façon, mais elle n'est visible que dans le fichier qui la déclare :

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

Un **nom** compte dès que deux extensions offrent le même membre sur le même type : l'appel devient **ambigu** et ne compile pas. Le nom permet de résoudre le conflit de deux façons. Lorsque les extensions viennent de fichiers différents, vous pouvez `show` ou `hide` l'une d'elles dans l'import :

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Ou, n'importe où, vous pouvez appliquer l'extension **explicitement**, en enveloppant la valeur dans le nom de l'extension comme s'il s'agissait d'un constructeur :

```dart
print(Loud('hi').describe());
```

Les extensions sans nom ne peuvent être ni masquées ni appliquées explicitement ; préférez donc les extensions nommées dans le code que d'autres importeront.

---

Une extension générique peut prendre des **fonctions** en paramètres, exactement comme le font `where` et `map`. Le type de la fonction s'écrit avec le type d'élément `T`, si bien que le callback reçoit des éléments du bon type :

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
