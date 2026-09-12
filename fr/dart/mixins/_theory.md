Une classe ne peut `extend` qu'une seule superclasse, mais très souvent le même comportement est nécessaire à des classes qui n'ont rien d'autre en commun. Un **mixin** est une tranche de comportement réutilisable qu'un nombre quelconque de classes peut adopter.

On le déclare avec le mot-clé **`mixin`**, et une classe l'adopte avec le mot-clé **`with`** :

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` ne déclare aucun membre en propre, et pourtant chaque `Fish` possède `swim`, car les membres du mixin deviennent des membres de la classe. Un mixin peut être utilisé par autant de classes que vous voulez, liées ou non.

---

Le corps d'un mixin ressemble au corps d'une classe : des méthodes, des getters et des champs, écrits exactement de la même façon. La différence réside dans ce que vous pouvez faire avec la déclaration elle-même.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

Le nom d'un mixin est aussi un **type**, donc `Server() is Timestamped` vaut `true` et une variable peut être déclarée comme `Timestamped t = Server();`. Deux classes sans lien partagent désormais une même implémentation sans que l'une hérite de l'autre.

---

Un mixin ne se limite pas aux méthodes : il peut aussi déclarer des **champs**, et chaque objet de chaque classe utilisant le mixin obtient sa propre copie de ces champs.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

C'est ce qui fait d'un mixin plus qu'une interface : il apporte à la fois les données et le code qui les manipule.

---

Une déclaration `mixin` n'est **pas** une classe. Elle existe uniquement pour être mélangée dans d'autres classes, elle n'a donc pas de constructeur propre et ne peut être ni instanciée ni étendue :

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

Le nom fonctionne toujours comme un type, donc `Team() is Scored` et `Scored s = Team();` sont tous deux valides. Un mixin n'a pas de constructeur, donc un champ non nullable doit être initialisé là où il est déclaré (ou marqué `late`), comme `int score = 0;` ci-dessus.

---

Un mixin peut déclarer un membre **sans corps**. Un tel membre est abstrait : le mixin l'utilise, et la classe qui adopte le mixin doit le fournir.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

Le mixin apporte le comportement, la classe apporte les données. Un champ dans la classe, comme `final String name;`, suffit à satisfaire un getter abstrait de même nom.

---

En assemblant les pièces, un programme qui utilise un mixin comporte trois parties : la déclaration `mixin`, une ou plusieurs classes qui l'adoptent avec `with`, et le code qui appelle le membre partagé.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Les déclarations de niveau supérieur peuvent être écrites dans n'importe quel ordre en Dart, mais la lecture d'un fichier de haut en bas est plus facile lorsque le mixin vient avant les classes qui l'utilisent.

---

Une classe peut utiliser **plusieurs mixins à la fois**, listés après `with` et séparés par des virgules. Dart les applique **de gauche à droite**, empilant chacun au-dessus du précédent, si bien que lorsque deux mixins déclarent le même membre, le **dernier** de la liste l'emporte :

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

Cet empilement s'appelle la **linéarisation** : `with A, B` construit la chaîne `Object` → `A` → `B` → la classe elle-même.

---

Puisque le dernier mixin l'emporte, l'ordre de la liste `with` fait partie du sens de la classe, ce n'est pas un détail de style. Le réordonner change l'implémentation dont l'objet finit par disposer :

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

Les membres déclarés par un seul mixin ne sont jamais en compétition : ils sont disponibles quel que soit l'ordre. Lisez `with X, Y` comme « partir de `X`, puis laisser `Y` le redéfinir ».

---

Les mixins et `extends` fonctionnent ensemble. Une classe peut avoir une superclasse **et** une liste de mixins, et les mixins sont toujours appliqués **par-dessus** la superclasse :

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

La chaîne ici est `Object` → `Document` → `Timestamped` → `Report`. Un membre est recherché à partir de la fin de la chaîne, donc `Report().header()` trouve d'abord la version de `Timestamped`. Déclarer le même membre dans la superclasse et dans un mixin est parfaitement légal : c'est ainsi qu'un mixin remplace ou enveloppe un comportement hérité.

---

Le corps de la classe se trouve tout à la fin de la chaîne, donc un membre déclaré dans la classe **redéfinit** le même membre venant de n'importe lequel de ses mixins. À l'intérieur de la redéfinition, **`super`** atteint la version fournie par le mixin :

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

Le mixin lui-même reste intact : `Guest` obtient toujours le `greet` d'origine. `super.greet()` est ce qui permet à `Host` de s'appuyer sur le comportement partagé au lieu de le copier.

---

Certains comportements n'ont de sens que par-dessus une classe particulière et ont besoin des membres de cette classe pour faire leur travail. La clause **`on`** exprime cette exigence :

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` fait deux choses : il permet au mixin d'utiliser les membres de `Animal`, comme `name` ci-dessus, et il restreint qui peut utiliser le mixin. `class Rock with Noisy {}` est une erreur de compilation, car `Rock` n'est pas un `Animal`.

---

Un mixin avec une clause `on` lit les membres de sa superclasse comme s'ils étaient les siens, ce qui en fait un bon emplacement pour un comportement qui décore un type existant :

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` redéfinit `kind`, et `show` récupère la redéfinition automatiquement : le mixin appelle toujours le membre sur l'objet réel.

---

Une fois qu'un mixin a une clause `on`, il peut **redéfinir** un membre de ce type et appeler **`super`** pour atteindre la version située en dessous de lui dans la chaîne :

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` n'est pas le `log` propre au mixin, c'est celui situé en dessous de lui, donc il n'y a pas de récursion infinie. Empilez plusieurs mixins de ce genre avec `with A, B` et chacun enveloppe le précédent : l'appel entre d'abord dans le **dernier** mixin puis descend jusqu'à la superclasse.

---

Une déclaration `mixin` ne peut être ni instanciée ni étendue, et une simple `class` ne peut pas être utilisée après `with`. Lorsque vous avez besoin d'une déclaration qui fonctionne dans les **deux** sens, écrivez **`mixin class`** :

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

Une `mixin class` paie cette flexibilité par deux restrictions : elle doit étendre `Object`, elle ne peut donc pas avoir sa propre clause `extends`, et elle ne doit pas déclarer de constructeur, car un mixin n'en exécute jamais.

---

Les mixins, l'héritage et les interfaces résolvent trois problèmes différents :

- **`extends`** donne à une classe une seule superclasse, pour une relation « est une sorte de ». Il n'y a qu'une seule place, elle doit donc revenir à la relation la plus forte.
- **`with`** ajoute un comportement dont de nombreuses classes sans lien ont besoin. Il n'y a pas de limite, et l'implémentation est partagée, pas copiée.
- **`implements`** promet un ensemble de membres mais n'apporte **aucune** implémentation : chaque classe doit écrire le corps elle-même.

Le signe révélateur d'un besoin de mixin est une méthode que vous copieriez sinon dans des classes sans parent commun naturel, comme `Duck`, `Plane` et `Kite` qui ont tous besoin du même `fly`.

---

Les mixins empilés permettent de combiner des règles petites et indépendantes en une seule classe. Chaque mixin redéfinit le même membre, fait sa propre part et appelle `super` pour transmettre le travail. Comme l'appel entre d'abord dans le **dernier** mixin, l'ordre de la liste `with` décide quelle règle s'exécute avant laquelle :

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` double chaque dépôt. Ajoutez un second mixin après `Doubled` et il reçoit le dépôt en premier, avant même que `Doubled` le voie.
