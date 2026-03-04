Se requiere toma de decisiones cuando queremos ejecutar código solo si se cumple una cierta condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `niceWeather` y realizar la acción de jugar afuera `si` esta variable es `true`, como:
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Continuemos con el ejemplo anterior.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
Hemos visto que la instrucción `if` ejecuta el bloque de código solo si la condición es `true`.
Otra cosa importante a considerar es representada por los **corchetes ondulantes** `{}` que indican un bloque de código.

---

Acabamos de ver cómo ejecutar un bloque de código si ocurre una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Vamos a jugar afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En Swift podemos usar la instrucción `else`, como:
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Supongamos que tenemos otra condición a verificar, como en este ejemplo:
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
y el resultado de este código es `the number is 3`.
En primer lugar, verifiquemos si el número es igual a 2, esto es falso.
Entonces pasemos a la segunda instrucción y verifiquemos si `num` es igual a 3, siendo verdadero ejecutamos el siguiente bloque de código imprimiendo `the number is 3`

---

Podemos agregar tantas instrucciones `else if` como queramos, no hay límites
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
y el resultado de este código es `the number is 4`.

---

También podemos anidar una instrucción condicional (`if`, `else if` o `else`) dentro de otra instrucción condicional, para crear una estructura más compleja.
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
y el resultado de este código es `the number is 4`.

---

El operador condicional ternario es un operador especial con tres partes, que toma la forma `question ? answer1 : answer2`.
Es un atajo para evaluar una de dos expresiones según si `question` es verdadera o falsa.
Si `question` es verdadera, evalúa `answer1` y devuelve su valor; de lo contrario, evalúa `answer2` y devuelve su valor.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
El código abreviado para el código anterior es:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` se establece igual a `a`, porque la condición `a < b` fue verdadera

---

El operador _nil-coalescing_ `a ?? b` desenvuelve un `a` opcional si contiene un valor, o devuelve un valor predeterminado `b` si `a` es `nil`.
La expresión `a` es siempre de un tipo opcional.
La expresión `b` debe coincidir con el tipo que se almacena dentro de a.
El operador nil-coalescing es una abreviatura del código siguiente:
```swift
a != nil ? a! : b
```
