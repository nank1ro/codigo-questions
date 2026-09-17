Un **Set** (conjunto) es una colección que almacena valores del mismo tipo sin un orden definido y, lo más importante, **sin duplicados**: cada valor aparece como máximo una vez.
Los sets son perfectos cuando solo te importa *qué* valores están presentes, no cuántas veces ni en qué posición.
Declaras un set con el tipo `Set<Element>` y un literal al estilo de un array:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
La anotación de tipo es obligatoria: sin ella, Swift crearía un array.
Si el literal contiene un valor más de una vez, el set conserva solo una copia:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
La propiedad `count` indica cuántos valores distintos contiene el set.

---

Al igual que los arrays, los sets pueden ser constantes (`let`) o variables (`var`). Solo un set `var` puede modificarse después de ser creado.
Para crear un set vacío, llamas al inicializador del tipo, porque un literal vacío `[]` por sí solo no le indicaría a Swift qué tipo de elemento usar:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
La propiedad `isEmpty` es `true` cuando el set no tiene elementos, igual que con los arrays.

---

Como un set nunca almacena el mismo valor dos veces, su `count` es el número de valores *distintos*, sin importar cuántas veces se haya escrito cada uno en el literal.

---

Para comprobar si un valor está en un set, usa el método `contains(_:)`, que devuelve un `Bool`:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
Esta comprobación es muy rápida en un set, incluso con miles de elementos, lo que es una de las principales razones para preferir un set sobre un array en pruebas de pertenencia.

---

Un set `var` puede modificarse con `insert(_:)` y `remove(_:)`:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 ya está ahí: nada cambia
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 no está ahí: nada cambia
```
Insertar un valor que ya está presente no tiene efecto, y eliminar un valor que no está presente no provoca un error.
`remove(_:)` devuelve el valor eliminado como un opcional (`nil` cuando no se eliminó nada), por lo que puedes comprobar si la eliminación realmente ocurrió.
Para vaciar un set por completo, llama a `removeAll()`.

---

Puedes recorrer un set con `for`-`in`, pero recuerda que un set **no tiene un orden definido**: los elementos pueden salir en cualquier orden, y ese orden puede cambiar entre ejecuciones.
Cuando el orden importa, llama primero a `sorted()`: devuelve un nuevo **array** con los elementos en orden ascendente, dejando el set sin modificar.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 en líneas separadas
}
```

---

Los sets admiten las operaciones clásicas de la teoría de conjuntos. Cada una devuelve un **nuevo** set y deja los originales sin cambios:
- `a.union(b)` contiene todos los elementos que están en `a`, en `b`, o en ambos
- `a.intersection(b)` contiene solo los elementos que están en **ambos**, `a` y `b`
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

Dos operaciones más completan la familia:
- `a.subtracting(b)` contiene los elementos de `a` que **no** están en `b`
- `a.symmetricDifference(b)` contiene los elementos que están en `a` o en `b`, pero **no en ambos**
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
A diferencia de `union` e `intersection`, `subtracting` no es simétrica: `a.subtracting(b)` y `b.subtracting(a)` suelen ser diferentes.

---

Los sets también pueden compararse entre sí. Estos métodos devuelven un `Bool`:
- `a.isSubset(of: b)` es `true` cuando cada elemento de `a` también está en `b`
- `a.isSuperset(of: b)` es `true` cuando `a` contiene cada elemento de `b`
- `a.isDisjoint(with: b)` es `true` cuando `a` y `b` no tienen ningún elemento en común
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

Los sets y los arrays se convierten fácilmente entre sí.
Pasar un array a `Set(...)` crea un set a partir de sus elementos, lo cual es la forma más rápida de **eliminar duplicados**:
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} en algún orden
```
Pasar un set a `Array(...)` devuelve un array, pero como un set no tiene orden, los elementos salen en una secuencia impredecible.
Por eso, cuando necesitas un resultado ordenado, normalmente llamas a `sorted()` sobre el set, que ya devuelve un array:
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
