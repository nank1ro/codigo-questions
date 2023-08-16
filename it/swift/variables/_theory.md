Le variabili sono contenitori per la memorizzazione di valori (dati).
Ogni variabile in Swift è un oggetto.
Per creare una variabile, possiamo darle un **nome** tenendo presente che non deve contenere spazi.
Una variabile viene create nel momento in cui le si assegna per la prima volta un valore.
Con Swift dichiariamo le costanti con la parola chiave `let` e le variabili con la parola chiave `var`.
Il valore di una costante non può essere cambiato dopo che viene impostato, mentre una variabile può essere impostata con un valore diverso in futuro
Un esempio di creazione di una variabile denominata `x` è:
```swift
var x = 1
```
In questo modo, abbiamo assegnato il valore `1` alla variabile chiamata `x`.
Se stampiamo la variabile `x` otteniamo il numero `1`:
```swift
>>> print(x)
1
```

---

Le variabili vengono chiamate in questo modo perche' il valore che memorizzano può cambiare.
Possiamo aggiornare `x` usando `=` assegnando un nuovo valore:
```swift
>>> var x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Possiamo anche dare alle variabili i valori di altre variabili.
Qui, possiamo dare alla variabile `y` il valore di` x`
```swift
var x = 5
var y = x
print(y) // stampa 5
```

---

Quando aggiorniamo una variabile, essa dimentica il suo valore precedente.
Qui stampiamo due volte la variabile `x` e vediamo come cambia il suo valore
```swift
var x = 5
print(x) // stampa 5
x = 10
print(x) // stampa 10
```

---

Le variabili stringa possono essere dichiarate usando le doppie virgolette:
```swift
>>> let x = "Maggio"
```

---

Se vogliamo assegnare piu' parole al nome di una variabile, utilizziamo il **camelCase**.
È la pratica di scrivere frasi in modo tale che ogni parola al centro della frase inizi con la lettera maiuscola
