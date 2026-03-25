Une **classe** est un modèle pour créer des objets. Elle regroupe des données (champs) et des comportements (méthodes) liés.

En Dart, vous déclarez une classe avec le mot-clé `class` suivi du nom de la classe (par convention, en PascalCase) :

```dart
class Car {
  String brand = 'Toyota';
}
```

Vous créez une **instance** (objet) de la classe ainsi :

```dart
final car = Car();
print(car.brand); // Toyota
```

---

Un **constructeur** est une méthode spéciale qui s'exécute lorsque vous créez une instance d'une classe. Il est utilisé pour initialiser les champs de l'objet.

En Dart, le constructeur le plus simple utilise la **syntaxe abrégée** `this.nomChamp` pour assigner des paramètres directement aux champs :

```dart
class Car {
  String brand;
  Car(this.brand);
}

void main() {
  final car = Car('Toyota');
  print(car.brand); // Toyota
}
```

---

Une **méthode** est une fonction définie à l'intérieur d'une classe. Les méthodes décrivent le comportement d'un objet.

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double area() {
    return 3.14 * radius * radius;
  }
}

void main() {
  final c = Circle(5);
  print(c.area()); // 78.5
}
```

Les méthodes peuvent accéder directement aux champs de l'objet par leur nom (ou via `this.nomChamp`).

---

Un **getter** est une méthode spéciale qui ressemble à une propriété lorsqu'on y accède. Utilisez le mot-clé `get` pour en définir un :

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // accédé comme un champ, pas un appel de méthode
}
```

Les getters sont utiles pour les valeurs calculées dérivées des champs.

---

L'**héritage** permet à une classe de réutiliser les champs et les méthodes d'une autre classe. Utilisez le mot-clé `extends` pour créer une sous-classe (classe enfant) :

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('Meow');
  }
}
```

La classe enfant appelle le constructeur parent avec `super(...)`. L'annotation `@override` indique que la méthode remplace la version du parent.
