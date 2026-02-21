Los **objetos** son similares a los arreglos, pero accedes a los valores buscando una *clave* en lugar de un índice
Una clave puede ser cualquier cadena o número.
Los objetos se encierran entre llaves, así:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
Este es un diccionario llamado `objectName` con tres *pares clave-valor*.
La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.

---

Acceder a los valores del diccionario por clave es igual que acceder a los valores del arreglo por índice:
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Like Arrays, Dictionaries are _mutable_.
This means they can be changed after they are created (if are not declared constant).
One advantage of this is that we can add new _key/value pairs_ to the dictionary after it is created like so:
```javascript
dictName[newKeyName] = newValue;
```

---

Debido a que las variables de diccionario son mutables, se pueden cambiar de muchas formas.
Los elementos se pueden eliminar de un diccionario con la palabra clave 'delete':
```javascript
delete dictName[keyName];
```
eliminará la clave `keyName` y su valor asociado del diccionario.

---

What if we want to list all the keys of the dictionary?
Well, these's the `Object.keys()` method.

---

What if we want to list all the values of the dictionary?
Well, these's the `Object.values()` method.

---

Al igual que con los arreglos, podemos iterar entre los elementos del diccionario usando el método `Object.entries()`.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
