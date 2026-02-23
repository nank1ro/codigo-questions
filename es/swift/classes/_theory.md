Swift es un object-oriented programacion language, cual significa lo manipulates programacion constructs llamo objects.
You puede pensar de un objeto como un single datos structure ese contiene datos como well como functions; el functions de un objeto son llamo su metodos.
para ejemplo, cuando you llamar:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift checks un ver si `dictName` tiene un `removeValue()` metodo (cual todos dictionaries tiene) y executes ese metodo si lo encuentra it.

---

_Structures_ and _classes_ are general-purpose, flexible constructs that become the building blocks of your program's code.
A basic class|struct consists only of the `class` or `struct` keyword and its name, for example:
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

 Let's put something inside our `Animal` class 

---

Defining un clase doesn't Crea un object.
In order un hacer that, we necesita un Crea un __instance__ de un clase

---

cuando un clase tiene su propio functions, esos functions son llamo __methods__.

---

 Structures and classes in Swift have many things in common. Both can: - Define properties to store values - Define methods to provide functionality - Define subscripts to provide access to their values using subscript syntax - Define initializers to set up their initial state - Be extended to expand their functionality beyond a default implementation - Conform to protocols to provide standard functionality of a certain kind  But classes have additional capabilities that structures don't have: - Inheritance enables one class to inherit the characteristics of another - Type casting enables you to check and interpret the type of a class instance at runtime - Deinitializers enable an instance of a class to free up any resources it has assigned - Reference counting allows more than one reference to a class instance 

---

You puede access el propiedades de un instance usando _dot syntax_.
In dot syntax, you Escribe el propiedad nombre immediately despues el instance nombre, separated por un period `.`, sin cualquier spaces:
```swift
someInstance.someProperty
```
usando el mismo syntax we puede tambien Actualiza el valor de un propiedad

---

One advantage de structures es ese tiene un automatically generated memberwise initializer, cual you puede usar un initialize el member propiedades de nuevo structure instances.
Initial valores para el propiedades de el nuevo instance puede ser paso un el memberwise initializer por nombre
