Sabemos como repetir código usando um loop `while`.
Como este programa que repete instruções para exibir `hello`
```c
int counter = 0;

while (counter < 5) {
    printf("Hello\n");
    counter++;
}
```
Mas podemos fazer o mesmo com loops `for`:
```c
for (int i = 0; i < 5; i++) {
    printf("Hello\n");
}
```

---

Em um loop `for` podemos especificar quantas vezes queremos que nosso loop execute

---

Podemos usar `<` para iterar até o próximo número excluído, ou `<=` para iterar até o próximo número incluído

---

A variável chamada `i` é a variável contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repetição do loop estamos atualmente
