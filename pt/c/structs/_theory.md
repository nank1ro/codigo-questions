Uma **struct** agrupa valores relacionados de tipos diferentes em um único novo tipo. Cada valor dentro dela é chamado de **membro**.
A declaração lista os membros entre chaves e termina com um ponto e vírgula; ela cria o tipo `struct Point`, mas ainda nenhuma variável:
```c
struct Point {
    int x;
    int y;
};
```
Uma variável desse tipo é declarada com `struct Point`, e seus membros podem ser inicializados **em ordem** com chaves, como um array:
```c
struct Point p = {3, 4}; // x is 3, y is 4
```
Os membros são lidos e escritos com o operador **ponto** `.`:
```c
printf("%d\n", p.x); // prints "3"
p.y = 10;
```

---

Inicializar membros em ordem é frágil: se a struct ganhar um membro, todos os inicializadores se deslocam. Desde o C99, um **inicializador designado** nomeia cada membro com um ponto, em qualquer ordem:
```c
struct Point p = {.y = 4, .x = 3};
```
Membros que não são listados recebem `0`, então `{.y = 5}` dá `x` igual a `0`. Isso é diferente de uma variável declarada sem nenhum inicializador, `struct Point q;`, cujos membros contêm **lixo de memória** até você atribuir valores a eles:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Uma struct pode ser passada para uma função como qualquer outro valor. O parâmetro é declarado com o nome completo do tipo, e a função lê os membros com `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
A struct deve ser declarada **antes** da função que a usa, para que o compilador já conheça seus membros.

---

Escrever `struct Point` toda vez é verboso. Com `typedef` você dá à struct um nome de tipo curto, e a própria struct pode permanecer anônima:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
O novo nome `Temperature` é usado sozinho, sem a palavra-chave `struct` na frente dele. Essa é a forma mais comum de declarar structs em programas reais.

---

Um membro pode ser, ele próprio, uma struct. Um segmento, por exemplo, é feito de dois pontos:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
A struct interna é inicializada com seu próprio par de chaves, e seus membros são acessados encadeando o operador ponto:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // prints "5"
```

---

Structs podem ser armazenadas em um array como qualquer outro tipo. Cada elemento é inicializado com suas próprias chaves, e um loop os visita um por um, indexando primeiro e depois usando o ponto:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Um array de structs é passado para uma função exatamente como um array de números: o parâmetro é escrito como `Item items[]` e, como o array não carrega seu comprimento, o tamanho é passado separadamente:
```c
int count_free(Item items[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (items[i].price == 0) {
            count++;
        }
    }
    return count;
}
```

---

Quando uma struct é passada para uma função **por valor**, a função recebe uma **cópia** dela. Alterar um membro do parâmetro altera apenas a cópia, e a variável de quem chamou permanece como estava:
```c
void reset(Point p) {
    p.x = 0; // changes the copy
}
```
Para permitir que uma função modifique a struct de quem chamou, passe seu **endereço** com `&` e declare o parâmetro como um **ponteiro**, `Point *p`. O ponteiro se refere à variável original em vez de uma cópia:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Copiar também custa tempo para structs grandes, então ponteiros são a escolha usual mesmo quando nada é modificado.

---

Através de um ponteiro, os membros são acessados com o operador **seta** `->` em vez do ponto:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` é um atalho para `(*b).size`: primeiro siga o ponteiro, depois pegue o membro. O ponto funciona apenas em uma struct, a seta apenas em um ponteiro para uma struct.
Quem chama passa o endereço de sua variável com `&`, e a mudança feita através do ponteiro fica visível após a chamada.

---

Uma função que recebe um ponteiro para uma struct pode atualizar o valor original no local. Essa é a forma padrão de escrever funções "modificadoras" em C, em que o primeiro parâmetro é a struct a ser alterada e os outros são os dados a aplicar:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
Leitura e escrita passam pela mesma seta: `p->score += 10` soma ao membro da struct à qual o ponteiro se refere.

---

Uma função também pode **retornar** uma struct. Construa-a em uma variável local e retorne-a; quem chama recebe uma cópia do valor inteiro:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
É assim que C retorna mais de um valor de uma função: agrupe-os em uma struct.

---

`sizeof` também funciona em structs, e é a forma correta de saber quanta memória uma ocupa:
```c
printf("%zu\n", sizeof(Point));
```
O tamanho é **pelo menos** a soma dos tamanhos dos membros. Pode ser maior, porque o compilador pode inserir bytes de **padding** não usados para que cada membro fique em um endereço adequado ao seu tipo: `struct { char c; int n; }` geralmente tem `8` bytes, não `5`. Nunca use um valor fixo para o tamanho de uma struct; pergunte ao `sizeof`.

---

Structs não podem ser comparadas com `==`: escrever `a == b` em duas structs é um **erro de compilação**. Compare-as **membro por membro** em vez disso, combinando os resultados com `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
O mesmo vale para `<` e `>`: você decide qual membro define a ordem.

---

Uma struct frequentemente contém texto, armazenado como um membro array de `char` com tamanho fixo:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Um membro array não pode ser atribuído com `=` depois da declaração: `p.name = "Ann"` não compila. Copie o texto para ele com `strcpy` de `string.h`, passando o membro como destino:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Apenas um inicializador com chaves na declaração aceita a string diretamente: `Person p = {"Ann", 30};`.

---

`printf` não tem especificador para uma struct inteira. A solução usual é uma pequena função que imprime os membros em um formato fixo, para que cada parte do programa mostre o valor da mesma maneira:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Juntando tudo: uma função que recebe um ponteiro para uma struct pode atualizar um membro de texto com `strcpy` através da seta, já que `item->name` é o array de `char` dentro da struct original:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Lembre-se de adicionar `#include <string.h>` no topo do seu código para usar `strcpy`.
