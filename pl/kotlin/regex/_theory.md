**Wyrażenie regularne** (albo **regex**) to mały wzorzec, który opisuje kształt tekstu: „cztery cyfry”, „słowo, po którym następuje `@`”, „cokolwiek między cudzysłowami”. W Kotlinie wzorzec jest obiektem `Regex`, tworzonym na dwa równoważne sposoby:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
Większość znaków we wzorcu oznacza samą siebie, ale kilka z nich to **skróty**:
- `\d` to dowolna cyfra, zapisywana w ciągu znaków Kotlina jako `"\\d"`, ponieważ `\` wymaga znaku ucieczki
- `[a-z]` to dowolna mała litera, a `[abc]` to dowolny ze znaków `a`, `b` lub `c`
- `+` po elemencie oznacza „jeden lub więcej”, więc `\d+` to ciąg cyfr

Najprostsze pytanie, jakie możesz zadać, to `matches`, które jest `true` tylko wtedy, gdy wzorzec opisuje **cały** ciąg znaków:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` jest często zbyt surowe: zwykle chcesz tylko wiedzieć, czy wzorzec pojawia się **gdziekolwiek** w tekście. Do tego służy `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
Obok `\d` są jeszcze dwa skróty, których będziesz używać bez przerwy: `\w` to znak słowa (litera, cyfra lub `_`), a `\s` to znak białej spacji. Każdy z nich można powtórzyć za pomocą **kwantyfikatora**:
- `+` jeden lub więcej
- `*` zero lub więcej
- `?` zero lub jeden
- `{3}` dokładnie trzy, `{2,4}` od dwóch do czterech

Podwajanie każdego ukośnika wstecznego jest męczące, więc wzorce zapisuje się zwykle jako **surowe ciągi znaków** w potrójnych cudzysłowach, gdzie `\` jest zwykłym znakiem:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` mówi tylko, *czy* wzorzec tam jest. `find` mówi także **co** i **gdzie**: zwraca pierwsze dopasowanie jako `MatchResult` albo `null`, gdy nie ma czego znaleźć.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` to dopasowany tekst, a `range` to indeksy, które zajmuje on w oryginalnym ciągu znaków. Ponieważ wynik jest nullable, sięgasz do niego bezpiecznym wywołaniem `?.`, które zwraca `null` zamiast powodować awarię, gdy nie znaleziono dopasowania:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Nawiasy okrągłe we wzorcu tworzą **grupę przechwytującą**: fragment dopasowania, który chcesz odczytać osobno. Przechowuje je `MatchResult.groupValues`, gdzie indeks `0` to całe dopasowanie, a `1`, `2`, ... to kolejne grupy od lewej do prawej:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Gdy nie ma żadnego dopasowania, `find` zwraca `null` i nie ma czego odczytywać, więc funkcja wydobywająca grupę zwykle decyduje, co zwrócić w takim przypadku:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Liczenie nawiasów, aby ustalić, że host to grupa `2`, staje się kruche, gdy tylko wzorzec się rozrasta. Grupie można nadać **nazwę** za pomocą `(?<name>...)` i odczytać ją z `groups` po tej nazwie:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` zwraca grupę jako `MatchGroup?`, więc nadal pytasz o jej `.value`. Grupa z nazwą jest też numerowana jak zwykle, więc `groupValues[1]` działa obok niej bez zmian.

---

`find` zatrzymuje się na pierwszym dopasowaniu. `findAll` zwraca **każde** dopasowanie jako `Sequence<MatchResult>`: leniwy łańcuch, który możesz traktować jak listę, używając `map`, `filter`, `count` i `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Gdy nic nie pasuje, `findAll` zwraca pustą sekwencję zamiast `null`, więc nie trzeba pisać bezpiecznego wywołania. Wypisanie samej sekwencji nie jest przydatne, pokazuje obiekt, a nie dopasowania: najpierw zamień ją na listę.

---

`replace` przepisuje tekst: zwraca **nowy** ciąg znaków, w którym każde dopasowanie zastąpiono podanym tekstem, pozostawiając oryginał nietknięty.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
W ciągu zastępującym `$1`, `$2`, ... oznaczają grupy przechwycone w danym dopasowaniu, więc możesz zmienić kolejność lub ponownie użyć dopasowanych fragmentów:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` to całe dopasowanie. Gdy potrzebujesz dosłownego `$` w tekście zastępującym, poprzedź go znakiem ucieczki jako `\$`.
`replace` przepisuje **każde** dopasowanie, więc gdy przepisany ma być tylko cały ciąg znaków, przypnij wzorzec **kotwicami** `^` (początek tekstu) i `$` (koniec tekstu):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

