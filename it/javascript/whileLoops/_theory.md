Spesso in programmazione, e' necessario ripetere un blocco di codice, ad esempio:
```javascript
console.log("2 secondi");
console.log("3 secondi");
console.log("4 secondi");
console.log("5 secondi");
```
Questo produce il seguente output:
```javascript
2 secondi
3 secondi
4 secondi
5 secondi
```
Ovviamente, per lunghe dichiarazioni passeremmo molto tempo a scrivere il codice, ma fortunatamente possiamo usare i cicli.
Usiamo il ciclo `while`, in modo da ottenene lo stesso output di sopra.
```javascript
var contatore = 2;
while (contatore <= 5) {
    console.log(`${contatore} secondi`);
    contatore += 1;
}
```
Quindi abbiamo creato una variabile `contatore` assegnandole `2`, il valore iniziale.
Poi abbiamo usato la parola chiave `while` che eseguirà il blocco di codice finche' la condizione `contatore <= 5` è `true`.
All'interno del blocco di codice, **NON** dovremo dimenticare la linea di codice `contatore += 1`.
In quanto incrementa il valore del `contatore`, altrimenti il nostro ciclo sarà infinito

---

Per controllare le ripetizioni di un ciclo `while`, si inizializza una variabile con un determinato numero.
Chiamiamo questa variabile contatore

---

Poi, nella condizione del `while` usiamo una comparazione per confrontare la variabile `contatore` con un numero.

---

All'interno del blocco di codice, per fermare il ciclo `while`, incrementiamo la variabile `contatore`

---

L'ordine di scrittura del codice influisce sull'output

---

In Swift abbiamo anche la variante **repeat-while** del ciclo `while`.
Esegue un singolo passaggio attraverso il blocco del ciclo _prima_ di considerare la condizione del ciclo.
Poi continua a ripetere il loop fino a quando la condizione è `false`.
Il ciclo __repeat-while__ in Swift è analogo al ciclo __do-while__ in altri linguaggi di programmazione
