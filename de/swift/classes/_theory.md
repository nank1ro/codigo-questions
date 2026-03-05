Swift ist eine objektorientierte Programmiersprache, was bedeutet, dass sie mit Programmierkonstrukten umgeht, die als Objekte bezeichnet werden.
Sie können sich ein Objekt als eine einzelne Datenstruktur vorstellen, die Daten sowie Funktionen enthält; die Funktionen eines Objekts werden als dessen Methoden bezeichnet.
Wenn Sie beispielsweise aufrufen:
```swift
dictName.removeValue(forKey: "keyName")
```
prüft Swift, ob `dictName` eine `removeValue()`-Methode hat (die alle Wörterbücher haben) und führt diese Methode aus, falls sie vorhanden ist.

---

_Strukturen_ und _Klassen_ sind universelle, flexible Konstrukte, die die Bausteine Ihres Programmcodes bilden.
Eine grundlegende Klasse|Struktur besteht nur aus dem Schlüsselwort `class` oder `struct` und ihrem Namen, zum Beispiel:
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

Lassen Sie uns etwas in unsere `Animal`-Klasse einfügen

---

Das Definieren einer Klasse erstellt kein Objekt.
Um das zu tun, müssen wir eine __Instanz__ einer Klasse erstellen

---

Wenn eine Klasse ihre eigenen Funktionen hat, werden diese Funktionen __Methoden__ genannt.

---

Strukturen und Klassen in Swift haben viel gemeinsam. Beide können:
- Eigenschaften definieren, um Werte zu speichern
- Methoden definieren, um Funktionalität bereitzustellen
- Subscripts definieren, um auf ihre Werte mit Subscript-Syntax zuzugreifen
- Initialisierer definieren, um ihren Anfangszustand einzurichten
- Erweitert werden, um ihre Funktionalität über eine Standardimplementierung hinaus auszubauen
- Sich an Protokolle halten, um standardmäßige Funktionalität einer bestimmten Art bereitzustellen

Aber Klassen haben zusätzliche Funktionen, die Strukturen nicht haben:
- Vererbung ermöglicht es einer Klasse, die Merkmale einer anderen zu erben
- Typecasting ermöglicht es Ihnen, den Typ einer Klasseninstanz zur Laufzeit zu überprüfen und zu interpretieren
- Deinitialisierer ermöglichen einer Klasseninstanz, alle zugewiesenen Ressourcen freizugeben
- Referenzzählung ermöglicht mehr als eine Referenz zu einer Klasseninstanz

---

Sie können auf die Eigenschaften einer Instanz mit der _Punkt-Syntax_ zugreifen.
In der Punkt-Syntax schreiben Sie den Eigenschaftsnamen unmittelbar nach dem Instanznamen, getrennt durch einen Punkt `.`, ohne Leerzeichen:
```swift
someInstance.someProperty
```
Mit der gleichen Syntax können wir auch den Wert einer Eigenschaft aktualisieren

---

Ein Vorteil von Strukturen ist, dass sie einen automatisch generierten Memberwise-Initialisierer haben, den Sie verwenden können, um die Membereigenschaften neuer Strukturinstanzen zu initialisieren.
Anfangswerte für die Eigenschaften der neuen Instanz können nach Name an den Memberwise-Initialisierer übergeben werden
