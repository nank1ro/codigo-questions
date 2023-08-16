Avrai potuto considerare la situazione in cui vorresti riutilizzare un pezzo di codice, cambiando solo alcuni valori.
Invece di riscrivere l'intero codice, e' molto piu' pulito definire una funzione, che può poi essere utilizzata ripetutamente.
In JavaScript usiamo la parola chiave `function` seguita dal nome della funzione:
```javascript
function saluta() {
    console.log("Ciao!");
}
saluta();
// stampa "Ciao!"
```

---

Le parentesi nella definizione di __funzione__ non devono essere vuote se vogliamo specificare i parametri

---

A volte vogliamo che una funzione __restituisca__ un valore.
Bene, possiamo usare la parola chiave `return`

---

Le funzioni possono avere parametri di ingresso multipli, che vengono scritti tra le parentesi della funzione, separati dalle virgole.
```javascript
function saluta(nome, nuovoUtente) {
  var saluto = `Ciao ${nome}!`;
  if (nuovoUtente) {
    saluto += "Benvenuto a bordo :)";
  }
  return saluto;
}
// stampa "Ciao Smith! Benvenuto a bordo :)":)"
console.log(saluta("Smith", true));
```

---

È possibile definire un valore di _default_ per qualsiasi parametro di una funzione assegnando un valore al parametro dopo il suo tipo.
Se viene definito un valore di default, si può omettere quel parametro quando si chiama la funzione
```javascript
function unaFunzione(parametroSenzaDefault, parametroConDefault = 12) {
    // esegui qui il codice della funzione
}
```

---

Un _parametro rest accetta zero o più valori di un tipo specifico.
Per aggiungere un parametro rest usiamo `...` prima del nome del parametro.
I valori passati ad un parametro rest sono resi disponibili all'interno del corpo della funzione come array.
Per esempio, un parametro rest con il nome `numeri viene reso disponibile all'interno del corpo della funzione come un array costante chiamato `numeri`

---

Nelle funzioni possiamo aggiungere un _commento opzionale_ che spieghi il funzionamento di una funzione:
```javascript
// Stampa 'Hello World' nella console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Possiamo usare `//` per commentare una singola linea, mentre `/** */` per un commento multi-linea
