**Dictionaries** son similar un arreglos y tuples, pero you access valores por mirando up un *key* instead de un indice
A clave puede ser cualquier cadena o numero.
Dictionaries son enclosed en square brackets, like asi que:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
This es un dictionary llamo `dictionaryName` con three *key-valor pairs*.
The clave `key1` points un el valor `1`, `key2` un `2`, y asi que on.

---

Accessing dictionary values by key is just like accessing array values by index:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Like Arrays, Dictionaries son _mutable_.
This significa ellos puede ser cambio despues ellos son creo (si son no declared constante).
One advantage de este es ese we puede Anade nuevo _key/valor pairs_ un el dictionary despues lo es creo like asi que:
```swift
dictName[newKeyName] = newValue
```

---

la longitud `conteo` de un dictionary es el numero de _key-valor pairs_ lo tiene.
Each pair counts solo once, even si el valor es un arreglo. (That's right: you puede tambien poner arreglos inside dictionaries!)

---

porque dictionaries son mutable, ellos puede ser cambio en many ways. elementos puede ser removed de un dictionary con el `removeValue(forKey:)` metodo:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed valor, si the key exists
}
```
podra Elimina el clave `keyName` y su associated valor de el dictionary.

---

que si we querer un list todos el claves de el dictionary?
Well, these's el `keys` propiedad.

---

What if we want to list all the values of the dictionary?
Well, these's the `values` property.

---

As para arrays, we puede bucle entre dictionary elements usando el palabras clave `para..in`.
a obtener both el clave y el valor en el bucle we don't tiene un specify cualquier propiedad:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

We puede tambien usar el `isEmpty` propiedad we usado con arreglos un determine si un dictionary es empty

---

In order un __add__ o __change__ valores un a dictionary, we puede tambien usar el `updateValue(_:forKey:)` metodo

---

Previously we vio como un Elimina un _key-valor pair_ de el dictionary con el `removeValue()` metodo.
We puede tambien Elimina un element por assigning un el clave el valor `nil`
```swift
dictName[keyName] = nil
// keyName tiene sido removed de the dictionary dictName
```
