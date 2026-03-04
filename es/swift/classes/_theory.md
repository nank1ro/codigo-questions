Swift es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos.
Puedes pensar en un objeto como una estructura de datos única que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas a:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift verifica si `dictName` tiene un método `removeValue()` (que todos los diccionarios tienen) y ejecuta ese método si lo encuentra.

---

Las _estructuras_ y las _clases_ son construcciones flexibles de propósito general que se convierten en los bloques de construcción del código de tu programa.
Una clase|estructura básica consiste solo en la palabra clave `class` o `struct` y su nombre, por ejemplo:
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

Pongamos algo dentro de nuestra clase `Animal`

---

Definir una clase no crea un objeto.
Para hacerlo, necesitamos crear una __instancia__ de una clase

---

Cuando una clase tiene sus propias funciones, esas funciones se llaman __métodos__.

---

Las estructuras y las clases en Swift tienen mucho en común. Ambas pueden:
- Definir propiedades para almacenar valores
- Definir métodos para proporcionar funcionalidad
- Definir subíndices para proporcionar acceso a sus valores usando sintaxis de subíndice
- Definir inicializadores para configurar su estado inicial
- Extenderse para expandir su funcionalidad más allá de una implementación predeterminada
- Conformarse con protocolos para proporcionar funcionalidad estándar de un cierto tipo

Pero las clases tienen capacidades adicionales que las estructuras no tienen:
- La herencia permite que una clase herede las características de otra
- El casting de tipos te permite verificar e interpretar el tipo de una instancia de clase en tiempo de ejecución
- Los desinicializadores permiten que una instancia de una clase libere los recursos que ha asignado
- El conteo de referencias permite más de una referencia a una instancia de clase

---

Puedes acceder a las propiedades de una instancia usando _sintaxis de punto_.
En sintaxis de punto, escribes el nombre de la propiedad inmediatamente después del nombre de la instancia, separado por un punto `.`, sin espacios:
```swift
someInstance.someProperty
```
Usando la misma sintaxis también podemos actualizar el valor de una propiedad

---

Una ventaja de las estructuras es que tienen un inicializador miembro generado automáticamente, que puedes usar para inicializar las propiedades miembro de nuevas instancias de estructura.
Los valores iniciales para las propiedades de la nueva instancia se pueden pasar al inicializador miembro por nombre
