C é uma linguagem **tipada estaticamente**: toda variável é declarada com um tipo que determina o que ela pode armazenar e quanta memória ocupa.
Os três tipos que você mais vai usar são:
- `int` para números inteiros, como `30` ou `-4`
- `double` para números com parte decimal, como `1.75`
- `char` para um único caractere, escrito entre aspas simples como `'A'`

Cada tipo tem seu próprio **especificador de formato** do `printf`: `%d` imprime um `int`, `%f` imprime um `double` (com seis casas decimais por padrão) e `%c` imprime um `char`:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// prints "30 1.750000 A"
```
Usar o especificador errado para um tipo imprime lixo, então sempre combine-os corretamente.

---

C tem dois tipos de ponto flutuante: `float` (precisão simples, cerca de 7 dígitos significativos) e `double` (precisão dupla, cerca de 15 dígitos significativos).
Um literal decimal como `1.75` é um `double`; para escrever um literal `float`, adicione o sufixo `f`, como em `1.75f`.
Prefira `double`, a menos que a memória seja limitada: ele é o padrão e é mais preciso.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Uma função que retorna um resultado decimal deve declarar `double` como seu tipo de retorno, e parâmetros `double` aceitam tanto argumentos inteiros quanto decimais:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` imprime seis casas decimais, o que raramente é o que você quer. Coloque uma precisão entre `%` e `f` para escolher quantas casas decimais mostrar: `%.2f` imprime duas casas decimais, `%.1f` imprime uma, e o valor é **arredondado**, não cortado:
```c
double price = 9.987;
printf("%.2f\n", price); // prints "9.99"
printf("%.1f\n", price); // prints "10.0"
```
Um `float` é impresso com os mesmos especificadores que um `double`: quando passado para `printf`, ele é convertido automaticamente para `double`.

---

O resultado de `/` depende dos tipos de seus operandos.
Quando **ambos** os operandos são inteiros, o resultado é um inteiro e a parte decimal é descartada: `7 / 2` é `3`, não `3.5`.
Quando **pelo menos um** operando é um valor de ponto flutuante, a divisão mantém as casas decimais: `7 / 2.0` é `3.5`.
```c
printf("%d\n", 7 / 2);     // prints "3"
printf("%f\n", 7 / 2.0);   // prints "3.500000"
```
Escrever o literal como `2.0` em vez de `2` é a forma mais simples de forçar uma divisão de ponto flutuante.

---

C converte entre tipos numéricos **implicitamente** quando um valor é atribuído a uma variável de tipo diferente.
- um `int` armazenado em um `double` é ampliado sem perdas: `double d = 3;` faz `d` valer `3.0`
- um `double` armazenado em um `int` é **truncado**: `int n = 3.99;` faz `n` valer `3` (os compiladores geralmente avisam sobre isso)

A conversão acontece apenas no momento da atribuição. A expressão à direita é calculada primeiro, com seus próprios tipos:
```c
double d = 7 / 2;
```
Aqui `7 / 2` é uma divisão inteira que resulta em `3`, e só então `3` é convertido para `3.0`.

---

Quando a conversão implícita não é o que você quer, ou você quer torná-la visível, use uma **conversão explícita** (cast): escreva o tipo de destino entre parênteses antes do valor.
```c
double x = 3.99;
int n = (int) x;   // n is 3
```
Fazer o cast de um valor de ponto flutuante para `int` **trunca em direção a zero**: `(int) 3.99` é `3` e `(int) -2.5` é `-2`, nenhum arredondamento acontece.
O cast se aplica apenas ao valor logo depois dele, então `(int) x * 2` faz o cast de `x` primeiro e depois multiplica.

---

Um cast é a forma padrão de obter uma divisão de ponto flutuante entre duas variáveis `int`: faça o cast de **um operando** para `double` antes de dividir.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Fazer o cast do resultado inteiro, como em `(double) (total / count)`, é um erro comum: a divisão inteira já aconteceu e as casas decimais foram perdidas.

---

Um `char` é, na verdade, um pequeno inteiro: ele armazena o **código ASCII** do caractere.
`'A'` é `65`, `'a'` é `97` e `'0'` é `48`, e caracteres consecutivos têm códigos consecutivos.
É por isso que você pode fazer aritmética com caracteres:
- `'a' + 1` é `98`, o código de `'b'`
- `'7' - '0'` é `55 - 48`, ou seja, o número `7`

