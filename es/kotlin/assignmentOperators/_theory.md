Los operadores de asignación se usan para asignar valores a variables.
El operador de asignación más básico es `=`, que asigna el valor de la derecha a la variable de la izquierda:
```kotlin
var x = 10
```
Aquí, `10` se asigna a la variable `x`.
También puedes reasignar un nuevo valor a una variable existente:
```kotlin
x = 20
```
Ahora `x` contiene el valor `20`.

---

El operador `+=` es una forma abreviada que suma un valor a una variable y asigna el resultado de vuelta a ella.
En lugar de escribir:
```kotlin
x = x + 5
```
Puedes escribir:
```kotlin
x += 5
```
Ambas expresiones hacen lo mismo: incrementan el valor de `x` en `5`.

---

El operador `-=` resta un valor de una variable y asigna el resultado de vuelta a ella.
En lugar de escribir:
```kotlin
x = x - 3
```
Puedes escribir:
```kotlin
x -= 3
```
Esto disminuye el valor de `x` en `3`.

---

El operador `*=` multiplica una variable por un valor y asigna el resultado de vuelta a ella.
En lugar de escribir:
```kotlin
x = x * 4
```
Puedes escribir:
```kotlin
x *= 4
```
Esto multiplica `x` por `4` y almacena el resultado de vuelta en `x`.

---

El operador `/=` divide una variable por un valor y asigna el resultado de vuelta a ella.
En lugar de escribir:
```kotlin
x = x / 2
```
Puedes escribir:
```kotlin
x /= 2
```
Nota: cuando ambos operandos son `Int`, Kotlin realiza **división entera** (la parte fraccionaria se descarta):
```kotlin
var x = 7
x /= 2
// x ahora vale 3 (no 3.5)
```
