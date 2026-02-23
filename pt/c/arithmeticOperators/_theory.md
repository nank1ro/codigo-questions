Os operadores são usados para realizar operações em variáveis e valores.
Vamos começar com the arithmetic operators, in particular with the **addition** `+` operator.
É usado para somar dois números, like:
```
>>> 5 + 3
8
```

---

Let's continue with the **subtraction** `-` operator.
É usado para subtract one number from another, like:
```
>>> 5 - 3
2
```

---

Let's see the **multiplication** `*` operator.
É usado para multiplicar dois números together, like:
```
>>> 5 * 3
15
```

---

Let's see the **division** `/` operator.
É usado para dividir dois números together, like:
```c
>>> 10 / 5
2
```

---

Let's see the **modulus** `%` operator.
É usado para find the remainder after a division between two numbers, like:
```
>>> 5 % 2
1
```
This evaluates to 1 because 5 divided by 2 has a quotient of 2 and a remainder of 1
```
>>> 9 % 3
0
```
This other evaluates to 0 because 9 divided by 3 has a quotient of 3 and leaves a remainder of 0

---

C doesn't have an **exponentiation** operator, so we have to use the `pow()` function included in the `math.h` library.
Exponentiation corresponds to repeated multiplication of the base: that is, **b** with exponent *n* is the product of multiplying *n* bases:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Let's see the **floor division** using the `floor()` function.
This function returns the integral part of the quotient, for example:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Also referred to as integer division. The resultant value is a whole integer, though the result's *type* is not necessarily int.