Ciąg zastępujący może tylko przestawiać fragmenty, które dostał. Gdy nowy tekst trzeba **obliczyć**, przekaż do `replace` lambdę: otrzymuje ona `MatchResult` i zwraca ciąg znaków, który zajmie jego miejsce.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Wewnątrz lambdy masz pełny `MatchResult`, więc `m.value`, `m.range` i `m.groupValues` są dostępne. Zauważ, że `$1` nie ma tu znaczenia: to zwykły znak w ciągu, który zwracasz.

---

`split` tnie ciąg znaków wszędzie tam, gdzie pasuje wzorzec, i zwraca kawałki jako `List<String>`. W przeciwieństwie do dzielenia po stałym separatorze, separator w postaci wyrażenia regularnego może opisać całą rodzinę separatorów:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
Dopasowane separatory nie są częścią wyniku. Jeśli tekst zaczyna się lub kończy separatorem, sąsiadujący z nim kawałek jest pusty:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` przyjmuje `limit` jako drugi argument, aby zatrzymać się po zadanej liczbie kawałków, pozostawiając resztę nietkniętą w ostatnim z nich.

---

Wzorce rozróżniają wielkość liter: `Regex("kotlin")` nie pasuje do `"Kotlin"`. Zamiast pisać `[kK][oO]...`, przekaż opcję jako drugi argument:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
Opcja należy do obiektu `Regex`, więc każda jego metoda jej przestrzega: tak samo `matches`, `find`, `findAll`, `replace` i `split`. Inne przydatne opcje to `RegexOption.MULTILINE`, dzięki której `^` i `$` pasują w każdym wierszu, oraz `RegexOption.DOT_MATCHES_ALL`. Aby je połączyć, przekaż zbiór: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` pasuje także do `cat` wewnątrz `catalog`. Aby wymagać całego słowa, użyj **granicy słowa** `\b`: pasuje ona do pustej pozycji między znakiem słowa a czymkolwiek innym, włącznie z początkiem i końcem tekstu.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Wzorzec jest zwykłym ciągiem znaków, więc można go zbudować z części w czasie działania programu:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

Znaki `. * + ? ( ) [ ] { } | ^ $ \` mają specjalne znaczenie wewnątrz wzorca. Najbardziej zdradliwy jest `.`, który pasuje do **dowolnego** znaku, a nie do kropki. Aby oznaczał sam siebie, poprzedź go ukośnikiem wstecznym:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
Gdy szukany tekst pochodzi ze zmiennej i ma być potraktowany dosłownie, pozwól bibliotece dodać znaki ucieczki za pomocą `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` razem z grupami zamienia wiersz tekstu w dane o strukturze. Każdy `MatchResult` z sekwencji niesie własne `groupValues`, więc jeden łańcuch może zbudować listę, mapę albo sumę:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` buduje mapę z par `key to value` zwracanych przez lambdę. Gdy wzorzec ma stałą liczbę grup, `destructured` pozwala rozpakować je do nazwanych zmiennych zamiast odczytywać po indeksie:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Nawiasy kwadratowe definiują **klasę znaków**: jeden znak z wymienionego zbioru. Wewnątrz nich możesz używać zakresów, a `^` na początku neguje całą klasę:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
Klasa wybiera tylko spośród pojedynczych znaków. Aby wybrać spośród całych alternatyw, użyj `|`, zwykle zamkniętego w grupie, żeby nie pochłonął reszty wzorca:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Ponieważ `findAll` daje sekwencję, znane ci już metody agregujące działają także na dopasowaniach: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Wydobycie liczb ze swobodnego tekstu to zadanie dwuetapowe: dopasuj je, a potem zamień tekst na liczbę.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Realistyczny wzorzec zwykle miesza wszystko naraz: grupy, aby zachować potrzebne części, `\.` z ucieczką dla dosłownych kropek oraz lambdę zastępującą, aby odbudować wokół nich tekst.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Trzymaj wzorce tak proste, jak pozwala na to zadanie: wzorzec próbujący opisać każdy poprawny adres e-mail jest nieczytelny, podczas gdy `\w+@\w+\.\w+` w zupełności wystarczy, aby znaleźć adresy w zdaniu.
