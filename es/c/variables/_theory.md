Las variables son contenedores para almacenar valores de datos.
Cada variable en C es un objeto y, como otros lenguajes de programación, C tiene comandos para declarar una variable.
Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
Un ejemplo de creación de variable llamada `x` es:
```c
int x = 1;
```
De esta manera hemos asignado el valor `1` a la variable _entero_ llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```c
>>> printf("%i\n", x);
1
```

---

Las variables se llaman así porque el valor que almacenan puede cambiar.
Podemos actualizar `x` usando `=` y dándole un nuevo valor.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

We can also give variables the values of other variables. Here, we can give to the `y` variable the value of `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

When we update a variable, it forgets its previous value.
Here we can display the `x` variable twice and see how its value updates.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

In C string variables can be declared only by using double quotes:
```c
char x[] = "May";
```

---

If we want a variable name with multiple words, we use **snake case**.
It means using `_` to connect the additional words.
