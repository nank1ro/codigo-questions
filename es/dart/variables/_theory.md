Las variables son contenedores para almacenar valores.
Cada variable en Dart es un objeto (`Object`).
Para crear una variable, tenemos que darle un __nombre__ teniendo en cuenta que no debe contener espacios.
Echa un vistazo a lo siguiente:

```dart
int number = 1;
```

Esta sentencia declara una variable llamada `number` de tipo `int`.
Luego establece el valor de la variable en número `1`.
La parte `int` de la declaración se conoce como __anotación de tipo__, e indica explícitamente a Dart el tipo de la variable.

---

En el ejemplo anterior, vimos la creación de una variable:

```dart
int number = 1;
```

No te dejes engañar por el símbolo `=`.
No es el símbolo de igualdad como en matemáticas, sino que se conoce como el __operador de asignación__ porque asigna un valor a la variable.
El signo de igualdad, por otro lado, es `==`.

---

Si deseas cambiar el valor de una variable, simplemente asígnale un valor diferente del mismo tipo:

```dart
int number = 1;
number = 2;
```

---

El tipo `int` permite almacenar números enteros.
Para guardar números decimales en su lugar, podemos usar el tipo `double`:

```dart
double pi = 3.14159;
```

Este ejemplo es similar al anterior. Sin embargo, esta vez, la variable es de tipo `double`, un tipo que permite almacenar números decimales con alta precisión.

---

Dart es un lenguaje __type-safe__ (seguro de tipos).
Esto significa que cuando asignas un tipo a una variable, no puedes cambiarlo después. Aquí hay un ejemplo:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

3.14159` es de tipo `double`, pero ya has definido `integerNumber` con tipo `int`.

Por supuesto, ocasionalmente puede ser útil asignar tipos relacionados a la misma variable. Por ejemplo, podrías querer una variable `integerNumber` que acepte tanto números `int` como `double`, como aquí:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Tanto `int` como `double` extienden `num`, por lo que ambos tipos se aceptan.
Sin embargo, si intentamos asignar una `String` el compilador devuelve un error.

---

Si te gusta vivir con riesgo, podemos ignorar completamente la __seguridad de tipos__ del lenguaje usando el tipo `dynamic`.
Esto te permite asignar cualquier tipo de valor a la variable.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

Este enfoque está fuertemente desaconsejado porque los errores ya no son interceptados por el _analizador_ del código, sino solo en _runtime_ (cuando el programa se está ejecutando).

---

Dart soporta __inferencia de tipos__.
No es necesario indicar el tipo de una variable ya que Dart puede inferir su tipo.
La palabra clave `var` le dice a Dart que use el tipo más apropiado.

```dart
var number = 5;
```

No es necesario decirle a Dart que el número `5` es de tipo `int`.
Dart infiere el tipo y hace que `number` sea de tipo `int`.

---

Dart soporta dos tipos diferentes de "_variables_" cuyo valor nunca cambia. Se declaran con las palabras clave `const` y `final`.
Comencemos viendo qué se entiende por `const`.

## const (constantes)

Las variables cuyo valor puedes cambiar se conocen como __datos mutables__. Los datos mutables se usan a menudo en exceso y pueden presentar problemas. Es fácil perder de vista todos los puntos en el código que pueden cambiar el valor de una variable.

Por esta razón, debes usar `const`antes en lugar de `var`iables siempre que sea posible. Estas variables que no pueden cambiar de valor también se llaman __datos inmutables__.

Para crear una constante en Dart usamos la palabra clave `const`:

```dart
const number = 5;
```

Al igual que `var`, Dart con la __inferencia de tipos__ determina que `number` es de tipo `int`.

---

Cuando has declarado una variable constante, ya no puedes cambiar su valor. Por ejemplo:

```dart
const number = 2;
number = 3; // Error
```

Este código produce el error:
> Constant variables can't be assigned a value.

Es decir, no es posible cambiar el valor de una variable constante.

---

A menudo te encontrarás en la situación de querer usar una constante pero sin conocer el valor en el momento de la compilación. Solo conocerás el valor después de que el programa haya comenzado a ejecutarse.
Este tipo de constante se conoce como __constante de tiempo de ejecución__.

En Dart `const` se usa solo para __constantes de tiempo de compilación__ para valores que el compilador puede determinar antes de que se ejecute el programa.

Si no puedes crear una variable constante porque no conoces su valor en tiempo de compilación, entonces debes usar la palabra clave `final` para que la variable sea una __constante de tiempo de ejecución__.

Hay muchas razones por las que no puedes conocer el valor de una variable antes de ejecutar el programa. Por ejemplo, tendrías que obtener el valor del servidor o pedírselo al usuario.

---

Aquí hay un ejemplo de un valor que solo se puede obtener en tiempo de ejecución:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` es una función para obtener la fecha y hora actual de cuando se ejecuta el código.
Con el campo `hour` accedemos al número de horas que han pasado desde el inicio del día.

Dado que el valor de `hour` es diferente dependiendo de cuándo se ejecute el código, esto se puede definir como el valor _runtime_.

Si intentas cambiar el valor de una variable `final`, obtienes un error.
