C não tem interpolação de strings: texto e valores são combinados pelo `printf` por meio de uma **string de formato**, onde cada especificador `%` é substituído pelo argumento correspondente. Os especificadores mais comuns são:
```c
printf("%d\n", 42);      // imprime "42" (int, %i é o mesmo)
printf("%f\n", 2.5);     // imprime "2.500000" (double, 6 casas decimais por padrão)
printf("%s\n", "hi");    // imprime "hi" (string)
printf("%c\n", 'A');     // imprime "A" (caractere único)
printf("%x\n", 255);     // imprime "ff" (int como hexadecimal minúsculo)
printf("100%%\n");       // imprime "100%" (um sinal de porcentagem literal)
```
O especificador deve corresponder ao tipo do argumento: exibir um `double` com `%d` ou um `int` com `%s` não converte o valor, ele exibe lixo de memória ou faz o programa travar.

---

`sprintf` funciona exatamente como o `printf`, mas em vez de escrever na tela ele escreve o texto formatado em um array de `char`, chamado de **buffer**, seguido do `'\0'` terminador:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // imprime "3-7"
```
O buffer deve ser declarado antes da chamada e deve ser grande o suficiente para todo o texto mais o terminador, caso contrário o `sprintf` escreve além do seu fim.

---

Uma função que constrói uma string geralmente recebe o buffer como parâmetro e o preenche com `sprintf`. Quem chama é dono do array, e após a chamada pode ler o resultado:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // imprime "Hello, Ada!"
```
Nestes exercícios o `string.h` já está incluído acima do seu código, então o `strcmp` pode ser usado para comparar o resultado.

---

`%x` exibe um inteiro em hexadecimal com letras minúsculas, e `%X` faz o mesmo com letras maiúsculas. `%c` recebe um código de caractere inteiro e exibe o caractere que ele representa, então `%c` com `65` exibe `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // imprime "1f 1F B"
```

---

Um número entre `%` e a letra define a **largura** mínima do campo. O valor é preenchido com espaços à esquerda, e **flags** colocadas logo após o `%` mudam o preenchimento:
```c
printf("[%5d]\n", 42);  // imprime "[   42]" alinhado à direita em 5 colunas
printf("[%-5d]\n", 42); // imprime "[42   ]", a flag - alinha à esquerda
printf("[%05d]\n", 42); // imprime "[00042]", a flag 0 preenche com zeros
printf("[%+d]\n", 42);  // imprime "[+42]", a flag + sempre mostra o sinal
```
Um valor maior que a largura nunca é cortado, o campo simplesmente cresce.

---

Largura e flags funcionam com todos os especificadores, então `%02x` exibe um inteiro como hexadecimal preenchido com zeros até dois dígitos. É assim que cores são escritas como `#rrggbb`:
```c
printf("%02x\n", 5);   // imprime "05"
printf("%02x\n", 255); // imprime "ff"
```

---

Um ponto seguido de um número define a **precisão**. Para `%f` é o número de casas decimais, com arredondamento; para `%s` é o número máximo de caracteres exibidos:
```c
printf("%.2f\n", 3.14159);    // imprime "3.14"
printf("%.3s\n", "formatting"); // imprime "for"
```
Largura e precisão podem ser combinadas: `%8.2f` exibe duas casas decimais alinhadas à direita em 8 colunas.

---

A precisão é a maneira usual de controlar como um `double` aparece em uma string. Uma razão como `0.425` vira uma porcentagem multiplicando por `100` e exibindo uma casa decimal seguida de `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out é "42.5%"
```

---

`sprintf` e `printf` **retornam** o número de caracteres escritos, sem contar o `'\0'` terminador. Esse é o comprimento da string que acabou de ser construída, sem uma chamada separada de `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // imprime "3"
```

---

`sprintf` não tem ideia do tamanho do buffer. O `snprintf` recebe o tamanho do buffer como seu segundo argumento e nunca escreve mais do que `size - 1` caracteres mais o `'\0'`, cortando o texto se necessário. Seu valor de retorno é o comprimento que o texto **completo** teria, então um resultado maior ou igual a `size` significa que a saída foi truncada:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // imprime "formatt 10"
```
`sizeof buffer` dá o tamanho do array em bytes, que para um array de `char` é o seu número de elementos.

---

Comparar o valor de retorno do `snprintf` com o tamanho do buffer diz se tudo coube. Este é o padrão seguro para construir strings de comprimento desconhecido:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out contém apenas os primeiros size - 1 caracteres de text
}
```

---

Uma string pode ser construída em várias etapas escrevendo cada pedaço logo após o anterior. O valor de retorno indica onde o texto termina, então `buffer + n` é o endereço do terminador e o próximo `sprintf` pode continuar a partir daí:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer é "Hello, world", n é 12
```
Somar cada valor de retorno a `n` mantém `n` igual ao comprimento total do texto construído até então.

---

Strings também podem ser combinadas sem uma string de formato. O `strcat` do `string.h` acrescenta uma cópia do seu segundo argumento ao fim do primeiro, que deve ter espaço livre suficiente, e o `strncat` acrescenta no máximo um dado número de caracteres:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text é "Hi!!!"
strncat(text, "abcdef", 2); // text é "Hi!!!ab"
```
Ambos sempre adicionam o `'\0'` terminador após os caracteres acrescentados.

---

Quando não há nada para formatar, o `puts` exibe uma string seguida de uma nova linha. Ao contrário do `printf`, ele não interpreta `%`, então o texto é exibido exatamente como escrito:
```c
puts("Done");      // imprime "Done" e uma quebra de linha
puts("50% off");   // imprime "50% off" e uma quebra de linha
printf("50% off"); // indefinido: % off não é um especificador válido
```
O `puts` é a escolha certa para texto fixo, e o `printf` quando valores devem ser inseridos.

---

O `strncat` é útil quando apenas uma parte de uma string deve ser acrescentada, ou quando o pedaço acrescentado deve ser limitado a um comprimento máximo:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name é "file.ba"
```
Quando o limite é maior que a string, a string inteira é acrescentada.

---

Juntando tudo: uma linha de relatório combina um campo de texto alinhado à esquerda, um separador e um número alinhado à direita com um número fixo de casas decimais, escrito com `snprintf` para que nunca estoure o buffer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out é "Ada   |  9.5"
```
Enquanto cada valor couber na sua largura, todas as linhas têm o mesmo comprimento, então as colunas se alinham quando as linhas são exibidas uma abaixo da outra.
