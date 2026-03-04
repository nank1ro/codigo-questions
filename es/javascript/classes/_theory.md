JavaScript es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos.
Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas a:
```javascript
arrayName.push("value");
```
JavaScript comprueba si `arrayName` tiene un método `push()` (que todos los arrays tienen) y ejecuta ese método si lo encuentra.

---

Las _clases_ son construcciones de propósito general y flexibles que se convierten en los bloques de construcción del código de tu programa.
Una clase básica consta solo de la palabra clave `class` y su nombre, por ejemplo:
```javascript
class ClassName {
    // class definition
}
```

---

Pongamos algo dentro de nuestra clase `Animal`
Para añadir algunos parámetros tenemos que usar el `constructor` por defecto

---

Definir una clase no crea un objeto.
Para hacer eso, necesitamos crear una __instancia__ de una clase.
En JavaScript, para crear una nueva instancia de una clase, siempre usamos la palabra clave `new` antes del nombre de la clase.
Si quieres asignar un valor por defecto a un parámetro, hazlo en la lista de parámetros del constructor

---

Cuando una clase tiene sus propias funciones, esas funciones se llaman __métodos__.

---

JavaScript nos permite crear una clase como hijo de otra, usando la palabra clave `extends`

---

Puedes acceder a las propiedades de una instancia usando _sintaxis de punto_.
En sintaxis de punto, escribes el nombre de la propiedad inmediatamente después del nombre de la instancia, separado por un punto `.`, sin espacios:
```javascript
someInstance.someProperty
```
Usando la misma sintaxis también podemos actualizar el valor de una propiedad
