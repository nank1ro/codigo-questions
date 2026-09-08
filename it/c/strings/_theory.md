Il C non ha un tipo stringa dedicato: una **stringa** è un array di `char` che termina con un carattere speciale, il **terminatore nullo** `'\0'`.
Il modo più semplice per crearne una è un letterale stringa tra doppi apici:
```c
char name[] = "Codigo";
```
Il compilatore conta i caratteri e aggiunge il `'\0'` alla fine per te.
Per stampare una stringa usa il segnaposto `%s`:
```c
printf("%s\n", name);
// stampa "Codigo"
```

---

Il terminatore nullo occupa spazio in memoria: il letterale `"hi"` occupa 3 byte, `'h'`, `'i'` e `'\0'`.
Quando dichiari tu stesso la dimensione, lascia sempre spazio per esso:
```c
char word[6] = "hello"; // 5 lettere + '\0'
```
Senza il terminatore, il C non ha modo di sapere dove finisce la stringa.

---

L'header `string.h` fornisce funzioni che lavorano sulle stringhe.
`strlen` restituisce il numero di caratteri prima del terminatore nullo (il terminatore stesso non viene contato):
```c
strlen("hello"); // 5
```
Una funzione che riceve una stringa dichiara il parametro come `char *text`, un puntatore al primo carattere.
In questi esercizi `string.h` e `ctype.h` sono già inclusi sopra il tuo codice.

---

Poiché una stringa è un array, ogni carattere ha un indice a partire da `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Un singolo carattere si stampa con `%c`. I caratteri possono anche essere sostituiti:
```c
word[0] = 'K'; // ora word è "Koding"
```

---

Poiché ogni stringa termina con `'\0'`, puoi percorrerla senza conoscerne in anticipo la lunghezza: continua finché il carattere corrente non è il terminatore.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Un array non può essere assegnato con `=` dopo la sua dichiarazione:
```c
char copy[20];
copy = "Codigo"; // errore
```
Per copiare una stringa usa `strcpy(destination, source)` da `string.h`.
La destinazione deve essere abbastanza grande da contenere tutti i caratteri più il `'\0'`.

---

`strcat(destination, source)` aggiunge `source` alla fine di `destination`:
```c
char text[20] = "Hello";
strcat(text, " World");
// ora text è "Hello World"
```
Come con `strcpy`, l'array di destinazione deve avere abbastanza spazio per il risultato.

---

Due stringhe non possono essere confrontate con `==`: questo confronterebbe i loro indirizzi in memoria, non i loro caratteri.
Usa invece `strcmp(first, second)`, che restituisce `0` quando le due stringhe contengono esattamente gli stessi caratteri:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // non 0
```

---

`strcmp` confronta le stringhe carattere per carattere usando i loro codici carattere.
Il risultato è negativo quando la prima stringa viene prima della seconda, positivo quando viene dopo, e `0` quando sono uguali:
```c
strcmp("a", "b"); // negativo
strcmp("b", "a"); // positivo
```

---

`strncpy(destination, source, n)` copia al massimo `n` caratteri.
Se `source` è più lunga di `n`, non viene scritto alcun `'\0'`: devi terminare tu stesso il risultato.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix è "Cod"
```

---

L'header `ctype.h` fornisce funzioni che lavorano su un singolo carattere.
`toupper(c)` restituisce la versione maiuscola di una lettera e `tolower(c)` quella minuscola; qualsiasi altro carattere viene restituito invariato:
```c
char letter = toupper('a'); // 'A'
```

---

Una stringa viene passata a una funzione come puntatore, quindi una funzione che riceve `char *text` può modificare direttamente i caratteri del chiamante.
Combinare un ciclo fino a `'\0'` con `toupper` converte un'intera stringa:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` funziona come `printf`, ma scrive il testo formattato in un array di caratteri invece che sullo schermo:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer è "3 items"
```
Il buffer deve essere abbastanza grande per tutto il testo e il suo `'\0'`.

---

`sprintf` è un modo comodo per trasformare un numero in testo: una volta che è in un buffer, ogni funzione per stringhe può lavorarci.
