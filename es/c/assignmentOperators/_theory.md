Ya hemos aprendido que para asignar un valor a una variable podemos usar el signo `=`, como:
```c
int a = 5;
```

---

Ya tenemos una variable inicializada `total`
```c
int total = 5;
```
Supongamos que queremos sumar el número `2` a la variable `total`, podemos escribir
```c
total = total + 2;
```
¡Está bien! Pero hay una versión más corta para hacer lo mismo:
```c
total += 2;
```
El signo `+=` se llama **asignación de adición**.
Suma un valor al valor de la variable y asigna el resultado a esa variable.

---

Al igual que en la asignación de adición, tenemos la **asignación de decremento** `-=`.
La funcionalidad es la misma, la única diferencia es que realiza la resta.
Entonces los siguientes son exactamente lo mismo
```c
num = num - 5;
// es igual a
num -= 5;
```

---

Veamos el operador **asignación de multiplicación** `*=`.
Multiplica la variable por un valor y asigna el resultado a esa variable.
Entonces los siguientes son exactamente lo mismo
```c
num = num * 5;
// es igual a
num *= 5;
```

---

Veamos el operador **asignación de división** `/=`.
Divide la variable por un valor y asigna el resultado a esa variable.
Entonces los siguientes son exactamente lo mismo
```c
num = num / 5;
// es igual a
num /= 5;
```

---

Veamos el operador **asignación de módulo** `%=`.
Calcula el módulo de la variable y un valor y asigna el resultado a esa variable.
Entonces los siguientes son exactamente lo mismo
```c
num = num % 5;
// es igual a
num %= 5;
```
