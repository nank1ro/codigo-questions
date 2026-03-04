Los arrays son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un único nombre de variable.
Un array almacena múltiples valores de uno o varios tipos y utiliza **índices** para distinguir estos valores.
Puedes asignar elementos a un array con una expresión de la forma:
```javascript
var arrayName = [item1, item2];
```

---

Puedes acceder a un elemento individual del array por su índice.
Un índice es como una dirección que identifica el lugar del elemento en el array.
El índice aparece directamente después del nombre del array, entre corchetes, así:
```javascript
arrayName[index];
```
Los índices de los arrays comienzan con `0`, ¡**no** `1`! Accedes al primer elemento de un array así: `arrayName[0]`.
El segundo elemento en un array está en el índice 1: `arrayName[1]`.

---

Un índice de array se comporta como cualquier otro nombre de variable.
Se puede usar para acceder así como para asignar valores.
Viste cómo acceder a un índice de array así:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
Así es cómo funciona una asignación:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Al igual que los strings, los arrays tienen una **longitud**.
La longitud de un array es el número de elementos que contiene

---

Un array no tiene que tener una longitud fija.
¡Puedes añadir elementos al final de un array en cualquier momento!
Para agregar un elemento a un array usamos la función `push`:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

A veces, solo quieres acceder a una porción de un array.
Considera el siguiente código:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
Primero, creamos un array llamado `numbers`.
Luego, tomamos una subsección del array y la almacenamos en el array slice.
Hacemos esto definiendo los índices que queremos incluir después del nombre del array: `numbers.slice(1, 3)`.
Ten en cuenta que el índice derecho está excluido

---

¡En JavaScript podemos dividir un array como queramos!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
Si tu división de array incluye el primer o último elemento en un array, el índice para ese elemento no tiene que ser incluido

---

Los elementos del array pueden ser de cualquier tipo.
```javascript
var arrayName = ["one", 2, true];
```
De hecho, arriba tenemos, en orden, un string, un entero y un booleano.
¡Pero también podemos tener arrays con arrays!

---

A veces necesitas buscar un elemento en un array.
En JavaScript podemos usar el método `indexOf()`:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
El código anterior imprime el primer índice que contiene el string `"Zac"`, `1` en este caso.
También podemos insertar elementos en un array en un índice específico, usando el método `splice()`:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
El código anterior inserta `"Ali"` en el índice `1`, que mueve todo, después de este índice, hacia abajo en 1.
El segundo valor `0` significa _deleteCount_, en este caso, no borramos ningún elemento en el array; pero si hubiéramos especificado `1` el valor `Zac` habría sido eliminado del array

---

En JavaScript podemos recorrer un array de una manera muy simple usando las palabras clave `for..of`:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
Un nombre de variable sigue la palabra clave `for`, se le asignará el valor de cada elemento del array en turno.
