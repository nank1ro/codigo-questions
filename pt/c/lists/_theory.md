Uma **lista ligada** armazena valores em **nós** separados espalhados pela memória: cada nó guarda um valor e um ponteiro para o próximo nó, e o último aponta para `NULL`. O ponteiro interno se refere ao tipo que está sendo declarado, então a struct precisa de uma **tag** para nomear a si mesma; o nome do `typedef` ainda não existe dentro das chaves:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Os nós são ligados armazenando o endereço de um no `next` do outro, e os membros do nó apontado são acessados com a seta:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Nós declarados como variáveis locais desaparecem quando sua função retorna, então as listas são construídas no **heap** com `malloc` de `stdlib.h`. Ele reserva o número de bytes solicitado e retorna o endereço deles, ou `NULL` quando a memória se esgota; `sizeof(Node)` é a quantidade certa para um nó:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
A memória do heap nunca é liberada por conta própria: cada nó obtido de `malloc` deve ser devolvido com `free(node)` assim que não for mais necessário. Nesses exercícios `stdlib.h` está incluído e `Node` é declarado acima do seu código.

---

Uma lista é mantida por um único ponteiro para seu primeiro nó, a **cabeça**. Todos os outros nós são alcançados a partir da cabeça seguindo o `next`, e a seta pode ser encadeada: `head->next` é o segundo nó e `head->next->next` o terceiro. Uma lista vazia é uma cabeça igual a `NULL`, e o `next` do último nó também é `NULL`, então seguir uma seta a mais desreferencia `NULL` e trava o programa.

---

Percorrer uma lista, chamado de **percurso**, é um loop que começa na cabeça e segue o `next` até alcançar `NULL`. Um loop `for` o expressa em uma única linha, com um ponteiro como variável do loop:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
Não há índice: a única forma de alcançar um nó é pelo ponteiro armazenado no nó anterior.

---

Adicionar um nó no **início** o cria, faz ele apontar para a cabeça atual e o retorna como a nova cabeça. Quem chama armazena o resultado de volta em sua variável de cabeça:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Inserir em uma lista vazia funciona da mesma forma: o novo nó aponta para `NULL` e se torna a lista inteira.

---

Liberar uma lista significa liberar cada nó, um passo de percurso por vez. O ponteiro `next` deve ser salvo **antes** de o nó ser liberado, porque um nó liberado não deve mais ser lido, nem mesmo o seu `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Escrever `free(head)` e depois `head = head->next` lê memória que acabou de ser liberada, o que é comportamento indefinido. `free(NULL)` é permitido e não faz nada, então uma lista vazia não precisa de caso especial.

---

Uma lista não armazena seu comprimento: ele precisa ser contado com um percurso. A forma `while` do loop mantém o ponteiro do lado de fora, o que é útil quando o corpo do loop atualiza outras variáveis:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Para uma lista vazia o corpo do loop nunca é executado e a contagem permanece `0`.

---

Adicionar um nó no **fim** precisa do último nó, aquele cujo `next` é `NULL`. A função caminha até encontrá-lo, então anexa o novo nó ali e retorna a cabeça inalterada:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Quando a lista está vazia não há último nó para alcançar: o novo nó é simplesmente retornado como a cabeça.

---

Buscar em uma lista é um percurso que compara cada valor e para na primeira correspondência. A função retorna um ponteiro para o nó encontrado, ou `NULL` quando chega ao fim da lista sem correspondência:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Retornar o nó em vez do valor permite que quem chama o modifique ou o use como ponto de partida para outra operação.

---

Depois de `free(p)` a variável `p` ainda contém o endereço antigo, mas a memória para a qual ela aponta não é mais sua: `p` agora é um **ponteiro pendente**. Ler ou escrever através dele, ou liberá-lo uma segunda vez, é comportamento indefinido: o programa pode imprimir o valor antigo, imprimir lixo ou travar, e o compilador não reclamará. Quando um ponteiro deve sobreviver ao `free`, defina-o como `NULL` logo depois, para que qualquer uso posterior seja capturado por uma verificação de `NULL` em vez disso.

---

Inserir **depois de** um determinado nó não precisa de percurso: o novo nó assume o sucessor de `node`, então `node` é apontado para o novo:
```c
new_node->next = node->next;
node->next = new_node;
```
A ordem das duas atribuições importa: definir `node->next` primeiro sobrescreveria o único ponteiro para o resto da lista, e esses nós seriam perdidos. Inserir depois do último nó também funciona, já que o seu `next` é `NULL`.

---

Remover o primeiro nó é o espelho de `push_front`: salve o endereço do segundo nó, libere o primeiro e retorne o endereço salvo como a nova cabeça. Quem chama armazena o resultado de volta em sua variável de cabeça:
```c
Node *next = head->next;
free(head);
return next;
```
Remover até a cabeça ser `NULL` libera a lista inteira, um nó por chamada.

---

Remover um nó no meio precisa do nó **anterior** a ele, então o percurso mantém dois ponteiros: `prev`, o nó já visitado, e `cur`, o que está sendo examinado. Quando `cur` corresponde, `prev->next` é feito para pulá-lo e `cur` é liberado. Se a correspondência é a própria cabeça, `prev` ainda é `NULL` e a nova cabeça é `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Quando nenhum nó corresponde, a lista é retornada inalterada.

---

Inverter uma lista vira cada ponteiro `next` para o outro lado, no próprio lugar, com três ponteiros: `prev` é a parte já invertida, `head` o nó sendo processado e `next` uma cópia do resto da lista, salvo antes de o elo ser alterado. A cada passo o nó atual é apontado de volta para `prev`, então tanto `prev` quanto `head` avançam:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Quando `head` alcança `NULL` todos os elos foram invertidos e `prev` é a nova cabeça.

---

Uma lista ligada é barata onde um array é caro, e vice-versa. Adicionar ou remover no **início** é um par de atribuições de ponteiros não importa o comprimento, enquanto um array teria que deslocar cada elemento. Por outro lado os nós não são contíguos, então não há `list[i]`: alcançar o n-ésimo nó, o último ou o comprimento total significa caminhar da cabeça por todos os nós intermediários. Programas que anexam com frequência mantêm um segundo ponteiro para o último nó, a **cauda**, para evitar essa caminhada.

---

Juntando tudo: uma lista muitas vezes é construída a partir de um array. Inserir no início inverte a ordem, então o array é percorrido **de trás para frente**, do último elemento ao primeiro, e o primeiro elemento acaba na cabeça. O programa então imprime a lista com um percurso e a libera nó por nó, para que cada `malloc` seja correspondido por um `free`.
