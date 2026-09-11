Una **lista concatenata** memorizza i valori in **nodi** separati sparsi in memoria: ogni nodo contiene un valore e un puntatore al nodo successivo, e l'ultimo punta a `NULL`. Il puntatore interno si riferisce al tipo che si sta dichiarando, quindi la struct ha bisogno di un **tag** per dare un nome a se stessa; il nome del `typedef` non esiste ancora dentro le graffe:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
I nodi sono collegati memorizzando l'indirizzo di uno nel `next` di un altro, e i membri del nodo puntato si raggiungono con la freccia:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

I nodi dichiarati come variabili locali scompaiono quando la loro funzione restituisce, quindi le liste si costruiscono nello **heap** con `malloc` di `stdlib.h`. Essa riserva il numero di byte richiesto e ne restituisce l'indirizzo, oppure `NULL` quando la memoria è esaurita; `sizeof(Node)` è la quantità giusta per un nodo:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
La memoria dello heap non viene mai rilasciata da sola: ogni nodo ottenuto da `malloc` deve essere restituito con `free(node)` una volta che non serve più. In questi esercizi `stdlib.h` è incluso e `Node` è dichiarato sopra il tuo codice.

---

Una lista è retta da un singolo puntatore al suo primo nodo, la **testa**. Ogni altro nodo si raggiunge dalla testa seguendo `next`, e la freccia può essere concatenata: `head->next` è il secondo nodo e `head->next->next` il terzo. Una lista vuota è una testa uguale a `NULL`, e anche il `next` dell'ultimo nodo è `NULL`, quindi seguire una freccia di troppo dereferenzia `NULL` e fa andare in crash il programma.

---

Percorrere una lista, detto **attraversamento**, è un ciclo che parte dalla testa e segue `next` finché non raggiunge `NULL`. Un ciclo `for` lo esprime in una sola riga, con un puntatore come variabile di ciclo:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
Non esiste un indice: l'unico modo per raggiungere un nodo è attraverso il puntatore memorizzato in quello che lo precede.

---

Aggiungere un nodo **all'inizio** lo crea, lo fa puntare alla testa attuale e lo restituisce come nuova testa. Chi chiama memorizza il risultato nella propria variabile testa:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Inserire in una lista vuota funziona allo stesso modo: il nuovo nodo punta a `NULL` e diventa l'intera lista.

---

Liberare una lista significa liberare ogni nodo, un passo di attraversamento alla volta. Il puntatore `next` deve essere salvato **prima** che il nodo sia liberato, perché un nodo liberato non deve più essere letto, nemmeno il suo `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Scrivere `free(head)` e poi `head = head->next` legge memoria appena rilasciata, il che è un comportamento indefinito. `free(NULL)` è consentito e non fa nulla, quindi una lista vuota non ha bisogno di casi speciali.

---

Una lista non memorizza la sua lunghezza: va contata con un attraversamento. La forma `while` del ciclo mantiene il puntatore all'esterno, il che è comodo quando il corpo del ciclo aggiorna altre variabili:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Per una lista vuota il corpo del ciclo non viene mai eseguito e il conteggio resta `0`.

---

Aggiungere un nodo **in fondo** richiede l'ultimo nodo, quello il cui `next` è `NULL`. La funzione cammina finché non lo trova, poi vi aggancia il nuovo nodo e restituisce la testa invariata:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Quando la lista è vuota non c'è un ultimo nodo fino a cui camminare: il nuovo nodo è semplicemente restituito come testa.

---

Cercare in una lista è un attraversamento che confronta ogni valore e si ferma alla prima corrispondenza. La funzione restituisce un puntatore al nodo trovato, oppure `NULL` quando raggiunge la fine della lista senza corrispondenze:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Restituire il nodo anziché il valore permette a chi chiama di modificarlo o di usarlo come punto di partenza per un'altra operazione.

---

Dopo `free(p)` la variabile `p` contiene ancora il vecchio indirizzo, ma la memoria a cui punta non è più tua: `p` è ora un **puntatore pendente**. Leggere o scrivere attraverso di esso, o liberarlo una seconda volta, è un comportamento indefinito: il programma può stampare il vecchio valore, stampare dati senza senso o andare in crash, e il compilatore non si lamenterà. Quando un puntatore deve sopravvivere alla `free`, assegnagli `NULL` subito dopo, così ogni uso successivo viene intercettato da un controllo su `NULL`.

---

Inserire **dopo** un dato nodo non richiede attraversamento: il nuovo nodo subentra al successore di `node`, poi `node` viene fatto puntare a quello nuovo:
```c
new_node->next = node->next;
node->next = new_node;
```
L'ordine delle due assegnazioni conta: impostare prima `node->next` sovrascriverebbe l'unico puntatore al resto della lista, e quei nodi andrebbero persi. Inserire dopo l'ultimo nodo funziona anch'esso, poiché il suo `next` è `NULL`.

---

Rimuovere il primo nodo è l'immagine speculare di `push_front`: salva l'indirizzo del secondo nodo, libera il primo e restituisce l'indirizzo salvato come nuova testa. Chi chiama memorizza il risultato nella propria variabile testa:
```c
Node *next = head->next;
free(head);
return next;
```
Fare pop finché la testa è `NULL` libera l'intera lista, un nodo per chiamata.

---

Rimuovere un nodo in mezzo richiede il nodo **prima** di esso, quindi l'attraversamento mantiene due puntatori: `prev`, il nodo già visitato, e `cur`, quello in esame. Quando `cur` corrisponde, si fa in modo che `prev->next` lo salti e `cur` viene liberato. Se la corrispondenza è la testa stessa, `prev` è ancora `NULL` e la nuova testa è `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Quando nessun nodo corrisponde, la lista viene restituita invariata.

---

Invertire una lista gira tutti i puntatori `next` al contrario, sul posto, usando tre puntatori: `prev` è la parte già invertita, `head` il nodo in lavorazione e `next` una copia del resto della lista, salvata prima che il collegamento venga cambiato. A ogni passo il nodo corrente viene fatto puntare indietro a `prev`, poi sia `prev` che `head` avanzano:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Quando `head` raggiunge `NULL` ogni collegamento è stato invertito e `prev` è la nuova testa.

---

Una lista concatenata è economica dove un array è costoso, e viceversa. Aggiungere o rimuovere **all'inizio** sono un paio di assegnazioni di puntatori, qualunque sia la lunghezza, mentre un array dovrebbe spostare ogni elemento. D'altra parte i nodi non sono contigui, quindi non esiste `list[i]`: raggiungere l'n-simo nodo, l'ultimo o la lunghezza totale significa camminare dalla testa attraverso ogni nodo di mezzo. I programmi che aggiungono in fondo spesso mantengono un secondo puntatore all'ultimo nodo, la **coda**, per evitare quell'attraversamento.

---

Unendo il tutto: una lista è spesso costruita a partire da un array. Inserire all'inizio inverte l'ordine, quindi l'array viene percorso **all'indietro**, dall'ultimo elemento al primo, e il primo elemento finisce in testa. Il programma poi stampa la lista con un attraversamento e la libera nodo per nodo, così che ogni `malloc` sia abbinata a una `free`.
