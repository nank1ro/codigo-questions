Le variabili sono contenitori per la memorizzazione di valori (dati).
Ogni variabile in C è un oggetto e come altri linguaggi di programmazione, C necessita di comandi per dichiarare le variabili.
Per creare una variabile, dobbiamo darle un **tipo** e un **nome** tenendo presente che non deve contenere spazi.
Viene creata una variabile nel momento in cui le si assegna per la prima volta un valore.
Un esempio di creazione di una variabile denominata `x` e':
```c
int x = 1;
```
In questo modo, abbiamo assegnato il valore `1` alla variabile _intera_ chiamata `x`.
Se stampiamo la variabile `x` otteniamo il numero `1`:
```c
>>> printf("%i\n", x);
1
```

---

Le variabili vengono chiamate in questo modo perche' il valore che memorizzano può cambiare.
Possiamo aggiornare `x` usando `=` assegnando un nuovo valore:
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

Possiamo anche dare alle variabili i valori di altre variabili. Qui, possiamo dare alla variabile `y` il valore di `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Quando aggiorniamo una variabile, essa dimentica il suo valore precedente.
Qui stampiamo due volte la variabile `x` e vediamo come cambia il suo valore
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

In C le variabili di tipo stringa possono essere dichiarate soltanto utilizzando le doppie virgolette:
```c
char x[] = "Maggio";
```

---

Se vogliamo assegnare piu' parole al nome di una variabile, utilizziamo lo **snake case**.
Bisogna quindi usare `_` per collegare le parole aggiuntive.
