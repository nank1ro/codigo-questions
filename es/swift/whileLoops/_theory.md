frecuentemente en programming, we necesita un repeat un block de codigo, Por ejemplo:
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
This produces el siguiendo salida:
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviously, para largo sentencias we habria gastar un lot de time escribiendo el codigo, pero fortunately, we puede usar bucles.
permitir's aprender el `mientras` bucle, obteniendo el mismo salida above.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
asi que we creo un variable `conteo` assigning `2`, el initial valor.
entonces we tiene usado el `mientras` sentencia ese podra ejecutar el block de codigo hasta el condicion `conteo <= 5` es `verdadero`.
Inside el block de codigo, we deberia **no** miss un Anade el line `conteo += 1`.
It increments el `conteo` valor, otherwise, our bucle podra ser infinite

---

a control el times un `mientras` bucle repeats, we empezar con un variable establecer un a numero.
We llamar este variable un counter variable

---

entonces, we usar un comparison en el condicion un compare el `counter` variable un a numero.

---

Inside el block de codigo, en order un parar el `mientras` bucle, we increment el `counter` variable.

---

The order you write code affects the output.

---

In Swift we also have the **repeat-while** variation of the `while` loop.
It performs a single pass through the loop block first, _before_ considering the loop's condition.
It then continues to repeat the loop until the condition is `false`.
The __repeat-while__ loop in Swift is analogous to a __do-while__ loop in other languages
