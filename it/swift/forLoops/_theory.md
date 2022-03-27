Sappiamo come ripetere il codice usando un ciclo `while`.
Come questo programma che ripete le istruzioni per stampare `ciao`.
```swift
var contatore = 0

while contatore < 5 {
	print("ciao")
	contatore += 1
}
```
Ma possiamo fare lo stesso con i cicli `for`:
```swift
for i in 0..<5 {
	print("ciao")
}
```

---

In un ciclo `for` possiamo specificare quante volte vogliamo che il nostro ciclo si ripeta

---

Possiamo usare `..<` per iterare escludendo l'indice destro, oppure `...` per iterare includendo l'indice destro

---

La variabile chiamata `i` e' la variabile contatore.
Possiamo darle il nome che vogliamo.
Conta qual e' la ripetizione del ciclo in cui ci troviamo attualmente

---

La funzione `stride()` restituisce una sequenza di numeri.
Richiede i parametri _from_, _to_ e _by_.
Questa è la sintassi della funzione:
```swift
stride(from:to:by:)
```
Ricordati che il valore `to` viene escluso

---

Con la funzione `stride()` possiamo anche usare i range inclusivi:
```swift
stride(from:through:by:)
```
In questo caso il valore `through` è incluso

---

In Swift abbiamo anche il ciclo `forEach`.
In effetti, il `forEach` richiama la suddetta closure su ogni elemento della sequenza nello stesso ordine di un ciclo `for..in`
```swift
// questo è un array, lo vedremo presto
let numeri: [Int] = [1, 3, 5, 7, 9] 
numeri.forEach { num in 
	print(num)
}
```
Il metodo `forEach` è diverso dal ciclo `for..in` in due modi importanti:
1. Le istruzioni `break` o `continue` non possono essere utilizzati per uscire o saltare le chiamate della closure.
2. L'utilizzo della dichiarazione di `return` nella closure del corpo uscirà solo dalla closure e non dallo scopo esterno, inoltre non salterà le chiamate successive.
