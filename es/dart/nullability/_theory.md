Ya sabes cómo declarar una variable con un tipo, como `String name = 'Ada';`. Sin embargo, a veces un valor simplemente **falta**: un usuario sin apodo, una búsqueda que no encuentra nada, un texto que no se puede convertir en un número. Dart representa un valor faltante con `null`.

Desde Dart 2.12 el lenguaje tiene **seguridad nula sólida** (*sound null safety*): un tipo normal como `String` **nunca** puede contener `null`. Intentar asignárselo es un error de compilación, así que el programa ni siquiera se ejecuta:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Para permitir un valor faltante añades un signo de interrogación `?` después del tipo. Un `String?` contiene un `String` o `null`, y al imprimir `null` se muestra la palabra `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Los tipos sin `?` se llaman **no nulos** (*non-nullable*), los tipos con `?` son **nullable**.

---

Una variable nullable declarada **sin valor** empieza siendo `null`, por lo que se puede omitir `= null`:

```dart
int? age;
print(age); // null
```

Una variable no nula no tiene ese valor por defecto: Dart se niega a compilar cualquier código que la lea antes de que se le haya asignado un valor.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Llamar a un método o leer una propiedad sobre `null` provocaría un fallo, así que Dart no te deja hacerlo sobre un valor nullable con el punto habitual:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

El operador de **acceso null-aware** `?.` resuelve esto: si el valor es `null` la expresión completa es `null` y no se evalúa nada más; en caso contrario funciona como un `.` normal:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Como el resultado puede ser `null`, su tipo es nullable: `text?.length` es un `int?`, no un `int`.

---

A menudo un valor faltante debe reemplazarse por un valor **por defecto**. El operador **if-null** `??` devuelve el operando izquierdo cuando no es `null`, y el operando derecho en caso contrario:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` solo reacciona ante `null`: una cadena vacía `''` o el número `0` son valores reales, por lo que se mantienen.

`??` combina bien con `?.`, porque `?.` produce un resultado nullable:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

La gran ventaja de la seguridad nula es que la mayoría de los errores con `null` los encuentra el **compilador**, no tus usuarios. Las reglas hasta ahora:

- un tipo no nulo (`String`, `int`, `List<int>`...) nunca puede ser `null`
- un tipo nullable (`String?`, `int?`, `List<int>?`...) sí puede, y empieza siendo `null` cuando se declara sin valor
- `.` sobre un valor nullable no compila: usa `?.` o proporciona un valor por defecto con `??`

---

El operador de **asignación if-null** `??=` asigna un valor a una variable **solo si** esa variable es actualmente `null`; en caso contrario la deja intacta:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, ya tenía un valor
```

También funciona con las entradas de un mapa, que son nullable porque una clave puede faltar:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // añadido
stock['apple'] ??= 9; // ignorado
print(stock); // {apple: 4, pear: 1}
```

---

A veces **tú** sabes que un valor nullable no es `null` en un cierto punto, aunque el compilador no pueda saberlo. El operador de **aserción nula** (*null assertion*) `!` convierte un `String?` en un `String` al prometer que el valor está presente:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Ten cuidado: `!` mueve la comprobación del tiempo de compilación al tiempo de ejecución. Si el valor **es** `null`, el programa lanza un error y se detiene:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Usa `!` con moderación, y solo cuando un `null` allí sería un error de todos modos.

---

Recuerda la diferencia entre los tres operadores que has visto sobre un valor nullable:

- `?.` devuelve `null` cuando el valor es `null`, y nunca lanza un error
- `??` reemplaza `null` por un valor por defecto
- `!` asume que el valor está presente y **lanza un error en tiempo de ejecución** cuando no lo está

Ninguno de ellos es un error de compilación: el compilador confía en tu `!`, y solo el programa en ejecución puede descubrir que la promesa se rompió.

---

