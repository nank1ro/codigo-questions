JavaScript ist eine objektorientierte Programmiersprache, was bedeutet, dass sie mit Programmierkonstrukten arbeitet, die Objekte genannt werden.
Ein Objekt kann man sich als eine einzelne Datenstruktur vorstellen, die sowohl Daten als auch Funktionen enthält; die Funktionen eines Objekts werden seine Methoden genannt.
Zum Beispiel, wenn du aufrufst:
```javascript
arrayName.push("value");
```
überprüft JavaScript, ob `arrayName` eine `push()`-Methode hat (die alle Arrays haben) und führt diese Methode aus, wenn sie gefunden wird.

---

_Klassen_ sind vielseitige, flexible Strukturen, die die Bausteine deines Programmcodes bilden.
Eine grundlegende Klasse besteht nur aus dem `class`-Schlüsselwort und ihrem Namen, zum Beispiel:
```javascript
class ClassName {
    // class definition
}
```

---

Lass uns etwas in unsere `Animal`-Klasse einfügen
Um Parameter hinzuzufügen, müssen wir den Standard-`constructor` verwenden

---

Eine Klasse zu definieren, erstellt kein Objekt.
Um das zu tun, müssen wir eine __Instanz__ einer Klasse erstellen.
In JavaScript verwenden wir immer das `new`-Schlüsselwort vor dem Klassennamen, um eine neue Instanz zu erstellen.
Wenn du einen Standardwert einem Parameter zuweisen möchtest, mach das in der Konstruktor-Parameterliste

---

Wenn eine Klasse ihre eigenen Funktionen hat, werden diese Funktionen __Methoden__ genannt.

---

JavaScript ermöglicht es uns, eine Klasse als untergeordnete Klasse einer anderen zu erstellen, indem wir das `extends`-Schlüsselwort verwenden

---

Du kannst auf die Eigenschaften einer Instanz mit _Punkt-Syntax_ zugreifen.
Bei der Punkt-Syntax schreibst du den Eigenschaftsnamen unmittelbar nach dem Instanznamen, getrennt durch einen Punkt `.`, ohne Leerzeichen:
```javascript
someInstance.someProperty
```
Mit der gleichen Syntax können wir auch den Wert einer Eigenschaft aktualisieren
