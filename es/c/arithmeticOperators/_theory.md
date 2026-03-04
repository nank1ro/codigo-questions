Los operadores se utilizan para realizar operaciones en variables y valores.
Comencemos con los operadores aritméticos, en particular con el operador **suma** `+`.
Se utiliza para sumar dos números, como:
```
>>> 5 + 3
8
```

---

Continuemos con el operador **resta** `-`.
Se utiliza para restar un número de otro, como:
```
>>> 5 - 3
2
```

---

Veamos el operador **multiplicación** `*`.
Se utiliza para multiplicar dos números juntos, como:
```
>>> 5 * 3
15
```

---

Veamos el operador **división** `/`.
Se utiliza para dividir dos números entre sí, como:
```c
>>> 10 / 5
2
```

---

Veamos el operador **módulo** `%`.
Se utiliza para encontrar el residuo después de una división entre dos números, como:
```
>>> 5 % 2
1
```
Esto se evalúa a 1 porque 5 dividido por 2 tiene un cociente de 2 y un residuo de 1
```
>>> 9 % 3
0
```
Este otro se evalúa a 0 porque 9 dividido por 3 tiene un cociente de 3 y deja un residuo de 0

---

C no tiene un operador **exponenciación**, así que tenemos que usar la función `pow()` incluida en la biblioteca `math.h`.
La exponenciación corresponde a la multiplicación repetida de la base: es decir, **b** con exponente *n* es el producto de multiplicar *n* bases:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Veamos la **división entera** usando la función `floor()`.
Esta función devuelve la parte integral del cociente, por ejemplo:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
También se conoce como división entera. El valor resultante es un número entero, aunque el *tipo* del resultado no es necesariamente int.
