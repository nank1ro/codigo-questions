A volte un valore è semplicemente assente: un utente senza secondo nome, una ricerca che non trova nulla, un testo che non può essere trasformato in un numero.
Swift rappresenta un valore assente con `nil`, ma una variabile normale non può mai contenerlo:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Per permettere un valore assente dichiari un tipo **opzionale** aggiungendo un punto interrogativo `?` dopo il tipo.
Un `Int?` contiene un `Int` oppure `nil`:
```swift
var age: Int? = 30
age = nil // consentito
```
Una variabile opzionale dichiarata senza valore parte come `nil`.

---

Puoi confrontare un opzionale con `nil` usando `==` e `!=`, e puoi anche confrontarlo direttamente con un valore semplice del tipo racchiuso:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Ricorda che `Int?` e `Int` sono due tipi diversi: un `Int?` può essere vuoto, un `Int` non lo è mai.

---

Un opzionale è come una scatola: prima di usare il valore al suo interno devi aprirla, operazione che Swift chiama **scompattamento**.
Il modo più rapido è lo **scompattamento forzato** con un punto esclamativo `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
Il `!` dice a Swift "sono sicuro che qui c'è un valore". Se ti sbagli e l'opzionale è `nil`, il programma si interrompe subito con un crash a runtime:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
Per questo lo scompattamento forzato è considerato pericoloso: usalo solo quando sei certo che il valore esista.

---

Lo scompattamento forzato è sicuro solo quando hai già verificato che l'opzionale non sia `nil`:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Controllare `nil` e poi scompattare forzatamente è prolisso. Swift offre il **binding opzionale** con `if let`, che scompatta l'opzionale e salva il valore in una nuova costante in un solo passaggio:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value è un Int, non un Int?
} else {
    print("No score")
}
```
Il corpo dell'`if` viene eseguito solo quando l'opzionale contiene un valore; al suo interno `value` è un semplice `Int` e non serve `!`.

---

Quando un valore assente significa "fermati qui", `guard let` è più chiaro di `if let`.
Scompatta l'opzionale e, se questo fallisce, esegue il blocco `else`, che deve uscire dall'ambito corrente (con `return`, `break`, `continue` o `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // da qui in poi name è una String
}
```
A differenza di `if let`, la costante scompattata resta disponibile per il resto della funzione, quindi il percorso principale non è annidato dentro un `if`.

---

Un uso tipico di `guard let` è validare l'input di una funzione all'inizio e restituire un valore di riserva quando manca:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Molto spesso tutto ciò che vuoi da un opzionale è il suo valore o un valore predefinito.
L'**operatore di coalescenza nil** `??` fa esattamente questo: scompatta l'opzionale se ha un valore, altrimenti restituisce il valore alla sua destra:
```swift
let score: Int? = nil
let points = score ?? 0 // points è un Int uguale a 0
```
Il valore predefinito deve avere lo stesso tipo del valore racchiuso.
Puoi concatenare più `??`: vince il primo valore diverso da `nil`.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` è il modo più breve per trasformare un opzionale in un valore semplice quando esiste un valore predefinito sensato:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Quando concatena `??`, Swift valuta da sinistra a destra e si ferma al primo valore diverso da `nil`; l'ultimo valore predefinito viene usato solo quando ogni opzionale precedente è `nil`.

---

Accedere a una proprietà o richiamare un metodo su un opzionale richiederebbe prima di scompattarlo.
L'**optional chaining** con `?.` lo fa al posto tuo: se l'opzionale è `nil` l'intera espressione diventa `nil`, altrimenti l'accesso prosegue:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? che contiene "SWIFT"
```
Il risultato è sempre un opzionale, anche quando la proprietà stessa non lo è.
Le catene possono essere lunghe quanto serve, e si combinano bene con `??`:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

L'optional chaining dà il meglio di sé quando i dati possono mancare a più livelli: un oggetto può essere `nil`, e una delle sue proprietà può esserlo a sua volta.
Una singola catena `?.` gestisce entrambi i casi senza nessun `if`.

---

Un singolo `if let` o `guard let` può scompattare più opzionali insieme: separa i binding con delle virgole.
Il corpo viene eseguito solo se ogni opzionale ha un valore:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
Puoi anche aggiungere una condizione booleana dopo i binding, come `if let n = number, n > 0`.

---

Legare più opzionali in un unico `if let` mantiene il codice piatto: un solo ramo `else` copre ogni valore assente.

---

Molte operazioni possono fallire, e Swift segnala il fallimento restituendo un opzionale.
Convertire del testo in un numero è l'esempio classico: `Int("42")` restituisce un `Int?` che contiene `42`, mentre `Int("abc")` restituisce `nil`.
Anche `Int("3.5")` è `nil`, perché il testo non è un numero intero; usa `Double("3.5")` per i decimali.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Altri esempi sono `array.first` (`nil` per un array vuoto) e `dictionary[key]` (`nil` quando la chiave manca).

---

Poiché una conversione può fallire, il suo risultato è sempre un opzionale e deve essere scompattato prima dell'uso, anche quando sei sicuro che il testo sia un numero valido.

---

Le conversioni che possono fallire si abbinano naturalmente a `guard let`: converti, esci se il risultato è `nil`, poi lavora con il valore semplice.

---

A volte vuoi trasformare il valore all'interno di un opzionale e mantenere il risultato opzionale, senza scompattare e reimpacchettare a mano.
Gli opzionali hanno un metodo `map`: applica la closure al valore se ce n'è uno, e restituisce `nil` altrimenti.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? che contiene 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Combinato con una conversione che può fallire crea una pipeline compatta: `Int(text).map { $0 + 1 }`.
