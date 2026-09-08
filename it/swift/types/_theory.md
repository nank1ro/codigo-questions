Ogni valore in Swift ha un **tipo**, che indica al compilatore che tipo di dato è e cosa puoi farci.
I tipi di base sono:
- `Int`: un numero intero, come `42` o `-7`
- `Double`: un numero con una parte decimale, come `3.14`
- `String`: un pezzo di testo, come `"Hello"`
- `Character`: un singolo carattere, come `"a"`
- `Bool`: oppure `true` o `false`

Puoi indicare il tipo di una costante o di una variabile con un'**annotazione di tipo**: due punti e il nome del tipo dopo il nome:
```swift
let age: Int = 36
let name: String = "Ada"
```
Un valore di un tipo non può essere memorizzato in una costante di un altro tipo: `let age: Int = "36"` è un errore di compilazione.

---

Il più delle volte non scrivi l'annotazione di tipo: Swift **deduce** il tipo dal valore che assegni, seguendo alcune regole sui literal:
- un numero senza punto decimale, come `42`, è un `Int`
- un numero con punto decimale, come `3.14`, è un `Double`
- il testo tra virgolette doppie è una `String`
- `true` e `false` sono `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift ha anche `Float`, un numero decimale che usa la metà della memoria di un `Double` ma è meno preciso, quindi un literal decimale non viene mai dedotto come `Float`: devi richiederlo con un'annotazione.
Allo stesso modo `"a"` viene dedotta come `String`, quindi un `Character` ha sempre bisogno di un'annotazione.

---

La funzione `type(of:)` restituisce il tipo di un valore, utile per controllare cosa ha dedotto Swift:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Quando vuoi un tipo diverso da quello dedotto, aggiungi un'annotazione. Un literal numero intero può essere memorizzato in una costante `Double` o `Float`, e un literal di un solo carattere in una costante `Character`:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift non converte mai da solo tra tipi numerici: sommare un `Int` a un `Double` è un errore di compilazione, anche se entrambi sono numeri.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Per combinarli crei un nuovo valore del tipo di cui hai bisogno, passando il valore all'inizializzatore del tipo:
```swift
let total = Double(apples) * price // 4.5
```
Funziona anche al contrario: `Int(4.5)` produce un `Int`, mantenendo solo la parte intera del numero.

---

`Int(x)` non arrotonda: **tronca**, semplicemente scartando la parte decimale, quindi `Int(3.99)` è `3` e `Int(-3.99)` è `-3`.
Per arrotondare al numero intero più vicino, chiama prima `rounded()` sul `Double` e poi converti:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
I valori intermedi come `2.5` vengono arrotondati lontano da zero: `2.5` diventa `3.0` e `-2.5` diventa `-3.0`.

---

Il tipo degli operandi decide come funziona la divisione. Quando entrambi sono `Int`, l'operatore `/` esegue la **divisione tra interi**: il risultato è un `Int` e il resto viene scartato.
Quando almeno un operando è un `Double`, `/` esegue la divisione in virgola mobile e mantiene la parte decimale:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Quindi per ottenere un risultato decimale da due valori `Int` devi convertire almeno uno dei due in `Double` **prima** di dividere: `Double(7 / 2)` è `3.0`, perché la divisione tra interi è già avvenuta.

---

Quando una funzione deve restituire un risultato decimale calcolato da numeri interi, converti gli operandi in `Double` prima di dividere e dichiara il tipo di ritorno come `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Ricorda che `count` di un array è a sua volta un `Int`, quindi richiede la stessa conversione.

---

Numeri e stringhe si convertono con la stessa sintassi degli inizializzatori. `String(42)` trasforma un numero nel testo `"42"`, esattamente come interpolandolo con `"\(42)"`.
La direzione opposta può fallire, perché non ogni testo è un numero, quindi `Int("42")` restituisce un `Int?` **opzionale**: qui contiene `42`, ma `Int("hello")` è `nil`.
Come hai imparato nelle lezioni sulla nullabilità, puoi fornire un fallback con `??` o scompattarlo con `if let`:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` riesce solo quando tutto il testo è un numero intero valido, con un segno opzionale:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Per il testo decimale usa `Double(text)`, che restituisce un `Double?` nello stesso modo: `Double("3.5")` è `Optional(3.5)`.

---

Un **alias di tipo** dà a un tipo esistente un nuovo nome, con la parola chiave `typealias`:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` e `Int` sono lo stesso tipo, quindi si mescolano liberamente. Un alias non aggiunge alcuna sicurezza: rende solo il codice più leggibile quando un tipo comune ha un significato specifico nel tuo programma.

---

Un `Int` usa 64 bit, quindi può rappresentare solo numeri in un intervallo fisso. Il valore più grande e il più piccolo sono disponibili come `Int.max` e `Int.min`:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Andare oltre questi limiti si chiama **overflow**. A differenza di molti altri linguaggi, Swift non ricomincia silenziosamente dall'altra estremità dell'intervallo: un'operazione che va in overflow è un **errore a runtime** che ferma il programma.

---

`Int.max` e `Int.min` sono utili come valori iniziali quando cerchi un estremo: qualsiasi numero reale è più piccolo di `Int.max`, quindi è un valore iniziale sicuro per "il più piccolo visto finora":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Come hai visto nelle lezioni sulle stringhe, iterare su una `String` ti dà un `Character` alla volta. Un `Character` non è una `String`, quindi per usarlo come testo lo converti con `String(c)`.
Quando il carattere è una cifra, la proprietà `wholeNumberValue` ti dà il suo valore numerico come `Int?`: è `nil` per i caratteri che non sono cifre.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Poiché `Int(text)` e `Double(text)` restituiscono `nil` in caso di fallimento, confrontare il risultato con `nil` ti dice se un testo è un numero di quel tipo:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Nota l'ultima riga: ogni testo accettato da `Int` è accettato anche da `Double`, quindi controlla prima `Int` quando vuoi distinguerli.

---

A volte hai bisogno di memorizzare insieme valori di tipi diversi. Il tipo speciale `Any` può contenere un valore di tipo **qualsiasi**, quindi un array dichiarato come `[Any]` può mescolare numeri, stringhe e booleani:
```swift
let items: [Any] = [1, "two", true]
```
Ogni elemento ricorda comunque il suo tipo reale, che `type(of:)` rivela. Per lavorare con il valore come il suo tipo reale usi un **cast condizionale** con `as?`, che restituisce un opzionale: contiene il valore quando il tipo corrisponde e `nil` altrimenti:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` è l'ultima risorsa: un array di un unico tipo concreto è più sicuro e più facile da usare, quindi preferiscilo quando puoi.

---

I cast condizionali si concatenano naturalmente con `else if` per gestire diversi tipi possibili, convertendo ciascuno nel tipo di cui hai bisogno per il risultato:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
Un `Int` memorizzato in `Any` è ancora un `Int`: `as? Double` su di esso restituisce `nil`, perché `as?` controlla il tipo, non converte i numeri.
