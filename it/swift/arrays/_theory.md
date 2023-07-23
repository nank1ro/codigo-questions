Gli array sono un tipo di dati che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
Un'array memorizza valori multipli di qualsiasi tipo e utilizza gli **indici** per distinguere questi valori.
E' possibile assegnare gli elementi ad un array con un'espressione della forma:
```swift
var nomeArray: [tipoElementi] = [elemento1, elemento2]
```
`tipoElementi` sta ad indicare il tipo degli elementi all'interno dell'array, per esempio, può essere `Int`, `String`, `Any`...

---

E' possibile accedere ad un singolo valore dell'array tramite il suo indice.
Un indice e' come un indirizzo che identifica il posto dell'elemento nell'array.
L'indice si inserisce direttamente dopo il nome dell'array, tra le parentesi, in questo modo:
```swift
nomeArray[indice]
```
Gli indici degli array iniziano con `0`, **non** `1`! Per ottenere il primo valore dell'array usiamo: `nomeArray[0]`.
Il secondo elemento dell'array si trova all'indice 1: `nomeArray[1]`.

---

L'indice di un'array si comporta come qualsiasi altro nome di variabile!
Può essere usato per ottenere e assegnare valori.
Abbiamo visto come accedere ad una valore di un'array:
```swift
var nomi = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Stampa il valore "Jeremiah"
print(nomi[0])
```
Ecco come funziona l'assegnazione:
```swift
var nomi = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assegna il nuovo valore "Jordan"
nomi[0] = "Jordan"
// Stampa il valore "Jordan"
print(nomi[0])
```

---

Proprio come le stringhe, gli array hanno una lunghezza `count`.
La lunghezza di un array e' il numero di elementi che contiene

---

Un'array non deve avere una lunghezza fissa.
Puoi aggiungere elementi alla fine di un'array quando vuoi!
Per aggiungere un elemento ad un'array usiamo la funzione `append()`:
```swift
var lettere = ["a", "b"]
lettere.append("c")
print(lettere)
// stampa ["a", "b", "c"]
```

---

A volte si vuole accedere solo a una parte di un'array.
Considera il seguente codice:
```swift
let numeri = [1, 2, 3, 4]
let fetta = numeri[1...2]
print(fetta)
// stampa [2, 3]
```
Per prima cosa, creiamo un array chiamato `numeri`.
Poi, prendiamo una sottosezione dell'array e la memorizziamo nel nuovo array `fetta`.
Lo facciamo definendo gli indici che vogliamo includere dopo il nome: `numeri[1...2]`.
In Swift possiamo includere l'ultimo indice utilizzando`...`, ma possiamo anche escluderlo usando `..<`

---

In Swift possiamo dividere un'array come vogliamo!
```swift
// Ottieni i primi due elementi
nomeArray[..<2]
// Ottieni dal quarto fino all'ultimo elemento
nomeArray[3...]
```
Se la tua porzione di array include il primo o l'ultimo elemento di un'array, l'indice non deve essere incluso

---

Gli elementi dell'array possono essere di qualsiasi tipo, se specifichiamo il tipo `Any`:
```swift
var nomeArray: [Any] = ["uno", 2, true]
```
Difatti, sopra abbiamo, in quest'ordine, una stringa, un intero e un booleano.
Ma possiamo anche avere un'array di array, e così via!

---

A volte è necessario cercare un elemento in un array.
In Swift possiamo usare il metodo `firstIndex()`:
```swift
var nomi: [String] = ["Trevor", "Zac", "Glenn"]
if let indice = nomi.firstIndex(of: "Zac") {
  print(indice)
}
// stampa 1
```
Il codice qui sopra stampa il primo indice che contiene la stringa `"Zac"`, `1` in questo caso.
Possiamo anche inserire elementi in un'array in un indice specifico, usando il metodo `insert()`:
```swift
nomi.insert("Ali", at: 1)
// stampa ["Trevor", "Ali", "Zac", "Glenn"]
```
Il codice qui sopra inserisce `"Ali"` all'indice `1`, e incrementa l'indice di 1 a tutti gli elementi che lo seguono

---

In Swift possiamo far scorrere un array in un ciclo in un modo molto semplice usando le parole chiave `for..in`:
```swift
var numeri = [1, 2, 3]
for num in numeri {
    print(num)
}
// stampa 1, 2, 3 
```
Un nome di variabile segue la parola chiave `for`, ad essa verrà assegnato il valore di ogni elemento dell'array a turno.

---

Le **tuple** sono come gli array, ma possiamo dare un nome agli elementi ed usare questi nomi per riferirci ad essi.
Per creare una tupla usiamo le parentesi tonde `()`. 
```swift
var persona = (nome: "John", cognome: "Smith")
var nome = persona.nome // John
var cognome = persona.cognome // Smith
```
