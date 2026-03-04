Las variables son contenedores para almacenar valores de datos.
Cada variable en C es un objeto y al igual que otros lenguajes de programación, C tiene comandos para declarar una variable.
Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
Un ejemplo de creación de una variable llamada `x` es:
```c
int x = 1;
```
De esta manera hemos asignado el valor `1` a la variable de tipo _entero_ llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```c
>>> printf("%i\n", x);
1
```

---

Las variables se llaman de esta manera porque el valor que almacenan puede cambiar.
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

También podemos dar a las variables los valores de otras variables. Aquí, podemos dar a la variable `y` el valor de `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Cuando actualizamos una variable, olvida su valor anterior.
Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

En C las variables de cadena solo se pueden declarar usando comillas dobles:
```c
char x[] = "May";
```

---

Si queremos un nombre de variable con múltiples palabras, usamos **snake case**.
Significa usar `_` para conectar las palabras adicionales.
