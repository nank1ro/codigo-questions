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
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
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
    print(number) // 1, 2, 3 on separate lines
}
```
