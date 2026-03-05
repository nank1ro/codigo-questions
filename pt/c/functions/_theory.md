Você pode ter considerado a situação em que gostaria de reutilizar um trecho de código, apenas com alguns valores diferentes.
Em vez de reescrever todo o código, é muito mais limpo definir uma função, que pode então ser usada repetidamente.
Em C usamos o `return_type` seguido pelo nome da `function`, por exemplo:
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

Os parênteses na __definição da função__ não precisam estar vazios se quisermos especificar parâmetros

---

Às vezes queremos que uma função __retorne__ um valor.
Bem, existe a palavra-chave `return`.

---

Funções podem ter múltiplos parâmetros de entrada, que são escritos dentro dos parênteses da função, separados por vírgulas.
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

Nas funções podemos adicionar um _comentário opcional_ que explica o que a função faz:
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
Podemos usar `//` para um comentário de uma linha e `/* */` para um comentário de múltiplas linhas
