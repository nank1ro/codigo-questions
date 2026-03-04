Probablemente hayas considerado la situación en la que deseas reutilizar una parte del código, solo con algunos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función que luego se puede usar repetidamente.
En C usamos el `return_type` seguido del nombre de la `function`, por ejemplo:
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

Los paréntesis en la __definición de función__ no tienen que estar vacíos si queremos especificar parámetros

---

A veces queremos que una función __devuelva__ un valor.
Bueno, existe la palabra clave `return`.

---

Las funciones pueden tener múltiples parámetros de entrada, que se escriben dentro de los paréntesis de la función, separados por comas.
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

En las funciones podemos agregar un _comentario opcional_ que explique qué hace la función:
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
Podemos usar `//` para un comentario de una sola línea y `/* */` para un comentario de varias líneas
