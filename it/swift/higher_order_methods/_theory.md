Una **funzione di ordine superiore** è una funzione che prende un'altra funzione come argomento, ne restituisce una, o entrambe le cose. Hai già incontrato `map`, `filter`, `reduce` e `sorted(by:)`: prendono una closure e la applicano agli elementi di una collezione. Swift ne ha molte altre, e conoscerle ti permette di sostituire lunghi cicli con una singola riga leggibile.
`compactMap` funziona come `map`, ma la closure restituisce un optional e i risultati `nil` vengono scartati:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` è `nil`, quindi quell'elemento scompare e il risultato è un `[Int]`, non un `[Int?]`.

---

`flatMap` è per le closure che restituiscono un **array**: invece di costruire un array di array, unisce tutti gli array restituiti in un unico risultato piatto:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
La closure può anche trasformare ogni array interno prima che venga appiattito, per esempio `teams.flatMap { $0.reversed() }` dà `["Bob", "Ann", "Cid"]`.

---

Le tre varianti di `map` differiscono solo per ciò che la closure restituisce:
- `map`: qualsiasi valore, un risultato per elemento
- `compactMap`: un optional, i risultati `nil` vengono scartati
- `flatMap`: un array, tutti i risultati vengono uniti in un unico array

La closure passata a `flatMap` può a sua volta chiamare `map` sull'array interno, annidando una trasformazione dentro l'altra:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` costruisce un nuovo valore accumulato a ogni passo, il che è dispendioso quando il risultato è un array o un dizionario. `reduce(into:)` passa alla closure l'accumulatore come parametro `inout`, così può essere modificato sul posto senza `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` crea un dizionario vuoto, e `result[word, default: 0]` legge il conteggio corrente oppure `0` quando la chiave è assente.

---

Alcune funzioni di ordine superiore rispondono a una domanda sulla collezione invece di trasformarla. Tutte prendono una closure che restituisce un `Bool`:
- `first(where:)` restituisce il primo elemento che soddisfa la closure, oppure `nil` se non c'è nessuno
- `contains(where:)` restituisce `true` se almeno un elemento la soddisfa
- `allSatisfy` restituisce `true` se ogni elemento la soddisfa

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
A differenza di `filter`, `first(where:)` si ferma alla prima corrispondenza e non costruisce un nuovo array.

---

`contains(where:)` e `allSatisfy` sostituiscono il pattern comune di un ciclo con una variabile flag. Entrambi si fermano appena la risposta è nota: `contains(where:)` alla prima corrispondenza, `allSatisfy` al primo elemento che fallisce.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` è la forma con trailing closure di `contains(where:)`, da non confondere con `contains(_:)`, che cerca un valore specifico.

---

Le funzioni di ordine superiore funzionano su qualsiasi array, inclusi gli array dei tuoi struct. Concatenare `filter` e poi `map` è il modo abituale per selezionare alcuni elementi ed estrarre un valore da ciascuno:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Farlo nell'ordine opposto, prima `map` e poi `filter`, perderebbe la proprietà `pages` prima che il controllo possa usarla.

---

Quando una closure legge solo una proprietà, puoi passare una **key path** invece: `\.name` significa "la proprietà `name` dell'elemento", e `map(\.name)` è uguale a `map { $0.name }`.
Ordinare in base a una proprietà usa la consueta closure a due argomenti, che confronta quella proprietà su entrambi gli elementi:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Per ordinare in base a **più di un criterio**, confronta la prima proprietà e passa alla seconda solo quando i primi valori sono uguali:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Qui le persone sono ordinate per età, e le persone con la stessa età sono ordinate per nome. La closure deve restituire `true` solo quando il primo elemento dovrebbe venire prima del secondo, quindi il caso di parità passa al confronto successivo.

---

`enumerated()` trasforma un array in una sequenza di coppie `(offset, element)`, così una closure può usare la posizione di ogni elemento insieme al suo valore:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Poiché ogni coppia è una tupla, la closure può anche destrutturarla: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` accoppia gli elementi di due sequenze posizione per posizione, producendo una sequenza di tuple. Si ferma alla fine della più corta:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Dentro la closure `$0` è l'elemento della prima sequenza e `$1` quello della seconda. `zip` è una funzione libera, non un metodo: si scrive `zip(a, b)`, non `a.zip(b)`.

---

`forEach` è il gemello di ordine superiore del ciclo `for-in`: chiama la closure una volta per elemento, in ordine. La differenza sta in come esci dal ciclo. In un `for-in` puoi uscire con `break` o proseguire con `continue`; dentro una closure di `forEach` `break` e `continue` non sono consentiti, e `return` termina solo la **chiamata corrente** della closure, poi l'elemento successivo viene elaborato come al solito:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Usa `forEach` per un breve effetto collaterale su ogni elemento, e `for-in` quando ti serve fermarti in anticipo.

---

`Dictionary(grouping:by:)` divide una collezione in un dizionario di array. La closure calcola la **chiave** di ogni elemento, e tutti gli elementi con la stessa chiave finiscono nello stesso array:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` trasforma ogni valore di un dizionario mantenendo le chiavi, quindi è il passo naturale dopo il raggruppamento:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` prende elementi dall'inizio **finché** la closure restituisce `true`, e si ferma al primo elemento che fallisce, anche se gli elementi successivi potrebbero passare di nuovo. `drop(while:)` è il suo complementare: salta quella stessa sequenza iniziale e restituisce tutto il resto:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Entrambi restituiscono un `ArraySlice`, una vista sull'array originale che si stampa come un array e può essere trasformato in uno con `Array(...)`.

---

Puoi scrivere le tue funzioni di ordine superiore. Una funzione che prende una closure e **restituisce una nuova closure** costruita a partire da essa è un pattern comune: la closure restituita cattura quella originale, quindi il parametro deve essere `@escaping`.
Per esempio, `negate` trasforma un predicato nel suo opposto, pronto per essere passato a `filter`:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Nota che `filter(negate(isEven))` passa la closure come argomento normale, senza la sintassi della trailing closure.

---

`map` e `filter` su un array sono **eager**: ognuno elabora l'intero array e ne costruisce uno nuovo prima che il passo successivo parta. Su una grande collezione, o quando ti serve solo il primo risultato, è lavoro sprecato.
La proprietà `lazy` restituisce una vista le cui operazioni girano solo quando un elemento viene effettivamente richiesto, un elemento alla volta attraverso tutta la catena:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Qui solo `1, 2, ..., 8` vengono elevati al quadrato: `first(where:)` chiede elementi finché uno non soddisfa la condizione, e la catena si ferma lì. Senza `lazy`, `map` eleverebbe al quadrato tutti i 1000 numeri prima.
