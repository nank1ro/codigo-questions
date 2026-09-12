Una clase solo puede `extend` una superclase, pero muy a menudo el mismo comportamiento lo necesitan clases que no tienen nada más en común. Un **mixin** es una porción reutilizable de comportamiento que cualquier número de clases puede incorporar.

Se declara uno con la palabra clave **`mixin`**, y una clase lo incorpora con la palabra clave **`with`**:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` no declara ningún miembro propio, y sin embargo todo `Fish` tiene `swim`, porque los miembros del mixin pasan a ser miembros de la clase. Un mixin puede ser usado por tantas clases como quieras, relacionadas o no.

---

El cuerpo de un mixin se parece al cuerpo de una clase: métodos, getters y campos, escritos exactamente igual. La diferencia está en lo que puedes hacer con la declaración en sí.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

El nombre de un mixin también es un **tipo**, así que `Server() is Timestamped` es `true` y una variable puede declararse como `Timestamped t = Server();`. Dos clases sin relación comparten ahora una misma implementación sin que ninguna herede de la otra.

---

Un mixin no se limita a los métodos: también puede declarar **campos**, y cada objeto de cada clase que use el mixin obtiene su propia copia de ellos.

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

Esto es lo que hace que un mixin sea más que una interfaz: aporta tanto los datos como el código que trabaja sobre ellos.

---

Una declaración `mixin` **no** es una clase. Existe solo para mezclarse en otras clases, así que no tiene constructor propio y no puede instanciarse ni extenderse:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

El nombre sigue funcionando como tipo, así que `Team() is Scored` y `Scored s = Team();` son ambos válidos. Un mixin no tiene constructor, así que un campo no anulable debe inicializarse donde se declara (o marcarse `late`), como `int score = 0;` arriba.

---

Un mixin puede declarar un miembro **sin cuerpo**. Ese miembro es abstracto: el mixin lo usa, y la clase que incorpora el mixin tiene que proporcionarlo.

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

El mixin aporta el comportamiento, la clase aporta los datos. Un campo en la clase, como `final String name;`, es suficiente para satisfacer un getter abstracto del mismo nombre.

---

Juntando las piezas, un programa que usa un mixin tiene tres partes: la declaración `mixin`, una o más clases que lo incorporan `with`, y el código que llama al miembro compartido.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Las declaraciones de nivel superior pueden escribirse en cualquier orden en Dart, pero leer un archivo de arriba abajo es más fácil cuando el mixin va antes de las clases que lo usan.

---

Una clase puede usar **varios mixins a la vez**, listados después de `with` y separados por comas. Dart los aplica **de izquierda a derecha**, apilando cada uno sobre el anterior, así que cuando dos mixins declaran el mismo miembro gana el **último** de la lista:

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

Este apilamiento se llama **linearización**: `with A, B` construye la cadena `Object` → `A` → `B` → la propia clase.

---

Como el último mixin gana, el orden de la lista `with` es parte del significado de la clase, no un detalle de estilo. Reordenarla cambia la implementación con la que el objeto acaba:

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

Los miembros que solo un mixin declara nunca compiten: están disponibles sea cual sea el orden. Lee `with X, Y` como "empieza desde `X`, luego deja que `Y` lo sobrescriba".

---

Los mixins y `extends` funcionan juntos. Una clase puede tener una superclase **y** una lista de mixins, y los mixins siempre se aplican **encima de** la superclase:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

La cadena aquí es `Object` → `Document` → `Timestamped` → `Report`. Un miembro se busca empezando por el final de la cadena, así que `Report().header()` encuentra primero la versión de `Timestamped`. Declarar el mismo miembro en la superclase y en un mixin es perfectamente legal: es así como un mixin reemplaza o envuelve el comportamiento heredado.

---

El cuerpo de la clase está al final mismo de la cadena, así que un miembro declarado en la clase **sobrescribe** el mismo miembro que venga de cualquiera de sus mixins. Dentro de la sobrescritura, **`super`** alcanza la versión que el mixin proporcionó:

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

El mixin en sí queda intacto: `Guest` sigue obteniendo el `greet` original. `super.greet()` es lo que permite a `Host` construir sobre el comportamiento compartido en lugar de copiarlo.

---

Algunos comportamientos solo tienen sentido encima de una clase concreta, y necesitan los miembros de esa clase para hacer su trabajo. La cláusula **`on`** declara el requisito:

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

`on Animal` hace dos cosas: permite al mixin usar los miembros de `Animal`, como `name` arriba, y restringe quién puede usar el mixin. `class Rock with Noisy {}` es un error de compilación, porque `Rock` no es un `Animal`.

---

Un mixin con una cláusula `on` lee los miembros de su superclase como si fueran suyos, y eso es lo que lo convierte en un buen sitio para un comportamiento que decora un tipo existente:

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

`Square` sobrescribe `kind`, y `show` recoge la sobrescritura automáticamente: el mixin siempre llama al miembro sobre el objeto real.

---

Una vez que un mixin tiene una cláusula `on`, puede **sobrescribir** un miembro de ese tipo y llamar a **`super`** para alcanzar la versión que está debajo de él en la cadena:

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

`super.log` no es el `log` del propio mixin, es el que está debajo de él, así que no hay recursión infinita. Apila varios mixins así con `with A, B` y cada uno envuelve al anterior: la llamada entra primero en el **último** mixin y baja hasta la superclase.

---

Una declaración `mixin` no puede instanciarse ni extenderse, y una `class` normal no puede usarse después de `with`. Cuando necesitas una única declaración que funcione de **ambas** maneras, escribe **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

Una `mixin class` paga esa flexibilidad con dos restricciones: debe extender `Object`, así que no puede tener cláusula `extends` propia, y no debe declarar un constructor, porque un mixin nunca ejecuta uno.

---

Los mixins, la herencia y las interfaces resuelven tres problemas distintos:

- **`extends`** da a una clase una superclase, para una relación de "es una especie de". Hay una sola plaza, así que debería ir para la relación más fuerte.
- **`with`** añade comportamiento que muchas clases sin relación necesitan. No hay límite, y la implementación se comparte, no se copia.
- **`implements`** promete un conjunto de miembros pero no aporta **ninguna** implementación: cada clase tiene que escribir el cuerpo por sí misma.

Una señal reveladora de que quieres un mixin es un método que de otro modo copiarías en clases que no tienen un padre común natural, como `Duck`, `Plane` y `Kite` necesitando todas el mismo `fly`.

---

Los mixins apilados son la forma de combinar en una sola clase reglas pequeñas e independientes. Cada mixin sobrescribe el mismo miembro, hace su propia parte y llama a `super` para pasarle el trabajo. Como la llamada entra primero en el **último** mixin, el orden de la lista `with` decide qué regla se ejecuta antes que cuál:

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

`class A extends Account with Doubled {}` duplica cada depósito. Añade un segundo mixin después de `Doubled` y será quien reciba el depósito primero, antes de que `Doubled` lo vea.
