Sabemos cómo repetir código usando un bucle `while`.
Como este programa repitiendo declaraciones para mostrar `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Pero podemos hacer lo mismo con bucles `for`:
```swift
for i in 0..<5 {
    print("hello")
}
```

---

En un bucle `for` podemos especificar cuántas veces queremos que se ejecute nuestro bucle

---

Podemos usar `..<` para hacer un bucle hasta el siguiente número excluido, o `...` para hacer un bucle hasta el siguiente número incluido

---

La variable llamada `i` es la variable contador.
Podemos darle el nombre que queremos.
Cuenta en qué repetición del bucle nos encontramos actualmente

---

La función `stride()` devuelve una secuencia de números.
Requiere los parámetros _from_, _to_ y _by_.
Esta es la sintaxis de la función:
```swift
stride(from:to:by:)
```
Tenga en cuenta que el valor `to` se excluye

---

Con la función `stride()` también podemos usar rangos cerrados, usando:
```swift
stride(from:through:by:)
```
En este caso el valor `through` se incluye

---

En Swift también tenemos el bucle `forEach`.
De hecho, `forEach` llama al cierre dado en cada elemento de la secuencia en el mismo orden que un bucle `for-in`:
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
El uso del método `forEach` es distinto de un bucle `for-in` de dos formas importantes:
1. La declaración `break` o `continue` no se puede usar para salir de la llamada actual del cierre del cuerpo o para omitir llamadas posteriores.
2. El uso de la declaración `return` en el cierre del cuerpo solo saldrá del cierre y no del alcance externo, y no omitirá llamadas posteriores.
