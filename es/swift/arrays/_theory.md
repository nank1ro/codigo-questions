Los arrays son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un único nombre de variable.
Un array almacena múltiples valores de uno o múltiples tipos y usa **índices** para distinguir estos valores.
Puedes asignar elementos a un array con una expresión de la forma:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` representa el tipo de elementos dentro del array, por ejemplo, puede ser `Int`, `String`, `Any`...

---

Puedes acceder a un elemento individual del array por su índice.
Un índice es como una dirección que identifica la posición del elemento en el array.
El índice aparece directamente después del nombre del array, entre corchetes, así:
```swift
arrayName[index]
```

Los índices del array comienzan en `0`, **¡no** en `1`! Accedes al primer elemento de un array así: `arrayName[0]`.
El segundo elemento en un array está en el índice 1: `arrayName[1]`.

---

Un índice de array se comporta como cualquier otro nombre de variable.
Puede usarse para acceder así como para asignar valores.
Viste cómo acceder a un índice de array así:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
Así es como funciona una asignación:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

Al igual que las cadenas, los arrays tienen una **longitud** `count`.
La longitud de un array es el número de elementos que contiene

---

Un array no tiene que tener una longitud fija.
¡Puedes agregar elementos al final de un array cuando quieras!
Para agregar un elemento a un array utilizamos la función `append`:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

A veces, solo quieres acceder a una parte de un array.
Considera el siguiente código:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
Primero, creamos un array llamado `numbers`.
Luego, tomamos una subsección del array y la almacenamos en el array slice.
Lo hacemos definiendo los índices que queremos incluir después del nombre del array: `numbers[1...2]`.
En Swift podemos incluir el último índice usando `...`, pero también podemos excluir el último índice usando `..<`

---

¡En Swift podemos dividir un array como queramos!
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
Si tu división de array incluye el primer o último elemento en un array, el índice de ese elemento no tiene que incluirse

---

Los elementos del array pueden ser de cualquier tipo, si especificamos el tipo `Any`:
```swift
var arrayName: [Any] = ["one", 2, true]
```
De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.
¡Pero también podemos tener arrays con arrays!

---

A veces necesitas buscar un elemento en un array.
En Swift podemos usar el método `firstIndex()`:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.
También podemos insertar elementos en un array en un índice específico, usando el método `insert()`:
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
El código anterior inserta `"Ali"` en el índice `1`, lo que mueve todo después de este índice una posición hacia abajo

---

En Swift podemos recorrer un array de una manera muy simple usando las palabras clave `for..in`:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
Un nombre de variable sigue a la palabra clave `for`, se le asignará el valor de cada elemento del array a su vez.

---

Las **tuplas** son como arrays pero puedes nombrar los elementos y usar esos nombres para referirte a ellos
Para crear una tupla usamos los paréntesis `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
