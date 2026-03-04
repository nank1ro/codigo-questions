Las listas son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.
Una lista almacena múltiples valores de uno o más tipos e utiliza **índices** para distinguir estos valores.
Puedes asignar elementos a una lista con una expresión de la forma:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` representa el tipo de los elementos dentro de la lista, por ejemplo, puede ser `Int`, `String`, `Any`...

---

Una lista es una colección de elementos con un orden específico. Hay dos tipos de listas en Kotlin:

- `List` no puede ser modificada después de crearla.
- `MutableList` puede ser modificada después de crearla, lo que significa que puedes añadir, eliminar o actualizar sus elementos.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ lanza un Error porque las `List`s son _de solo lectura_.

Para crear una lista modificable usa la palabra clave `mutableListOf`
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

Puedes acceder a un elemento individual de la lista por su índice.
Un índice es como una dirección que identifica el lugar del elemento en la lista.
El índice aparece directamente después del nombre de la lista, entre corchetes, así:
```kotlin
listName[index]
```

Los índices de las listas comienzan en `0`, ¡**no** en `1`! Accedes al primer elemento de una lista así: `listName[0]` o `listName.get(0)` o incluso `listName.first()`.
El segundo elemento en una lista está en el índice __1__: `listName[1]`.

---

El índice es realmente un desplazamiento desde el primer elemento. Por ejemplo, cuando dices `list[2]` no estás pidiendo el segundo elemento de la lista, sino el elemento que está 2 posiciones desplazado desde el primer elemento. Por lo tanto `list[0]` es el primer elemento (desplazamiento cero), `list[1]` es el segundo elemento (desplazamiento de 1), `list[2]` es el tercer elemento (desplazamiento de 2), y así sucesivamente.

Un índice de lista se puede usar tanto para acceder como para asignar valores.
Viste cómo acceder a un índice de lista así:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
Así es como funciona una asignación:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

Al igual que las cadenas, las listas tienen una **longitud** obtenida con el getter `size`.
La longitud de una lista es el número de elementos que contiene

---

Otra operación útil de lista es el método `contains` para averiguar si un elemento dado está en la lista.
Por ejemplo, si tienes una lista de nombres, puedes usar el método `contains` para averiguar si un nombre dado está presente en la lista.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

Una lista mutable no tiene que tener una longitud fija.
¡Puedes añadir elementos al final de una lista en cualquier momento!
Para añadir un elemento a una lista mutable usamos la función `add` o el atajo `+=`:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

Como vimos en el ejemplo anterior, podemos añadir elementos uno por uno usando la función `add`.
Pero si tenemos que añadir todos los elementos de otra lista a la vez podemos simplemente usar la función `addAll`, o el atajo `+=`:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

A veces, solo quieres acceder a una parte de una lista.
Considera el siguiente código:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: primero, creamos una lista de _solo lectura_ llamada `numbers`.
__[2]__: luego, tomamos una subsección de la lista usando la función `slice` y la almacenamos en la lista slice.
Lo hacemos definiendo los índices que queremos incluir dentro de la función `slide`.

En Kotlin podemos incluir el último índice usando `..`, pero también podemos excluir el último índice usando `until`

---

Los elementos de las listas pueden ser de cualquier tipo, si especificamos el tipo `Any`:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
De hecho, arriba tenemos, en orden, un `String`, un `Integer` y un `Boolean`.
¡Pero también podemos tener listas con listas!

---

A veces necesitas buscar un elemento en una lista.
En Kotlin podemos usar el método `indexOfFirst`:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

El método `indexOfFirst` toma una función __predicado__ que será evaluada para cada elemento en la lista hasta que sea verdadera, devolviendo el _índice_ del elemento.
El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.

También podemos insertar elementos en una lista modificable en un índice específico, usando el método `add(index, element)`:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
El código anterior inserta `"Ali"` en el índice `1`, lo que mueve todo lo que viene después de este índice, un lugar hacia abajo

---

En Kotlin podemos recorrer una lista de una forma muy simple usando las palabras clave `for..in`:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
Un nombre de variable sigue a la palabra clave `for`, se le asignará el valor de cada elemento de la lista a su vez.
