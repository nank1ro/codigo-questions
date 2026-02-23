Las variables son contenedores para almacenar valores de datos.
Cada variable en Kotlin es un objeto.
Para crear una variable, necesitamos darle un __nombre__ teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
En Kotlin declaras constantes con la palabra clave `val` (abreviatura de _value_) y variables con la palabra clave `var` (abreviatura de _variable_).
El valor de una constante no puede cambiarse una vez que se establece, mientras que una variable puede establecerse a un valor diferente en el futuro.
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
Podemos actualizar `x` usando `=` y dándole un nuevo valor.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

También podemos dar a variables los valores de otras variables. Here, we can give to the `y` variable the value of `x`
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

If we want a variable name with multiple words, we use **camelCase**.
It is the practice of writing phrases such that each word in the middle of the phrase begins with a capital letter
