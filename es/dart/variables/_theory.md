Las variables son contenedores para almacenar valores.
Cada variable en Dart es un objeto (`Object`).
Para crear una variable, debemos darle un __nombre__ teniendo en cuenta que no debe contener espacios.
Observa lo siguiente:

```dart
int numero = 1;
```

Esta declaración declara una variable llamada `numero` de tipo `int`.
Luego establece el valor de la variable en el numero `1`.
La parte `int` de la declaración se conoce como __anotación de tipo__, y le dice a Dart explícitamente el tipo de la variable.

---

Si deseas cambiar el valor de una variable, simplemente asígnale un valor diferente del mismo tipo:

```dart
int numero = 1;
numero = 2;
```

---

En el ejemplo anterior, vimos la creación de una variable:

```dart
int numero = 1;
```

No te dejes engañar por el símbolo `=`.
No es el símbolo de igualdad como en matemáticas, sino que se conoce como el __operador de asignación__ porque asigna un valor a la variable.
El signo de igualdad, por otro lado, es `==`.

---

Dart es un lenguaje __con seguridad de tipos__.
Esto significa que cuando asignas un tipo a una variable, no puedes cambiarlo después. Aquí tienes un ejemplo:

```dart
int numeroEntero = 1;
numeroEntero = 3.14159; // Error
```

3.14159` es de tipo `double`, pero ya has definido `numeroEntero` con el tipo `int`.

Por supuesto, ocasionalmente podría ser útil asignar tipos relacionados a la misma variable. Por ejemplo, podrías querer una variable `numeroEntero` que acepte tanto números `int` como `double`, así:

```dart
num numero;
numero = 1; // OK
numero = 3.14159; // OK
numero = '10'; // Error
```

Tanto `int` como `double` extienden `num`, por lo que se aceptan ambos tipos.
Sin embargo, si intentamos asignar un `String`, el compilador devuelve un error.

---

Dart admite la __inferencia de tipos__.
No es necesario indicar el tipo de una variable ya que Dart puede inferirlo.
La palabra clave `var` le dice a Dart que use el tipo más apropiado.

```dart
var numero = 5;
```

No es necesario decirle a Dart que el número `5` es de tipo `int`.
Dart infiere el tipo y hace que `numero` sea de tipo `int`.

---

El tipo `int` permite almacenar números enteros.
Para guardar números decimales en su lugar, podemos usar el tipo `double`:

```dart
double pi = 3.14159;
```

Este ejemplo es similar al anterior. Esta vez, sin embargo, la variable es de tipo `double`, un tipo que permite almacenar números decimales con alta precisión.

---

Si te gusta vivir peligrosamente, podemos ignorar por completo la __seguridad de tipos__ del lenguaje usando el tipo `dynamic`.
Esto te permite asignar cualquier tipo de valor a la variable.

```dart
dynamic numero;
numero = 1; // OK
numero = 3.14159; // OK
numero = '10'; // OK
```

Este enfoque está fuertemente desaconsejado ya que los errores ya no son interceptados por el _analizador_ del código, sino solo en _tiempo de ejecución_ (cuando el programa está funcionando).

---

Dart admite dos tipos diferentes de "_variables_" cuyo valor nunca cambia. Se declaran con las palabras clave `const` y `final`.
Comencemos viendo qué significa `const`.

## const (constantes)

Las variables cuyo valor puedes cambiar se conocen como __datos mutables__. Los datos mutables a menudo se usan en exceso y pueden presentar problemas. Es fácil perder el rastro de todos los puntos en el código que pueden cambiar el valor de una variable.

Por esta razón, debes usar `const`antes en lugar de `var`iables siempre que sea posible. Estas variables que no pueden cambiar de valor también se llaman __datos inmutables__.

Para crear una constante en Dart usamos la palabra clave `const`:

```dart
const numero = 5;
```

Al igual que `var`, Dart con la __inferencia de tipos__ determina que `numero` es de tipo `int`.

---

Cuando has declarado una variable constante, ya no puedes cambiar su valor. Por ejemplo:

```dart
const numero = 2;
numero = 3; // Error
```

Este código produce el error:
> Constant variables can't be assigned a value.

Es decir, no es posible cambiar el valor de una variable constante.

---

A menudo te encontrarás en la situación de querer usar una constante pero sin conocer el valor en tiempo de compilación. Solo conocerás el valor después de que el programa haya comenzado su ejecución.
Este tipo de constante se conoce como __constante en tiempo de ejecución__.

En Dart, `const` solo se usa para __constantes en tiempo de compilación__ para valores que pueden ser determinados por el compilador antes de que se ejecute el programa.

Si no puedes crear una variable constante porque no conoces su valor en tiempo de compilación, entonces debes usar la palabra clave `final` para hacer que la variable sea una __constante en tiempo de ejecución__.

Hay muchas razones por las que no puedes conocer el valor de una variable antes de ejecutar el programa. Por ejemplo, tendrías que obtener el valor del servidor, o pedirle al usuario que lo ingrese.

---

A menudo te encontrarás en la situación de querer usar una constante pero sin conocer el valor en tiempo de compilación. Solo conocerás el valor después de que el programa haya comenzado su ejecución.
Este tipo de constante se conoce como una __constante de tiempo de ejecución__.

En Dart, `const` solo se usa para __constantes en tiempo de compilación__ para valores que pueden ser determinados por el compilador antes de que se ejecute el programa.

Si no puedes crear una variable constante porque no conoces su valor en tiempo de compilación, entonces debes usar la palabra clave `final` para hacer que la variable sea una __constante de tiempo de ejecución__.

Hay muchas razones por las que no puedes conocer el valor de una variable antes de ejecutar el programa. Por ejemplo, tendrías que obtener el valor del servidor, o pedirle al usuario que lo ingrese.
