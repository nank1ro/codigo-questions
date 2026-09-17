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

---

Die Methode `split(separator)` zerlegt einen String in ein **Array** von Teilen und trennt dabei bei jedem `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// gibt [ 'I', 'like', 'JavaScript' ] aus
```
Das Gegenteil ist die Array-Methode `join(separator)`, die die Teile wieder zu einem String zusammenfügt:
```javascript
console.log(words.join("-"));
// gibt I-like-JavaScript aus
```

---

Benutzereingaben enthalten oft zusätzliche Leerzeichen. Die Methode `trim()` gibt eine Kopie des Strings zurück, bei der Leerraum an **beiden** Enden entfernt wurde:
```javascript
let input = "   hello   ";
console.log(input.trim());
// gibt hello aus
```
`trimStart()` entfernt nur führenden Leerraum und `trimEnd()` nur nachfolgenden Leerraum.
Leerzeichen in der Mitte des Strings werden nie berührt.

---

Die Methode `replace(search, replacement)` gibt einen neuen String zurück, bei dem das **erste** Vorkommen von `search` durch `replacement` ersetzt wird:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// gibt blue red aus
```
Um **jedes** Vorkommen zu ersetzen, verwende `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// gibt blue blue aus
```

---

Die Methode `repeat(count)` gibt den String zurück, der `count`-mal wiederholt wird:
```javascript
console.log("ab".repeat(3));
// gibt ababab aus
console.log("ab".repeat(0));
// gibt einen leeren String aus
```

---

Die Methode `padStart(targetLength, padString)` fügt `padString` am **Anfang** des Strings hinzu, bis er `targetLength` Zeichen erreicht. `padEnd()` macht dasselbe am Ende:
```javascript
console.log("7".padStart(3, "0"));
// gibt 007 aus
console.log("Tea".padEnd(6, "."));
// gibt Tea... aus
```
Wenn der String bereits lang genug ist, wird er unverändert zurückgegeben.
Zahlen haben keine String-Methoden, also wandle sie zuerst mit `String(number)` um.

---

Zwei Strings sind mit `===` nur dann gleich, wenn sie exakt dieselben Zeichen in derselben Groß-/Kleinschreibung haben:
```javascript
console.log("hello" === "hello");
// gibt true aus
console.log("hello" === "Hello");
// gibt false aus
```
Die Operatoren `<` und `>` vergleichen Strings alphabetisch, Zeichen für Zeichen.
Großbuchstaben kommen vor Kleinbuchstaben, daher ist `"Zoo" < "apple"` gleich `true`.

---

Strings sind **unveränderlich** (immutable): Einmal erstellt, kann ein String nie mehr geändert werden.
Eine Zuweisung an einen Index bewirkt nichts, und jede String-Methode gibt einen **neuen** String zurück, anstatt das Original zu verändern:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// gibt hello aus
word.toUpperCase();
console.log(word);
// gibt hello aus
```
Um ein Ergebnis zu behalten, weise es der Variable erneut zu:
```javascript
word = word.toUpperCase();
```

---

Der Aufruf von `split("")` mit einem leeren Trennzeichen wandelt einen String in ein Array seiner einzelnen Zeichen um.
Arrays haben eine `reverse()`-Methode, sodass du einen String umkehren kannst, indem du ihn aufteilst, umkehrst und wieder zusammenfügst:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// gibt cba aus
```
