Sappiamo come ripetere il codice usando un ciclo `while`.
Come questo programma che ripete le istruzioni per stampare "ciao".
```python
contatore = 0

while contatore < 5:
    print("ciao")
    contatore += 1
```
Ma possiamo fare lo stesso con i cicli `for`:
```python
for i in range(5):
    print("ciao")
```

---

In un ciclo `for` possiamo specificare quante volte vogliamo che il nostro ciclo si ripeta con la funzione `range()`

---

Aggiungendo un numero come `5`, all'interno della funzione `range()`, significa eseguire il blocco di codice 5 volte, da `0` fino a `4`.

---

La variabile chiamata `i` e' la variabile contatore.
Possiamo darle il nome che vogliamo.
Conta qual e' la ripetizione del ciclo in cui ci troviamo attualmente

---

La funzione `range()` restituisce una sequenza di numeri, partendo da 0 di default, aumenta di 1 (di default), e si ferma prima di un numero specificato.
Questa e' la sintassi della funzione:
```python
range(inizio, fine, passo)
```
`inizio` e `passo` sono facoltativi, mentre `fine` e' obbligatorio
