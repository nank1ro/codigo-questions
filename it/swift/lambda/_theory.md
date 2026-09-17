Una **closure** è un blocco di codice che puoi passare in giro e richiamare più tardi, come una funzione senza nome.
La sintassi completa dell'espressione closure mette i parametri e il tipo di ritorno tra parentesi graffe, seguiti dalla parola chiave `in` e dal corpo:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Come qualsiasi altro valore, una closure può essere memorizzata in una costante e poi richiamata usando il nome della costante:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Scrivere ogni tipo all'interno della closure è spesso superfluo. Quando la costante ha un **tipo di funzione** esplicito, Swift deduce i tipi dei parametri e del ritorno, quindi devi elencare solo i nomi dei parametri prima di `in`:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
Il tipo `(Int) -> Int` si legge "una funzione che accetta un `Int` e restituisce un `Int`".
Quando il corpo è un'unica espressione, la parola chiave `return` può essere omessa anch'essa, questo si chiama **ritorno implicito**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift va oltre: dentro una closure puoi fare riferimento agli argomenti con i **nomi abbreviati degli argomenti** `$0`, `$1`, `$2` e così via, senza dichiarare alcun parametro né la parola chiave `in`.
`$0` è il primo argomento, `$1` il secondo:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
I tipi continuano a provenire dall'annotazione `(Int, Int) -> Int`.

---

Poiché le closure sono valori, una funzione può accettarne una come parametro. Il tipo del parametro è semplicemente il tipo di funzione:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
La funzione `apply` non sa cosa fa `operation`, sa solo che accetta un `Int` e restituisce un `Int`, e la richiama come qualsiasi altra funzione.

---

Quando una closure è l'**ultimo** argomento di una funzione, puoi scriverla dopo la parentesi di chiusura della chiamata. Questa è la sintassi della **trailing closure**:
```swift
print(apply(5) { $0 + 1 }) // 6
```
Se la closure è l'unico argomento, le parentesi possono essere omesse del tutto:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Entrambe le forme richiamano esattamente la stessa funzione, la sintassi finale è solo più facile da leggere quando la closure è lunga.

---

Le closure danno il meglio di sé con i metodi degli array che ne accettano una come argomento. `map` richiama la closure su ogni elemento e restituisce un nuovo array con i risultati:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
L'array originale non viene modificato. Poiché `map` accetta una singola closure come argomento, la sintassi trailing closure è il modo abituale di richiamarlo.

---

`filter` mantiene solo gli elementi per cui la closure restituisce `true`. La closure riceve un elemento e deve restituire un `Bool`:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Gli elementi mantengono il loro ordine originale, e il risultato è un nuovo array dello stesso tipo di elemento.

---

`reduce` combina tutti gli elementi in un unico valore. Accetta un valore iniziale e una closure con due argomenti: il valore accumulato finora e l'elemento corrente. La closure restituisce il nuovo valore accumulato:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Qui `$0` inizia come `1`, poi diventa `1 * 1`, `1 * 2`, `2 * 3` e infine `6 * 4`.
Poiché `map`, `filter` e `reduce` restituiscono tutte dei valori, possono essere concatenate: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` restituisce un nuovo array ordinato. La closure riceve due elementi e restituisce `true` quando il primo deve venire **prima** del secondo:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
La closure può confrontare qualsiasi cosa, ad esempio `words.sorted { $0.count < $1.count }` ordina le stringhe dalla più corta alla più lunga.

---

Una closure può usare variabili dichiarate al di fuori del suo corpo. Le **cattura**: la variabile continua a esistere finché la closure esiste, anche dopo che la funzione che l'ha dichiarata è terminata.
Questo permette a una funzione di costruire una closure con il proprio stato privato:
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int` è il tipo di una closure senza parametri che restituisce un `Int`. Ogni chiamata alla closure restituita incrementa lo stesso `count` catturato:
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

Restituire una closure è un modo pratico per costruire funzioni personalizzate. I parametri della funzione esterna vengono catturati dalla closure che restituisce:
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
Il tipo di ritorno `(Int) -> Int` descrive la closure, e la forma abbreviata `$0` si riferisce all'argomento di quella closure, non a quello di `makeAdder`.

---

Una closure memorizzata in una costante può essere passata ovunque sia previsto un argomento di tipo closure, usando la label dell'argomento del parametro:
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

Ogni chiamata a una funzione che restituisce una closure crea una **nuova** variabile catturata. Due closure costruite da chiamate separate non condividono il loro stato:
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
Lo stato è condiviso solo tra chiamate della stessa closure.

---

Per impostazione predefinita, una closure passata a una funzione deve essere usata solo mentre quella funzione è in esecuzione. Se la funzione memorizza la closure o restituisce un'altra closure che la usa, la closure **sfugge** dalla funzione, e il suo parametro deve essere contrassegnato con `@escaping`:
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
Senza `@escaping` il compilatore segnala un errore, perché la closure restituita userebbe `task` dopo che `twice` è terminata.

---

Le closure possono essere memorizzate in array come qualsiasi altro valore. Il tipo di elemento è il tipo di funzione:
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
Scorrere un array del genere e richiamare ogni closure in sequenza costruisce una piccola **pipeline** di trasformazioni.
