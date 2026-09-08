C não tem um tipo dedicado para strings: uma **string** é um array de `char` que termina com um caractere especial, o **terminador nulo** `'\0'`.
A forma mais fácil de criar uma é um literal de string entre aspas duplas:
```c
char name[] = "Codigo";
```
O compilador conta os caracteres e adiciona o `'\0'` no final para você.
Para exibir uma string, use o especificador `%s`:
```c
printf("%s\n", name);
// prints "Codigo"
```

---

O terminador nulo ocupa espaço em memória: o literal `"hi"` ocupa 3 bytes, `'h'`, `'i'` e `'\0'`.
Quando você mesmo declara o tamanho, sempre deixe espaço para ele:
```c
char word[6] = "hello"; // 5 letters + '\0'
```
Sem o terminador, o C não tem como saber onde a string termina.

---

O cabeçalho `string.h` fornece funções que trabalham com strings.
`strlen` retorna o número de caracteres antes do terminador nulo (o próprio terminador não é contado):
```c
strlen("hello"); // 5
```
Uma função que recebe uma string declara o parâmetro como `char *text`, um ponteiro para o primeiro caractere.
Nestes exercícios, `string.h` e `ctype.h` já estão incluídos acima do seu código.

---

Como uma string é um array, cada caractere tem um índice começando em `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Um único caractere é exibido com `%c`. Os caracteres também podem ser substituídos:
```c
word[0] = 'K'; // word is now "Koding"
```

---

Como toda string termina com `'\0'`, você pode percorrê-la sem saber seu tamanho de antemão: continue enquanto o caractere atual não for o terminador.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Um array não pode receber uma atribuição com `=` após sua declaração:
```c
char copy[20];
copy = "Codigo"; // error
```
Para copiar uma string, use `strcpy(destination, source)` de `string.h`.
O destino deve ser grande o suficiente para conter todos os caracteres mais o `'\0'`.

---

`strcat(destination, source)` anexa `source` ao final de `destination`:
```c
char text[20] = "Hello";
strcat(text, " World");
// text is now "Hello World"
```
Assim como em `strcpy`, o array de destino deve ter espaço suficiente para o resultado.

---

Duas strings não podem ser comparadas com `==`: isso compararia seus endereços em memória, não seus caracteres.
Use `strcmp(first, second)`, que retorna `0` quando as duas strings contêm exatamente os mesmos caracteres:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // not 0
```

---

`strcmp` compara as strings caractere por caractere usando seus códigos de caractere.
O resultado é negativo quando a primeira string vem antes da segunda, positivo quando vem depois, e `0` quando são iguais:
```c
strcmp("a", "b"); // negative
strcmp("b", "a"); // positive
```

---

`strncpy(destination, source, n)` copia no máximo `n` caracteres.
Se `source` for mais longa que `n`, nenhum `'\0'` é escrito: você precisa terminar o resultado você mesmo.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix is "Cod"
```

---

O cabeçalho `ctype.h` fornece funções que trabalham com um único caractere.
`toupper(c)` retorna a versão maiúscula de uma letra e `tolower(c)` a versão minúscula; qualquer outro caractere é retornado sem alteração:
```c
char letter = toupper('a'); // 'A'
```

---

Uma string é passada para uma função como um ponteiro, então uma função que recebe `char *text` pode alterar os caracteres do chamador diretamente.
Combinar um loop até `'\0'` com `toupper` converte uma string inteira:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` funciona como `printf`, mas escreve o texto formatado em um array de caracteres em vez de exibi-lo na tela:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer is "3 items"
```
O buffer deve ser grande o suficiente para todo o texto e seu `'\0'`.

---

`sprintf` é uma forma prática de transformar um número em texto: uma vez em um buffer, qualquer função de string pode trabalhar sobre ele.
