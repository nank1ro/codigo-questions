A menudo en la programación, necesitamos repetir un bloque de código, por ejemplo:
```swift
print("2 segundos")
print("3 segundos")
print("4 segundos")
print("5 segundos")
```
Esto produce la siguiente salida:
```swift
2 segundos
3 segundos
4 segundos
5 segundos
```
Obviamente, para sentencias largas pasaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
Entonces creamos una variable `count` asignando `2`, el valor inicial.
Luego usamos la declaración `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.
Dentro del bloque de código, **NO** debemos perder la línea `count += 1`.
Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito

---

Para controlar las veces que se repite un bucle `while`, comenzamos con una variable establecida en un número.
Llamamos a esta variable una variable contador

---

Luego, usamos una comparación en la condición para comparar la variable `counter` con un número.

---

Dentro del bloque de código, para detener el bucle `while`, incrementamos la variable `counter`.

---

El orden en que escribes código afecta la salida.

---

En Swift también tenemos la variación **repeat-while** del bucle `while`.
Realiza un solo paso a través del bloque de bucle primero, _antes_ de considerar la condición del bucle.
Luego continúa repitiendo el bucle hasta que la condición sea `false`.
El bucle __repeat-while__ en Swift es análogo a un bucle __do-while__ en otros lenguajes
