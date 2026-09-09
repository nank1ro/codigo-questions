Ya sabes cómo añadir métodos a una clase que has escrito tú mismo. Pero ¿qué pasa con `String`, `int` o `List`, cuyo código vive en el SDK de Dart? No puedes editarlos, y a menudo desearías que tuvieran un método más.

Una **extensión** lo resuelve: añade nuevos miembros a un tipo **existente**, sin tocar su código fuente y sin crear una subclase. La sintaxis es:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

Dentro de la extensión, `this` hace referencia al valor sobre el que se llama al miembro. Una vez declarada la extensión, sus miembros se llaman exactamente igual que los miembros propios del tipo:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Las extensiones se declaran en el **nivel superior** de un archivo, junto a las clases y las funciones, nunca dentro de `main`.

---

Las extensiones funcionan con cualquier tipo, incluidos los números. Esta extensión da a cada `int` un método que lo duplica:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Como la extensión se aplica al **tipo**, puedes llamar al método sobre una variable o directamente sobre un **literal**. Los literales negativos necesitan paréntesis, de lo contrario el punto se lee antes que el signo menos:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Una extensión también puede declarar **getters**, que se leen como propiedades, sin paréntesis. Dentro de una extensión puedes llamar directamente a los miembros propios del tipo: `this.` es opcional, exactamente igual que dentro de una clase.

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

Elige un getter cuando el miembro solo **lee** un valor y no recibe parámetros; elige un método cuando realiza trabajo o necesita argumentos.

---

El tipo después de `on` puede ser un tipo **parametrizado** como `List<int>`. La extensión se aplica entonces solo a listas de ese tipo de elementos: `[1, 2].total()` funciona, `['a', 'b'].total()` no compila.

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

Dentro de la extensión, `this` es la lista, así que puedes recorrerla, indexarla o llamar a `length` como de costumbre.

---

Una extensión sobre `List<int>` no puede usarse en una `List<String>`. Para escribir una única extensión que funcione para **cualquier** tipo de elemento, dale a la extensión un **parámetro de tipo**, escrito entre ángulos después de su nombre, y úsalo en el tipo de la cláusula `on`:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` es un marcador de posición para "el que sea el tipo de elemento": en una `List<int>` se convierte en `int`, en una `List<String>` se convierte en `String`, así que el getter de arriba devuelve un `int` o un `String` en consecuencia. El compilador sustituye `T` por ti en cada llamada.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Una extensión sobre `String` no puede llamarse sobre un `String?`: el valor podría ser `null` y el compilador rechaza la llamada. Si en cambio declaras la extensión sobre el tipo **nullable**, el método puede llamarse directamente sobre un `String?` y, dentro de él, `this` tiene tipo `String?`, así que debes manejar tú mismo el caso `null`, por ejemplo con `??`:

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

Un `int` no nullable puede pasarse donde se espera un `int?`, así que la extensión funciona con ambos.

---

Una extensión puede añadir métodos, getters, setters y operadores, pero **no puede añadir campos de instancia**. Un valor `int` tiene una disposición fija en memoria, y una extensión es solo un conjunto de funciones que el compilador te deja llamar con la sintaxis de punto: no hay sitio para almacenar datos extra por valor.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Los getters y setters de una extensión solo pueden calcular valores a partir de `this` o delegar en miembros existentes: no pueden recordar nada entre llamadas.

---

Una extensión puede declarar miembros **static**. Como en una clase, pertenecen a la propia extensión, no a ningún valor, y se accede a ellos a través del **nombre de la extensión**, no a través del tipo que extiende:

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

Los miembros static son un lugar práctico para constantes y funciones de utilidad relacionadas con el tipo extendido.

---

Las extensiones no son solo para tipos del SDK: también puedes extender **tus propias clases**. Esto es útil cuando la clase viene de un paquete que no controlas, o cuando quieres mantener la clase pequeña y añadir ayudantes opcionales junto al código que los necesita.

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

La extensión ve los campos y métodos públicos de la clase, exactamente igual que el código escrito fuera de la clase.

---

Dart permite a un tipo definir qué significan operadores como `+`, `*` o `==` para sus valores, usando un método cuyo nombre es la palabra clave `operator` seguida del símbolo. El lado derecho del operador es el parámetro del método:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Como las extensiones pueden declarar operadores, puedes dar a un tipo existente un operador nuevo que aún no tenga. `String` tiene `+` y `*`, pero no `-`, así que una extensión puede definir qué significa `'hello world' - 'o'`.

---

¿Qué ocurre si una extensión declara un miembro que el tipo **ya tiene**? El miembro propio del tipo siempre gana: los miembros de una extensión solo se tienen en cuenta cuando el propio tipo no tiene ningún miembro con ese nombre. El miembro de la extensión se ignora silenciosamente, no hay error ni sobrescritura.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Así que una extensión puede añadir miembros y llenar huecos, pero nunca puede **cambiar** el comportamiento de los miembros existentes.

---

El nombre de una extensión es opcional. Una extensión **sin nombre** funciona de la misma manera, pero solo es visible en el archivo que la declara:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

Un **nombre** importa en cuanto dos extensiones ofrecen el mismo miembro sobre el mismo tipo: la llamada se vuelve **ambigua** y no compila. El nombre te permite resolver el conflicto de dos maneras. Cuando las extensiones vienen de archivos diferentes, puedes hacer `show` o `hide` de una de ellas en el import:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

O, en cualquier lugar, puedes aplicar la extensión **explícitamente**, envolviendo el valor con el nombre de la extensión como si fuera un constructor:

```dart
print(Loud('hi').describe());
```

Las extensiones sin nombre no pueden ocultarse ni aplicarse explícitamente, así que prefiere las extensiones con nombre en código que otros importarán.

---

Una extensión genérica puede recibir **funciones** como parámetros, exactamente igual que hacen `where` y `map`. El tipo de la función se escribe con el tipo de elemento `T`, así que el callback recibe elementos del tipo correcto:

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
