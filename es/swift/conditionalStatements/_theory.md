Decision haciendo es requirio cuando we querer un ejecutar codigo solo si un certain condicion es satisfied.
permitir's assume we querer un jugar outside solo si el weather es nice.
In programming, we puede save un booleano variable `niceWeather` y realizar el action de jugando outside `si` este variable es `verdadero`, like:
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Continuemos con el previous ejemplo.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
We've visto ese el `si` sentencia executes el block de codigo solo si el condicion es `verdadero`.
Another importante thing un considerar es represented por el **curly brackets** `{}` cual indicate un codigo block.

---

We just saw how to execute a block of code if a condition occurs, now let's see how to execute another block of code if the first condition fails.
We go to play outside if the weather is nice; otherwise, we stay home.
In Swift we can use the `else` statement, like:
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Supongamos que tenemos otra condición para verificar, como en este ejemplo:
```swift
var num = 3
if num == 2 {
    print("el número es 2")
} else if num == 3 {
    print("el número es 3")
} else {
    print("haz algo más")
}
```
y la salida de este código es `el número es 3`.
Primero, verifiquemos si el número es igual a 2, esto es falso.
Así que pasemos a la segunda sentencia y verifiquemos si `num` es igual a 3, siendo verdadero ejecutamos el siguiente bloque de código imprimiendo `el número es 3`

---

Podemos agregar tantas sentencias `else if` como queramos, no hay límites
```swift
var num = 4
if (num == 2) {
    print("el número es 2")
} else if num == 3 {
    print("el número es 3")
} else if (num == 4) {
    print("el número es 4")
} else if (num == 5) {
    print("el número es 5")
} else if (num == 6) {
    print("el número es 6")
}
```
y la salida de este código es `el número es 4`.

---

We can also nest a conditional statement (`if`, `else if` or `else`) inside another conditional statement, to create a more complex structure.
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
and the output of this code is `the number is 4`.

---

The ternary conditional operador es un special operador con three parts, cual toma el form `question ? answer1 : answer2`.
It's un shortcut para evaluating uno de dos expresiones based en whether `question` es verdadero o falso.
si `question` es verdadero, lo evaluates `answer1` y devuelve su valor; otherwise, lo evaluates `answer2` y devuelve su valor.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
The shortand codigo para el encima de codigo es:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` es establecer Igual un `a`, porque el condicion `a < b` era verdadero

---

```swift
a != nil ? a! : b
```

 The _nil-coalescing operator_ `a ?? b` unwraps an optional `a` if it contains a value, or returns a default value `b` if `a` is `nil`. The expression `a` is always of an optional type. The expression `b` must match the type that is stored inside a. The nil-coalescing operator is shorthand for the code below:
