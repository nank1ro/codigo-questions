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
