Ya hemos aprendido que para asignar un valor a una variable podemos usar el signo `=`, como:
```swift
let a = 5
```

---

Ya tenemos una variable inicializada `total`
```swift
var total = 5
```
Digamos que queremos agregar el número `2` a la variable `total`, podemos escribir
```swift
total = total + 2
```
¡Bien, funciona! Pero hay una versión más corta para hacer lo mismo:
```swift
total += 2
```
El signo `+=` se llama **asignación de adición**.
Agrega un valor al valor de la variable y asigna el resultado a esa variable.

---

Al igual que en la asignación de adición, tenemos la **asignación de decremento** `-=`.
La funcionalidad es la misma, la única diferencia es que realiza la resta.
Entonces los siguientes son exactamente iguales
```swift
var num = num - 5
// es igual a
num -= 5
```

---

Veamos el operador de **asignación de multiplicación** `*=`.
Multiplica la variable por un valor y asigna el resultado a esa variable.
Entonces los siguientes son exactamente iguales
```swift
var num = num * 5
// es igual a
num *= 5
```

---

Veamos el operador de **asignación de división** `/=`.
Divide la variable por un valor y asigna el resultado a esa variable.
Entonces los siguientes son exactamente iguales
```swift
num = num / 5
// es igual a
num /= 5
```

---

Veamos el operador de **asignación de resto** `%=`.
Calcula el resto de la variable y un valor, y asigna el resultado a esa variable.
Entonces los siguientes son exactamente iguales
```swift
num = num % 5
// es igual a
num %= 5
```
