Los `Set`s son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.
La principal diferencia con las `List`s es que un `Set` permite solo un elemento de cada valor.

Al igual que las `List`s, un `Set` almacena múltiples valores de uno o más tipos e utiliza **índices** para distinguir estos valores.
Puedes asignar elementos a un conjunto con una expresión de la forma:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` representa el tipo de los elementos dentro del conjunto, por ejemplo, puede ser `Int`, `String`, `Any`...

---

Un `Set` es una colección de elementos __únicos__ sin un orden específico.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

En __[1]__ estamos intentando crear un conjunto con el número __1__ presente dos veces pero como puedes ver cada elemento debe ser único y el segundo __1__ es automáticamente descartado.

---

Hay dos tipos de `Set`s en Kotlin:

- `Set` no puede ser modificado después de crearlo.
- `MutableSet` puede ser modificado después de crearlo, lo que significa que puedes añadir, eliminar o actualizar sus elementos.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ lanza un Error porque los `Set`s son de _solo lectura_.

Para crear un conjunto modificable usa la palabra clave `mutableSetOf`
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

La actividad más común de `Set` es probar la pertenencia usando `in` o `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

Como puedes ver arriba, `in` y `contains` devuelven un `Bool` diciendo si el elemento pasado está presente en el conjunto

---

El orden de los elementos en un `Set` no es importante.
De hecho, si intentas comparar dos `Set`s con los mismos elementos pero en diferente orden, obtendrás que son iguales.

---

En los `Set`s puedes realizar varias operaciones como verificar la unión, intersección, diferencia y subconjunto.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

Para convertir un `Set` a una `List` podemos usar la función `toList()`
