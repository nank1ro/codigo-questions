Las variables son contenedores para almacenar valores de datos.
Toda variable en Kotlin es un objeto.
Para crear una variable, necesitamos darle un __nombre__ teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
En Kotlin declaras constantes con la palabra clave `val` (abreviatura de _value_) y variables con la palabra clave `var` (abreviatura de _variable_).
El valor de una constante no se puede cambiar una vez que se establece, mientras que una variable se puede establecer en un valor diferente en el futuro.
Un ejemplo de creación de una variable llamada `x` es:
```kotlin
var x = 1
```
De esta manera hemos asignado el valor `1` a la variable llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```kotlin
println(x) // prints 1
```

---

Las variables se llaman así porque el valor que almacenan puede cambiar.
Podemos actualizar `x` utilizando `=` y dándole un nuevo valor.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

También podemos asignar a las variables los valores de otras variables. Aquí, podemos asignar a la variable `y` el valor de `x`
```kotlin
var x = 5
var y = x
println(y) // prints 5
```

---

Cuando actualizamos una variable, olvida su valor anterior. Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.
```kotlin
var x = 5
println(x) // prints 5
x = 10
println(x) // prints 10
```

---

En Kotlin las variables de cadena solo se pueden declarar usando comillas dobles:
```kotlin
val x = "May"
```

---

Si queremos un nombre de variable con múltiples palabras, usamos **camelCase**.
Es la práctica de escribir frases de tal manera que cada palabra en el medio de la frase comience con una letra mayúscula
