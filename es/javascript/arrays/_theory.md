Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.
Un arreglo almacena múltiples valores de uno o varios tipos y usa **índices** para distinguir estos valores.
Puedes asignar elementos a un arreglo con una expresión de la forma:
```javascript
var arrayName = [item1, item2];
```

---

Puedes acceder a un elemento individual del arreglo por su índice.
Un índice es como una dirección que identifica el lugar del elemento en el arreglo.
El índice aparece directamente después del nombre del arreglo, entre corchetes, así:
```javascript
arrayName[index];
```
Los índices del arreglo comienzan con `0`, **no** con `1`! Accedes al primer elemento de un arreglo así: `arrayName[0]`.
El segundo elemento de un arreglo está en el índice 1: `arrayName[1]`.

---

Un índice de arreglo se comporta como cualquier otro nombre de variable.
Se puede usar para acceder así como para asignar valores.
You saw how to access an array index like this:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
This is how an assignment works:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Just like strings, arrays have a **length**.
An arrays's length is the number of items it contains

---

Un arreglo no tiene que tener una longitud fija.
¡Puedes agregar elementos al final de un arreglo en cualquier momento!
Para agregar un elemento a un arreglo usamos la función `push`:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

A veces, solo quieres acceder a una porción de un arreglo.
Considera el siguiente código:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
Primero, creamos un arreglo llamado `numbers`.
Luego, tomamos una subsección del arreglo y la almacenamos en el arreglo slice.
Hacemos esto definiendo los índices que queremos incluir después del nombre del arreglo: `numbers.slice(1, 3)`.
Ten en cuenta que el índice derecho está excluido

---

In JavaScript we can slice an array as we want!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
Si tu slice de arreglo incluye el primer o último elemento de un arreglo, el índice de ese elemento no tiene que estar incluido

---

Los elementos del arreglo pueden ser de cualquier tipo.
```javascript
var arrayName = ["one", 2, true];
```
De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.
¡Pero también podemos tener arreglos con arreglos!

---

A veces necesitas buscar un elemento en un arreglo.
In JavaScript we can use the `indexOf()` method:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.
También podemos insertar elementos en un arreglo en un índice específico, usando el método `splice()`:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
El código anterior inserta `"Ali"` en el índice `1`, que mueve todo, después de este índice, hacia abajo por 1.
El segundo valor `0` significa _deleteCount_, en este caso, no eliminamos ningún elemento del arreglo; pero si hubiéramos especificado `1`, el valor `Zac` habría sido eliminado del arreglo

---

En JavaScript podemos iterar a través de un arreglo de una manera muy simple usando las palabras clave `for..of`:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3 
```
Un nombre de variable sigue a la palabra clave `for`, se le asignará el valor de cada elemento del arreglo a su vez.
