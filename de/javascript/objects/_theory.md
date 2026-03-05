**Objekte** sind ähnlich wie Arrays, aber Sie greifen auf Werte zu, indem Sie einen *Schlüssel* (Key) anstelle eines Index suchen.
Ein Schlüssel kann jede Zeichenkette oder Zahl sein.
Objekte werden in geschweifte Klammern eingeschlossen, wie hier:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
Dies ist ein Wörterbuch (Dictionary) namens `objectName` mit drei *Schlüssel-Wert-Paaren*.
Der Schlüssel `key1` verweist auf den Wert `1`, `key2` auf `2`, usw.

---

Der Zugriff auf Wörterbuch-Werte nach Schlüssel funktioniert genauso wie der Zugriff auf Array-Werte nach Index:
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Wie Arrays sind Wörterbücher (Dictionaries) _veränderlich_ (mutable).
Das bedeutet, sie können nach ihrer Erstellung verändert werden (wenn sie nicht als Konstante deklariert sind).
Ein Vorteil davon ist, dass wir neue _Schlüssel/Wert-Paare_ zum Wörterbuch nach seiner Erstellung hinzufügen können, wie hier:
```javascript
dictName[newKeyName] = newValue;
```

---

Da Wörterbuch-Variablen veränderlich sind, können sie auf viele Arten geändert werden.
Elemente können mit dem Schlüsselwort 'delete' aus einem Wörterbuch entfernt werden:
```javascript
delete dictName[keyName];
```
Dies entfernt den Schlüssel `keyName` und seinen zugehörigen Wert aus dem Wörterbuch.

---

Was ist, wenn wir alle Schlüssel des Wörterbuchs auflisten möchten?
Nun, da gibt es die `Object.keys()`-Methode.

---

Was ist, wenn wir alle Werte des Wörterbuchs auflisten möchten?
Nun, da gibt es die `Object.values()`-Methode.

---

Wie bei Arrays können wir mit der `Object.entries()`-Methode zwischen Wörterbuch-Elementen durchlaufen.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
