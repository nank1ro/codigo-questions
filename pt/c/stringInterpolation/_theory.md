C não tem interpolação de strings: texto e valores são combinados pelo `printf` por meio de uma **string de formato**, onde cada especificador `%` é substituído pelo argumento correspondente. Os especificadores mais comuns são:
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
O especificador deve corresponder ao tipo do argumento: exibir um `double` com `%d` ou um `int` com `%s` não converte o valor, ele exibe lixo de memória ou faz o programa travar.

---

`sprintf` funciona exatamente como o `printf`, mas em vez de escrever na tela ele escreve o texto formatado em um array de `char`, chamado de **buffer**, seguido do `'\0'` terminador:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
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
printf("%s\n", message); // prints "Hello, Ada!"
```
Nestes exercícios o `string.h` já está incluído acima do seu código, então o `strcmp` pode ser usado para comparar o resultado.

---

`%x` exibe um inteiro em hexadecimal com letras minúsculas, e `%X` faz o mesmo com letras maiúsculas. `%c` recebe um código de caractere inteiro e exibe o caractere que ele representa, então `%c` com `65` exibe `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

Um número entre `%` e a letra define a **largura** mínima do campo. O valor é preenchido com espaços à esquerda, e **flags** colocadas logo após o `%` mudam o preenchimento:
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
Um valor maior que a largura nunca é cortado, o campo simplesmente cresce.

---

Largura e flags funcionam com todos os especificadores, então `%02x` exibe um inteiro como hexadecimal preenchido com zeros até dois dígitos. É assim que cores são escritas como `#rrggbb`:
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

Um ponto seguido de um número define a **precisão**. Para `%f` é o número de casas decimais, com arredondamento; para `%s` é o número máximo de caracteres exibidos:
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
Largura e precisão podem ser combinadas: `%8.2f` exibe duas casas decimais alinhadas à direita em 8 colunas.

---

A precisão é a maneira usual de controlar como um `double` aparece em uma string. Uma razão como `0.425` vira uma porcentagem multiplicando por `100` e exibindo uma casa decimal seguida de `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf` e `printf` **retornam** o número de caracteres escritos, sem contar o `'\0'` terminador. Esse é o comprimento da string que acabou de ser construída, sem uma chamada separada de `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf` não tem ideia do tamanho do buffer. O `snprintf` recebe o tamanho do buffer como seu segundo argumento e nunca escreve mais do que `size - 1` caracteres mais o `'\0'`, cortando o texto se necessário. Seu valor de retorno é o comprimento que o texto **completo** teria, então um resultado maior ou igual a `size` significa que a saída foi truncada:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer` dá o tamanho do array em bytes, que para um array de `char` é o seu número de elementos.

---

Comparar o valor de retorno do `snprintf` com o tamanho do buffer diz se tudo coube. Este é o padrão seguro para construir strings de comprimento desconhecido:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

Uma string pode ser construída em várias etapas escrevendo cada pedaço logo após o anterior. O valor de retorno indica onde o texto termina, então `buffer + n` é o endereço do terminador e o próximo `sprintf` pode continuar a partir daí:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
Somar cada valor de retorno a `n` mantém `n` igual ao comprimento total do texto construído até então.

---

Strings também podem ser combinadas sem uma string de formato. O `strcat` do `string.h` acrescenta uma cópia do seu segundo argumento ao fim do primeiro, que deve ter espaço livre suficiente, e o `strncat` acrescenta no máximo um dado número de caracteres:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
Ambos sempre adicionam o `'\0'` terminador após os caracteres acrescentados.

---

Quando não há nada para formatar, o `puts` exibe uma string seguida de uma nova linha. Ao contrário do `printf`, ele não interpreta `%`, então o texto é exibido exatamente como escrito:
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
O `puts` é a escolha certa para texto fixo, e o `printf` quando valores devem ser inseridos.

---

O `strncat` é útil quando apenas uma parte de uma string deve ser acrescentada, ou quando o pedaço acrescentado deve ser limitado a um comprimento máximo:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
Quando o limite é maior que a string, a string inteira é acrescentada.

---

Juntando tudo: uma linha de relatório combina um campo de texto alinhado à esquerda, um separador e um número alinhado à direita com um número fixo de casas decimais, escrito com `snprintf` para que nunca estoure o buffer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
Enquanto cada valor couber na sua largura, todas as linhas têm o mesmo comprimento, então as colunas se alinham quando as linhas são exibidas uma abaixo da outra.
