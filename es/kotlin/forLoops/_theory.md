> La palabra clave `for` ejecuta un bloque de código para cada valor en una secuencia.

El bucle `for` itera a través de cualquier cosa que proporcione un iterador.

La sintaxis de `for` es la siguiente:
```kotlin
for (item in collection) print(item)
```

El cuerpo de `for` también puede ser un bloque
```kotlin
for (item in collection) {
    print(item)
}
```

Cada vez que pasa el bucle, `item` recibe el siguiente elemento en los valores.

Aquí hay un bucle `for` repitiendo una acción un número fijo de veces:

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

La salida muestra el índice `i` recibiendo cada valor en el rango del _1_ al _3_.

---

Un _rango_ es un intervalo de valores definido por un par de puntos finales.
Hay dos formas básicas de definir rangos:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ usando la sintaxis `..` incluye ambos límites en el rango resultante.
- __[2]__ `until` excluye el final. La salida muestra que _3_ no es parte del rango.

---

Puedes iterar sobre un rango en orden inverso.

Probablemente esperarías que `3..1` funcione, desafortunadamente, el equipo de Kotlin ha decidido importar esta funcionalidad de una manera diferente.

De hecho, si intentas ejecutar este fragmento de código:
```kotlin
for (i in 3..1) println(i)
```

Verás que no se imprime nada.
Para hacerlo funcionar, tenemos que usar la palabra clave `downTo`:

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` produce un rango decreciente.

---

El _paso_ predeterminado de un rango es __1__, pero puedes establecer explícitamente otro valor.

Puedes definir el __paso__ de tu bucle `for` usando la palabra clave `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

Como puedes ver, el bloque de código se ejecuta con un paso de _2_ en lugar de _1_, cambiando completamente nuestra salida.

---

También puedes producir un rango de _caracteres_.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

Puedes iterar sobre una __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

En el ejemplo anterior, hemos impreso cada carácter + 1, así que `'a'` se convierte en `'b'`, `'b'` se convierte en `'c'` y así sucesivamente.

Esto es posible porque los caracteres se almacenan como números correspondientes a sus [Códigos ASCII](https://en.wikipedia.org/wiki/ASCII).

Por lo tanto, agregar un entero a un carácter produce un nuevo carácter correspondiente al nuevo valor de código.

---

En caso de que simplemente necesites repetir un bloque de código `n` veces, puedes usar la función `repeat(times: Int)`.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

Incluso puedes acceder al índice con
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

En Kotlin también podemos usar el `for-in` para colecciones iterables llamando al cierre dado en cada elemento:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

En Kotlin también tenemos el bucle `forEach`.
Llama al cierre dado en cada elemento en la secuencia en el mismo orden que un bucle `for-in`:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

El uso del método `forEach` se diferencia de un bucle `for-in` de dos formas importantes:
1. Las instrucciones `break` o `continue` no se pueden usar para salir de la llamada actual del cierre del cuerpo o para omitir llamadas posteriores. (_En realidad es posible con anotaciones, pero es un tema más complejo que no veremos ahora._)
2. El uso de la instrucción `return` en el cierre del cuerpo solo saldrá del cierre y no del alcance externo, y no omitirá llamadas posteriores.
