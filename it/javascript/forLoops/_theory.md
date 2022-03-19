Sappiamo come ripetere il codice usando un ciclo `while`.
Come questo programma che ripete le istruzioni per stampare `ciao`.
```javascript
var contatore = 0;

while (contatore < 5) {
	console.log("ciao");
	contatore++;
}
```
Ma possiamo fare lo stesso con i cicli `for`:
```javascript
for (let i = 0; i < 5; i++) {
	console.log("ciao");
}
```

---

In un ciclo `for` possiamo specificare quante volte vogliamo che il nostro ciclo si ripeta.

---

Possiamo usare `<` per iterare escludendo l'indice destro, oppure `<=` per iterare includendo l'indice destro

---

La variabile chiamata `i` e' la variabile contatore.
Possiamo darle il nome che vogliamo.
Conta qual e' la ripetizione del ciclo in cui ci troviamo attualmente

---

In JavaScript abbiamo anche il ciclo `forEach`.
In effetti, il `forEach` richiama la suddetta closure su ogni elemento della sequenza nello stesso ordine di un ciclo `for..in`
```javascript
// questo è un array, lo vedremo presto
let numeri = [1, 3, 5, 7, 9];
numeri.forEach((num) => console.log(num));}
```
Il metodo `forEach` è diverso dal ciclo `for..in` in due modi importanti:
1. Le istruzioni `break` o `continue` non possono essere utilizzati per uscire o saltare le chiamate della closure.
2. L'utilizzo della dichiarazione di `return` nella closure del corpo uscirà solo dalla closure e non dallo scopo esterno, inoltre non salterà le chiamate successive.
NOTA: `=>` questo viene chiamato _funzione a freccia_ ed è una sintassi più breve per le funzioni che sostituisce le parentesi graffe {} e restituisce il valore (se necessario)
