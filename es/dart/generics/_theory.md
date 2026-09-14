Una `List` no solo guarda valores, guarda valores **de un solo tipo**. El tipo se escribe entre corchetes angulares justo después del nombre de la colección:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

Aquí `String` e `int` son **argumentos de tipo**, y un tipo que recibe uno se llama **genérico**. La clase de las listas se escribe una sola vez, y `List<String>` y `List<int>` son dos tipos distintos producidos a partir de ella.

La recompensa es que el compilador sabe qué hay dentro:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first is a String
```

---

`List` no es la única colección genérica. Un `Set` recibe un argumento de tipo, y un `Map` recibe **dos**: uno para las claves y otro para los valores, en ese orden.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Un literal de colección vacío no se puede deducir a partir de su contenido, así que escribes los argumentos de tipo sobre el propio literal:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Una vez conocidos los tipos, todo lo que sacas de la colección ya tiene el tipo correcto: `ages['Ada']` es un `int?`, nunca un valor misterioso.

---

Dart también tiene el tipo `dynamic`, que significa que "todo vale". Una `List<dynamic>` acepta cualquier valor, así que parece más cómoda que una `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

La trampa es que nada se comprueba mientras escribes el código. Cada llamada sobre un valor `dynamic` se resuelve mientras el programa se ejecuta, así que un error tipográfico como `things.first.toUpperCse()` compila felizmente y revienta delante de un usuario.

Los genéricos son la alternativa: un solo trozo de código que funciona con **cualquier** tipo, mientras que cada uso suyo sigue comprobándose con **un** tipo. Ese es el punto entero de este tema.

---

No estás limitado a las clases genéricas que trae Dart: puedes declarar las tuyas. Un **parámetro de tipo** va entre corchetes angulares después del nombre de la clase, y a partir de ahí es un tipo normal dentro del cuerpo:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` es solo un marcador de posición. Se rellena cuando se crea un `Box`, ya sea explícitamente o por inferencia:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inferred from the argument
print(a.value + 1);      // 8, the compiler knows value is an int
```

La letra no importa: `T` es una convención para "tipo", nada más.

---

Una función puede ser genérica por sí sola, sin vivir dentro de una clase genérica. El parámetro de tipo va entre el nombre y la lista de parámetros:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T is String here
print(firstOf([10, 20]));        // 10, T is int here
```

Un solo cuerpo de función, comprobado una vez, reutilizado para cada tipo. El argumento de tipo normalmente se deduce de los argumentos, pero puede escribirse explícitamente cuando la inferencia no tiene nada en que basarse:

```dart
final empty = firstOf<String>(<String>[]); // throws, but the type is clear
```

Los métodos dentro de una clase siguen exactamente la misma regla.

---

Dentro de una clase genérica el parámetro de tipo es visible en todas partes: en los campos, en los parámetros del constructor, en las firmas de los métodos y en los cuerpos de los métodos. Se declara una sola vez, junto al nombre de la clase, y cualquier miembro puede usarlo.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

Crear el objeto es lo que decide el tipo: `Holder<String>('fig')` hace que `item` sea un `String`, `Holder<int>(3)` hace que sea un `int`.

---

Una clase puede declarar más de un parámetro de tipo, separados por comas. `Map<K, V>` es el ejemplo incluido en el lenguaje: un tipo para las claves y otro para los valores.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

El **orden** es parte del tipo: `Entry<String, int>` y `Entry<int, String>` son tipos sin relación, y un valor de uno no puede asignarse al otro. Los parámetros de tipo también pueden reordenarse en un tipo de retorno, que es como un método puede entregar una versión invertida del objeto:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Con la seguridad nula sólida el signo de interrogación puede aparecer en dos lugares distintos, y significan dos cosas distintas:

```dart
Box<int?> a = Box(null); // a box that exists and holds a nullable int
Box<int>? b = null;      // no box at all, but if there is one it holds an int
```

En `Box<int?>` el **argumento de tipo** es nullable, así que `a.value` tiene tipo `int?` y puede ser `null`, mientras que `a` en sí siempre está ahí. En `Box<int>?` la **variable** es nullable, así que `b` puede ser `null` y necesitas `b?.value` o `b!.value` para llegar a su interior.

Un `T` sencillo significa `T extends Object?`, así que un argumento de tipo nullable como `Box<int?>` es perfectamente legal.

---

La diferencia importa en cuanto usas el valor. Sobre un `Box<int?>` accedes al campo con normalidad y luego te ocupas del `null` que hay dentro, mientras que sobre un `Box<int>?` primero tienes que superar la caja ausente:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, the box is there, its content is null

Box<int>? b = null;
print(b?.value ?? 0); // 0, the box itself is missing
```

