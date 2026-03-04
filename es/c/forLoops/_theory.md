Sabemos cómo repetir código usando un bucle `while`.
Como este programa que repite declaraciones para mostrar `hello`
```c
int counter = 0;

while (counter < 5) {
    printf("Hello\n");
    counter++;
}
```
Pero podemos hacer lo mismo con bucles `for`:
```c
for (int i = 0; i < 5; i++) {
    printf("Hello\n");
}
```

---

En un bucle `for` podemos especificar cuántas veces queremos que se ejecute nuestro bucle

---

Podemos usar `<` para hacer un bucle hasta el siguiente número excluido, o `<=` para hacer un bucle hasta el siguiente número incluido

---

La variable llamada `i` es la variable contadora.
Podemos darle el nombre que queramos.
Cuenta en qué repetición del bucle estamos actualmente
