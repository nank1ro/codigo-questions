Un'**espressione regolare** (o **regex**) è un piccolo pattern che descrive una forma di testo: "quattro cifre", "una parola seguita da `@`", "qualsiasi cosa tra virgolette". In Kotlin un pattern è un oggetto `Regex`, costruito in due modi equivalenti:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
La maggior parte dei caratteri in un pattern rappresenta sé stesso, ma alcuni sono **abbreviazioni**:
- `\d` è una qualsiasi cifra, scritto `"\\d"` in una stringa Kotlin perché `\` va preceduto da un escape
- `[a-z]` è una qualsiasi lettera minuscola, e `[abc]` è una qualsiasi tra `a`, `b` o `c`
- `+` dopo un elemento significa "uno o più di esso", quindi `\d+` è una sequenza di cifre

La domanda più semplice che puoi porre è `matches`, che vale `true` solo quando il pattern descrive l'**intera** stringa:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` è spesso troppo rigido: di solito vuoi solo sapere se il pattern compare **da qualche parte** nel testo. Per questo esiste `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
Accanto a `\d` ci sono altre due abbreviazioni che userai di continuo: `\w` è un carattere di parola (lettera, cifra o `_`) e `\s` è un carattere di spaziatura. Ognuno di essi può essere ripetuto con un **quantificatore**:
- `+` uno o più
- `*` zero o più
- `?` zero o uno
- `{3}` esattamente tre, `{2,4}` da due a quattro

Raddoppiare ogni backslash diventa fastidioso, quindi i pattern di solito si scrivono come **stringhe raw** con triple virgolette, dove `\` è solo un carattere:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` dice solo *se* il pattern è presente. `find` dice anche **cosa** e **dove**: restituisce la prima corrispondenza come `MatchResult`, oppure `null` quando non c'è nulla da trovare.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` è il testo trovato e `range` sono gli indici che copre nella stringa originale. Poiché il risultato è nullable vi si accede con la chiamata sicura `?.`, che dà `null` invece di andare in crash quando non è stata trovata nessuna corrispondenza:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Le parentesi tonde in un pattern creano un **gruppo di cattura**: un pezzo della corrispondenza che vuoi rileggere separatamente. `MatchResult.groupValues` li contiene, con l'indice `0` per la corrispondenza intera e `1`, `2`, ... per i gruppi, da sinistra a destra:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Quando non c'è affatto una corrispondenza, `find` restituisce `null` e non c'è nulla da leggere, quindi una funzione che estrae un gruppo di solito decide cosa restituire in quel caso:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Contare le parentesi per scoprire che l'host è il gruppo `2` diventa fragile non appena il pattern cresce. A un gruppo si può dare un **nome** con `(?<name>...)` e leggerlo da `groups` tramite quel nome:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` restituisce il gruppo come `MatchGroup?`, quindi devi comunque chiederne il `.value`. Un gruppo con nome viene anche numerato come al solito, quindi `groupValues[1]` continua a funzionare al suo fianco.

---

`find` si ferma alla prima corrispondenza. `findAll` restituisce **tutte** le corrispondenze, come `Sequence<MatchResult>`: una catena pigra che puoi trattare come una lista con `map`, `filter`, `count` e `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Quando nulla corrisponde, `findAll` restituisce una sequenza vuota invece di `null`, quindi non c'è nessuna chiamata sicura da scrivere. Stampare la sequenza stessa non è utile, mostra l'oggetto, non le corrispondenze: trasformala prima in una lista.

---

`replace` riscrive il testo: restituisce una **nuova** stringa in cui ogni corrispondenza è sostituita dal rimpiazzo, lasciando intatto l'originale.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
Nella stringa di rimpiazzo, `$1`, `$2`, ... rappresentano i gruppi catturati di quella corrispondenza, così puoi riordinare o riutilizzare i pezzi che hai trovato:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` è la corrispondenza intera. Se ti serve un `$` letterale nel rimpiazzo, scrivilo con l'escape come `\$`.
`replace` riscrive **ogni** corrispondenza, quindi quando solo una stringa completa deve essere riscritta, fissa il pattern con le **ancore** `^` (inizio del testo) e `$` (fine del testo):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

