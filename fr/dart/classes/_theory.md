Une **classe** est un plan pour créer des objets. En Dart, on définit une classe avec le mot-clé `class` suivi du nom de la classe et d'une paire d'accolades :

```dart
class Animal {
  // fields and methods go here
}
```

Par convention, les noms de classe utilisent le **PascalCase** (chaque mot commence par une majuscule).

---

Une classe peut avoir des **variables d'instance** (aussi appelées champs) qui contiennent des données pour chaque objet. On les déclare dans le corps de la classe, en donnant à chacune une valeur initiale :

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Chaque objet créé à partir de cette classe aura ses propres valeurs de `name` et `age`.

---

Un **constructeur** est une méthode spéciale exécutée lors de la création (instanciation) d'un objet à partir d'une classe. Le constructeur porte le même nom que la classe :

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Un paramètre écrit `this.name` stocke la valeur passée au constructeur directement dans le champ `name` du nouvel objet. Un champ défini ainsi n'a pas besoin de valeur initiale.

On crée un objet avec le mot-clé `new` (facultatif en Dart) ou simplement le nom de la classe :

```dart
var dog = Animal('Rex');
```

---

Le paramètre `this.x` vu dans l'exercice précédent est une forme abrégée. La forme longue affecte chaque paramètre à son champ dans le corps du constructeur (`this.x` est le champ, `x` est le paramètre) :

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

La même classe peut s'écrire :

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Cette forme plus courte s'appelle les **paramètres formels d'initialisation**.

---

Une **méthode** est une fonction définie à l'intérieur d'une classe. Les méthodes décrivent le comportement d'un objet :

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

On appelle une méthode sur un objet avec la notation pointée : `dog.speak()`.

---

`this` fait référence à l'**instance actuelle** de la classe, c'est-à-dire l'objet sur lequel la méthode a été appelée. À l'intérieur d'une méthode, on peut l'utiliser pour accéder aux propres champs de l'objet :

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Ici, `this.radius` lit le champ `radius` du cercle sur lequel `diameter()` a été appelé. Lorsqu'il n'y a pas d'autre variable portant le même nom, `this.` peut être omis : `radius * 2` fonctionne de la même façon.

---

Dart prend en charge les **constructeurs nommés**, qui permettent de définir d'autres façons de créer un objet. Les constructeurs nommés s'écrivent `ClassName.constructorName` :

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

La partie après les deux-points est la **liste d'initialisation** : elle affecte les champs avant l'exécution du corps du constructeur. On peut alors créer un objet à l'origine avec : `var p = Point.origin();`

---

Un **getter** est une méthode spéciale qui lit une valeur calculée ou privée et ressemble à un accès à une propriété. On le définit avec le mot-clé `get` :

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

On accède à un getter comme à un champ : `circle.area` (sans parenthèses).

La flèche `=> expr` est une forme abrégée d'un corps qui ne fait que renvoyer une valeur : `{ return expr; }`. Elle fonctionne pour les getters ainsi que pour toute fonction ou méthode :

```dart
double half(double n) => n / 2;
```

---

Un **setter** est une méthode spéciale qui permet d'assigner une valeur tout en exécutant une logique de validation. On le définit avec le mot-clé `set` :

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

Le nom du champ est souvent préfixé par `_` pour le marquer comme privé.

---

L'**héritage** permet à une classe (la **sous-classe**) d'étendre une autre classe (la **superclasse**) et de réutiliser ses champs et méthodes. Utilisez le mot-clé `extends` :

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog` hérite de `name` et `speak()` depuis `Animal` et ajoute sa propre méthode `fetch()`. Une classe qui ne déclare aucun constructeur en obtient un par défaut sans paramètres, ce qui permet d'écrire `var dog = Dog();` puis d'appeler à la fois `dog.speak()` et `dog.fetch()`.

---

Lorsque le constructeur d'une sous-classe doit appeler le constructeur de la superclasse, utilisez le mot-clé `super` dans la **liste d'initialisation** :

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)` transmet l'argument `brand` au constructeur de `Vehicle`.

---

La **redéfinition de méthode** permet à une sous-classe de fournir sa propre implémentation d'une méthode qui existe déjà dans la superclasse. Utilisez l'annotation `@override` :

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

L'annotation `@override` indique à Dart (et aux autres développeurs) que vous remplacez intentionnellement la méthode de la superclasse.

---

Une **classe abstraite** est une classe qui ne peut pas être instanciée directement. Elle sert de base définissant un contrat — des méthodes qui doivent être implémentées par les sous-classes. On marque les méthodes abstraites en omettant leur corps :

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

Essayer d'instancier `Shape()` directement provoque une erreur.

---

Les **membres statiques** appartiennent à la classe elle-même plutôt qu'à une instance particulière. On les déclare avec le mot-clé `static` et on y accède directement via la classe :

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

Les champs et méthodes statiques sont partagés par toutes les instances.

---

Un **constructeur factory** utilise le mot-clé `factory` et permet de contrôler la création d'objets — par exemple en renvoyant une instance mise en cache ou un sous-type :

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Chaque appel à `Logger()` renvoie la même instance (patron singleton).
