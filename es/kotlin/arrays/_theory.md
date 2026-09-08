Un **array** almacena un número fijo de valores del mismo tipo bajo un único nombre de variable.
Creas uno con `arrayOf`, lees un elemento con corchetes y un **índice** que empieza en `0`, y obtienes el número de elementos con `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
El último elemento está en el índice `size - 1`.

---

`arrayOf(1, 2, 3)` crea un `Array<Int>` donde cada elemento es un objeto boxed (envuelto).
Para tipos primitivos, Kotlin ofrece tipos dedicados y más eficientes como `IntArray`, `DoubleArray` y `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
También puedes construir un array de un tamaño dado con una lambda de **inicialización** que recibe cada índice, o un `IntArray` relleno de ceros:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Cada array tiene dos propiedades útiles para trabajar con índices:
- `indices` es el rango de índices válidos, de `0` al último
- `lastIndex` es el índice del último elemento, es decir, `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Incluso cuando un array se declara con `val`, sus **elementos** se pueden reemplazar asignando a un índice:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Para visitar cada elemento puedes usar un bucle `for` o `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Ten en cuenta que `n` e `it` son copias de solo lectura de los valores y no se pueden reasignar, así que para modificar elementos necesitas su índice.

---

Para comprobar si un array contiene un valor usa `in` o `contains`, ambos devuelven un `Boolean`.
`indexOf` devuelve el índice de la primera aparición, o `-1` cuando el valor no está presente:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Imprimir un array directamente no muestra sus elementos, imprime algo como `[Ljava.lang.String;@1b6d3586`.
Usa `joinToString` para construir una cadena legible, opcionalmente con un separador personalizado (el predeterminado es `", "`), o `contentToString` para obtener los elementos entre corchetes:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Los arrays se pueden ordenar **en el mismo array** o copiar en una nueva colección ordenada:
- `sort()` y `sortDescending()` reordenan el propio array y no devuelven nada
- `reverse()` invierte el orden del propio array
- `sorted()`, `sortedDescending()` y `reversed()` dejan el array intacto y devuelven una nueva `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Los arrays numéricos vienen con funciones de agregación:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` y `min()` lanzan una excepción con un array vacío, usa `maxOrNull()` y `minOrNull()` cuando el array pueda estar vacío.

---

La principal diferencia entre un array y una `MutableList` es que un array tiene un **tamaño fijo**: una vez creado puedes reemplazar sus elementos, pero nunca puedes añadir ni quitar uno, no existe una función `add`.
Expresiones como `nums + 4` no hacen crecer `nums`, construyen un array completamente nuevo:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Prefiere una `MutableList` cuando el número de elementos cambia con el tiempo, y un array cuando se conoce de antemano o cuando necesitas el rendimiento de los tipos primitivos.

---

Los arrays admiten las mismas funciones de transformación que las listas. `filter` conserva los elementos que cumplen una condición y `map` transforma cada elemento.
Ambas devuelven una nueva `List`, no un array:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Como el resultado es una lista, imprimirla directamente muestra sus elementos.

---

Cuando necesitas tanto el índice como el valor mientras iteras, usa `withIndex()` y desestructura cada par, o `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Los arrays y las listas se convierten fácilmente entre sí:
- `toList()` y `toMutableList()` copian un array en una lista
- `toTypedArray()` copia una lista en un `Array<T>`
- `toIntArray()` copia una lista de `Int` en un `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Cada conversión crea una **copia**, así que cambiar el resultado no afecta al original.

---

A diferencia de las listas, dos arrays con los mismos elementos **no** son iguales con `==`: los arrays se comparan por referencia, así que `==` es `true` solo para el mismo objeto de array.
Para comparar el contenido usa `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Como los arrays tienen un tamaño fijo, tomar una parte de uno significa crear un nuevo array:
- `copyOf()` copia todo el array, `copyOf(n)` copia los primeros `n` elementos
- `copyOfRange(from, to)` copia los elementos desde el índice `from` hasta `to` **excluido**
- `sliceArray(range)` copia los elementos en los índices del rango, ambos extremos incluidos
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
