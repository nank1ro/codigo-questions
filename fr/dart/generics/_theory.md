Une `List` ne se contente pas de contenir des valeurs, elle contient des valeurs **d'un seul type**. Le type s'écrit entre chevrons juste après le nom de la collection :

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` et `int` ici sont des **arguments de type**, et un type qui en prend un est appelé **générique**. La classe de liste n'est écrite qu'une fois, et `List<String>` et `List<int>` sont deux types différents produits à partir d'elle.

L'avantage, c'est que le compilateur sait ce qu'elle contient :

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // correct : first est un String
```

---

`List` n'est pas la seule collection générique. Un `Set` prend un argument de type, et une `Map` en prend **deux** : un pour les clés et un pour les valeurs, dans cet ordre.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Un littéral de collection vide ne peut pas être déduit de son contenu, vous écrivez donc les arguments de type sur le littéral lui-même :

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Une fois les types connus, tout ce que vous sortez de la collection a déjà le bon type : `ages['Ada']` est un `int?`, jamais une valeur mystérieuse.

---

Dart possède aussi le type `dynamic`, qui signifie « tout est permis ». Une `List<dynamic>` accepte toutes les valeurs, elle semble donc plus pratique qu'une `List<String>` :

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepté
print(things.first.toUpperCase()); // accepté
```

Le hic, c'est que rien n'est vérifié pendant que vous écrivez le code. Chaque appel sur une valeur `dynamic` est résolu pendant l'exécution du programme, si bien qu'une faute de frappe comme `things.first.toUpperCse()` se compile sans broncher et explose devant un utilisateur.

Les génériques sont l'alternative : un seul morceau de code qui fonctionne avec **n'importe quel** type, alors que chaque utilisation reste vérifiée pour **un** type. C'est tout l'objet de ce sujet.

---

Vous n'êtes pas limité aux classes génériques livrées avec Dart : vous pouvez déclarer les vôtres. Un **paramètre de type** s'écrit entre chevrons après le nom de la classe, et à partir de là c'est un type normal à l'intérieur du corps :

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` n'est qu'un espace réservé. Il est rempli quand une `Box` est créée, explicitement ou par inférence :

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inféré depuis l'argument
print(a.value + 1);      // 8, le compilateur sait que value est un int
```

La lettre n'a pas d'importance : `T` est une convention pour « type », rien de plus.

---

Une fonction peut être générique à elle seule, sans vivre dans une classe générique. Le paramètre de type se place entre le nom et la liste des paramètres :

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T est String ici
print(firstOf([10, 20]));        // 10, T est int ici
```

Un seul corps de fonction, vérifié une fois, réutilisé pour chaque type. L'argument de type est généralement déduit des arguments, mais il peut être écrit explicitement quand l'inférence n'a rien à se mettre sous la dent :

```dart
final empty = firstOf<String>(<String>[]); // lève une exception, mais le type est clair
```

Les méthodes à l'intérieur d'une classe suivent exactement la même règle.

---

À l'intérieur d'une classe générique, le paramètre de type est visible partout : dans les champs, dans les paramètres du constructeur, dans les signatures des méthodes et dans leurs corps. Il est déclaré une seule fois, à côté du nom de la classe, et chaque membre peut l'utiliser.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

C'est la création de l'objet qui décide du type : `Holder<String>('fig')` fait de `item` un `String`, `Holder<int>(3)` en fait un `int`.

---

Une classe peut déclarer plusieurs paramètres de type, séparés par des virgules. `Map<K, V>` est l'exemple intégré : un type pour les clés, un pour les valeurs.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

L'**ordre** fait partie du type : `Entry<String, int>` et `Entry<int, String>` sont des types sans lien, et une valeur de l'un ne peut pas être affectée à l'autre. Les paramètres de type peuvent aussi être réordonnés dans un type de retour, ce qui permet à une méthode de rendre une version inversée de l'objet :

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Avec la sécurité null complète, le point d'interrogation peut se placer à deux endroits différents, et ils ont deux sens différents :

```dart
Box<int?> a = Box(null); // une boîte qui existe et contient un int nullable
Box<int>? b = null;      // pas de boîte du tout, mais s'il y en a une, elle contient un int
```

Dans `Box<int?>`, c'est l'**argument de type** qui est nullable, donc `a.value` est de type `int?` et peut valoir `null`, alors que `a` lui-même existe toujours. Dans `Box<int>?`, c'est la **variable** qui est nullable, donc `b` peut valoir `null` et il faut `b?.value` ou `b!.value` pour accéder à son contenu.