Comprobar un valor nullable con `if` es más seguro que `!`, y Dart te lo recompensa. Después de una comprobación como `if (x != null)`, el compilador sabe que `x` no puede ser `null` dentro del bloque, por lo que trata `x` como no nulo allí. Esto se llama **promoción de tipos** (*type promotion*):

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // aquí n es int, no hace falta !
  }
  return 0;
}
```

La promoción también funciona después de un retorno anticipado:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n es int de aquí en adelante
}
```

La promoción se aplica a las **variables locales y los parámetros**, cuyo valor no puede cambiar a tus espaldas entre la comprobación y el uso.

---

La promoción de tipos **no** funciona sobre un **campo** de una clase que puede cambiarse desde fuera, porque entre la comprobación y el uso otro fragmento de código (un getter sobreescrito en una subclase, otro método) podría devolverlo a `null`:

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

La solución estándar es copiar el campo en una **variable local**, que sí se promociona:

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

Un campo no nulo normalmente debe recibir un valor en el constructor. Cuando el valor solo se conoce **más tarde** (después de leer un archivo, abrir una conexión...), puedes marcar el campo `late`: el compilador acepta que falte el inicializador y confía en que asignarás el campo antes de leerlo.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Leer un campo `late` que aún no ha sido asignado lanza un `LateInitializationError` en tiempo de ejecución. Como `!`, `late` cambia una garantía en tiempo de compilación por una comprobación en tiempo de ejecución, así que es una promesa que debes cumplir.

`late` también puede combinarse con un inicializador, que entonces se ejecuta **de forma perezosa**, la primera vez que se lee la variable:

```dart
late String report = buildReport(); // buildReport() se ejecuta solo cuando se usa report
```

---

La nulabilidad determina cómo declaras los **parámetros nombrados**. Un parámetro nombrado con un tipo nullable es opcional: cuando quien lo llama lo omite, simplemente es `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Un parámetro nombrado con un tipo no nullable y sin valor por defecto no tendría ningún valor si se omitiera, así que Dart te exige marcarlo `required`; quien llama debe entonces pasarlo siempre:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

La nulabilidad también se aplica a los **elementos** de una colección. Una `List<int>` nunca contiene `null`, mientras que una `List<int?>` sí puede:

```dart
List<int?> scores = [7, null, 9];
```

Fíjate en la diferencia con `List<int>?`, que es una lista que puede faltar ella misma, pero que, cuando está presente, solo contiene números reales.

Para deshacerte de los elementos `null`, `nonNulls` devuelve un `Iterable` solo con los valores presentes, tipado sin `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` hace lo mismo y también funciona cuando la lista mezcla varios tipos.

---

Muchas funciones de biblioteca usan `null` para indicar que algo **no se pudo hacer**. Convertir una cadena en un número es el ejemplo clásico: `int.parse` lanza un `FormatException` cuando el texto no es un número, mientras que `int.tryParse` devuelve `null` en su lugar y te deja decidir qué hacer:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

El tipo de retorno de `int.tryParse` es `int?`, así que todo lo que has aprendido se aplica: `??` para un valor por defecto, `?.` para encadenar, y una comprobación `if` para promocionar. `double.tryParse` funciona de la misma manera.

---

Dos operadores más tienen una variante null-aware.

La **cascada null-aware** `?..` ejecuta una cadena de operaciones en cascada solo cuando el objeto no es `null`, y las omite todas en caso contrario:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // no pasa nada, numbers sigue siendo null
```

El **spread null-aware** `...?` inserta los elementos de una colección nullable en un literal, sin añadir nada cuando la colección es `null`:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Sin el `?`, `...extra` sobre una `List<int>?` sería un error de compilación.

---

Los datos reales están llenos de huecos: un campo de formulario que queda vacío, una columna que falta en un archivo, una cadena que no es del todo un número. Las herramientas de este capítulo se combinan de forma natural para manejarlos: `nonNulls` para descartar los elementos que faltan, `int.tryParse` para convertir de forma segura, y `??` o una comprobación `if` para lidiar con lo que no se pudo convertir.
