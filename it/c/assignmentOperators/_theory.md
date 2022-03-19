Abbiamo già imparato che per assegnare un valore a una variabile possiamo usare il segno `=`, come:
```c
int a = 5;
```

---

Abbiamo già inizializzato una variabile `totale`
```c
int totale = 5;
```
Ipotizziamo di voler aggiungere il numero `2` alla variabile` totale`, possiamo scrivere
```c
totale = totale + 2;
```
Ok, funziona! Ma esiste una versione piu' breve per fare la stessa cosa:
```c
totale += 2;
```
Il segno `+=` si chiama operatore di **assegnazione di addizione**.
Somma un determinato valore al valore corrente della variabile, infine assegna il risultato alla suddetta variable.

---

Abbiamo anche l'operatore di **assegnazione di sottrazione** `-=`.
La funzionalità e' la stessa dell'operatore di assegnazione di addizione, l'unica differenza e' che, ovviamente, esegue la sottrazione.
Quindi le seguenti linee di codice eseguono la stessa operazione:
```c
num = num - 5;
// è uguale a 
num -= 5;
```

---

Vediamo l'operatore di **assegnazione di moltiplicazione** `*=`.
Serve a moltiplicare la variabile per un valore e assegna il risultato alla suddetta variabile.
Quindi le seguenti linee di codice eseguono la stessa operazione:
```c
num = num * 5;
// è uguale a
num *= 5;
```

---

Vediamo l'operatore di **assegnazione di divisione** `/=`.
Serve a dividere la variabile per un valore e assegna il risultato alla suddetta variabile.
Quindi le seguenti linee di codice eseguono la stessa operazione:
```c
num = num / 5;
// è uguale a
num /= 5;
```

---

Vediamo l'operatore di **assegnazione di modulo** `%=`.
Serve a calcolare il modulo della variabile e un valore e assegna il risultato alla suddetta variabile.
Quindi le seguenti linee di codice eseguono la stessa operazione:
```c
num = num % 5;
// è uguale a
num %= 5;
```
