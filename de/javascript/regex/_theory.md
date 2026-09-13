Ein **regulärer Ausdruck** (oder **Regex**) ist ein kleines Muster, das eine Form von Text beschreibt. Damit beantwortest du Fragen wie „Enthält dieser String eine Zahl?" oder „Wo kommt das Wort `cat` vor?".

In JavaScript ist die kürzeste Schreibweise ein **Regex-Literal**: das Muster zwischen zwei Schrägstrichen.
```javascript
const pattern = /cat/;
```
Gewöhnliche Zeichen in einem Muster passen auf sich selbst, deshalb findet `/cat/` die drei Buchstaben `c`, `a`, `t` an beliebiger Stelle in einem String.

Das Einfachste, was du mit einem Muster tun kannst, ist zu fragen, ob es in einem String vorkommt. Die Methode **`test`** nimmt den Text entgegen und gibt `true` oder `false` zurück:
```javascript
console.log(/cat/.test("the cat sleeps"));
// prints true
console.log(/cat/.test("the dog sleeps"));
// prints false
```
Beachte, dass `test` das Muster *irgendwo* im String sucht; der ganze String muss nicht übereinstimmen.

---

Muster werden nützlich, wenn sie eine *Art* von Zeichen beschreiben statt ein genau bestimmtes Zeichen. Einige **Escape-Sequenzen** decken die meisten Bedürfnisse ab:
- `\d` eine beliebige Ziffer, von `0` bis `9`
- `\w` ein beliebiges Wortzeichen: ein Buchstabe, eine Ziffer oder `_`
- `\s` ein beliebiges Whitespace-Zeichen: ein Leerzeichen, ein Tabulator, ein Zeilenumbruch

```javascript
console.log(/\d/.test("room 12"));
// prints true
console.log(/\d/.test("lobby"));
// prints false
```
Ein **Quantor** gibt an, wie oft sich der vorherige Teil wiederholen darf. Der häufigste ist `+`, bedeutet „einmal oder öfter":
```javascript
console.log(/\d+/.test("42"));
// prints true
```
`/\d/` passt also auf eine einzelne Ziffer und `/\d+/` auf eine Folge von Ziffern. Bei einem einfachen `test` verhalten sich beide gleich, weil beide nur eine vorhandene Ziffer brauchen.

---

Ein Literal wie `/\d+/` ist fest, sobald du es geschrieben hast. Wenn das Muster **zur Laufzeit erstellt** werden muss, verwende den **`RegExp`-Konstruktor**, der das Muster als String entgegennimmt:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// prints true
```
Es gibt eine Falle. Innerhalb eines Strings beginnt ein Backslash eine Escape-Sequenz für den *String*, deshalb verschwindet er, bevor das Regex ihn je zu sehen bekommt. Um einen echten Backslash ins Muster zu bringen, musst du ihn verdoppeln:
```javascript
const digits = new RegExp("\\d+");
// the same pattern as /\d+/
```
Schreibt man stattdessen `new RegExp("\d+")`, ergibt sich das Muster `/d+/`, das auf den Buchstaben `d` passt, nicht auf eine Ziffer.

Bevorzuge das Literal, wenn das Muster beim Schreiben des Codes schon bekannt ist; es ist kürzer und braucht keine verdoppelten Backslashes.

---

Zwei weitere Bausteine, mit denen du fast jede Textform beschreiben kannst.

Eine **Zeichenklasse** ist eine Menge von Zeichen in eckigen Klammern; sie passt auf genau eines davon. Ein Bindestrich schreibt einen Bereich, und ein `^` am Anfang negiert die Menge:
```javascript
/[aeiou]/   // one vowel
/[a-z]/     // one lowercase letter
/[A-Z0-9]/  // one uppercase letter or one digit
/[^0-9]/    // one character that is not a digit
```
**Quantoren** geben an, wie oft sich der vorherige Teil wiederholt: `+` einmal oder öfter, `*` nullmal oder öfter, `?` nullmal oder einmal und `{n}` genau `n`-mal.

Zum Schluss verankern **Anker** das Muster an den Enden des Textes: `^` bedeutet „Hier geht es los" und `$` bedeutet „Hier hört es auf". Ohne sie kann ein Muster an beliebiger Stelle im String passen, deshalb ist `/\d{2}/.test("abc12def")` gleich `true`. Mit beiden Ankern muss der ganze String übereinstimmen:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// prints false
console.log(/^\d{2}$/.test("12"));
// prints true
```

