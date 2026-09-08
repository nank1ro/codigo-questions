Uma **enumeração** (`enum`) dá nomes a um conjunto de constantes inteiras relacionadas, para que você possa escrever `RED` em vez de um número solto.
Você a declara com a palavra-chave `enum`, um nome e a lista de constantes entre chaves:
```c
enum Color { RED, GREEN, BLUE };
```
Toda constante é um inteiro: a menos que você diga o contrário, a primeira é `0` e cada uma seguinte é a anterior mais um, então `RED` é `0`, `GREEN` é `1` e `BLUE` é `2`.
Como são inteiros, você as imprime com `%d`:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

A numeração continua automaticamente para quantas constantes você listar: a quarta constante é `3`, a quinta é `4`, e assim por diante.
Os nomes geralmente são escritos em maiúsculas, como outras constantes, e devem ser únicos em todo o programa: duas enumerações não podem compartilhar o nome de uma constante.

---

Você também pode dar um valor explícito a uma constante com `=`; as constantes seguintes continuam contando a partir desse valor:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Os valores explícitos não precisam ser consecutivos ou crescentes: `enum Status { OK = 200, NOT_FOUND = 404 };` é perfeitamente válido.

---

Uma enumeração também é um tipo: você pode declarar uma variável desse tipo escrevendo `enum` seguido do nome da enumeração, e atribuir a ela uma de suas constantes:
```c
enum Color favorite = GREEN;
```
Como as constantes são inteiros, você compara variáveis enum com os operadores usuais:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Uma enumeração pode ser o tipo de um parâmetro de função, exatamente como `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
Dentro da função, um `switch` é a maneira natural de tratar cada constante, porque constantes de enum podem ser usadas diretamente como rótulos `case`:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Quando cada caso de um `switch` trata uma constante, lembre-se do `break` depois de cada um, caso contrário a execução cai para o próximo caso.
Um caso `default` não é necessário se você cobrir todas as constantes da enumeração.

---

Uma função também pode retornar uma enumeração; basta usar o tipo enum como tipo de retorno e retornar uma de suas constantes:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Retornar uma constante nomeada é muito mais claro para quem chama a função do que retornar um `0` ou `1` solto.

---

Escrever `enum Color` toda vez é verboso. Com `typedef` você dá à enumeração um nome de tipo curto, e a própria enumeração pode ficar anônima:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
O novo nome `Color` é usado sozinho, sem a palavra-chave `enum` na frente dele.

---

Uma constante de enum é convertida para `int` automaticamente, então `int n = BLUE;` é válido e armazena `2`.
Fazer o caminho inverso é feito com um **cast**, escrevendo o tipo enum entre parênteses antes do inteiro:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C não verifica se o número corresponde a uma constante: `(enum Color)7` compila mesmo que nenhuma constante seja `7`, então valide os inteiros antes de convertê-los.

---

Aritmética em um valor de enum produz um `int` simples: `GREEN + 1` é `2`, não `BLUE`.
Para guardar o resultado de volta em uma variável enum ou retorná-lo de uma função, faça um cast para o tipo enum:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Combinado com o operador de resto `%`, isso permite percorrer as constantes em ciclo e voltar à primeira.

---

Um truque comum é adicionar uma constante extra no final da enumeração, geralmente chamada `COUNT`: como a numeração começa em `0`, seu valor é exatamente o número de constantes reais que vêm antes dela.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Essa sentinela permite percorrer todas as constantes sem fixar o número no código, e continua correta quando você adiciona constantes antes dela:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

A sentinela `COUNT` também é o tamanho perfeito para um array com uma posição por constante, e as constantes se tornam índices legíveis nele:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Um loop de `0` até `FRUIT_COUNT` visita cada posição, e o índice do loop pode ser convertido de volta para `enum Fruit` quando você precisar retorná-lo.

---

C não oferece nenhuma forma integrada de obter o nome de uma constante de enumeração: `printf("%d\n", SUMMER)` imprime `2`, não `Summer`. A solução habitual é uma pequena função com um `switch` que retorna a string correspondente a cada constante.

---

Valores de enum podem ser armazenados em arrays como qualquer outro inteiro: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` guarda três frutas, e cada elemento pode ser comparado com uma constante.
