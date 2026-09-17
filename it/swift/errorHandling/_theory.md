In Swift un errore è un **valore**, non un crash. Qualsiasi tipo può farne le veci adottando il protocollo `Error`, e un enum è la scelta abituale perché i casi nominano esattamente cosa può andare storto:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Una funzione che può fallire è contrassegnata con `throws`, e segnala il fallimento con `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Chiamare una simile funzione richiede `try`, e la chiamata deve trovarsi dentro un blocco `do` seguito da un blocco `catch` che dice cosa fare quando fallisce:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
Quando `throw` viene eseguito, il resto del blocco `do` viene saltato e `catch` prende il controllo. Niente crash: il programma continua dopo il `catch`.

---

Una funzione che lancia errori può comunque restituire un valore. La parola chiave `throws` va tra la lista dei parametri e la freccia di ritorno:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Leggendola ad alta voce: *square prende un `Int`, può lanciare un errore e restituisce un `Int`*.

Alla chiamata il valore esiste solo quando non è stato lanciato nessun errore, quindi l'assegnazione vive dentro il blocco `do`:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
Il `try` non è un ornamento opzionale: il compilatore rifiuta la chiamata senza, così chi legge vede sempre quali righe possono fallire.

---

Un `catch` senza pattern gestisce ogni errore allo stesso modo. Il più delle volte vuoi reagire a un fallimento particolare, quindi un `catch` può portare un **pattern**: il caso che è disposto a gestire.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift prova le clausole `catch` dall'alto verso il basso ed esegue la prima il cui pattern corrisponde.

L'ultimo `catch` non ha un pattern di proposito. Un `catch` con pattern copre solo il caso che nomina, e Swift esige che ogni errore venga gestito da qualche parte, quindi un blocco `do` che elenca pattern ha bisogno di un `catch` finale senza pattern per raccogliere il resto.

---

L'ordine conta. Swift confronta il valore lanciato con ogni pattern `catch` nell'ordine in cui sono scritti e si ferma alla prima corrispondenza, quindi un `catch` senza pattern messo per primo inghiottirebbe tutto ciò che sta sotto. Tieni i casi specifici in alto e il catch-all in basso.

Un errore che non corrisponde a nessun pattern non viene ignorato: finisce nell'ultimo `catch` senza pattern.

---

Un caso di errore può portare dati. Dai al caso dei **valori associati** e il `throw` li compila, così chi gestisce l'errore scopre non solo *cosa* è fallito ma anche *quanto*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
Il `catch` corrispondente lega quei valori con `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
Il nome dopo `let` lo scegli tu; è una nuova costante disponibile solo dentro quel blocco `catch`. È così che un errore trasporta un messaggio utile senza che tu debba incollare numeri nelle stringhe nel punto in cui il fallimento avviene.

---

Un enum di solito contiene ogni modo in cui un singolo compito può fallire, un caso per motivo:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Scrivere un `catch` per caso diventa ripetitivo. Invece, cattura l'intero tipo in una volta e usa `switch` sul valore:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` significa *cattura qualsiasi cosa che sia un `FormError`, e chiamala `error`*. Dentro il blocco `error` ha il tipo dell'enum, quindi `switch` vede i casi e controlla che li abbia coperti tutti. Il `catch` finale senza pattern è comunque richiesto, perché un altro tipo di errore potrebbe arrivare a questo blocco `do`.

---

Un validatore si legge meglio quando i rifiuti arrivano prima e il vero lavoro resta non indentato in fondo. `guard` è fatto per questo: enuncia la condizione che deve valere, e il suo blocco `else` viene eseguito quando non vale.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
Il blocco `else` di un `guard` deve uscire dallo scope corrente, e `throw` è uno dei modi per farlo, accanto a `return`, `break` e `continue`. Diversi `guard` impilati all'inizio di una funzione si leggono come un elenco delle regole che l'input deve soddisfare.

---

A volte non ti interessa *perché* qualcosa è fallito, ma solo che sia fallito. `try?` trasforma una chiamata lanciante in un **opzionale**: il valore quando riesce, `nil` quando lancia.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
Niente `do`, niente `catch`: il fallimento viene ripiegato nell'opzionale che sai già come scompattare. Il prezzo è che il valore dell'errore viene buttato via, quindi ricorri a `try?` solo quando non c'è davvero nulla da riferire.

---

Siccome `try?` produce un opzionale, l'operatore di coalescenza nil `??` completa il lavoro fornendo un valore di riserva:
```swift
let port = (try? readPort(text)) ?? 8080
```
Le parentesi contano. Altrimenti `try?` cercherebbe di coprire l'intera espressione incluso il `??`, e il compilatore ti chiede di essere esplicito su dove finisce la chiamata che lancia.

