Una **string** è un pezzo di testo. In Swift scrivi un literal di string tra virgolette doppie, e il suo tipo è `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Come per qualsiasi altro valore, `let` crea una costante che non può essere modificata e `var` crea una variabile che può esserlo.
Swift deduce il tipo `String` dal literal, quindi l'annotazione di tipo è opzionale.

---

L'**interpolazione di stringhe** inserisce il valore di un'espressione all'interno di un literal di stringa. Racchiudi l'espressione tra `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Qualsiasi tipo può essere interpolato: numeri, booleani e altre stringhe vengono tutti convertiti automaticamente in testo.

---

Due stringhe possono essere unite con l'operatore `+`, che produce una nuova stringa:
```swift
let full = "Hello" + " " + "world" // Hello world
```
Per aggiungere testo alla fine di una variabile stringa esistente usa `+=`. La variabile deve essere dichiarata con `var`, perché il suo valore cambia:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

La proprietà `count` restituisce il numero di caratteri di una stringa, e `isEmpty` è `true` quando la stringa non ha alcun carattere:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Ogni carattere viene contato, inclusi spazi e punteggiatura.

---

Una `String` è una collezione di valori `Character`. Un `Character` è una singola lettera, cifra, simbolo o spazio, e si scrive con le stesse virgolette doppie di una stringa, quindi serve un'annotazione di tipo per ottenerne uno:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Controllare `isEmpty` è preferibile a confrontare `count` con `0`: si legge meglio e non deve contare ogni carattere.

---

Un **literal di stringa multilinea** inizia e finisce con tre virgolette doppie `"""`, ciascuna sulla propria riga. Ogni riga tra di esse diventa parte della stringa, e le interruzioni di riga vengono preservate:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
Questo stampa le due righe esattamente come sono state scritte. Le virgolette di chiusura `"""` determinano anche l'indentazione: qualsiasi spazio bianco prima di esse viene rimosso dall'inizio di ogni riga.

---

Poiché una stringa è una collezione di caratteri, puoi iterarla con un ciclo `for`-`in`. Ogni iterazione ti dà un `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
Un `Character` può essere confrontato con `==` a un literal di carattere, quindi contare quante volte un carattere appare è solo un ciclo con un contatore.

---

A differenza degli array, le stringhe non possono essere indicizzate con un intero come `text[2]`: alcuni caratteri occupano più memoria di altri, quindi Swift usa un tipo dedicato `String.Index` per indicare una posizione.
`startIndex` è la posizione del primo carattere ed `endIndex` è la posizione *dopo* l'ultimo. Per spostarti da un indice usa `index(_:offsetBy:)`, poi indicizza la stringa con il risultato:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Spostarsi oltre la fine della stringa causa un crash a runtime, quindi l'offset deve rimanere entro `count`.

---

Lavorare con gli indici è prolisso, quindi Swift offre delle scorciatoie per i casi più comuni:
- `first` e `last` restituiscono il primo e l'ultimo carattere come `Character?` opzionale (`nil` per una stringa vuota)
- `prefix(n)` restituisce i primi `n` caratteri e `suffix(n)` gli ultimi `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` e `suffix` restituiscono una `Substring`, una vista sul testo originale. Per salvarla come una vera `String`, racchiudila in `String(...)`. Se `n` è più grande di `count`, ottieni semplicemente l'intera stringa.

---

Tre metodi rispondono alle domande più comuni sul contenuto di una stringa, e ciascuno restituisce un `Bool`:
- `contains(_:)` è `true` quando la stringa include il testo indicato (o il carattere) in qualsiasi punto
- `hasPrefix(_:)` è `true` quando la stringa inizia con il testo indicato
- `hasSuffix(_:)` è `true` quando la stringa finisce con il testo indicato
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Tutti e tre distinguono tra maiuscole e minuscole: `"Swift".hasPrefix("s")` è `false`.

---

Poiché `contains`, `hasPrefix` e `hasSuffix` restituiscono dei booleani, si combinano naturalmente con `||` e `&&` per costruire controlli più complessi.

---

`uppercased()` e `lowercased()` restituiscono una **nuova** stringa con ogni lettera convertita in maiuscolo o minuscolo. La stringa originale non viene modificata:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Entrambi sono metodi, quindi non dimenticare le parentesi.

---

Convertire in minuscolo è il modo abituale per confrontare del testo ignorando maiuscole e minuscole: due stringhe che differiscono solo nel maiuscolo/minuscolo diventano uguali una volta che entrambe sono convertite in minuscolo.

---

`split(separator:)` scompone una stringa in un array di parti ovunque compaia il carattere separatore. `joined(separator:)` fa il contrario: incolla gli elementi di un array in un'unica stringa, mettendo il separatore tra di essi:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Come `prefix`, anche `split` restituisce valori `Substring`; racchiudine uno in `String(...)` se devi salvarlo come `String`.

---

Dividere su uno spazio è il modo più semplice per scomporre una frase in parole, e unire è il modo per ricostruire il testo a partire da un array.

---

Il framework Foundation aggiunge molti metodi aggiuntivi per le stringhe. Uno dei più utili è `replacingOccurrences(of:with:)`, che restituisce una nuova stringa in cui ogni occorrenza del primo testo viene sostituita dal secondo:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Ricordati di scrivere `import Foundation` in cima al file, altrimenti il metodo non è disponibile. Le chiamate ai metodi possono essere concatenate, quindi `text.lowercased().replacingOccurrences(of: " ", with: "_")` è valido.

---

Le stringhe possono essere confrontate con gli stessi operatori dei numeri. `==` verifica che due stringhe abbiano esattamente gli stessi caratteri, mentre `<` e `>` le confrontano in ordine alfabetico, carattere per carattere:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
Il confronto distingue tra maiuscole e minuscole, e ogni lettera maiuscola viene **prima** di ogni lettera minuscola, quindi `"B" < "a"` è `true`.

---

Un `Character` non è una `String`, quindi non può essere unito direttamente a una stringa con `+`. Convertilo prima con `String(...)`:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Combinare questo con un ciclo `for`-`in` ti permette di ricostruire una stringa un carattere alla volta, ad esempio mettendo ogni nuovo carattere davanti a quelli raccolti finora.
