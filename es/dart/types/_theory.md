Los tipos te permiten categorizar los diferentes tipos de datos que usas en tu código.
En Dart, un __tipo__ es una forma de decirle al compilador cómo vas a usar un dato determinado.
Aquí tienes un ejemplo de los tipos que Dart soporta:
- int
- String
- double
- dynamic
- num

Dart soporta muchos otros tipos. Estos listados son los principales que usarás.

---

Está bien si defines explícitamente el tipo de una variable, por ejemplo:
```dart
int enteroNumero = 2;
double decimalNumero = 3.14;
```

---

Las variables con tipo explícito también pueden ser constantes, solo agrega la palabra clave `const` o `final` antes del tipo:
```dart
const int enteroNumero = 2;
final double decimalNumero = 3.14;
```

> Nota: Los datos mutables te permiten cambiarlos cuando quieras de manera fácil. Sin embargo, muchos programadores experimentados aprecian los beneficios de los datos inmutables. Cuando un valor es inmutable, puedes confiar en que nadie podrá cambiar el valor después de que lo crees. Limitar tus datos de esta manera previene muchos errores difíciles de encontrar y hace que el programa sea más fácil de entender y probar.

---

Aunque es posible anotar el tipo de una variable, esto es redundante. Sabes que `10` es de tipo `int` y `3.14` es de tipo `double`. El compilador de Dart puede inferirlo gracias a la __inferencia de tipos__. No todos los lenguajes de programación tienen _inferencia de tipos_, y esto hace que Dart sea un lenguaje de programación muy potente.

Simplemente puedes eliminar el tipo de las variables, por ejemplo:
```dart
const numeroEntero = 2;
final numeroDecimal = 3.14;
```

Cuando el tipo de una variable no se anota explícitamente, Dart tratará de inferir su tipo.

---

Aunque es posible notar el tipo de una variable, esto es redundante. Sabes que `10` es de tipo `int` y `3.14` es de tipo `double`. El compilador de Dart puede inferirlo gracias a la __inferencia de tipos__. No todos los lenguajes de programación tienen _inferencia de tipos_, y esto hace que Dart sea un lenguaje de programación muy potente.

Simplemente puedes eliminar el tipo de las variables, por ejemplo:
```dart
const enteroNumero = 2;
final decimalNumero = 3.14;
```

Cuando el tipo de una variable no se nota explícitamente, Dart intentará inferir su tipo.

---

La palabra clave `is` te permite verificar si una variable es del tipo que defines. Pero también puedes verificar si una variable no es del tipo definido con la palabra clave `is!`
```dart
final numero = 3.14;
print(numero is! int); // true
```

---

Otra opción que tienes para ver el tipo de una variable de _tiempo de ejecución_ es usar la propiedad `runtimeType` que está disponible para todos los tipos.
```dart
final numero = 3.14;
print(numero.runtimeType); // double
```

---

A veces te encontrarás en la situación de tener un tipo, pero necesitar convertirlo a otro. Podrías sentirte tentado a hacer:

```dart
var entero = 5;
var decimal = 3.14;
entero = decimal;
```

Pero Dart se quejará y te dará el error:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Algunos lenguajes de programación no son tan restrictivos y convertirán silenciosamente. La experiencia demuestra que este tipo de conversión implícita silenciosa es una fuente frecuente de errores y problemas de rendimiento. Dart ha deshabilitado esta característica para evitar estos problemas.

Recuerda, las computadoras dependen de los programadores para descubrir qué hacer. En Dart esto incluye ser explícito sobre el tipo de conversión.

En lugar de esperar una conversión implícita de Dart, necesitas decir explícitamente que quieres que Dart convierta el tipo por ti. Así es como convertir un número `double` a uno `int`:
```dart
var entero = decimal.toInt();
```

La asignación le dice a Dart, inequívocamente, que quieres convertir del tipo original `double` al nuevo tipo `double`.

> NOTAS: En este caso, asignar un valor decimal a un entero pierde precisión. La variable `entero` tiene el valor __3__ en lugar de __3.14__. Es por eso que es importante ser explícito. Dart quiere estar seguro de lo que estás haciendo y te informa que perderás información al convertir.

---

Hasta ahora hemos visto los operadores usados independientemente en enteros o decimales. ¿Qué sucede si tienes un entero y necesitas multiplicarlo con un número decimal? Veamos un ejemplo:
```dart
const radio = 5;
const pi = 3.14;
const circunferencia = 2 * pi * radio;
```

`radio` es de tipo `int` mientras que `pi` es de tipo `double`. ¿Cuál será el tipo de `circunferencia`? Dart asignará el tipo `double` a la variable `circunferencia`. Esta es la opción más segura ya que si la hubiera hecho de tipo `int` podría haber causado una pérdida de precisión.

Si quieres un `int` como resultado, tienes que hacer la conversión explícitamente:
```dart
const circunferencia = (2 * pi * radio).toInt();
```

Los paréntesis le dicen a Dart que multiplique primero, y luego tome el resultado y lo convierta a un valor entero. Desafortunadamente, el analizador no gustará de este código:
 > Const variables must be initialized with a constant value.

El problema es que el método `toInt` es un método solo de tiempo de ejecución. Esto significa que la variable `circunferencia` no puede determinarse en tiempo de compilación, por lo que no es posible que la variable sea constante. Para corregirlo, reemplaza `const` con `final`:

```dart
final circunferencia = (2 * pi * radio).toInt();
```

Ahora `circunferencia` es una variable __constante de tiempo de ejecución__ de tipo `int`.
