> Las computadoras son ideales para tareas repetitivas.

La forma más básica de repetición usa la palabra clave `while`.
Esto repite un bloque siempre que la _expresión booleana_ de control sea verdadera:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
La expresión booleana se evalúa una vez al principio del bucle y
nuevamente antes de cada iteración adicional a través del bloque.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Aquí hemos creado una variable `x`, asignándole el valor inicial de __3__.

Luego usamos la declaración `while` que ejecutará el bloque de código hasta que la condición `x > 0` sea `verdadera`.

Dentro del bloque de código, **NO** debemos omitir agregar la línea `x--`.
Disminuye el valor de `x`, de lo contrario, nuestro bucle será infinito.

---

Analicemos este fragmento de código.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Inicializamos la variable `counter` a __0__.
- __[2]__: La expresión condicional para el _while_ dice: "repite las declaraciones en el cuerpo mientras el contador sea menor que _100_".
- __[3]__: El operador `+=` suma _10_ a `counter` y asigna el resultado a `counter` en una sola operación.

La salida del código anterior es _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Hay una segunda forma de usar _while_, en conjunción con la palabra clave `do`.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
Como puedes ver, el `do-while` es bastante similar al bucle `while`, excepto por una diferencia importante:
> el cuerpo del bucle se ejecuta una vez antes de que la condición se evalúe.

En otras palabras, el cuerpo del `do-while` siempre se ejecuta al menos una vez, incluso si la expresión de condición inicialmente produce `false`.

En contraste, el cuerpo de un bucle `while` nunca se ejecutará si la condición produce `false` la primera vez.

---

El bucle _while_ admite las tres expresiones de salto estructural:
- `break` termina el bucle envolvente más cercano.
- `continue` procede al siguiente paso del bucle envolvente más cercano.
- `return` por defecto retorna desde la función envolvente más cercana o función anónima (_lo veremos más tarde cuando hablemos de funciones_).

Aquí hay un ejemplo del uso de `continue` dentro de un bucle _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

Como puedes ver en __[1]__ cuando `i` es igual a _2_, omitimos y _continuamos_ al siguiente paso. De hecho, el número 2 nunca se imprime.

---

Aquí hay un ejemplo del uso de `break` dentro de un bucle _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

Como puedes ver en __[1]__ cuando `i` es igual a _2_, _rompemos_ el bucle. De hecho, los números 2 y 3 nunca se imprimen.
