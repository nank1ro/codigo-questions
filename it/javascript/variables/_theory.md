Le variabili sono contenitori per la memorizzazione di valori (dati).
Ogni variabile in JavaScript è un oggetto.
Per creare una variabile, possiamo darle un **nome** tenendo presente che non deve contenere spazi.
Una variabile viene create nel momento in cui le si assegna per la prima volta un valore.
Con JavaScript dichiariamo le costanti con le parole chiavi `let` e `const`, mentre le variabili con la parola chiave `var`.
Il valore di una costante non può essere cambiato dopo che viene impostato, mentre ad una variabile possiamo impostare un nuovo valore in futuro.
Un esempio di creazione di una variabile denominata `x` è:
```javascript
var x = 1;
```
In questo modo, abbiamo assegnato il valore `1` alla variabile chiamata `x`.
Se stampiamo la variabile `x` otteniamo il numero `1`:
```javascript
console.log(x);
// stampa 1
```

---

Le variabili vengono chiamate in questo modo perche' il valore che memorizzano può cambiare.
Possiamo aggiornare `x` usando `=` assegnando un nuovo valore:
```javascript
var x = 1;
console.log(x); // stampa 1
x = 2;
console.log(x); // stampa 2
```

---

Possiamo anche dare alle variabili i valori di altre variabili.
Qui, possiamo dare alla variabile `y` il valore di` x`
```javascript
var x = 5;
var y = x;
console.log(y); // stampa 5
```

---

Quando aggiorniamo una variabile, essa dimentica il suo valore precedente.
Qui stampiamo due volte la variabile `x` e vediamo come cambia il suo valore
```javascript
var x = 5;
console.log(x); // stampa 5
x = 10;
console.log(x); // stampa 10
```

---

In JavaScript le variabili stringa possono essere dichiarate sia usando le doppie virgolette che le singole:
```javascript
let x = "Maggio";
// entrambe sono la stessa stringa
let y = 'Maggio';
console.log(x === y);
// stampa true
```

---

Se vogliamo assegnare piu' parole al nome di una variabile, utilizziamo il **camelCase**.
È la pratica di scrivere frasi in modo tale che ogni parola al centro della frase inizi con la lettera maiuscola
