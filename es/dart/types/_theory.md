Los tipos te permiten categorizar todos los diferentes tipos de datos que usas en tu código.
En Dart, un __tipo__ es una forma de decirle al compilador cómo vas a usar un dato en particular.
Aquí hay un ejemplo de tipos que Dart soporta:
- int
- String
- double
- dynamic
- num

Dart soporta muchos otros tipos. Los enumerados son los principales que usarás.

---

Está bien si explícitamente defines el tipo de una variable, por ejemplo:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Las variables con tipo explícito también pueden ser constantes, simplemente agrega la palabra clave `const` o `final` antes del tipo:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Nota: Los datos mutables te permiten cambiarlos cuando quieras de manera fácil. Sin embargo, muchos programadores experimentados aprecian los beneficios de los datos inmutables. Cuando un valor es inmutable, puedes confiar en que nadie podrá cambiar el valor después de que lo crees. Limitar tus datos de esta manera previene muchos bugs difíciles de encontrar y hace que el programa sea más fácil de pensar y probar.

---

Aunque es posible anotar el tipo de una variable, esto es redundante. Sabes que `10` es de tipo `int` y `3.14` es de tipo `double`. El compilador de Dart puede inferirlo gracias a __type inference__. No todos los lenguajes de programación tienen _type inference_, y esto hace que Dart sea un lenguaje de programación muy poderoso.

Simplemente puedes eliminar el tipo de las variables, por ejemplo:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

Cuando el tipo de una variable no se anota explícitamente, Dart intentará inferir su tipo.

---

Hay una forma programática de verificar el tipo de una variable, es decir, con la palabra clave `is`:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

Como puedes ver, Dart ha asignado el tipo `double` a la variable `number`.

---

La palabra clave `is` te permite verificar si una variable es del tipo que defines. Pero también puedes verificar si una variable no es del tipo definido con la palabra clave `is!`
```dart
final number = 3.14;
print(number is! int); // true
```

---

Otra opción que tienes para ver el tipo de una variable de _runtime_ es usar la propiedad `runtimeType` que está disponible para todos los tipos.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

A veces te encontrarás en la situación de tener un tipo, pero necesitando convertirlo a otro. Podrías ser tentado a hacer:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

Pero Dart se quejará y te dará el error:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Algunos lenguajes de programación no son tan restrictivos y se convertirán silenciosamente. La experiencia muestra que este tipo de conversión implícita silenciosa es una fuente frecuente de bugs y problemas de rendimiento. Dart ha deshabilitado esta función para evitar estos problemas.

Recuerda, las computadoras dependen de los programadores para averiguar qué hacer. En Dart esto incluye ser explícito sobre el tipo de conversión.

En lugar de esperar una conversión implícita de Dart, necesitas decir explícitamente que quieres que Dart convierta el tipo para ti. Aquí está cómo convertir un número `double` a uno `int`:
```dart
var integer = decimal.toInt();
```

La asignación le dice a Dart, inequívocamente, que quieres convertir del tipo original `double` al nuevo tipo `double`.

> NOTAS: En este caso, asignar un valor decimal a un entero pierde precisión. La variable `integer` tiene el valor __3__ en lugar de __3.14__. Por eso es importante ser explícito. Dart quiere estar seguro de lo que estás haciendo y te hace saber que perderás información al convertir.

---

Hasta ahora hemos visto los operadores utilizados independientemente en enteros o decimales. ¿Y si tienes un entero y necesitas multiplicarlo por un número decimal? Veamos un ejemplo:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` es de tipo `int` mientras que `pi` es de tipo `double`. ¿Cuál será el tipo de `circumference`? Dart asignará el tipo `double` a la variable `circumference`. Esta es la opción más segura ya que si lo hubiera hecho de tipo `int` podría haber causado una pérdida de precisión.

Si quieres un `int` como resultado, tienes que hacer la conversión explícitamente:
```dart
const circumference = (2 * pi * radius).toInt();
```

Los paréntesis le dicen a Dart que multiplique primero, y luego tome el resultado y lo convierta a un valor entero. Desafortunadamente, el analizador no le gustará este código:
 > Const variables must be initialized with a constant value.

El problema es que el método `toInt` es un método de solo tiempo de ejecución. Esto significa que la variable `circumference` no se puede determinar en tiempo de compilación, por lo que no es posible que la variable sea constante. Para corregir reemplaza `const` con `final`:

```dart
final circumference = (2 * pi * radius).toInt();
```

Ahora `circumference` es una variable de __constante de tiempo de ejecución__ de tipo `int`.

---

A veces podrías tener una variable con un tipo genérico, pero necesitas funcionalidad que solo existe en un subtipo. Si estás seguro de que el tipo de la variable es el subtipo que necesitas, entonces puedes usar la palabra clave `as` para cambiar su tipo. Este procedimiento también se conoce como __type casting__, aquí hay un ejemplo:

```dart
num number = 3;
```

Digamos que queremos comprobar si el número es par, y la funcionalidad en cuestión está presente solo en el subtipo `int`.
```dart
print(number.isEven);
```

El código anterior debería darte un error de tipo:
> The getter `isEven` isn't defined for the type 'num'.

El tipo `num` es un tipo demasiado general para saber si un número es par o impar. Solo los números enteros pueden ser pares o impares.
El problema ocurre si `num` contiene un valor `double`, ya que `num` incluye tanto tipos `double` como `int`. En este caso, estamos seguros de que __3__ es un número entero, así que podemos hacer un cast a `int`

```dart
final integer = number as int;
print(integer.isEven); // false
```

La palabra clave `as` hace que el compilador reconozca la variable `integer` como si tuviera el tipo `int`. Esto te permite usar la propiedad `isEven` que está presente en números enteros. Dado que el número __3__ no es un número entero, el resultado es falso.

Debes tener cuidado al hacer un cast. Si haces un cast incorrecto del tipo obtendrás un error en tiempo de ejecución:
```dart
num numero = 3;
final decimale = numero as double;
```

Esto bloqueará el programa con el siguiente error:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

El tipo en tiempo de ejecución de `number` es `int` y no `double`. En Dart, no puedes hacer un cast con tipos del mismo nivel, como `int` y `double`. Solo puedes hacer un cast de subtipos.
