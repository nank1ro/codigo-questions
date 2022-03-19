Le variabili sono contenitori per la memorizzazione di valori (dati).
Ogni variabile in Kotlin è un oggetto.
Per creare una variabile, possiamo darle un __nome__ tenendo presente che non deve contenere spazi.
Una variabile viene create nel momento in cui le si assegna per la prima volta un valore.
In Kotlin dichiariamo le costanti con la parola chiave `val` (abbreviazione di _valore_) e le
variabili con la parola chiave `var` (abbreviazione di _variabile_).
Il valore di una costante non può essere cambiato dopo che viene impostato, mentre una variabile può essere impostata con un valore diverso in futuro
Un esempio di creazione di una variabile denominata `x` è:
```kotlin
var x = 1
```
In questo modo, abbiamo assegnato il valore `1` alla variabile chiamata `x`.
Se stampiamo la variabile `x` otteniamo il numero `1`:
```kotlin
println(x) // stampa 1
```

---

Le variabili vengono chiamate in questo modo perche' il valore che memorizzano può cambiare.
Possiamo aggiornare `x` usando `=` assegnando un nuovo valore:
```kotlin
var x = 1
println(x) // stampa 1
x = 2
println(x) // stampa 2
```

---

Possiamo anche dare alle variabili i valori di altre variabili.
Qui, possiamo dare alla variabile `y` il valore di` x`
```kotlin
var x = 5
var y = x
println(y) // stampa 5
```

---

Quando aggiorniamo una variabile, essa dimentica il suo valore precedente.
Qui stampiamo due volte la variabile `x` e vediamo come cambia il suo valore
```kotlin
var x = 5
println(x) // stampa 5
x = 10
println(x) // stampa 10
```

---

Le variabili stringa possono essere dichiarate usando le doppie virgolette:
```kotlin
val x = "Maggio"
```

---

Se vogliamo assegnare piu' parole al nome di una variabile, utilizziamo il **camelCase**.
È la pratica di scrivere frasi in modo tale che ogni parola al centro della frase inizi con la lettera maiuscola