O mesmo valor pode ser impresso como um caractere com `%c` ou como um número com `%d`:
```c
char c = 'A';
printf("%c %d\n", c, c); // prints "A 65"
```

---

Letras maiúsculas e minúsculas estão `32` posições distantes na tabela ASCII: `'A'` é `65` e `'a'` é `97`.
Subtrair `32` de uma letra minúscula, portanto, dá sua versão maiúscula, e o resultado pode ser armazenado de volta em um `char`:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` não é o único tipo inteiro. Modificadores mudam seu tamanho e intervalo:
- `short` usa menos memória e tem um intervalo menor (geralmente de -32768 a 32767)
- `long` tem um intervalo maior (em sistemas de 64 bits, cerca de ±9 quintilhões)
- `unsigned` remove o sinal: `unsigned int` vai de `0` a cerca de 4 bilhões, mas nunca pode ser negativo

Um literal que deve ser `long` recebe o sufixo `L`, um `unsigned` recebe o sufixo `U`, e cada tipo tem seu próprio especificador:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // prints "8000000000 40"
```
`%ld` imprime um `long`, `%u` um `unsigned int` e `%lu` um `unsigned long`. Um `int` simples, na maioria dos sistemas, comporta valores de até cerca de 2 bilhões, então `5000000000` não cabe nele.

---

O operador `sizeof` informa quantos **bytes** um tipo ou uma variável ocupa. Seu resultado tem o tipo `size_t`, que é impresso com `%zu`:
```c
printf("%zu\n", sizeof(int));  // prints "4" on most systems
```
O padrão garante apenas que `sizeof(char)` é `1` e que `short <= int <= long`, mas em um sistema típico de 64 bits os tamanhos são: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` é frequentemente usado para verificar quanta memória uma variável ocupa sem fixar o número no código.

---

Todo tipo inteiro tem um intervalo limitado, e o cabeçalho `limits.h` dá um nome a esses limites: `INT_MAX` e `INT_MIN` para `int`, `LONG_MAX` para `long`, `UINT_MAX` para `unsigned int`, e assim por diante.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // prints "2147483647" on most systems
```
Ultrapassar `INT_MAX` com um tipo com sinal é **comportamento indefinido**: o programa pode dar a volta, travar, ou fazer qualquer outra coisa. Verifique antes de calcular:
```c
if (a <= INT_MAX - b) { /* a + b is safe */ }
```
Observe que a verificação subtrai em vez de somar, porque o próprio `a + b` já poderia estourar.

---

Diferentemente dos tipos com sinal, a aritmética **unsigned** é bem definida quando sai do intervalo: o valor **dá a volta**, como um odômetro.
Somar `1` a `UINT_MAX` dá `0`, e subtrair `1` de `0` dá `UINT_MAX` (`4294967295` quando `unsigned int` tem 32 bits):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // prints "0"
```
É por isso que um loop que decrementa uma variável `unsigned` "até ficar negativa" nunca para: um valor unsigned nunca fica abaixo de `0`.

---

Desde o C99, o cabeçalho `stdbool.h` fornece o tipo `bool` com as constantes `true` (`1`) e `false` (`0`).
Um `bool` é um tipo inteiro com apenas dois valores, então converter qualquer número para `bool` dá `true` para todo valor diferente de zero e `false` para `0`. Isso é diferente de converter para `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, because 0.5 is not zero
int n = 0.5;   // 0, because the decimals are truncated
```
Comparações como `x != 0` já produzem um resultado compatível com `bool`, e uma função que retorna `bool` documenta que ela responde a uma pergunta de sim ou não.

---

Uma operação aritmética é realizada no tipo de seus operandos, **não** no tipo da variável que recebe o resultado.
Assim, `long big = n * n;` com um `n` do tipo `int` multiplica dois valores `int`, estoura se o produto for grande demais, e só então armazena o resultado (já incorreto) no `long`.
Faça o cast de um operando **antes** da operação para calcular no tipo mais amplo:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, computed as long
```
A mesma regra explica por que `(double) total / count` funciona: o cast muda o tipo do operando, e a divisão segue esse tipo.

---

Juntando tudo: escolha o tipo a partir do tipo de valor, combine cada especificador do `printf` com o tipo de seu argumento, e faça o cast quando um cálculo precisar acontecer em um tipo diferente do de seus operandos.
