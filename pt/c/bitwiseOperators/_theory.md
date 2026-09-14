Todo inteiro é armazenado na memória como uma sequência de **bits**, cada um sendo `0` ou `1`. O número `12` é armazenado como `00001100` e o número `10` como `00001010`.
Os **operadores bit a bit** trabalham nesses bits individuais em vez de no número como um todo. O operador **AND** `&` compara os dois valores bit por bit e mantém um `1` apenas onde *ambos* os bits são `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// prints "8"
```
Padrões de bits geralmente são escritos como literais hexadecimais como `0x0C`, porque cada dígito hexadecimal representa exatamente quatro bits. Sempre use tipos `unsigned` para trabalhar com bits e exiba-os com `%u`.

---

O operador **OR** `|` compara os dois valores bit por bit e mantém um `1` onde *pelo menos um* dos bits é `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// prints "14"
```
`|` é a maneira usual de mesclar dois padrões de bits em um só.

---

O operador **XOR** `^` (ou exclusivo) mantém um `1` apenas onde os dois bits são *diferentes*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// prints "6"
```
Uma propriedade útil decorre disso: aplicar o mesmo XOR duas vezes devolve o valor original.

---

O operador **NOT** `~` recebe um único operando e inverte todos os seus bits: cada `0` se torna `1` e cada `1` se torna `0`.
Um `unsigned int` possui 32 bits, então `~0x0Fu` inverte todos os 32 e produz um número muito grande. Para manter apenas o byte de que você precisa, combine `~` com `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// prints "240"
```
`~` tem precedência maior que `&`, então é aplicado primeiro.
Não confunda `~` com o `!` lógico: `!` olha para o valor como um todo e responde `0` ou `1`, enquanto `~` reescreve cada bit.

---

O operador **left shift** `<<` move cada bit um número de casas para a esquerda e preenche com zeros as casas liberadas à direita:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// prints "12"
```
Deslocar à esquerda por `n` multiplica o valor por 2 elevado a `n`.
Dois erros tornam um programa C indefinido: deslocar à esquerda um valor negativo e deslocar por uma quantidade igual ou maior que a largura do tipo (32 para `unsigned int`). Trabalhar com valores **unsigned** mantém você longe do primeiro.

---

O operador **right shift** `>>` move cada bit para a direita; os bits que caem na extremidade direita são descartados. Em um valor unsigned, as casas liberadas à esquerda são preenchidas com zeros:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// prints "3"
```
Deslocar à direita por `n` divide um valor unsigned por 2 elevado a `n`, descartando o resto.
Deslocar à direita um valor *negativo* não é portátil, o que é mais uma razão para manter o trabalho com bits em tipos `unsigned`.

---

Cada operador bit a bit binário tem uma forma de **atribuição composta** que atualiza uma variável no próprio lugar: `&=`, `|=`, `^=`, `<<=` e `>>=`.
```c
unsigned int x = 12;
x &= 10;  // same as x = x & 10;
x |= 1;   // same as x = x | 1;
x ^= 3;   // same as x = x ^ 3;
x <<= 1;  // same as x = x << 1;
x >>= 2;  // same as x = x >> 2;
```
Eles ficam mais legíveis do que repetir o nome da variável e são a maneira usual de alterar os bits de uma variável de flags.

---

Uma **máscara** é um valor cujos bits selecionam a parte de outro valor de que você precisa. Combinada com `&`, uma máscara mantém os bits que são `1` na máscara e zera todos os outros:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// prints "11"
```
`0x0F` mantém os quatro bits mais baixos, chamados de **nibble** baixo, e `0xFF` mantém os oito bits mais baixos, um byte inteiro.

---

Os bits são numerados a partir de `0`, começando no mais à direita, então `1u << n` é uma máscara com apenas o bit `n` ligado.
Para **definir** um único bit, ou seja, ligá-lo sem tocar nos outros, faça o OR do valor com essa máscara:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// prints "6"
```
Se o bit já estava ligado, o valor não muda, o que torna seguro repetir a definição de um bit.

---

Para **limpar** um único bit, ou seja, desligá-lo, faça o AND do valor com o *inverso* da máscara:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// prints "5"
```
`~(1u << 1)` é um valor com todos os bits ligados, exceto o bit `1`, então o AND mantém todo o resto intacto.

---

Para **alternar** um único bit, ou seja, invertê-lo independentemente do seu estado atual, faça o XOR do valor com a máscara:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// prints "7"
```
Como o XOR se desfaz a si mesmo, alternar o mesmo bit uma segunda vez devolve o valor original.

---

Para **testar** um único bit, faça o AND do valor com a máscara e verifique se o resultado é diferente de `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // prints "1"
printf("%d\n", (value & (1u << 2)) != 0); // prints "0"
```
O AND não produz `1`: ele produz `0` ou a própria máscara, que para o bit `3` é `8`. É por isso que o resultado é comparado com `!= 0` em vez de ser usado como resposta direta.

---

**Flags** são máscaras nomeadas, cada uma usando um bit diferente, que podem todas ser armazenadas em uma única variável. Elas são combinadas com `|` e lidas de volta com `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// prints "1"
```
Um único `unsigned int` pode, portanto, carregar 32 respostas sim/não independentes.

---

Antes do C23 não havia especificador de formato que exibisse um número em binário, e literais como `0b1010` também não eram C padrão. Para mostrar os bits você mesmo escreve o loop: percorra do bit mais alto até o bit `0` e exiba `(value >> i) & 1u` a cada passo.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// prints "0101"
```
Deslocar o valor para baixo por `i` traz o bit `i` para a posição mais à direita, onde `& 1u` o isola.

---

Contar quantos bits de um valor são `1` é um loop de bits clássico: teste o bit mais baixo com `& 1u`, adicione-o a um contador, depois desloque o valor uma casa para a direita com `>>=` e repita até não sobrar nada.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count is 2
```
O loop sempre termina, porque um valor unsigned deslocado à direita tempo suficiente se torna `0`.

---

Vários números pequenos geralmente são empacotados dentro de um valor maior. Para ler um deles de volta, primeiro desloque-o para baixo até que comece no bit `0`, depois aplique uma máscara para remover tudo acima dele:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// prints "18", the 0x12 byte
```
Deslocar primeiro e aplicar a máscara depois é a ordem a lembrar: a máscara sempre descreve o campo depois que ele chegou ao fundo.
