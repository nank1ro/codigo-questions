Es gibt Situationen, in denen Sie Code-Teile gerne wiederverwenden möchten, nur mit unterschiedlichen Werten.
Anstatt den gesamten Code zu schreiben, ist es viel sauberer, eine Funktion zu definieren, die dann wiederholt verwendet werden kann.
In Swift verwenden wir das Schlüsselwort `func` gefolgt vom Namen der Funktion:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Die Klammern in der __Funktionsdefinition__ müssen nicht leer sein, wenn wir Parameter angeben möchten

---

Manchmal möchten wir, dass eine Funktion einen Wert __zurückgibt__.
Dafür gibt es das Schlüsselwort `return`.

---

Funktionen können mehrere Eingabeparameter haben, die in den Klammern der Funktion stehen und durch Kommas getrennt sind.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

Sie können einen Tupel-Typ als Rückgabetyp für eine Funktion verwenden, um mehrere Werte als Teil eines zusammengesetzten Rückgabewerts zurückzugeben.

---

Wenn Sie kein Argumentlabel für einen Parameter möchten, schreiben Sie einen Unterstrich `_` statt eines expliziten Argumentlabels für diesen Parameter

---

Sie können einen _Standardwert_ für jeden Parameter in einer Funktion definieren, indem Sie einen Wert dem Parameter nach dem Typ des Parameters zuweisen.
Wenn ein Standardwert definiert ist, können Sie diesen Parameter beim Aufrufen der Funktion weglassen
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

Ein _variadischer Parameter_ akzeptiert null oder mehr Werte eines angegebenen Typs.
Sie verwenden einen variadischen Parameter, um anzugeben, dass der Parameter beim Aufrufen der Funktion eine unterschiedliche Anzahl von Eingabewerten erhalten kann.
Schreiben Sie variadische Parameter, indem Sie drei Punkte `...` nach dem Namen des Parametertyps einfügen.
Die an einen variadischen Parameter übergebenen Werte werden im Funktionskörper als ein Array des entsprechenden Typs verfügbar gemacht.
Beispielsweise wird ein variadischer Parameter mit dem Namen `numbers` und dem Typ `Double...` im Funktionskörper als konstantes Array namens numbers vom Typ `[Double]` verfügbar gemacht

---

In Funktionen können wir einen _optionalen Kommentar_ hinzufügen, der erklärt, was die Funktion tut:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
Wir können `///` für einen einzeiligen Kommentar und `/** */` für einen mehrzeiligen Kommentar verwenden
