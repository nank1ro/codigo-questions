JavaScript es un lenguaje de programación orientado a objetos, lo que significa que manipula constructos de programación llamados objetos.
Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas:
```javascript
arrayName.push("value");
```
JavaScript verifica si `arrayName` tiene un método `push()` (que todos los arreglos tienen) y ejecuta ese método si lo encuentra.

---

_Classes_ are general-purpose, flexible constructs that become the building blocks of your program's code.
A basic class consists only of the `class` keyword and its name, for example:
```javascript
class ClassName {
    // class definition
}
```

---

Let's put something inside our `Animal` class
To add some parameters we have to use the default `constructor`

---

Defining a class doesn't create an object.
In order to do that, we need to create an __instance__ of a class.
In JavaScript to create a new instance of a class, we always use the `new` keyword before the class name.
If you want to assign a default value to a parameter, do it in the constructor list of parameter names

---

When a class has its own functions, those functions are called __methods__.

---

JavaScript allows us to create a class as a child of another, using the `extends` keyword

---

You can access the properties of an instance using _dot syntax_.
In dot syntax, you write the property name immediately after the instance name, separated by a period `.`, without any spaces:
```javascript
someInstance.someProperty
```
Using the same syntax we can also update the value of a property