Escribir `b.value` sobre un `Box<int>?` no compila en absoluto: Dart se niega a leer un campo de algo que puede no existir.

---

Un `T` sin acotar podría ser cualquier cosa, así que dentro del cuerpo solo puedes usar lo que todo objeto tiene. Esto no compila:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Una **cota** lo resuelve. Escribir `T extends num` dice que "`T` solo puede ser un número", y a cambio el cuerpo puede usar todo lo que un `num` ofrece:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

La cota se comprueba en el punto de llamada: `half(4)` y `half(2.5)` están bien, `half('fig')` es un error de compilación. Una cota es una promesa en ambos sentidos, argumentos más estrechos a cambio de más poder dentro.

---

La palabra clave para una cota siempre es `extends`, incluso cuando la cota es una interfaz en lugar de una superclase. No hay `implements` en una lista de parámetros de tipo.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Sin la cota, `a > b` no compilaría: el operador de comparación pertenece a `num`, no a cualquier objeto.

---

Una cota puede mencionar al propio parámetro de tipo. `Comparable<T>` es la interfaz de todo lo que sabe compararse consigo mismo con otros de su mismo tipo, mediante `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // negative: fig comes first
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

Así que `T extends Comparable<T>` se lee como "cualquier tipo que pueda compararse consigo mismo", que es justo lo que necesita una función de ordenamiento o de máximo:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` y `DateTime` la satisfacen directamente. `int` y `double` implementan `Comparable<num>`, así que una lista de números simplemente se compara como `num`.

---

La misma cota funciona igual de bien para el elemento menor: solo cambia el signo de la comparación. `compareTo` devuelve un número negativo cuando el receptor va primero, así que `item.compareTo(best) < 0` significa "este es el menor".

---

Una clase genérica puede tener constructores con nombre y constructores **factory** como cualquier otra clase, y el parámetro de tipo está disponible dentro de ellos. Un constructor factory no crea el objeto por sí mismo: ejecuta un cuerpo y devuelve uno, lo que le permite elegir, reutilizar o construir la instancia de la manera que quiera.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

El argumento de tipo va en la clase, no en el nombre del constructor: `Box<int>.first(...)`. Dentro del factory, `<T>[]` es una `List<T>` vacía real, así que un factory es el lugar natural para construir un valor por defecto para un tipo que aún no conoces.

---

Un parámetro de tipo escrito sin cota no está en absoluto sin acotar: `class Box<T>` es la forma abreviada de `class Box<T extends Object?>`. Por eso `Box<int?>` se acepta, y por eso dentro de la clase nunca puedes asumir que `value` sea no nulo.

Para prohibir argumentos de tipo nullable, acota el parámetro con `Object`:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` es el tipo de todo excepto `null`, así que `T extends Object` se lee como "cualquier cosa, mientras esté realmente ahí".

---

Un `typedef` da un nombre a un tipo, y puede recibir parámetros de tipo propios. La razón habitual es nombrar una familia de tipos de función una sola vez en lugar de deletrearla en cada uso:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` es solo otra forma de escribir `int Function(String)`, así que ambos son intercambiables. La ganancia es legibilidad: un parámetro declarado como `Transform<I, O> transform` dice para qué sirve la función, mientras que `O Function(I)` solo dice cómo es.

Un typedef genérico y una función genérica se combinan de forma natural, con los parámetros de tipo de la propia función rellenando los del typedef.
