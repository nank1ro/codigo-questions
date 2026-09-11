Una **lista enlazada** guarda valores en **nodos** separados dispersos en memoria: cada nodo contiene un valor y un puntero al siguiente nodo, y el último apunta a `NULL`. El puntero interior se refiere al tipo que se está declarando, así que el struct necesita una **etiqueta** para nombrarse a sí mismo; el nombre del `typedef` todavía no existe dentro de las llaves:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Los nodos se enlazan guardando la dirección de uno en el `next` de otro, y los miembros del nodo apuntado se alcanzan con la flecha:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Los nodos declarados como variables locales desaparecen cuando su función retorna, así que las listas se construyen en el **heap** con `malloc` de `stdlib.h`. Reserva el número de bytes solicitado y devuelve su dirección, o `NULL` cuando la memoria se agota; `sizeof(Node)` es la cantidad justa para un nodo:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
La memoria del heap nunca se libera por sí sola: cada nodo obtenido de `malloc` debe devolverse con `free(node)` cuando ya no se necesite. En estos ejercicios `stdlib.h` está incluido y `Node` está declarado por encima de tu código.

---

Una lista se sostiene con un único puntero a su primer nodo, la **cabeza**. Todos los demás nodos se alcanzan desde la cabeza siguiendo `next`, y la flecha se puede encadenar: `head->next` es el segundo nodo y `head->next->next` el tercero. Una lista vacía es una cabeza igual a `NULL`, y el `next` del último nodo también es `NULL`, así que seguir una flecha de más desreferencia `NULL` y hace fallar el programa.

---

Recorrer una lista, lo que se llama un **recorrido**, es un bucle que empieza en la cabeza y sigue `next` hasta llegar a `NULL`. Un bucle `for` lo expresa en una sola línea, con un puntero como variable del bucle:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
No hay índice: la única forma de alcanzar un nodo es a través del puntero guardado en el anterior.

---

Añadir un nodo al **principio** lo crea, hace que apunte a la cabeza actual y lo devuelve como la nueva cabeza. Quien llama guarda el resultado de nuevo en su variable de cabeza:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Insertar en una lista vacía funciona igual: el nodo nuevo apunta a `NULL` y se convierte en toda la lista.

---

Liberar una lista significa liberar cada nodo, un paso de recorrido cada vez. El puntero `next` debe guardarse **antes** de liberar el nodo, porque un nodo liberado ya no debe leerse, ni siquiera su `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Escribir `free(head)` y después `head = head->next` lee memoria que acaba de liberarse, lo cual es un comportamiento indefinido. `free(NULL)` está permitido y no hace nada, así que una lista vacía no necesita un caso especial.

---

Una lista no guarda su longitud: hay que contarla con un recorrido. La forma con `while` del bucle mantiene el puntero fuera, lo que resulta útil cuando el cuerpo del bucle actualiza otras variables:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Para una lista vacía el cuerpo del bucle nunca se ejecuta y el contador se queda en `0`.

---

Añadir un nodo al **final** necesita el último nodo, el que tiene `next` igual a `NULL`. La función avanza hasta encontrarlo, luego engancha el nodo nuevo ahí y devuelve la cabeza sin cambios:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Cuando la lista está vacía no hay último nodo al que llegar: el nodo nuevo simplemente se devuelve como la cabeza.

---

Buscar en una lista es un recorrido que compara cada valor y se detiene en la primera coincidencia. La función devuelve un puntero al nodo encontrado, o `NULL` cuando llega al final de la lista sin encontrar coincidencia:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Devolver el nodo en lugar del valor permite a quien llama modificarlo o usarlo como punto de partida para otra operación.

---

Después de `free(p)` la variable `p` todavía guarda la dirección antigua, pero la memoria a la que apunta ya no es tuya: `p` es ahora un **puntero colgante**. Leer o escribir a través de él, o liberarlo una segunda vez, es un comportamiento indefinido: el programa puede imprimir el valor antiguo, imprimir basura o fallar, y el compilador no se quejará. Cuando un puntero debe sobrevivir al `free`, ponlo a `NULL` justo después, de modo que cualquier uso posterior quede atrapado por una comprobación de `NULL`.

---

Insertar **después** de un nodo dado no necesita recorrido: el nodo nuevo toma el sucesor de `node`, y luego `node` se apunta al nuevo:
```c
new_node->next = node->next;
node->next = new_node;
```
El orden de las dos asignaciones importa: poner `node->next` primero sobrescribiría el único puntero al resto de la lista, y esos nodos se perderían. Insertar después del último nodo también funciona, ya que su `next` es `NULL`.

---

Quitar el primer nodo es el espejo de `push_front`: guarda la dirección del segundo nodo, libera el primero y devuelve la dirección guardada como la nueva cabeza. Quien llama guarda el resultado de nuevo en su variable de cabeza:
```c
Node *next = head->next;
free(head);
return next;
```
Hacer pop hasta que la cabeza sea `NULL` libera toda la lista, un nodo por llamada.

---

Quitar un nodo en medio necesita el nodo **anterior**, así que el recorrido mantiene dos punteros: `prev`, el nodo ya visitado, y `cur`, el que se está examinando. Cuando `cur` coincide, se hace que `prev->next` lo salte y `cur` se libera. Si la coincidencia es la propia cabeza, `prev` sigue siendo `NULL` y la nueva cabeza es `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Cuando ningún nodo coincide, la lista se devuelve sin cambios.

---

Invertir una lista gira cada puntero `next`, en el sitio, con tres punteros: `prev` es la parte ya invertida, `head` el nodo que se está procesando y `next` una copia del resto de la lista, guardada antes de cambiar el enlace. En cada paso el nodo actual se apunta hacia `prev`, y luego tanto `prev` como `head` avanzan:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Cuando `head` llega a `NULL` todos los enlaces se han girado y `prev` es la nueva cabeza.

---

Una lista enlazada es barata donde un array es caro, y al revés. Añadir o quitar al **principio** es un par de asignaciones de punteros sin importar la longitud, mientras que un array tendría que desplazar cada elemento. Por otro lado los nodos no son contiguos, así que no hay `list[i]`: alcanzar el nodo n-ésimo, el último o la longitud total significa caminar desde la cabeza por cada nodo intermedio. Los programas que añaden al final suelen guardar un segundo puntero al último nodo, la **cola**, para evitar ese camino.

---

Todo junto: una lista a menudo se construye a partir de un array. Insertar al principio invierte el orden, así que el array se recorre hacia **atrás**, desde el último elemento al primero, y el primer elemento acaba en la cabeza. El programa luego imprime la lista con un recorrido y la libera nodo a nodo, de modo que cada `malloc` vaya acompañado de un `free`.
