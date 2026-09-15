Un lavoro non sempre finisce subito: scaricare un file, leggere da un database, attendere un timer. Se un programma si fermasse e aspettasse, nel frattempo non potrebbe succedere nient'altro. Swift risolve il problema con le **funzioni asincrone**.

Una funzione marcata **`async`** può mettersi in pausa a metà e riprendere più tardi. La parola chiave va dopo la lista dei parametri, prima della freccia:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Anche chiamarla è diverso: devi scrivere **`await`** davanti alla chiamata. `await` segna il punto esatto in cui il programma può mettersi in pausa e ti restituisce il valore semplice quando la funzione ha finito:
```swift
let n = await fetchNumber()
print(n)
// stampa 42
```
In uno script Swift il top level supporta già `await`, quindi puoi chiamare le funzioni asincrone direttamente, senza alcuna configurazione extra. Dimenticare `async` o `await` è un errore di compilazione, non un bug silenzioso.

---

Una funzione asincrona è pur sempre una funzione ordinaria: può accettare parametri e restituire un valore di qualsiasi tipo. Cambiano solo due cose, la parola chiave `async` nella firma e `await` in ogni punto di chiamata:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// stampa 10.0
```
Il valore restituito è un normale `Double`, non un involucro: quando `await` ha finito, lo usi esattamente come al solito.

---

Le funzioni asincrone di solito sono costruite una sopra l'altra. Dentro una funzione `async` puoi fare `await` di qualsiasi altra funzione `async`, e il risultato si usa come un qualsiasi valore normale:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// stampa 15
```
`await` è permesso solo dentro un contesto asincrono: una funzione `async`, oppure il top level di uno script. Una funzione normale, non `async`, non può fare `await` di nulla.

---

Il lavoro che si svolge nel tempo spesso fallisce: un server è giù, un file manca, l'input è sbagliato. Una funzione del genere è marcata **`async throws`** e si chiama con **`try await`**:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
Per gestire l'errore racchiudi la chiamata in un blocco `do` e la intercetti:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// stampa could not load
```
L'ordine delle parole chiave è fisso: prima viene `try`, poi `await`.

---

Quando non ti interessa *perché* la chiamata è fallita, `try?` è più corto di un blocco `do`. Trasforma una chiamata che può lanciare errori in un **opzionale**: il valore in caso di successo, `nil` in caso di fallimento. Combinato con `await` si scrive `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Poiché il risultato è opzionale, entra direttamente in un `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Usa `try? await` per un ripiego veloce, e `do` / `catch` quando l'errore in sé è importante.

---

Diverse chiamate con `await` scritte una dopo l'altra vengono eseguite in modo **sequenziale**: la seconda chiamata non inizia nemmeno finché la prima non ha restituito il risultato. Il codice si legge dall'alto verso il basso, esattamente come il codice ordinario:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
È quello che vuoi quando la seconda chiamata ha bisogno del risultato della prima. Quando le chiamate sono indipendenti, aspettarne una prima di iniziare l'altra è tempo sprecato, e i prossimi esercizi mostrano come evitarlo.

---

Per eseguire due chiamate indipendenti allo stesso tempo, dichiarale con **`async let`**. Il lavoro inizia subito e il programma continua senza aspettare:
```swift
async let left = step("A")
async let right = step("B")
```
Il valore non c'è ancora, quindi non puoi usare il binding direttamente: devi fare `await` nel punto in cui finalmente ti serve. Un solo `await` davanti all'espressione copre ogni `async let` al suo interno:
```swift
let both = await left + right
```
Se ogni chiamata impiega un secondo, la versione sequenziale richiede due secondi mentre la versione con `async let` ne richiede circa uno, perché le due chiamate si sovrappongono.

---

Quando ti servono i risultati separatamente, raccogli più binding `async let` in una tupla e fai `await` dell'intera tupla in una volta sola:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Entrambe le chiamate erano già in esecuzione; il singolo `await` aspetta finché la più lenta delle due non è finita. Ricorda che `async let` si limita ad avviare il lavoro: un `async let` su cui non fai mai `await` viene annullato e atteso implicitamente quando lo scope finisce.

---

`async let` è legato allo scope in cui è scritto. Per avviare un lavoro concorrente e tenerne il controllo, usa un **`Task`**. La closure passata a `Task { }` gira per conto suo e il task può essere memorizzato, passato in giro o restituito:
```swift
let job = Task {
    return await double(21)
}
```
Il risultato si legge più tardi con **`.value`**, che viene atteso:
```swift
print(await job.value)
// stampa 42
```
Il tipo dell'handle dice cosa produce e cosa può lanciare: `Task<Int, Never>` è un task che restituisce un `Int` e non lancia mai errori. A differenza di `async let`, un `Task` può essere creato anche da codice ordinario, non asincrono.

---

`Task.sleep` mette in pausa il task corrente per un po' senza bloccare nient'altro. Può essere interrotto, quindi è una chiamata asincrona che può lanciare errori e richiede `try await`. La durata si indica con helper come `.seconds`, `.milliseconds` o `.nanoseconds`:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
Questo è il modo standard per simulare un lavoro lento in un esempio, al posto di una vera chiamata di rete. Nota che non blocca il programma: mentre un task dorme, gli altri continuano a girare.

---

Ora la differenza tra sequenziale e concorrente è misurabile. Supponi che `work` dorma un secondo prima di restituire il valore:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Fare `await` delle chiamate una alla volta richiede circa **due** secondi, perché la seconda pausa inizia solo quando la prima è finita:
```swift
let a = await work(1)
let b = await work(2)
```
Avviarle con `async let` richiede circa **un** secondo, perché le due pause si sovrappongono:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Scrivere `await work(1) + await work(2)` su una sola riga non cambia nulla: le due chiamate vengono comunque valutate una dopo l'altra. La concorrenza viene da `async let` o dai task, mai da come è formattata la riga.

---

`async let` funziona quando sai quante chiamate ci siano mentre scrivi il codice. Per una lista la cui dimensione è nota solo a run time, usa un **task group**.

`withTaskGroup(of:)` apre un gruppo, `addTask` avvia un task figlio per ogni elemento e il gruppo poi si legge con `for await`, che consegna i risultati man mano che finiscono:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` dichiara cosa restituisce ogni task figlio. L'intera chiamata `withTaskGroup` è una sola espressione, quindi richiede un singolo `await` davanti e non restituisce nulla finché ogni task figlio non è finito.

---

Un task group ti consegna i risultati in **ordine di completamento**, non nell'ordine in cui i task sono stati aggiunti. Il task figlio più veloce arriva per primo, quindi raccogliere i valori in un array dà un ordine imprevedibile.

Quando l'ordine conta ci sono due rimedi. Se i valori possono semplicemente essere riordinati, ordinali alla fine:
```swift
return values.sorted()
```
Se ogni risultato appartiene a una posizione, fai in modo che ogni task restituisca una coppia `(index, value)` e la scriva in un array preparato:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
Una somma, un massimo o un conteggio non ha bisogno di nessuno dei due rimedi, perché l'ordine dei valori non cambia il risultato.
