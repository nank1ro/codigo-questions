Un'**espressione regolare** (regex) è un piccolo pattern che descrive una forma di testo: "una sequenza di cifre", "una parola seguita da un segno di uguale", "tre lettere maiuscole". Invece di scrivere cicli sui caratteri, descrivi la forma una volta sola e lasci che sia Swift a trovarla.

Swift scrive una regex tra `#/` e `/#`:
```swift
let digits = #/\d+/#
```
Dentro il pattern, `\d` significa "una cifra qualsiasi" e `+` significa "una o più ripetizioni della cosa precedente", quindi `\d+` significa "una sequenza di una o più cifre".

La domanda più semplice che puoi porsi è se un testo contiene una corrispondenza. `contains(_:)` accetta una regex e restituisce un `Bool`:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Usa sempre la forma `#/ ... /#` mostrata qui: la scrittura più corta `/ ... /` confonde il compilatore quando il pattern è scritto direttamente dentro una chiamata di metodo.

---

Poche scorciatoie coprono la maggior parte dei pattern. Ognuna corrisponde esattamente a **un** carattere:
- `\d` è una cifra
- `\w` è una lettera, una cifra o un underscore
- `\s` è uno spazio, una tabulazione o un'a capo
- `.` è un carattere qualsiasi

Per corrispondere a più di un carattere, aggiungi un **quantificatore** subito dopo il pattern:
- `+` significa uno o più
- `*` significa zero o più
- `?` significa zero o uno

Quindi `\w+` è una parola, `\s*` è una spaziatura opzionale e `\d?` è una cifra opzionale:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Un carattere senza significato speciale corrisponde semplicemente a se stesso, quindi `#/cat/#` corrisponde alle tre lettere `cat`.

---

Per impostazione predefinita un pattern può corrispondere in qualsiasi punto del testo. Le **ancore** lo legano invece a una posizione:
- `^` significa "l'inizio del testo"
- `$` significa "la fine del testo"

```swift
print("swift".contains(#/^sw/#))  // true, il testo inizia con sw
print("myswift".contains(#/^sw/#)) // false, sw non è all'inizio
print("swift".contains(#/ft$/#))  // true, il testo finisce con ft
```
Le ancore corrispondono a una posizione, non a un carattere, quindi non aggiungono nulla al contenuto della corrispondenza.

---

Quando nessuna delle scorciatoie va bene, elenca tra parentesi quadre i caratteri che accetti. `[abc]` corrisponde a una `a`, a una `b` o a una `c`, e un trattino scrive un intervallo:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Un numero tra graffe dice esattamente quante volte si ripete il pattern precedente: `{3}` significa tre volte, `{2,4}` significa tra due e quattro volte:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Racchiudere un pattern tra `^` e `$` con un conteggio è il modo usuale per controllare che un intero testo abbia una forma assegnata.

---

`contains(_:)` dice solo sì o no. Per ottenere il testo corrispondente, usa `firstMatch(of:)`. Restituisce una **corrispondenza opzionale**: `nil` quando non ha corrisposto nulla, quindi si abbina naturalmente con `if let`.

Il testo corrispondente è memorizzato nella proprietà `0` della corrispondenza, scritta `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` si ferma alla prima corrispondenza, anche quando il testo ne contiene altre.

---

`m.0` non è una `String` ma una `Substring`: una vista sul testo originale, non una copia. Si stampa esattamente come una stringa, ma dove è richiesta una `String` devi convertirla:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Gli inizializzatori dei numeri accettano direttamente una `Substring`, quindi `Int(m.0)` funziona senza la deviazione.

---

`matches(of:)` restituisce **tutte** le corrispondenze invece della prima, come array. L'array non è mai `nil`: quando non corrisponde nulla è semplicemente vuoto, quindi puoi scorrerlo o trasformarlo subito:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Ogni elemento è una corrispondenza, quindi `$0.0` dentro una `map` è il testo corrispondente:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Poiché `Int(_:)` accetta una `Substring`, trasformare il testo trovato in numeri è un passaggio solo. `compactMap` è comodo qui: scarta i valori che tornano `nil`:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Usa `map` quando ogni elemento si converte, `compactMap` quando alcuni possono fallire.

---

Le parentesi tonde attorno a una parte del pattern creano un **gruppo di cattura**: l'intera corrispondenza resta `m.0`, e la parte dentro le parentesi diventa `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
È così che tieni il pezzo interessante e butti via il testo circostante. Senza parentesi non esiste proprio `m.1`, e il codice non compila.

---

Un pattern può contenere diversi gruppi. Sono numerati da sinistra a destra in base alla loro parentesi di apertura, quindi il secondo è `m.2`, il terzo `m.3`, e così via:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` resta sempre l'intera corrispondenza, qualunque sia il numero di gruppi.

---

Contare le parentesi diventa fragile appena un pattern cresce. Dai invece un **nome** a un gruppo, scrivendo `?<nome>` subito dopo la sua parentesi di apertura, e legalo come proprietà della corrispondenza:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
I gruppi con nome restano numerati, quindi `m.1` continua a funzionare, ma `m.key` dice cosa contiene e sopravvive a un cambio del pattern.

---

`replacing(_:with:)` scambia ogni corrispondenza con un testo fisso e restituisce una nuova `String`, lasciando intatto l'originale:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Nota che `\d+` sostituisce un'intera sequenza di cifre con un singolo `#`, mentre `\d` sostituirebbe una cifra alla volta. È il pattern a decidere quanto scompare.

---

`split(separator:)` accetta anche una regex, così una sola chiamata gestisce separatori non sempre scritti allo stesso modo:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
Il pattern `[,;]\s*` significa "una virgola o un punto e virgola, seguiti da qualsiasi quantità di spazio", quindi ogni separatore è consumato per intero e non viene prodotto alcun campo vuoto. Il risultato è un array di `Substring`.

---

Validare un intero testo con `^` e `$` funziona, ma `wholeMatch(of:)` lo dice direttamente: restituisce una corrispondenza solo quando il pattern copre il testo dal primo carattere all'ultimo, e `nil` altrimenti:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Usa `firstMatch(of:)` per trovare qualcosa dentro un testo, e `wholeMatch(of:)` per controllare che un testo abbia una forma precisa.

---

Un literal `#/ ... /#` è fisso quando compili. Quando il pattern diventa noto solo a run time, per esempio perché lo ha digitato un utente, costruiscilo con `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Questo inizializzatore **lancia errori**: un pattern non valido come `"["` viene scoperto solo mentre il programma gira, quindi la chiamata richiede `try`, e l'errore deve essere gestito con `do`/`catch` (o `try?`) o propagato marcando `throws` la funzione circostante, come fa questo esercizio. Una regex costruita in questo modo non ha proprietà numerate note a compile time, ma `contains`, `matches(of:)` e `replacing` funzionano esattamente come prima.
