Gli array sono un tipo di dati che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
Un'array memorizza valori multipli di qualsiasi tipo e utilizza gli **indici** per distinguere questi valori.
È possibile assegnare gli elementi ad una lista con un'espressione della forma:
```c
tipo_dato nome_array[lunghezza_array] = {elemento1, elemento2};
```
`tipo_dato` è il tipo di dato che userai per l'array, per esempio `int`, `double`, etc.
`nome_array` è il nome della variabile che salta gli elementi.
`lunghezza_array` è la lunghezza massima che l'array può avere.
Infine, `elemento1` ed `elemento2` sono i valori che vogliamo salvare nell'array

---

È possibile accedere ad un singolo valore della lista tramite il suo indice.
Un indice è come un indirizzo che identifica il posto dell'elemento nella lista.
L'indice si inserisce direttamente dopo il nome della lista, tra le parentesi quadre, in questo modo:
```c
list_name[index];
```
Gli indici delle liste iniziano con `0`, **non** `1`! Per ottenere il primo valore della lista usiamo: `nome_lista[0]`.
Il secondo elemento della lista si trova all'indice 1: `nome_lista[1]`.

---

L'indice di una lista si comporta come qualsiasi altro nome di variabile!
Può essere usato per ottenere e assegnare valori.
Abbiamo visto come accedere ad una valore di una lista:
```c
int numeri[4] = {5, 6, 7, 8};
numeri[0]; // Gets the value 5
```
Ecco come funziona l'assegnazione:
```c
int numeri[4] = {5, 6, 7, 8};
numeri[0] = 1;
printf("%d\n", numeri[0]); // stampa il nuovo valore 1
```

---

Puoi calcolare la lunghezza in bytes di un array ottendo la `sizeof` dell'array, poi devi dividerla per la lunghezza di un elemento.
Questo funziona perché ogni elemento nell'array è dello stesso tipo, quindi ha la stezza grandezza in byte.
La risultante *lunghezza* è il numero di elementi che l'array contiene

---

Un array in C deve avere una lunghezza fissa.
Non puoi aggiungere elementi alla fine di un array, dopo averne dichiarato la grandezza.

---

In C programming, you can create an array of arrays.
Nella programmazione in C, puoi creare array di array.
Questi array sono conosciuti come array multidimensionali, per esempio:
```c
int numeri[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
