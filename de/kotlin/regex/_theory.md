Ein **regulärer Ausdruck** (oder **Regex**) ist ein kleines Muster, das die Form eines Textes beschreibt: „vier Ziffern“, „ein Wort gefolgt von `@`“, „alles zwischen Anführungszeichen“. In Kotlin ist ein Muster ein `Regex`-Objekt, das auf zwei gleichwertige Arten gebaut wird:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
Die meisten Zeichen in einem Muster stehen für sich selbst, aber einige sind **Kurzschreibweisen**:
- `\d` ist eine beliebige Ziffer, geschrieben als `"\\d"` in einer Kotlin-Zeichenkette, weil man `\` escapen muss
- `[a-z]` ist ein beliebiger Kleinbuchstabe, und `[abc]` ist eines von `a`, `b` oder `c`
- `+` nach einem Element bedeutet „eines oder mehr davon“, daher ist `\d+` eine Folge von Ziffern

Die einfachste Frage, die du stellen kannst, ist `matches`, die nur dann `true` ist, wenn das Muster auf die **gesamte** Zeichenkette passt:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, der Buchstabe ist keine Ziffer
```

---

`matches` ist oft zu streng: Meist will man nur wissen, ob das Muster **irgendwo** im Text vorkommt. Das erledigt `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, die ganze Zeichenkette sind keine Ziffern
println(digits.containsMatchIn("order 42"))  // true, "42" ist darin enthalten
```
Neben `\d` gibt es zwei weitere Kurzschreibweisen, die du ständig brauchst: `\w` ist ein Wortzeichen (Buchstabe, Ziffer oder `_`) und `\s` ist ein Whitespace-Zeichen. Jedes davon kann mit einem **Quantifizierer** wiederholt werden:
- `+` eines oder mehr
- `*` null oder mehr
- `?` null oder eines
- `{3}` genau drei, `{2,4}` von zwei bis vier

Doppelte Backslashes werden schnell unübersichtlich, daher werden Muster meist als **Raw-Strings** mit dreifachen Anführungszeichen geschrieben, in denen `\` nur ein gewöhnliches Zeichen ist:
```kotlin
val digits = Regex("""\d+""") // dasselbe wie Regex("\\d+")
```

---

`containsMatchIn` sagt nur, *ob* das Muster da ist. `find` sagt auch **was** und **wo**: Es gibt den ersten Treffer als `MatchResult` zurück, oder `null`, wenn es nichts zu finden gibt.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` ist der gefundene Text und `range` sind die Indizes, die er in der ursprünglichen Zeichenkette abdeckt. Weil das Ergebnis nullable ist, greifst du mit dem sicheren Aufruf `?.` darauf zu, der `null` liefert, statt abzustürzen, wenn kein Treffer gefunden wurde:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Runde Klammern in einem Muster erzeugen eine **erfassende Gruppe**: ein Teil des Treffers, den du separat zurücklesen willst. `MatchResult.groupValues` speichert sie, mit dem Index `0` für den ganzen Treffer und `1`, `2`, ... für die Gruppen, von links nach rechts:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Wenn es überhaupt keinen Treffer gibt, gibt `find` `null` zurück und es gibt nichts zu lesen, daher legt eine Funktion, die eine Gruppe extrahiert, üblicherweise fest, was sie in diesem Fall zurückgibt:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Klammern zu zählen, um herauszufinden, dass der Host Gruppe `2` ist, wird fragil, sobald das Muster wächst. Eine Gruppe kann mit `(?<name>...)` einen **Namen** bekommen und über diesen Namen aus `groups` gelesen werden:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` gibt die Gruppe als `MatchGroup?` zurück, daher fragst du weiterhin nach ihrem `.value`. Eine benannte Gruppe wird auch wie üblich nummeriert, sodass `groupValues[1]` daneben weiterhin funktioniert.

---

`find` stoppt beim ersten Treffer. `findAll` gibt **jeden** Treffer zurück, als `Sequence<MatchResult>`: eine verzögerte Kette, die du wie eine Liste mit `map`, `filter`, `count` und `toList` behandeln kannst.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Wenn nichts passt, gibt `findAll` eine leere Sequenz statt `null` zurück, daher musst du keinen sicheren Aufruf schreiben. Die Sequenz selbst auszugeben ist nicht nützlich, sie zeigt das Objekt, nicht die Treffer: Wandle sie zuerst in eine Liste um.

---

`replace` schreibt den Text um: Es gibt eine **neue** Zeichenkette zurück, in der jeder Treffer gegen den Ersatz getauscht ist, während das Original unverändert bleibt.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
Im Ersatz-String stehen `$1`, `$2`, ... für die erfassten Gruppen dieses Treffers, sodass du die gefundenen Teile neu ordnen oder wiederverwenden kannst:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` ist der ganze Treffer. Wenn du ein wörtliches `$` im Ersatz brauchst, escape es als `\$`.
`replace` schreibt **jeden** Treffer um, wenn also nur eine vollständige Zeichenkette umgeschrieben werden soll, verankerst du das Muster mit den **Ankern** `^` (Anfang des Texts) und `$` (Ende des Texts):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nichts wird ersetzt
```

---

Ein Ersatz-String kann nur die Teile neu anordnen, die er bekommt. Wenn der neue Text **berechnet** werden muss, übergib stattdessen ein Lambda an `replace`: Es erhält das `MatchResult` und gibt die Zeichenkette zurück, die an seine Stelle tritt.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Innerhalb des Lambdas hast du das volle `MatchResult`, daher sind `m.value`, `m.range` und `m.groupValues` alle verfügbar. Beachte, dass `$1` hier keine Bedeutung hat: Es ist ein gewöhnliches Zeichen in der Zeichenkette, die du auch immer zurückgibst.

---

`split` schneidet eine Zeichenkette an jeder Stelle auf, an der das Muster passt, und gibt die Teile als `List<String>` zurück. Anders als beim Aufteilen an einem festen Trennzeichen-String kann ein Regex-Trenner eine ganze Familie von Trennern beschreiben:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
Die erkannten Trenner sind nicht Teil des Ergebnisses. Wenn der Text mit einem Trenner beginnt oder endet, ist das angrenzende Teil leer:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` akzeptiert ein `limit` als zweites Argument, um nach einer gegebenen Anzahl von Teilen anzuhalten und den Rest unangetastet im letzten zu belassen.

