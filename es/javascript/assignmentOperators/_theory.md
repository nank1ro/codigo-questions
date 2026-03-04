Ya hemos aprendido que para asignar un valor a una variable podemos usar el signo `=`, como:
```javascript
let a = 5;
```

---

Ya tenemos una variable `total` inicializada
```javascript
var total = 5;
```
Digamos que queremos añadir el número `2` a la variable `total`, podemos escribir
```javascript
total = total + 2;
```
¡Bien, funciona! Pero hay una versión más corta para hacer lo mismo:
```javascript
total += 2;
```
El signo `+=` se llama **asignación de suma**.
Suma un valor al valor de la variable y asigna el resultado a esa variable.

---

Al igual que en la asignación de suma, tenemos la **asignación de decremento** `-=`.
La funcionalidad es la misma, la única diferencia es que realiza la resta.
Así que los siguientes son exactamente iguales
```javascript
var num = num - 5;
// es igual a
num -= 5;
```

---

Veamos el operador **asignación de multiplicación** `*=`.
Multiplica la variable por un valor y asigna el resultado a esa variable.
Así que los siguientes son exactamente iguales
```javascript
var num = num * 5;
// es igual a
num *= 5;
```

---

Veamos el operador **asignación de división** `/=`.
Divide la variable por un valor y asigna el resultado a esa variable.
Así que los siguientes son exactamente iguales
```javascript
num = num / 5;
// es igual a
num /= 5;
```

---

Veamos el operador **asignación de residuo** `%=`.
Calcula el residuo de la variable y un valor y asigna el resultado a esa variable.
Así que los siguientes son exactamente iguales
```javascript
num = num % 5;
// es igual a
num %= 5;
```
