Gli array sono un tipo di dati che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
Un'array memorizza valori multipli di qualsiasi tipo e utilizza gli **indici** per distinguere questi valori.
E' possibile assegnare gli elementi ad un array con un'espressione della forma:
```javascript
var arrayName = [item1, item2];
```

---

E' possibile accedere ad un singolo valore dell'array tramite il suo indice.
Un indice e' come un indirizzo che identifica il posto dell'elemento nell'array.
L'indice si inserisce direttamente dopo il nome dell'array, tra le parentesi, in questo modo:
```javascript
nomeArray[index];
```
Gli indici degli array iniziano con `0`, **non** `1`! Per ottenere il primo valore dell'array usiamo: `nomeArray[0]`.
Il secondo elemento dell'array si trova all'indice 1: `nomeArray[1]`.

---

L'indice di un'array si comporta come qualsiasi altro nome di variabile!
Può essere usato per ottenere e assegnare valori.
Abbiamo visto come accedere ad una valore di un'array:
```javascript
var nomi = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Stampa il valore "Jeremiah"
console.log(nomi[0]);
```
Ecco come funziona l'assegnazione:
```javascript
var nomi = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assegna il nuovo valore "Jordan"
nomi[0] = "Jordan";
// Stampa il valore "Jordan"
console.log(nomi[0]);
```

---

Proprio come le stringhe, gli array hanno una lunghezza **length**.
La lunghezza di un array e' il numero di elementi che contiene

---

Un'array non deve avere una lunghezza fissa.
Puoi aggiungere elementi alla fine di un'array quando vuoi!
Per aggiungere un elemento ad un'array usiamo la funzione `push()`:
```javascript
var lettere = ["a", "b"];
lettere.push("c");
console.log(lettere);
// stampa ["a", "b", "c"]
```

---

A volte si vuole accedere solo a una parte di un'array.
Considera il seguente codice:
```javascript
let numeri = [1, 2, 3, 4];
let fetta = numeri.fetta(1, 3);
console.log(fetta);
// stampa [2, 3]
```
Per prima cosa, creiamo un array chiamato `numeri`.
Poi, prendiamo una sottosezione dell'array e la memorizziamo nel nuovo array `fetta`.
Lo facciamo definendo gli indici che vogliamo includere dopo il nome: `numeri.slice(1, 3)`.
Ricordati che l'indice destro viene escluso

---

In JavaScript possiamo dividere un'array come vogliamo!
```javascript
// Ottieni i primi due elementi
nomeArray.slice(0, 2);
// Ottieni dal quarto fino all'ultimo elemento
nomeArray.slice(3);
```
Se la tua porzione di array include il primo o l'ultimo elemento di un'array, l'indice non deve essere dichiarato

---

Gli elementi dell'array possono essere di qualsiasi tipo
```javascript
var nomeArray = ["uno", 2, true];
```
Difatti, sopra abbiamo, in quest'ordine, una stringa, un intero e un booleano.
Ma possiamo anche avere un'array di array, e così via!

---

A volte è necessario cercare un elemento in un array.
In JavaScript possiamo usare il metodo `indexOf()`:
```javascript
var nomi = ["Trevor", "Zac", "Glenn"];
console.log(nomi.indexOf('Zac'));
// stampa 1
```
Il codice qui sopra stampa il primo indice che contiene la stringa `"Zac"`, `1` in questo caso.
Possiamo anche inserire elementi in un'array in un indice specifico, usando il metodo `splice()`:
```javascript
nomi.splice(1, 0, "Ali");
// stampa ["Trevor", "Ali", "Zac", "Glenn"]
```
Il codice qui sopra inserisce `"Ali"` all'indice `1`, e incrementa l'indice di 1 a tutti gli elementi che lo seguono
Il secondo valore `0` è riferito al parametro _deleteCount_; in questo caso, non cancelliamo alcun elemento nell'array, ma se avessimo specifigattoo `1`, il valore `Zac` sarebbe stato rimosso dall'array

---

In JavaScript possiamo far scorrere un array in un ciclo in un modo molto semplice usando le parole chiave `for..of`:
```javascript
var numeri = [1, 2, 3];
for (num of numeri) {
    console.log(num);
}
// prints 1, 2, 3 
```
Un nome di variabile segue la parola chiave `for`, ad essa verrà assegnato il valore di ogni elemento dell'array a turno.
