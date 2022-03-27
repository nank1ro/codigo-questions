Le variabili sono contenitori per la memorizzazione di valori (dati).
Ogni variabile in Python e' un oggetto e, diversamente da altri linguaggi di programmazione, Python non ha alcun comando per dichiarare una variabile.
Per creare una variabile, dobbiamo darle un **nome** tenendo presente che non deve contenere spazi.
Viene creata una variabile nel momento in cui le si assegna per la prima volta un valore.
Un esempio di creazione di una variabile denominata `x` e':
```python
x = 1
```
In questo modo, abbiamo assegnato il valore `1` alla variabile chiamata `x`.
Se stampiamo la variabile `x` otteniamo il numero `1`:
```python
>>> print(x)
1
```

---

Le variabili vengono chiamate in questo modo perche' il valore che memorizzano può cambiare.
Possiamo aggiornare `x` usando `=` assegnando un nuovo valore:
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Possiamo anche dare alle variabili i valori di altre variabili. Qui, possiamo dare alla variabile `y` il valore di` x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Quando aggiorniamo una variabile, essa dimentica il suo valore precedente.
Qui stampiamo due volte la variabile `x` e vediamo come cambia il suo valore
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Le variabili stringa possono essere dichiarate usando virgolette singole o doppie:
```python
>>> x = "Maggio"
>>> x = 'Maggio'
```
Entrambe sono la stessa cosa

---

Se vogliamo assegnare piu' parole al nome di una variabile, utilizziamo lo **snake case**.
Bisogna quindi usare `_` per collegare le parole aggiuntive.