Un `T` seul signifie `T extends Object?`, donc un argument de type nullable comme `Box<int?>` est parfaitement légal.

---

La différence importe dès que vous utilisez la valeur. Sur une `Box<int?>`, vous accédez au champ normalement puis vous traitez le `null` qu'elle contient, tandis que sur une `Box<int>?`, vous devez d'abord passer l'absence de boîte :

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, la boîte est là, son contenu est null

Box<int>? b = null;
print(b?.value ?? 0); // 0, la boîte elle-même est absente
```

Écrire `b.value` sur une `Box<int>?` ne compile pas du tout : Dart refuse de lire un champ de quelque chose qui n'existe peut-être pas.

---

Un `T` sans borne pourrait être n'importe quoi, donc à l'intérieur du corps vous ne pouvez utiliser que ce que tout objet possède. Ceci ne compile pas :

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Une **borne** règle le problème. Écrire `T extends num` dit que « `T` ne peut être qu'un nombre », et en échange le corps peut utiliser tout ce qu'un `num` offre :

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

La borne est vérifiée au point d'appel : `half(4)` et `half(2.5)` passent, `half('fig')` est une erreur de compilation. Une borne est une promesse dans les deux sens, des arguments plus restreints contre plus de puissance à l'intérieur.

---

Le mot-clé pour une borne est toujours `extends`, même quand la borne est une interface plutôt qu'une superclasse. Il n'y a pas de `implements` dans une liste de paramètres de type.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Sans la borne, `a > b` ne compilerait pas : l'opérateur de comparaison appartient à `num`, pas à tous les objets.

---

Une borne peut mentionner le paramètre de type lui-même. `Comparable<T>` est l'interface de tout ce qui sait se comparer à ses semblables, via `compareTo` :

```dart
print('fig'.compareTo('kiwi')); // négatif : fig arrive en premier
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

Ainsi, `T extends Comparable<T>` se lit « tout type qui peut être comparé à lui-même », exactement ce dont une fonction de tri ou de maximum a besoin :

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` et `DateTime` la satisfont directement. `int` et `double` implémentent `Comparable<num>`, donc une liste de nombres est simplement comparée comme des `num`.

---

La même borne fonctionne tout aussi bien pour le plus petit élément : seul le signe de la comparaison change. `compareTo` retourne un nombre négatif quand le récepteur vient en premier, donc `item.compareTo(best) < 0` signifie que celui-ci est plus petit.

---

Une classe générique peut avoir des constructeurs nommés et **factory** comme n'importe quelle autre classe, et le paramètre de type y est disponible. Un constructeur factory ne crée pas l'objet lui-même : il exécute un corps et en retourne un, ce qui lui permet de choisir, réutiliser ou construire l'instance comme bon lui semble.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

L'argument de type se place sur la classe, pas sur le nom du constructeur : `Box<int>.first(...)`. À l'intérieur de la factory, `<T>[]` est une véritable `List<T>` vide, donc une factory est l'endroit tout indiqué pour construire une valeur par défaut pour un type que vous ne connaissez pas encore.

---

Un paramètre de type écrit sans borne n'est pas du tout sans borne : `class Box<T>` est un raccourci pour `class Box<T extends Object?>`. C'est pourquoi `Box<int?>` est accepté, et pourquoi à l'intérieur de la classe vous ne pouvez jamais supposer que `value` est non null.

Pour interdire les arguments de type nullables, bornez le paramètre par `Object` :

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` est le type de tout ce qui existe à part `null`, donc `T extends Object` se lit « n'importe quoi, pourvu que ce soit réellement là ».

---

Un `typedef` donne un nom à un type, et il peut prendre ses propres paramètres de type. La raison habituelle est de nommer une famille de types de fonctions une bonne fois pour toutes au lieu de l'énoncer à chaque utilisation :

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` n'est qu'une autre façon d'écrire `int Function(String)`, les deux sont donc interchangeables. Le gain, c'est la lisibilité : un paramètre déclaré `Transform<I, O> transform` dit à quoi la fonction sert, tandis que `O Function(I)` dit seulement à quoi elle ressemble.

Un typedef générique et une fonction générique se combinent naturellement, les paramètres de type de la fonction remplissant ceux du typedef.
