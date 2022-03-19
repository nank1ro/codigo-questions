Sappiamo come ripetere il codice usando un ciclo `while`.
Come questo programma che ripete le istruzioni per stampare `ciao`.
```c
int contatore = 0;

while (contatore < 5) {
	printf("Ciao\n");
	contatore++;
}
```
Ma possiamo fare lo stesso con i cicli `for`:
```c
for (int i = 0; i < 5; i++) {
	printf("Ciao\n");
}
```

---

In un ciclo `for` possiamo specificare quante volte vogliamo che il nostro ciclo si ripeta

---

Possiamo usare `<` per eseguire il ciclo fino al numero che lo segue escluso, oppure `<=`per eseguire il ciclo fino al numero che lo segue incluso

---

La variabile chiamata `i` è la variabile contatore.
Possiamo darle il nome che vogliamo.
Conta qual è la ripetizione del ciclo in cui ci troviamo attualmente