---

Muster unterscheiden Groß- und Kleinschreibung: `Regex("kotlin")` passt nicht auf `"Kotlin"`. Statt `[kK][oO]...` zu schreiben, übergib eine Option als zweites Argument:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
Die Option gehört zum `Regex`, daher befolgt jede Methode dieses Objekts sie: `matches`, `find`, `findAll`, `replace` und `split` gleichermaßen. Weitere nützliche Optionen sind `RegexOption.MULTILINE`, die `^` und `$` in jeder Zeile passen lässt, und `RegexOption.DOT_MATCHES_ALL`. Um sie zu kombinieren, übergib ein Set: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` passt auch auf das `cat` in `catalog`. Um ein ganzes Wort zu verlangen, verwende die **Wortgrenze** `\b`: Sie passt auf die leere Position zwischen einem Wortzeichen und allem anderen, einschließlich Anfang und Ende des Texts.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Ein Muster ist eine gewöhnliche Zeichenkette, daher kann es zur Laufzeit aus Teilen zusammengesetzt werden:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

Die Zeichen `. * + ? ( ) [ ] { } | ^ $ \` haben eine besondere Bedeutung in einem Muster. Am tückischsten ist `.`, das auf **jedes** Zeichen passt, nicht auf einen Punkt. Um das Zeichen selbst zu meinen, escape es mit einem Backslash:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, der Punkt passt auf das x
println(Regex("""3\.14""").matches("3x14")) // false
```
Wenn der gesuchte Text aus einer Variable kommt und wörtlich genommen werden muss, überlass das Escapen der Bibliothek mit `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` und Gruppen verwandeln zusammen eine Textzeile in strukturierte Daten. Jedes `MatchResult` der Sequenz trägt sein eigenes `groupValues`, sodass eine einzige Kette eine Liste, eine Map oder eine Summe bauen kann:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` baut aus den `key to value`-Paaren, die das Lambda zurückgibt, eine Map. Wenn ein Muster eine feste Anzahl von Gruppen hat, kannst du mit `destructured` die Gruppen in benannte Variablen entpacken, statt sie über den Index zu lesen:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Eckige Klammern definieren eine **Zeichenklasse**: ein Zeichen aus der aufgeführten Menge. In ihnen kannst du Bereiche verwenden, und ein führendes `^` negiert die ganze Klasse:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, keine Ziffer erlaubt
```
Eine Klasse wählt nur zwischen einzelnen Zeichen. Um zwischen ganzen Alternativen zu wählen, verwende `|`, meist in eine Gruppe eingepackt, damit sie den Rest des Musters nicht verschlingt:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Weil `findAll` eine Sequenz liefert, funktionieren die aggregierenden Methoden, die du schon kennst, auch auf Treffern: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Zahlen aus freiem Text zu extrahieren ist eine Aufgabe in zwei Schritten: erst die Treffer finden, dann den Text in eine Zahl umwandeln.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Ein realistisches Muster mischt üblicherweise alles auf einmal: Gruppen, um die Teile zu behalten, die du brauchst, ein escaptes `\.` für die wörtlichen Punkte und einen Lambda-Ersatz, um den Text um sie herum neu aufzubauen.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Halte Muster so einfach wie die Aufgabe es erlaubt: Ein Muster, das jede gültige E-Mail-Adresse beschreiben will, ist unlesbar, während `\w+@\w+\.\w+` ausreicht, um die Adressen in einem Satz zu finden.
