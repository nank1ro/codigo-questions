Ein **String** ist eine Folge von Zeichen in Anführungszeichen, wie `"hello"` oder `'hello'`.
Jeder String hat eine `length`-Eigenschaft, die angibt, wie viele Zeichen er enthält:
```javascript
let greeting = "hello";
console.log(greeting.length);
// gibt 5 aus
```
Leerzeichen und Satzzeichen zählen ebenfalls als Zeichen.

---

Jedes Zeichen in einem String hat einen **Index**, beginnend bei `0`.
Du kannst ein einzelnes Zeichen mit eckigen Klammern oder mit der Methode `charAt()` lesen:
```javascript
let word = "hello";
console.log(word[0]);
// gibt h aus
console.log(word.charAt(1));
// gibt e aus
```
Das letzte Zeichen befindet sich am Index `length - 1`:
```javascript
console.log(word[word.length - 1]);
// gibt o aus
```

---

Strings bringen viele eingebaute **Methoden** mit. Zwei der einfachsten ändern die Groß-/Kleinschreibung jedes Buchstabens:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// gibt HELLO aus
console.log(word.toLowerCase());
// gibt hello aus
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
// gibt true aus
console.log(file.startsWith("ph"));
// gibt true aus
console.log(file.endsWith(".jpg"));
// gibt false aus
```
Der Vergleich unterscheidet Groß- und Kleinschreibung: `"Hello".includes("h")` ist `false`.

---

Die Methode `indexOf()` gibt den Index zurück, an dem ein Textstück **zum ersten Mal** im String vorkommt.
Wird der Text nicht gefunden, gibt sie `-1` zurück:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// gibt 2 aus
console.log(word.indexOf("z"));
// gibt -1 aus
```

---

Die Methode `slice(start, end)` extrahiert einen Teil eines Strings, vom Index `start` bis (aber ohne) Index `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// gibt Java aus
console.log(word.slice(4));
// gibt Script aus
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
// gibt 45 aus
```
