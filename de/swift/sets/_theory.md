Ein **Set** (eine Menge) ist eine Sammlung, die Werte desselben Typs ohne festgelegte Reihenfolge speichert und, was am wichtigsten ist, **keine Duplikate**: Jeder Wert kommt höchstens einmal vor.
Sets eignen sich perfekt, wenn dich nur interessiert, *welche* Werte vorhanden sind, nicht wie oft oder an welcher Position.
Du deklarierst ein Set mit dem Typ `Set<Element>` und einem Literal im Array-Stil:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
Die Typannotation ist erforderlich: Ohne sie würde Swift ein Array erstellen.
Wenn das Literal einen Wert mehrmals enthält, behält das Set nur eine Kopie:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
Die Eigenschaft `count` gibt an, wie viele unterschiedliche Werte das Set enthält.

---

Wie Arrays können Sets Konstanten (`let`) oder Variablen (`var`) sein. Nur ein `var`-Set kann nach seiner Erstellung geändert werden.
Um ein leeres Set zu erstellen, rufst du den Initialisierer des Typs auf, denn ein leeres Literal `[]` allein würde Swift nicht mitteilen, welchen Elementtyp du verwenden möchtest:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
Die Eigenschaft `isEmpty` ist `true`, wenn das Set keine Elemente enthält, genau wie bei Arrays.

---

Da ein Set niemals denselben Wert zweimal speichert, entspricht sein `count` der Anzahl der *unterschiedlichen* Werte, unabhängig davon, wie oft jeder einzelne im Literal geschrieben wurde.

---

Um zu prüfen, ob ein Wert in einem Set enthalten ist, verwendest du die Methode `contains(_:)`, die einen `Bool` zurückgibt:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
Diese Prüfung ist bei einem Set sehr schnell, selbst bei Tausenden von Elementen, was einer der Hauptgründe ist, für Zugehörigkeitsprüfungen ein Set einem Array vorzuziehen.

---

Ein `var`-Set kann mit `insert(_:)` und `remove(_:)` verändert werden:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
Das Einfügen eines bereits vorhandenen Werts hat keine Auswirkung, und das Entfernen eines nicht vorhandenen Werts verursacht keinen Fehler.
`remove(_:)` gibt den entfernten Wert als Optional zurück (`nil`, wenn nichts entfernt wurde), sodass du prüfen kannst, ob das Entfernen tatsächlich stattgefunden hat.
Um ein Set vollständig zu leeren, rufst du `removeAll()` auf.

---

Du kannst mit `for`-`in` über ein Set iterieren, aber denk daran, dass ein Set **keine festgelegte Reihenfolge** hat: Die Elemente können in beliebiger Reihenfolge erscheinen, und diese Reihenfolge kann sich zwischen den Durchläufen ändern.
Wenn die Reihenfolge wichtig ist, rufe zuerst `sorted()` auf: Es gibt ein neues **Array** mit den Elementen in aufsteigender Reihenfolge zurück und lässt das Set unverändert.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```
