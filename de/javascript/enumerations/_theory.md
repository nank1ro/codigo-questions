Eine **Enumeration** (oder *Enum*) ist ein gemeinsamer Typ für eine kleine Gruppe verwandter, fester Werte: die Wochentage, die Farben eines Kartenspiels, die möglichen Zustände einer Bestellung.
Anders als viele Sprachen hat JavaScript **kein** `enum`-Schlüsselwort. Der idiomatische Ersatz ist ein einfaches Objekt, dessen Eigenschaften die Mitglieder sind, das an `Object.freeze()` übergeben wird, damit niemand es später ändern kann:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
```
Laut Konvention wird das Objekt mit `const` deklariert, sein Name beginnt mit einem Großbuchstaben, und die Namen der Mitglieder werden in `UPPER_CASE` geschrieben, genau wie andere Konstanten.

---

Der in jedem Mitglied gespeicherte Wert liegt bei dir. **Strings** sind die häufigste Wahl, weil sie beim Ausgeben, Loggen oder Speichern in einer Datei gut lesbar sind:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// prints done
```
Einmal eingefroren, kann das Objekt auch keine neuen Eigenschaften mehr erhalten, und `Object.isFrozen(obj)` verrät dir, ob ein Objekt eingefroren wurde:
```javascript
console.log(Object.isFrozen(Status));
// prints true
```

---

Warum das Objekt überhaupt einfrieren? Ein eingefrorenes Objekt lehnt jede Änderung ab: Einem bestehenden Mitglied einen Wert zuzuweisen, ein neues hinzuzufügen oder eines zu löschen hat keine Wirkung.
Wie die Ablehnung sich zeigt, hängt vom Modus ab, in dem dein Code läuft:
- im **nicht-strikten Modus** (*Sloppy Mode*, der Standard für einfache Skripte) wird die Zuweisung **stillschweigend ignoriert**
- im **strikten Modus** (Dateien, die mit `"use strict"` beginnen, ES-Module und Klassenkörper) wird ein `TypeError` **ausgelöst**

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// prints s
console.log(Size.MEDIUM);
// prints undefined
```
So oder so behält die Enumeration die Werte, die du definiert hast, was genau das ist, was man von einer Reihe von Konstanten erwartet.

---

Mitglieder können auch **Zahlen** enthalten. Numerische Werte sind praktisch, wenn die Mitglieder eine natürliche Reihenfolge haben, weil du sie mit den üblichen Operatoren vergleichen kannst:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// prints true
```
Der Kompromiss ist die Lesbarkeit: Wenn du `Priority.HIGH` ausgibst, siehst du `3`, was dir viel weniger sagt als der String `"high"`.

---

Da eine Enumeration nur ein Objekt ist, kannst du sie mit den üblichen Objekt-Hilfsmitteln untersuchen:
- `Object.keys(Enum)` gibt ein Array mit den **Namen** der Mitglieder zurück
- `Object.values(Enum)` gibt ein Array mit den **Werten** der Mitglieder zurück
- `Object.entries(Enum)` gibt ein Array von `[name, value]`-Paaren zurück

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
`Object.values()` mit der Array-Methode `includes()` zu kombinieren ist der Standardweg, um zu prüfen, ob ein beliebiger Wert, zum Beispiel einer, der aus einer Benutzereingabe gelesen wurde, ein gültiges Mitglied ist:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
