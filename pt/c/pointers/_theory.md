Toda variável vive em algum lugar da memória, e esse lugar tem um número chamado **endereço**. O operador `&`, lido como "endereço de", dá o endereço de uma variável:
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
O especificador `%p` imprime um endereço; o número exato muda de uma execução para outra, então programas nunca dependem dele.
Um endereço é armazenado em uma variável **ponteiro**. Um ponteiro é declarado com o tipo para o qual ele aponta seguido de `*`:
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
Diz-se que `p` agora **aponta para** `x`. Dois ponteiros são iguais quando guardam o mesmo endereço, então `p == &x` é verdadeiro.

---

Um ponteiro por si só é apenas um endereço. Para ler o valor armazenado naquele endereço, você **desreferencia** o ponteiro com o operador `*`:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` significa "o valor para o qual `p` aponta", e é um `int` como o próprio `x`. O mesmo símbolo `*` tem dois papéis: em uma declaração `int *p` ele diz "isto é um ponteiro", em uma expressão `*p` ele segue o ponteiro até o valor.

---

Um ponteiro desreferenciado também pode ser **atribuído**. Escrever em `*p` armazena o novo valor no endereço guardado por `p`, então a variável para a qual ele aponta muda:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` e `*p` são dois nomes para a mesma memória. Atribuir a `p` sem o `*` mudaria, em vez disso, **qual endereço** o ponteiro guarda, não o valor armazenado nele.

---

Um ponteiro que ainda não aponta para nada deve guardar `NULL`, uma constante especial definida em `stdio.h` e `stddef.h` que significa "nenhum endereço":
```c
int *p = NULL;
```
Desreferenciar um ponteiro `NULL` é um erro em tempo de execução que trava o programa, então um ponteiro que pode ser `NULL` é verificado antes do uso:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Como `NULL` é zero, `if (p)` é uma abreviação comum para `if (p != NULL)`. Um ponteiro declarado sem inicializador contém lixo de memória, não `NULL`, então sempre inicialize os ponteiros.

---

Um ponteiro pode apontar para qualquer tipo: `double *`, `char *`, `bool *` e assim por diante. O tipo na declaração diz ao compilador quantos bytes ler quando o ponteiro é desreferenciado e o que eles significam:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
Um ponteiro deve corresponder ao tipo da variável para a qual aponta; `int *p = &price;` é rejeitado pelo compilador. `NULL` é o único valor que serve para um ponteiro de qualquer tipo.

---

Um ponteiro para `char` funciona como qualquer outro ponteiro: ele guarda o endereço de um único caractere, e `*p` lê ou escreve esse caractere:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
Ler por meio de um ponteiro e escrever por meio dele podem ser misturados livremente: `*p = *p + 1` transforma `'A'` em `'B'`.

---

Um ponteiro armazena um endereço, e todo endereço tem o mesmo tamanho em uma determinada máquina, não importa qual tipo esteja armazenado nele. O `sizeof` de um ponteiro é, portanto, o mesmo para `char *`, `int *` e `double *`: `8` bytes em um sistema de 64 bits, `4` em um de 32 bits:
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
Não confunda o tamanho do ponteiro com o tamanho daquilo para o que ele aponta: `sizeof(p)` é o tamanho do endereço, `sizeof(*p)` é o tamanho do valor.

---

Um nome de array usado em uma expressão dá o endereço de seu **primeiro elemento**, então ele pode ser atribuído a um ponteiro diretamente:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
Somar um inteiro a um ponteiro o move para frente por esse número de **elementos**, não bytes: `p + 1` é o endereço de `numbers[1]`, e `*(p + 1)` é `20`. O compilador escala o passo pelo tamanho do tipo.
A indexação funciona em ponteiros também: `p[i]` é definido como `*(p + i)`, então `p[2]` é `30`. Isso é chamado de **aritmética de ponteiros**.

---

Como `p + 1` é o próximo elemento, `p++` move um ponteiro para o próximo elemento. Um loop pode percorrer um array avançando um ponteiro em vez de um índice:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
Cada volta imprime o elemento para o qual `p` aponta, depois move `p` um elemento para frente.

---

Quando um array é passado para uma função, ele **decai** para um ponteiro para seu primeiro elemento. É por isso que os parâmetros `int values[]` e `int *values` significam exatamente a mesma coisa, e por que a função não pode saber o comprimento por si só: ela recebe apenas um endereço.
Ponteiros para o mesmo array podem ser comparados e subtraídos. `end - start` é o número de elementos entre eles, e um loop pode mover um ponteiro de um endereço a outro:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Passar `numbers` e `numbers + 3` descreve os três primeiros elementos sem um parâmetro separado de tamanho.

---

Argumentos de função são passados **por valor**: a função recebe uma cópia, e atribuir a um parâmetro nunca muda a variável de quem chamou. Para permitir que uma função mude uma variável, passe o endereço da variável e desreferencie o ponteiro dentro dela:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
O exemplo clássico é trocar duas variáveis, o que precisa de uma cópia temporária de um valor enquanto o outro é sobrescrito.

---

Uma função pode `return` apenas um valor. Para devolver mais, ela recebe ponteiros para variáveis pertencentes a quem chamou e escreve os resultados por meio deles. Tais parâmetros são chamados de **parâmetros de saída**:
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo is 4, hi is 9
```
Quem chama declara as variáveis, passa seus endereços e as encontra preenchidas após a chamada. Muitas funções padrão usam esse padrão, que é o motivo de `scanf("%d", &n)` precisar do `&`.

---

Um ponteiro para uma struct alcança os membros com a seta `->`, e o endereço de uma struct armazenada em um array é obtido com `&items[i]`. Uma função também pode **retornar** um ponteiro, por exemplo, para o elemento que ela encontrou:
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
Quem chama então lê os membros por meio do ponteiro retornado com `->`, depois de verificar que ele não é `NULL`. Retornar um ponteiro evita copiar a struct e permite que quem chama modifique o elemento original.

---

`const` pode proteger tanto o valor quanto o ponteiro, dependendo de onde é escrito:
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
Leia a declaração da direita para a esquerda: `p` é um ponteiro para um `int` constante; `q` é um ponteiro constante para um `int`. Um ponteiro para const é a maneira usual de prometer que uma função apenas **lê** o que recebe, como em `int sum(const int *values, int size)`. Uma variável normal pode ser passada para ela; a promessa limita apenas o que a função pode fazer.

---

Um ponteiro é uma variável, então ele tem um endereço próprio, e esse endereço pode ser armazenado em um **ponteiro para ponteiro**, declarado com dois asteriscos:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` é `p`, o endereço de `x`, e `**pp` segue os dois passos para chegar a `7`. Ponteiros para ponteiros permitem que uma função mude qual endereço um ponteiro guarda: ela recebe `&p` e atribui a `*pp`.

---

Juntando tudo: uma função que percorre um array com um ponteiro, mantém um ponteiro para o melhor elemento visto até agora e o retorna, ou `NULL` quando não há nada a retornar:
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
Quem chama compara o resultado com `NULL` antes de desreferenciá-lo, e pode usar `result - values` para recuperar o índice do elemento.
