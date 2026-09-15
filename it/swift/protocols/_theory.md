Un **protocollo** descrive cosa un tipo deve avere, senza dire come. È una lista di requisiti — proprietà e metodi — che qualsiasi tipo che lo adotta promette di fornire.

Lo dichiari con la parola chiave `protocol`. Un requisito di proprietà si scrive con il suo tipo seguito da un blocco che dice come può essere acceduta: `{ get }` significa che il tipo deve almeno permetterti di leggerla.
```swift
protocol Named {
    var name: String { get }
}
```
Un tipo **si conforma** al protocollo scrivendo il suo nome dopo i due punti e fornendo tutto ciò che il protocollo chiede:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Un protocollo non contiene dati propri: è un contratto. Ogni tipo che lo soddisfa può essere trattato allo stesso modo dal resto del tuo codice.

---

Un protocollo può anche richiedere dei **metodi**. Scrivi la firma — nome, parametri e tipo di ritorno — e ti fermi lì, senza corpo:
```swift
protocol Greeter {
    func greet() -> String
}
```
Un tipo che si conforma deve dichiarare un metodo con esattamente quella firma, e fornisce lui il corpo:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Se qualcosa differisce — il nome, un tipo di parametro, il tipo di ritorno — il tipo non si conforma, e il compilatore ti dice quale requisito manca.

---

Un requisito di proprietà indica sempre come la proprietà può essere usata. `{ get }` chiede solo che il valore possa essere letto; `{ get set }` chiede che possa essere letto **e** assegnato:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Un tipo che si conforma può sempre dare più di quanto il contratto chiede: una proprietà memorizzata `var` soddisfa `{ get }` alla perfezione. Non può mai dare meno — una costante `let`, o una proprietà calcolata di sola lettura, non può soddisfare `{ get set }`.

---

I protocolli non sono limitati alle struct. Una **classe** si conforma esattamente allo stesso modo, elencando il protocollo dopo i due punti:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
Se la classe eredita anche da un'altra classe, la superclasse viene prima nella lista e i protocolli la seguono. Un tipo può adottare più protocolli contemporaneamente, separati da virgole.

---

Anche un **enum** può conformarsi. Non ha proprietà memorizzate, quindi un requisito di proprietà di solito viene soddisfatto con una proprietà calcolata che fa switch sui case:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Struct, classi ed enum: tutti e tre adottano i protocolli allo stesso modo, e il codice scritto contro il protocollo funziona con tutti.

---

Un protocollo di solito raccoglie più di un requisito, e un tipo che si conforma deve soddisfarli tutti:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
L'ordine dei requisiti tra le parentesi graffe non conta, e nemmeno l'ordine in cui il tipo che si conforma li fornisce: il compilatore controlla solo che non manchi nulla.

---

Una struct è un tipo per valore, quindi un metodo che modifica una delle sue proprietà memorizzate deve essere marcato `mutating`. Quando quel metodo è un requisito del protocollo, anche il protocollo deve dirlo:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Senza `mutating` nel protocollo, una struct non potrebbe mai soddisfare il requisito. Le classi sono tipi per riferimento e non hanno mai bisogno della parola chiave: una classe soddisfa un requisito `mutating` con un metodo normale. Chiamare un metodo mutating richiede una `var` — su una `let` è un errore di compilazione.

---

La conformità non deve essere dichiarata accanto al tipo. Un'**extension** può aggiungerla in seguito, così la dichiarazione del tipo resta concentrata sui suoi dati:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
Funziona anche per i tipi che non hai scritto tu: puoi fare in modo che un tipo della libreria standard si conformi a uno dei tuoi protocolli senza toccarne il codice sorgente.

---

Un'extension di un **protocollo** è uno strumento diverso: aggiunge membri a ogni tipo che si conforma, presente e futuro. È così che dai a un requisito un'**implementazione predefinita**:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` non scrive mai `greet()` e si conforma comunque. Dentro l'extension del protocollo puoi usare ogni requisito del protocollo — qui `name` — perché qualsiasi tipo che si conforma ha la garanzia di averlo.

---

L'extension di un protocollo può anche aggiungere membri che il protocollo non ha mai elencato come requisiti. Sono comodità extra, disponibili su ogni tipo che si conforma:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` non è un requisito, quindi un tipo che si conforma non deve fornirla — la riceve semplicemente.

---

Un protocollo può costruire su un altro. Scrivere il nome di un protocollo dopo i due punti fa sì che il nuovo protocollo **erediti** ogni requisito del vecchio:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Un tipo che si conforma a `Aged` deve fornire `age` *e* `name`, e conta come tipo `Named` ovunque. Un protocollo può ereditare da più protocolli contemporaneamente, separati da virgole.

---

Un'implementazione predefinita è un ripiego, non una regola. Se un tipo che si conforma fornisce la sua versione di un requisito, è la sua versione quella che viene eseguita:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, non 0
```
Il default riempie solo i vuoti che il tipo lascia aperti.

---

La libreria standard è costruita con i protocolli, e i tuoi tipi possono adottarli.

`Equatable` dà a un tipo l'operatore `==`. Per una struct le cui proprietà memorizzate sono tutte `Equatable`, dichiarare la conformità basta — Swift scrive `==` per te:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` eredita da `Equatable` e aggiunge l'ordinamento. Implementi un solo operatore, `<`, scritto come una `static func` che prende i due valori, e ottieni `>`, `<=`, `>=`, più `sorted()`, `min()` e `max()` sulle collezioni gratis:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` decide cosa mostra `print` per il tuo tipo. Il suo unico requisito è una proprietà `description`:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Senza la conformità, stampare una struct produce un dump predefinito come `Coin(value: 25)`, e una proprietà `description` da sola non cambia nulla — `print` cerca il protocollo. Anche l'interpolazione delle stringhe usa `description`.

---

Un nome di protocollo da solo non è un tipo, è un vincolo, quindi Swift ti chiede di dire quale delle due cose intendi.

`some Shape` significa *un tipo specifico che si conforma*, fissato al tempo di compilazione. Chi chiama non scopre mai quale, ma è sempre lo stesso:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` significa *un contenitore che può tenere qualsiasi tipo che si conforma*, e due valori di quel tipo possono tenere tipi diversi. Ti serve ogni volta che il tipo concreto può variare, come dentro un array misto:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Entrambi ti permettono di chiamare i requisiti del protocollo. Preferisci `some` quando un solo tipo basta, perché non costa nulla a run time; usa `any` quando hai davvero bisogno di mescolare tipi.
