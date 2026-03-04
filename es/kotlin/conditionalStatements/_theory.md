La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una cierta condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `niceWeather` y realizar la acción de jugar afuera `if` esta variable es `true`, como:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

Continuemos con el ejemplo anterior.
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
Hemos visto que la sentencia `if` ejecuta el bloque de código solo si la condición es `true`.
Otra cosa importante a considerar está representada por los **llaves** `{}` que indican un bloque de código.

---

Acabamos de ver cómo ejecutar un bloque de código si se cumple una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Jugamos afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En Kotlin podemos usar la sentencia `else`, como:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Supongamos que tenemos otra condición a verificar, como en este ejemplo:
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
y la salida de este código es `the number is 3`.
En primer lugar, verifiquemos si el número es igual a 2, esto es falso.
Así que pasemos a la segunda sentencia y verifiquemos si `num` es igual a 3, siendo verdadero ejecutamos el siguiente bloque de código imprimiendo `the number is 3`

---

Podemos añadir tantas sentencias `else if` como queramos, no hay límites
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
y la salida de este código es `the number is 4`.

---

También podemos anidar una sentencia condicional (`if`, `else if` o `else`) dentro de otra sentencia condicional, para crear una estructura más compleja.
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
y la salida de este código es `the number is 4`.

---

El _operador elvis_ `a ?: b` desenvuelve un opcional `a` si contiene un valor, o devuelve un valor predeterminado `b` si `a` es `null`.
La expresión `a` es siempre de un tipo opcional.
La expresión `b` debe coincidir con el tipo que se almacena dentro de a.
El operador elvis es una forma abreviada del código siguiente:
```kotlin
if (a != null) a else b
```
