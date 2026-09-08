Un'**extension** aggiunge nuove funzionalità a un tipo esistente: un tipo della libreria standard come `Int` o `String`, oppure una struct o una classe che hai scritto tu.
Scrivi la parola chiave `extension` seguita dal nome del tipo, e metti i nuovi membri tra parentesi graffe:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Dentro l'extension, `self` è il valore su cui il metodo viene chiamato: in `4.squared()` è `4`. Una volta che l'extension esiste, ogni `Int` del programma ha il nuovo metodo, esattamente come se fosse sempre stato parte di `Int`.

---

Le extension funzionano su qualsiasi tipo, anche su quelli di cui non hai il codice sorgente. `String` viene dalla libreria standard, ma puoi comunque darle nuovi metodi:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Dentro un'extension puoi omettere `self.` quando chiami altri membri del tipo: `lowercased()` da solo significa `self.lowercased()`.

---

Un'extension non crea un nuovo tipo e non copia quello vecchio: aggiunge membri al tipo stesso, quindi ogni valore esistente e futuro di quel tipo li riceve.
È per questo che le extension sono così utili con i tipi che non puoi modificare, come quelli della libreria standard o di un framework: non puoi aprire il file dove `Int` è definito, ma puoi estenderlo da qualsiasi file del tuo programma.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

Oltre ai metodi, un'extension può aggiungere **proprietà calcolate**: proprietà che non memorizzano un valore ma lo calcolano ogni volta che vengono lette.
Una proprietà calcolata si dichiara con `var`, un'annotazione di tipo e un corpo tra parentesi graffe che restituisce il valore:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Si legge come qualsiasi proprietà, senza parentesi tonde: `7.isNegative`, non `7.isNegative()`.

---

Anche per `String` le proprietà calcolate nelle extension sono una scelta naturale. Il metodo `reversed()` restituisce i caratteri in ordine inverso, e `String(...)` li riporta a una stringa:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Come per i metodi, `reversed()` dentro l'extension significa `self.reversed()`.

---

Le extension possono aggiungere proprietà calcolate ma **non proprietà memorizzate**: questo non compila:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Una proprietà memorizzata ha bisogno di spazio dentro ogni istanza del tipo. I valori `Int` esistono già in tutto il tuo programma, e perfino in codice compilato molto prima della tua extension, quindi la loro disposizione in memoria non può cambiare. Una proprietà calcolata non occupa spazio, perché è solo codice che viene eseguito quando la proprietà viene letta.

---

`Int`, `String`, gli array e le struct sono **tipi valore**: un metodo non può cambiare il valore su cui è chiamato a meno che non sia marcato `mutating`. Anche le extension possono aggiungere metodi mutating:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
Dentro un metodo mutating puoi assegnare a `self`. Il valore deve essere memorizzato in una `var`: chiamare `increment()` su una costante `let` è un errore di compilazione.

---

Un metodo mutating può ricevere parametri come qualsiasi altro metodo, e può sostituire interamente `self` invece di aggiornarlo sul posto:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

Un'extension può aggiungere nuovi **inizializzatori** a un tipo. Per una struct questo è il posto migliore dove metterli: un `init` scritto dentro il corpo della struct sostituisce l'inizializzatore memberwise automatico, mentre uno aggiunto in un'extension lo mantiene.
Il nuovo inizializzatore di solito delega a uno esistente con `self.init(...)`:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Le extension non servono solo per i tipi di altri. Un modo diffuso di organizzare il tuo codice è tenere le proprietà memorizzate nel corpo della struct o della classe e aggiungere il comportamento in una o più extension, ognuna che raggruppa membri correlati:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
I membri aggiunti in un'extension possono usare direttamente le proprietà memorizzate, esattamente come se fossero scritti dentro il tipo.

---

Un'extension può anche far conformare un tipo a un **protocollo**, un elenco di requisiti che il tipo promette di implementare. Scrivi il nome del protocollo dopo il nome del tipo, separato da due punti, e aggiungi i membri richiesti nel corpo.
`CustomStringConvertible` è un protocollo standard con un solo requisito, una proprietà calcolata `description` di tipo `String`, che `print` usa per mostrare il valore:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Tenere ogni conformità a un protocollo nella sua extension è il modo abituale di organizzare un tipo Swift.

---

`Array` è un tipo generico: `[Int]` e `[String]` sono entrambi array, con un tipo **`Element`** diverso. Un'extension di `Array` si applica a tutti, il che è un problema quando il nuovo membro ha senso solo per alcuni elementi: non puoi sommare numeri che sono stringhe.
Una clausola `where` limita l'extension agli array il cui `Element` è un tipo dato:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` funziona, mentre `["a", "b"].largest` è un errore di compilazione: la proprietà non esiste su `[String]`.

---

Le extension possono aggiungere membri **static**: proprietà e metodi che appartengono al tipo stesso invece che a un singolo valore, marcati con la parola chiave `static` e usati attraverso il nome del tipo.
Una `static let` è ammessa anche se memorizza un valore, perché ne esiste una sola copia per tutto il tipo, non una per istanza:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
Un membro static non ha un valore `self` su cui lavorare: `Int.answer` si legge sul tipo, non su un numero.

---

I metodi static nelle extension sono un buon posto per piccole funzioni di fabbrica che costruiscono un valore del tipo. `String(repeating:count:)` è l'inizializzatore standard che ripete un pezzo di testo un certo numero di volte:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Le extension possono solo **aggiungere** membri, mai sostituire o sovrascrivere quelli esistenti. `override` appartiene alle sottoclassi, che sono un tipo diverso dal loro genitore; un'extension è lo stesso tipo, quindi dichiarare un metodo che esiste già è un errore di ridichiarazione:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
Se ti serve un comportamento diverso, aggiungi un metodo con un nuovo nome, oppure scrivi una sottoclasse quando il tipo è una classe.
