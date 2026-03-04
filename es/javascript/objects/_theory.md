**Los objetos** son similares a los arrays, pero accedes a los valores buscando una *clave* en lugar de un índice
Una clave puede ser cualquier cadena o número.
Los objetos están encerrados entre llaves, así:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
Este es un diccionario llamado `objectName` con tres *pares clave-valor*.
La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.

---

Acceder a los valores del diccionario por clave es igual que acceder a los valores del array por índice:
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Como los arrays, los diccionarios son _mutables_.
Esto significa que pueden cambiar después de ser creados (si no están declarados como constantes).
Una ventaja de esto es que podemos añadir nuevos _pares clave/valor_ al diccionario después de crearlo así:
```javascript
dictName[newKeyName] = newValue;
```

---

Debido a que las variables diccionarias son mutables, pueden ser cambiadas de muchas formas.
Los elementos pueden ser removidos de un diccionario con la palabra clave 'delete':
```javascript
delete dictName[keyName];
```
eliminará la clave `keyName` y su valor asociado del diccionario.

---

¿Y si queremos listar todas las claves del diccionario?
Bueno, existe el método `Object.keys()`.

---

¿Y si queremos listar todos los valores del diccionario?
Bueno, existe el método `Object.values()`.

---

Como con los arrays, podemos recorrer los elementos del diccionario usando el método `Object.entries()`.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
