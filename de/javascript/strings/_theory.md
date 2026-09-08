Ein **String** ist eine Folge von Zeichen in Anführungszeichen, wie `"hello"` oder `'hello'`.
Jeder String hat eine `length`-Eigenschaft, die angibt, wie viele Zeichen er enthält:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
Leerzeichen und Satzzeichen zählen ebenfalls als Zeichen.

---

Jedes Zeichen in einem String hat einen **Index**, beginnend bei `0`.
Du kannst ein einzelnes Zeichen mit eckigen Klammern oder mit der Methode `charAt()` lesen:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
Das letzte Zeichen befindet sich am Index `length - 1`:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

Strings bringen viele eingebaute **Methoden** mit. Zwei der einfachsten ändern die Groß-/Kleinschreibung jedes Buchstabens:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
```
Beide Methoden nehmen keine Argumente entgegen, also vergiss die Klammern nicht.

---

Um zu prüfen, ob ein String einen anderen String enthält, verwende diese Methoden, die alle einen Boolean zurückgeben:
- `includes(text)` ist `true`, wenn `text` irgendwo vorkommt
- `startsWith(text)` ist `true`, wenn der String mit `text` beginnt
- `endsWith(text)` ist `true`, wenn der String mit `text` endet

```javascript
let file = "photo.png";
console.log(file.includes("."));
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
Der Vergleich unterscheidet Groß- und Kleinschreibung: `"Hello".includes("h")` ist `false`.

---

Die Methode `indexOf()` gibt den Index zurück, an dem ein Textstück **zum ersten Mal** im String vorkommt.
Wird der Text nicht gefunden, gibt sie `-1` zurück:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

Die Methode `slice(start, end)` extrahiert einen Teil eines Strings, vom Index `start` bis (aber ohne) Index `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
```
Wenn du `end` weglässt, geht der Ausschnitt bis zum Ende des Strings.
Ein negativer Index zählt vom Ende: `word.slice(-3)` ist `"ipt"`.
Die Methode `substring(start, end)` funktioniert genauso, akzeptiert aber keine negativen Indizes.

---

`indexOf()` und `slice()` funktionieren gut zusammen: finde heraus, wo sich etwas befindet, und schneide den String dort.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// prints 45
```