Leggi la riga come una frase: *usa la porta che siamo riusciti a leggere, altrimenti 8080*. Due righe di `do`/`catch` collassano in una quando il recupero è davvero solo un valore predefinito.

---

C'è una terza forma: `try!`. Dice al compilatore *questa chiamata non può fallire*, quindi niente `do`, niente `catch` e niente opzionale. Se comunque fallisce, il programma si ferma immediatamente.
```swift
let pattern = try! Regex("[0-9]+")
```
Questa è la situazione in cui `try!` è giustificabile: l'argomento è un letterale scritto da te, nel tuo codice sorgente, e se è sbagliato il programma è rotto e dovrebbe fermarsi durante la tua prima esecuzione di prova.

Tutto ciò che arriva a runtime — una riga digitata da un utente, un file, una risposta di rete — può essere sbagliato in modi che non puoi vedere mentre scrivi il codice, e `try!` su di esso trasforma un fallimento recuperabile in un crash davanti all'utente. Lì usa `do`/`catch` oppure `try?`.

---

Quando una funzione lancia un errore, tutto ciò che viene dopo il `throw` viene saltato — inclusa la riga che avrebbe dovuto chiudere il file o rilasciare il lock. `defer` risolve il problema: registra un blocco ora e lo esegue quando lo scope corrente finisce, in qualunque modo finisca.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
La chiamata stampa `open`, poi `close`, e solo allora l'errore prosegue verso il chiamante. Se la funzione fosse restituita normalmente, `close` sarebbe comunque stato stampato — questo è il punto. Metti la pulizia subito accanto alla configurazione e smetti di preoccuparti di quale uscita prende il codice.

---

Uno scope può registrare più di un `defer`. Vengono eseguiti in ordine **inverso**: l'ultimo registrato è il primo a essere eseguito.

Non è una regola arbitraria. Le pulizie di solito annullano una configurazione avvenuta in ordine — apri il file, poi lo blocchi — e l'annullamento deve andare nel senso contrario: sblocca, poi chiudi. L'ordine inverso rende ogni `defer` l'immagine speculare della riga sopra di esso.

---

Una funzione che accetta una closure ha un problema: non può sapere se la closure che le viene passata lancerà un errore. Contrassegnare la funzione `throws` obbligherebbe ogni chiamante a scrivere `try`, anche quelli che passano una closure innocua. `rethrows` dice *lancio solo se la closure che mi hai dato lancia*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Dentro il corpo scrivi comunque `try`, perché la chiamata potrebbe davvero fallire. Al punto di chiamata il compilatore guarda la closure che hai passato:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // no try needed
```
La libreria standard lo usa ovunque — `map`, `filter` e `sorted(by:)` sono tutti `rethrows` — ed è per questo che non scrivi mai `try` davanti a un normale `map`.

---

Un blocco `do` non è limitato a un solo tipo di errore. Ogni passo può fallire a suo modo, e ogni fallimento ha il suo `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
Il primo `try` che lancia chiude il blocco, quindi i passi successivi non vengono mai eseguiti — il valore semplicemente non è mai esistito. È questo che rende leggibile questa forma: il percorso felice resta su una linea dritta in alto, e ogni modo in cui può andare storto è elencato sotto.

---

Dove si trova il blocco `do` decide quanto costa un singolo fallimento. Mettilo **dentro** il ciclo e ogni elemento ottiene il proprio tentativo, così un valore sbagliato viene saltato e il resto continua comunque:
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
Avvolgere invece l'intero ciclo in un unico `do` si fermerebbe al primo errore e non raggiungerebbe mai `7`. Nessuna delle due è sbagliata — è la differenza tra *un elemento sbagliato* e *arrendersi*.

---

Tutto in questo capitolo risponde a una sola domanda: chi si occupa del fallimento?

Una funzione che lancia errori si rifiuta di rispondere. Nomina ciò che è andato storto — un caso di un enum `Error`, che porta con sé tutto ciò di cui il gestore avrà bisogno — e passa la decisione più in alto. Chi chiama sceglie quindi uno strumento: `do`/`catch` per reagire caso per caso, `try?` e `??` per ripiegare su un valore predefinito, `defer` per pulire in uscita in ogni caso.

Questa separazione è tutto il punto. La funzione che rileva il problema raramente sa cosa dovrebbe succedere dopo, e il codice che lo sa raramente vuole ripetere il controllo.
