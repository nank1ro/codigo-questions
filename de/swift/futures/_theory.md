Manche Arbeiten sind nicht sofort fertig: Das Herunterladen einer Datei, das Lesen aus einer Datenbank, das Warten auf einen Timer. Wenn ein Programm einfach anhielte und wartete, könnte in der Zwischenzeit nichts anderes passieren. Swift löst das mit **asynchronen Funktionen**.

Eine Funktion, die mit **`async`** markiert ist, darf sich mitten in der Ausführung anhalten und später fortsetzen. Das Schlüsselwort steht nach der Parameterliste, vor dem Pfeil:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Auch der Aufruf ist anders: Du musst **`await`** vor den Aufruf schreiben. `await` markiert die genaue Stelle, an der das Programm anhalten darf, und liefert dir den reinen Wert, sobald die Funktion fertig ist:
```swift
let n = await fetchNumber()
print(n)
// gibt 42 aus
```
In einem Swift-Skript unterstützt die oberste Ebene bereits `await`, daher kannst du asynchrone Funktionen direkt aufrufen, ohne jeden zusätzlichen Aufwand. Vergisst du `async` oder `await`, ist das ein Kompilierfehler und kein stiller Bug.

---

Eine asynchrone Funktion ist trotzdem eine gewöhnliche Funktion: Sie kann Parameter entgegennehmen und einen Wert eines beliebigen Typs zurückgeben. Nur zwei Dinge ändern sich, das Schlüsselwort `async` in der Signatur und das `await` an jeder Aufrufstelle:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// gibt 10.0 aus
```
Der zurückgegebene Wert ist ein normales `Double`, kein Wrapper: Sobald `await` abgeschlossen ist, arbeitest du damit genau wie gewohnt.

---

Asynchrone Funktionen bauen meist aufeinander auf. Innerhalb einer `async`-Funktion darfst du auf jede andere `async`-Funktion mit `await` warten, und das Ergebnis wird wie jeder normale Wert verwendet:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// gibt 15 aus
```
`await` ist nur innerhalb eines asynchronen Kontexts erlaubt: einer `async`-Funktion oder der obersten Ebene eines Skripts. Eine gewöhnliche Funktion ohne `async` kann kein `await` verwenden.

---

