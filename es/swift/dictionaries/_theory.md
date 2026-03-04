Los **diccionarios** son similares a los arrays y tuplas, pero accedes a los valores buscando una *clave* en lugar de un índice
Una clave puede ser cualquier cadena o número.
Los diccionarios se encierran entre corchetes, así:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
Este es un diccionario llamado `dictionaryName` con tres *pares clave-valor*.
La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.

---

Acceder a valores de diccionario por clave es como acceder a valores de array por índice:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Como Arrays, los Dictionaries son _mutables_.
Esto significa que pueden ser cambiados después de ser creados (si no están declarados como constantes).
Una ventaja de esto es que podemos agregar nuevos _pares clave/valor_ al diccionario después de que es creado así:
```swift
dictName[newKeyName] = newValue
```

---

La longitud `count` de un diccionario es el número de _pares clave-valor_ que tiene.
Cada par cuenta solo una vez, incluso si el valor es un array. (¡Así es: ¡también puedes poner arrays dentro de diccionarios!)

---

Porque los diccionarios son mutables, pueden ser cambiados de muchas formas. Los elementos pueden ser removidos de un diccionario con el método `removeValue(forKey:)`:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
eliminará la clave `keyName` y su valor asociado del diccionario.

---

¿Y si queremos listar todas las claves del diccionario?
Bueno, existe la propiedad `keys`.

---

¿Y si queremos listar todos los valores del diccionario?
Bueno, existe la propiedad `values`.

---

Como con los arrays, podemos recorrer los elementos del diccionario usando las palabras clave `for..in`.
Para obtener tanto la clave como el valor en el bucle no tenemos que especificar ninguna propiedad:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

También podemos usar la propiedad `isEmpty` que usamos con arrays para determinar si un diccionario está vacío

---

Para __agregar__ o __cambiar__ valores a un diccionario, también podemos usar el método `updateValue(_:forKey:)`

---

Anteriormente vimos cómo eliminar un _par clave-valor_ del diccionario con el método `removeValue()`.
También podemos eliminar un elemento asignando a la clave el valor `nil`
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