Una stringa di rimpiazzo può solo riorganizzare i pezzi che le sono stati dati. Quando il nuovo testo deve essere **calcolato**, passa invece una lambda a `replace`: riceve il `MatchResult` e restituisce la stringa che ne prende il posto.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Dentro la lambda hai a disposizione il `MatchResult` completo, quindi `m.value`, `m.range` e `m.groupValues` sono tutti disponibili. Nota che `$1` qui non ha significato: è un carattere ordinario in qualsiasi stringa tu restituisca.

---

`split` taglia una stringa ovunque il pattern corrisponda e restituisce i pezzi come `List<String>`. A differenza della divisione su una stringa delimitatrice fissa, un separatore regex può descrivere un'intera famiglia di separatori:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
I separatori trovati non fanno parte del risultato. Se il testo inizia o finisce con un separatore, il pezzo accanto ad esso è vuoto:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` accetta un `limit` come secondo argomento per fermarsi dopo un dato numero di pezzi, lasciando il resto intatto nell'ultimo.

---

I pattern distinguono le maiuscole dalle minuscole: `Regex("kotlin")` non corrisponde a `"Kotlin"`. Invece di scrivere `[kK][oO]...`, passa un'opzione come secondo argomento:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
L'opzione appartiene al `Regex`, quindi ogni metodo di quell'oggetto la rispetta: `matches`, `find`, `findAll`, `replace` e `split` allo stesso modo. Altre opzioni utili sono `RegexOption.MULTILINE`, che fa corrispondere `^` e `$` a ogni riga, e `RegexOption.DOT_MATCHES_ALL`. Per combinarle, passa un set: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` corrisponde anche al `cat` dentro `catalog`. Per richiedere una parola intera, usa il **confine di parola** `\b`: corrisponde alla posizione vuota tra un carattere di parola e qualsiasi altra cosa, compreso l'inizio e la fine del testo.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Un pattern è una stringa ordinaria, quindi può essere costruito da parti a runtime:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

I caratteri `. * + ? ( ) [ ] { } | ^ $ \` hanno un significato speciale dentro un pattern. Il più insidioso è `.`, che corrisponde a un carattere **qualsiasi**, non a un punto. Per indicare il carattere stesso, mettilo in escape con un backslash:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
Quando il testo da cercare viene da una variabile e deve essere preso alla lettera, lascia fare l'escape alla libreria con `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` e i gruppi insieme trasformano una riga di testo in dati strutturati. Ogni `MatchResult` della sequenza porta con sé il proprio `groupValues`, quindi una sola catena può costruire una lista, una mappa o un totale:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` costruisce una mappa a partire dalle coppie `key to value` restituite dalla lambda. Quando un pattern ha un numero fisso di gruppi, `destructured` ti permette di spacchettarli in variabili nominate invece di leggerli per indice:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Le parentesi quadre definiscono una **classe di caratteri**: un solo carattere tratto dall'insieme elencato. Al loro interno puoi usare gli intervalli, e una `^` iniziale nega l'intera classe:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
Una classe sceglie solo tra caratteri singoli. Per scegliere tra alternative intere, usa `|`, di solito avvolto in un gruppo così che non ingoi il resto del pattern:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Poiché `findAll` dà una sequenza, i metodi di aggregazione che conosci già funzionano anche sulle corrispondenze: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Estrarre numeri da testo libero è un lavoro in due passi: trovarli, poi convertire il testo in numero.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Un pattern realistico di solito mescola tutto insieme: gruppi per conservare le parti che ti servono, un `\.` in escape per i punti letterali e un rimpiazzo con lambda per ricostruire il testo attorno a essi.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Mantieni i pattern semplici quanto il compito lo consente: un pattern che prova a descrivere ogni indirizzo email legale è illeggibile, mentre `\w+@\w+\.\w+` basta per trovare gli indirizzi in una frase.