Arbeiten, die sich über Zeit erstrecken, schlagen oft fehl: Ein Server ist nicht erreichbar, eine Datei fehlt, die Eingabe ist falsch. Eine solche Funktion wird mit **`async throws`** markiert und mit **`try await`** aufgerufen:
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
Um den Fehler zu behandeln, packst du den Aufruf in einen `do`-Block und fängst ihn ab:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// gibt could not load aus
```
Die Reihenfolge der Schlüsselwörter ist festgelegt: `try` kommt zuerst, dann `await`.

---

Wenn es dich nicht interessiert, *warum* der Aufruf fehlgeschlagen ist, ist `try?` kürzer als ein `do`-Block. Es macht aus einem werfenden Aufruf ein **Optional**: den Wert bei Erfolg, `nil` bei Fehlschlag. Zusammen mit `await` schreibt man es als `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Weil das Ergebnis ein Optional ist, passt es direkt in ein `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Verwende `try? await` für einen schnellen Ersatz, und `do` / `catch`, wenn der Fehler selbst wichtig ist.

---

Mehrere `await`-Aufrufe, die nacheinander stehen, laufen **sequenziell**: Der zweite Aufruf startet gar nicht erst, bis der erste zurückgekehrt ist. Der Code liest sich von oben nach unten, genau wie gewöhnlicher Code:
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
Das ist genau das, was du willst, wenn der zweite Aufruf das Ergebnis des ersten braucht. Sind die Aufrufe unabhängig voneinander, ist das Warten auf den einen vor dem Start des anderen verschwendete Zeit, und die nächsten Übungen zeigen, wie du das vermeidest.

---

Um zwei unabhängige Aufrufe gleichzeitig auszuführen, deklarierst du sie mit **`async let`**. Die Arbeit startet sofort, und das Programm läuft ohne Warten weiter:
```swift
async let left = step("A")
async let right = step("B")
```
Der Wert ist noch nicht da, daher kannst du die Bindung nicht direkt verwenden: Du musst sie mit `await` an der Stelle abwarten, an der du sie schließlich brauchst. Ein einziges `await` vor dem Ausdruck deckt jedes `async let` darin ab:
```swift
let both = await left + right
```
Braucht jeder Aufruf eine Sekunde, benötigt die sequenzielle Version zwei Sekunden, während die `async let`-Version etwa eine braucht, weil sich die beiden Aufrufe überlappen.

---

Wenn du die Ergebnisse einzeln brauchst, sammelst du mehrere `async let`-Bindungen in einem Tupel und wartest mit `await` auf das gesamte Tupel auf einmal:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Beide Aufrufe liefen bereits; das einzelne `await` wartet, bis das langsamere der beiden fertig ist. Denke daran, dass `async let` nur die Arbeit startet: Ein `async let`, auf das du nie wartest, wird abgebrochen und implizit mit `await` behandelt, wenn der Gültigkeitsbereich endet.

---

`async let` ist an den Gültigkeitsbereich gebunden, in dem es steht. Um nebenläufige Arbeit zu starten und einen Griff darauf zu behalten, verwendest du eine **`Task`**. Die an `Task { }` übergebene Closure läuft eigenständig, und der Task kann gespeichert, weitergereicht oder zurückgegeben werden:
```swift
let job = Task {
    return await double(21)
}
```
Das Ergebnis wird später mit **`.value`** gelesen, wobei darauf gewartet wird:
```swift
print(await job.value)
// gibt 42 aus
```
Der Typ des Handles sagt, was er erzeugt und was er werfen kann: `Task<Int, Never>` ist ein Task, der ein `Int` zurückgibt und nie wirft. Anders als `async let` kann ein `Task` auch aus gewöhnlichem, nicht-asynchronem Code erstellt werden.

---

`Task.sleep` hält den aktuellen Task eine Weile an, ohne etwas anderes zu blockieren. Er kann unterbrochen werden, daher ist es ein werfender asynchroner Aufruf und braucht `try await`. Die Dauer wird mit Helfern wie `.seconds`, `.milliseconds` oder `.nanoseconds` angegeben:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
Das ist die übliche Art, in einem Beispiel langsame Arbeit zu simulieren, anstelle eines echten Netzwerkaufrufs. Beachte, dass das Programm dadurch nicht einfriert: Während ein Task schläft, laufen die anderen weiter.

---

Jetzt ist der Unterschied zwischen sequenziell und nebenläufig messbar. Angenommen, `work` schläft eine Sekunde, bevor es zurückkehrt:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Die Aufrufe nacheinander mit `await` abzuwarten dauert etwa **zwei** Sekunden, weil die zweite Schlafphase erst beginnt, wenn die erste vorbei ist:
```swift
let a = await work(1)
let b = await work(2)
```
Sie mit `async let` zu starten dauert etwa **eine** Sekunde, weil sich beide Schlafphasen überlappen:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Wenn du `await work(1) + await work(2)` in eine einzige Zeile schreibst, ändert sich nichts: Die beiden Aufrufe werden trotzdem nacheinander ausgewertet. Nebenläufigkeit kommt von `async let` oder von Tasks, nie davon, wie die Zeile formatiert ist.

---

`async let` funktioniert, wenn du beim Schreiben des Codes weißt, wie viele Aufrufe es gibt. Für eine Liste, deren Größe erst zur Laufzeit bekannt ist, verwendest du eine **Task-Gruppe**.

`withTaskGroup(of:)` öffnet eine Gruppe, `addTask` startet je Element einen Kind-Task, und die Gruppe wird danach mit `for await` gelesen, das die Ergebnisse liefert, sobald sie fertig sind:
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
`of: Int.self` deklariert, was jeder Kind-Task zurückgibt. Der gesamte `withTaskGroup`-Aufruf ist ein einziger Ausdruck, daher braucht er ein einzelnes `await` davor, und er kehrt erst zurück, wenn jeder Kind-Task fertig ist.

---

Eine Task-Gruppe liefert dir Ergebnisse in **Fertigstellungsreihenfolge**, nicht in der Reihenfolge, in der die Tasks hinzugefügt wurden. Der schnellste Kind-Task kommt zuerst an, daher ergibt das Sammeln der Werte in einem Array eine unvorhersehbare Reihenfolge.

Wenn die Reihenfolge wichtig ist, gibt es zwei Lösungen. Lassen sich die Werte einfach umsortieren, sortierst du sie am Ende:
```swift
return values.sorted()
```
Gehört jedes Ergebnis zu einer Position, lässt du jeden Task ein Paar `(index, value)` zurückgeben und schreibst es in ein vorbereitetes Array:
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
Eine Summe, ein Maximum oder eine Zählung braucht keine der beiden Lösungen, weil die Reihenfolge der Werte das Ergebnis nicht ändert.