---

`test` sagt nur ja oder nein. Um den gefundenen Text selbst zu erhalten, rufe **`match`** auf dem String auf:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Wenn nichts passt, gibt `match` `null` zurück. Wenn etwas passt, gibt es ein Array-ähnliches Ergebnis zurück:
- `match[0]` ist der gefundene Text
- `match.index` ist die Position, an der der Treffer beginnt
- `match.input` ist der gesamte durchsuchte String

```javascript
console.log(match[0]);
// prints 42
console.log(match.index);
// prints 6
```
Da das Ergebnis `null` sein kann, prüfe es, bevor du `match[0]` liest.

---

Da `match` `null` zurückgibt, wenn das Muster nicht vorkommt, löst der sofortige Zugriff auf `match[0]` einen `TypeError: Cannot read properties of null` aus. Sichere die Stelle ab:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
Der Nullish-Coalescing-Operator schreibt dieselbe Absicherung in einer Zeile, weil `match?.[0]` `undefined` ist, wenn `match` `null` ist:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Runde Klammern um einen Teil eines Musters erzeugen eine **Capture-Gruppe**: Der Text, auf den dieser Teil gepasst hat, wird beiseitegelegt, damit du ihn später auslesen kannst.

Die Gruppen erscheinen nach `match[0]`, nummeriert von links nach rechts nach ihrer öffnenden Klammer:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// prints 2026-09-12
console.log(match[1]);
// prints 2026
console.log(match[3]);
// prints 12
```
`match[0]` ist also immer der gesamte Treffer, und `match[1]`, `match[2]`, ... sind die Gruppen. Eine Gruppe, die zu einem Muster gehört, das überhaupt nicht passt, lässt das gesamte `match` `null` zurückgeben.

---

Erfasse nur das, was du brauchst. Eine Gruppe ist nicht nur eine Möglichkeit, einen Teil später auszulesen; sie zeigt auch dem Leser, welcher Teil des Musters wichtig ist. In einem Zeitmuster, bei dem du nur die Minuten willst, klammere nur die Minuten und lasse den Rest ungruppiert:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// prints 35
```
Das ganze Muster muss weiterhin passen, also sind Stunden und Sekunden weiterhin erforderlich; sie werden nur nicht erfasst. Weniger Gruppen bedeuten weniger Nummern, die du beim Lesen von `match[1]`, `match[2]` und so weiter im Kopf behalten musst.

---

Runde Klammern zu zählen wird mühsam, und eine Gruppe in der Mitte eines Musters zu ergänzen, nummeriert alles Dahinter neu. Eine **benannte Gruppe** vermeidet beide Probleme: schreibe `?<name>` direkt hinter die öffnende Klammer und lies den Teil aus `match.groups` zurück:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// prints 2026
console.log(match.groups.month);
// prints 09
```
Benannte Gruppen sind weiterhin nummeriert, deshalb funktioniert `match[1]` weiterhin, aber `match.groups.year` sagt aus, was der Wert bedeutet. Wenn das Muster überhaupt keine benannte Gruppe hat, ist `match.groups` `undefined`.

---

Bis jetzt endete alles beim ersten Treffer. **Flags**, geschrieben nach dem schließenden Schrägstrich eines Literals, ändern das und andere Details der Suche:
- `g` global: finde jeden Treffer, nicht nur den ersten
- `i` ignoriere Groß- und Kleinschreibung, sodass `/cat/i` auch auf `Cat` und `CAT` passt

Mit dem `g`-Flag verhält sich `match` anders: Es gibt ein einfaches Array der gefundenen **Strings** zurück, ohne `index` und ohne Gruppen, oder `null`, wenn es keinen Treffer gibt:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// prints [ '1', '22', '333' ]
console.log(numbers.length);
// prints 3
```
Flags lassen sich in beliebiger Reihenfolge kombinieren, wie in `/cat/gi`. Beim `RegExp`-Konstruktor kommen sie ins zweite Argument: `new RegExp("\\d+", "g")`.

