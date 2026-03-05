Kotlin hat einen grundlegenden booleschen Typ namens `Boolean`.
Boolesche Werte werden logisch genannt, da sie nur „wahr" oder „falsch" sein können.
Sie können jeden Ausdruck in Kotlin auswerten und erhalten eine von zwei Antworten: `true` oder `false`.

---

Wir können den booleschen Wert `true` in einer Variable genauso speichern wie eine Zahl oder einen Text.

---

Der Gegenwert von `true` ist `false`.

---

Boolesche Werte können auch negiert werden, indem man das `!`-Zeichen davor verwendet, z. B.:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

Wir können auch boolesche Ausdrücke mit den Operatoren `&&` (_und_) und `||` (_oder_) erstellen:

- `&&` (_und_): ergibt „wahr", nur wenn der boolesche Ausdruck auf der linken Seite des Operators UND derjenige auf der rechten Seite beide wahr sind.
- `||` (_oder_): Ergibt „wahr", wenn entweder der Ausdruck auf der linken oder rechten Seite des Operators wahr ist, oder wenn beide wahr sind.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
