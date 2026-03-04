Las variables son contenedores para almacenar valores de datos.
Cada variable en Swift es un objeto.
Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que asignas un valor por primera vez.
En Swift declares constantes con la palabra clave `let` y variables con la palabra clave `var`.
El valor de una constante no se puede cambiar una vez que se establece, mientras que una variable se puede establecer en un valor diferente en el futuro.
Un ejemplo de creación de una variable llamada `x` es:
```swift
var x = 1
```
De esta manera hemos asignado el valor `1` a la variable llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```swift
print(x) // prints 1
```

---

Las variables se llaman así porque el valor que almacenan puede cambiar.
Podemos actualizar `x` usando `=` y dándole un nuevo valor.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

También podemos darles a las variables los valores de otras variables. Aquí, podemos darle a la variable `y` el valor de `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

Cuando actualizamos una variable, olvida su valor anterior. Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

En Swift las variables de cadena se pueden declarar solo usando comillas dobles:
```swift
let x = "May"
```

---

Si queremos un nombre de variable con múltiples palabras, usamos **camelCase**.
Es la práctica de escribir frases de modo que cada palabra en el medio de la frase comience con una letra mayúscula