---

Das `g`-Flag liefert dir jeden gefundenen String, aber es verwirft die Gruppen. Wenn du die Gruppen *jedes* Treffers brauchst, verwende **`matchAll`**. Es gibt einen Iterator vollständiger Match-Objekte zurück, jedes genau wie das Ergebnis eines gewöhnlichen `match`-Aufrufs:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// prints a -> 1
// prints b -> 2
```
`matchAll` erfordert das `g`-Flag; ohne es wirft es einen `TypeError`. Da es einen Iterator zurückgibt, spreade ihn mit `[...text.matchAll(pattern)]`, wenn du ein echtes Array willst, und beachte, dass er gar nichts liefert, wenn das Muster nie passt.

---

**`replace`** gibt einen neuen String zurück, in dem der Treffer gegen etwas anderes ausgetauscht ist. Der ursprüngliche String wird nie verändert.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// prints the dog sleeps
```
Innerhalb des Ersatzstrings haben einige Sequenzen eine besondere Bedeutung:
- `$1`, `$2`, ... der von Gruppe 1, Gruppe 2, ... erfasste Text
- `$<name>` der von einer benannten Gruppe erfasste Text
- `$&` der gesamte Treffer

Das macht `replace` zu einem Umformungswerkzeug und nicht nur zu einem Austausch:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// prints 12/09/2026
```
Ohne das `g`-Flag wird nur der **erste** Treffer ersetzt.

---

Um **jeden** Treffer statt nur den ersten umzuschreiben, hast du zwei Möglichkeiten:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// prints a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// prints a# b#
```
**`replaceAll`** ist das klarere von beiden und akzeptiert auch einen einfachen String als Muster. Wenn du ihm ein Regex gibst, muss dieses Regex **unbedingt** das `g`-Flag tragen, sonst wirft es einen `TypeError`; genau das verhindert den stillen Fehler, `replace` zu schreiben und nur den ersten Treffer zu korrigieren.

---

Der Ersatz muss kein String sein. Wenn du eine **Funktion** übergibst, wird sie einmal pro Treffer aufgerufen, und was auch immer sie zurückgibt, wird anstelle dieses Treffers eingefügt.

Die Funktion erhält zuerst den gesamten Treffer, dann jede Capture-Gruppe:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// prints 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// prints Ann Lee
```
Dies ist die einzige Möglichkeit, den Ersatz aus dem gefundenen Text zu berechnen, was `$1` allein nicht kann.

---

**`split`** schneidet einen String in ein Array auseinander. Bei einem einfachen String schneidet er an genau diesem Text, bei einem Regex schneidet er bei jedem Treffer des Musters, sodass ein einziger Aufruf mit wechselnden Trennern umgehen kann:
```javascript
console.log("a, b;c".split(", "));
// prints [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// prints [ 'a', 'b', 'c' ]
```
Die Trenner selbst sind nicht Teil des Ergebnisses. Achte auf einen Trenner am Anfang oder Ende des Strings: Er erzeugt einen leeren String im Array, weil es auf dieser Seite ein leeres Feld gibt.

---

Ein letztes Flag vervollständigt die Sammlung. Standardmäßig bedeuten `^` und `$` den Anfang und das Ende des **gesamten Strings**, deshalb kann ein mit `^` verankertes Muster nur ganz am Anfang passen, selbst wenn der Text mehrere Zeilen hat.

Das **`m`**-Flag (multiline) ändert das: `^` und `$` passen dann auch direkt nach und direkt vor jedem Zeilenumbruch, sodass jede Zeile für sich verankert ist:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// prints [ 'note a' ]
console.log(text.match(/^note.*/gm));
// prints [ 'note a', 'note c' ]
```
Zwei Details sind hier wichtig. Standardmäßig passt der `.` nicht auf einen Zeilenumbruch (nur das `s`-Flag ändert das), deshalb stoppt `.*` von selbst am Zeilenende. Und `match` mit dem `g`-Flag gibt `null` zurück, kein leeres Array, wenn nichts passt, kombiniere es also mit `?? []`, wenn du versprichst, ein Array zurückzugeben.
