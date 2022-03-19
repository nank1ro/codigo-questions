In C possiamo usare la funzione `printf' con un'espressione, per concatenare due o più stringhe insieme, come:
```c
>>> char c = 'C';
>>> printf("Ciao %c!\n", c);
Ciao C!
```
`%c` viene usato per inserire un singolo carattere

---

Le stringhe formattate ci consentono di mostrare espressioni come stringhe con numeri, senza ricevere alcun errore.
Per mostrare un numero intero usiamo l'espressione `%i`

---

Ogni stringa formattata consiste in due parti, il testo che vogliamo includere e l'espressione che vogliamo formattare all'interno del testo

---

Successivamente, aggiungiamo il tipo diverso di valore.
Come qui, con `%i`

---

L'inserimento di variabili come `amici` permette di mostrare il relativo valore

---

Possiamo usare le espressioni per inserire i valori quante volte vogliamo all'interno di una stringa formattata
