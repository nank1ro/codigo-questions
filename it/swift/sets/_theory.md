Un **Set** (insieme) è una collezione che memorizza valori dello stesso tipo senza un ordine definito e, soprattutto, **senza duplicati**: ogni valore compare al massimo una volta.
I set sono perfetti quando ti interessa solo *quali* valori sono presenti, non quante volte o in quale posizione.
Dichiari un set con il tipo `Set<Element>` e un literal in stile array:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
L'annotazione di tipo è obbligatoria: senza di essa Swift creerebbe un array.
Se il literal contiene un valore più di una volta, il set ne conserva solo una copia:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
La proprietà `count` indica quanti valori distinti contiene il set.

---

Come gli array, i set possono essere costanti (`let`) o variabili (`var`). Solo un set `var` può essere modificato dopo la creazione.
Per creare un set vuoto chiami l'inizializzatore del tipo, perché un literal vuoto `[]` da solo non direbbe a Swift quale tipo di elemento usare:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
La proprietà `isEmpty` è `true` quando il set non ha elementi, esattamente come con gli array.

---

Poiché un set non memorizza mai lo stesso valore due volte, il suo `count` è il numero di valori *distinti*, indipendentemente da quante volte ciascuno è stato scritto nel literal.

---

Per verificare se un valore è presente in un set usa il metodo `contains(_:)`, che restituisce un `Bool`:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
Questo controllo è molto veloce su un set, anche con migliaia di elementi, ed è uno dei motivi principali per preferire un set a un array per i test di appartenenza.

---

Un set `var` può essere modificato con `insert(_:)` e `remove(_:)`:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
Inserire un valore già presente non ha alcun effetto, e rimuovere un valore assente non causa un errore.
`remove(_:)` restituisce il valore rimosso come optional (`nil` quando non è stato rimosso nulla), così puoi verificare se la rimozione è effettivamente avvenuta.
Per svuotare completamente un set chiama `removeAll()`.

---

Puoi scorrere un set con `for`-`in`, ma ricorda che un set **non ha un ordine definito**: gli elementi possono uscire in qualsiasi ordine, e tale ordine può cambiare tra un'esecuzione e l'altra.
Quando l'ordine è importante, chiama prima `sorted()`: restituisce un nuovo **array** con gli elementi in ordine crescente, lasciando il set invariato.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```
