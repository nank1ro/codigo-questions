Czasami wartość po prostu nie istnieje: użytkownik bez drugiego imienia, wyszukiwanie bez wyniku, tekst, którego nie da się zamienić w liczbę.
Kotlin reprezentuje brakującą wartość za pomocą `null`, ale zwykła zmienna nigdy nie może jej przechowywać. Każdy typ jest domyślnie **non-null**:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Aby dopuścić brakującą wartość, deklarujesz typ **nullable**, dodając znak zapytania `?` po typie.
`String?` przechowuje albo `String`, albo `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` i `String?` to dwa różne typy: `String` nigdy nie jest nieobecny, `String?` może być.

---

Różnica między `String` a `String?` jest sprawdzana przez **kompilator**, a nie w czasie działania.
Przypisanie `null` do typu non-null albo przekazanie wartości nullable tam, gdzie oczekiwana jest wartość non-null, to błąd kompilacji, więc program w ogóle się nie uruchamia:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
W ten sposób Kotlin unika awarii „null pointer”, typowych dla innych języków: wartość może być nieobecna tylko tam, gdzie jawnie zadeklarowałeś to za pomocą `?`.

---

Zapis `?` działa wszędzie tam, gdzie występuje typ: funkcja może przyjmować parametr nullable i może zwracać wartość nullable.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
Nie można wywołać metody bezpośrednio na wartości nullable, ponieważ może ona być `null`.
Operator **bezpiecznego wywołania** `?.` wywołuje metodę tylko wtedy, gdy wartość nie jest `null`; w przeciwnym razie całe wyrażenie ma wartość `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
Wynik bezpiecznego wywołania jest zawsze nullable: `word?.length` to `Int?`, a nie `Int`.

---

Bardzo często jedyną rzeczą, jakiej chcesz od wartości nullable, jest sama wartość albo wartość domyślna.
**Operator Elvisa** `?:` robi dokładnie to: zwraca lewą stronę, gdy nie jest `null`, a w przeciwnym razie wartość po swojej prawej stronie:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Ponieważ prawa strona jest używana tylko wtedy, gdy lewa jest `null`, wynik jest non-null, gdy wartość domyślna jest non-null.
`?:` dobrze łączy się z `?.`, aby zamienić bezpieczne wywołanie z powrotem w zwykłą wartość:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Bezpieczne wywołania można **łączyć w łańcuchy**: gdy tylko jedno ogniwo jest `null`, reszta łańcucha jest pomijana, a całe wyrażenie staje się `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Łańcuch zakończony `?:` daje wynik non-null w jednej linii:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Łańcuchy bezpiecznych wywołań sprawdzają się przy zagnieżdżonych obiektach, gdzie dowolny poziom może być nieobecny:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Każdy `?.` chroni kolejny krok, a końcowy `?:` dostarcza wartość domyślną.

---

Operator **asercji non-null** `!!` zamienia wartość nullable w wartość non-null, mówiąc kompilatorowi „jestem pewien, że to nie jest `null`”:
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Jeśli się mylisz i wartość jest `null`, program ulega awarii w czasie działania z `NullPointerException`, czyli z tym właśnie błędem, któremu Kotlin miał zapobiegać:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Używaj `!!` tylko wtedy, gdy wartość naprawdę nie może być `null`; w pozostałych przypadkach preferuj `?.`, `?:` i sprawdzanie `null`.

---

Gdy sprawdzisz wartość pod kątem `null` za pomocą `if`, kompilator to zapamiętuje: w gałęzi, w której wiadomo, że wartość jest non-null, jest ona **smart cast** do typu non-null i możesz używać jej bezpośrednio, bez `?.` czy `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
To samo dzieje się po wcześniejszym wyjściu z funkcji:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Smart casty działają na zmiennych `val` i parametrach funkcji, których wartość nie może się zmienić między sprawdzeniem a użyciem.

---

`let` wykonuje blok kodu z wartością, na której został wywołany; wewnątrz bloku jest ona dostępna jako `it`.
W połączeniu z bezpiecznym wywołaniem `?.let` wykonuje blok **tylko** wtedy, gdy wartość nie jest `null`, a wewnątrz bloku `it` jest non-null:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
To zwięzła alternatywa dla `if (x != null) { ... }`, gdy potrzebujesz wartości tylko wewnątrz bloku.

---

`let` również **zwraca** wartość ostatniego wyrażenia w swoim bloku, więc `?.let` może przekształcić wartość nullable, a `?:` może wstawić wartość domyślną, gdy jest ona `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Gdy `price` jest `null`, blok `let` jest pomijany, wyrażenie ma wartość `null`, a operator Elvisa zwraca `"free"`.

---

Kolekcje również mogą przechowywać elementy nullable: `List<Int?>` może zawierać wpisy `null`, podczas gdy `List<Int>` nigdy.
`filterNotNull()` zwraca nową listę bez wpisów `null`, a typ jej elementów staje się non-null, dzięki czemu możesz swobodnie korzystać z elementów:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Wiele funkcji standardowych zwraca `null` zamiast zawieść. `toIntOrNull()` przekształca ciąg znaków w `Int` albo zwraca `null`, gdy tekst nie jest liczbą całkowitą:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` przekształca każdy element jak `map`, ale pomija wyniki, które są `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Czasami właściwości nie można nadać wartości w momencie tworzenia obiektu, ale wiesz, że zostanie ona ustawiona, zanim będzie użyta.
Zamiast czynić ją nullable, oznacz ją słowem `lateinit`: typ pozostaje non-null i nie trzeba używać `?.` przy jej odczycie:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` ma pewne zasady: działa tylko na właściwościach `var`, tylko z typami non-null i nie działa z typami pierwotnymi, takimi jak `Int` czy `Boolean`.
Odczytanie właściwości `lateinit` przed jej przypisaniem rzuca `UninitializedPropertyAccessException`; możesz najpierw sprawdzić ją za pomocą `::player.isInitialized`.

---

Gdy `null` oznacza, że wywołujący popełnił błąd, zakończ działanie wcześnie za pomocą `requireNotNull`.
Zwraca ona wartość jako non-null, gdy jest obecna, a gdy jest `null`, rzuca `IllegalArgumentException` z opcjonalnym komunikatem:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Po wywołaniu kompilator wykonuje również smart cast samego `name` na `String`, więc `name.length` jest dozwolone od tej linii wzwyż.
W przeciwieństwie do `!!` awaria niesie czytelny komunikat i wskazuje, że to *argument* był nieprawidłowy.

---

Funkcję rozszerzającą można zadeklarować na **odbiorniku nullable**, więc można ją wywołać nawet na wartości `null`. Wewnątrz `this` jest nullable i musi zostać sprawdzone:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Zauważ, że w miejscu wywołania nie trzeba używać `?.`: funkcja sama obsługuje przypadek `null`.
Biblioteka standardowa używa tej sztuczki w `isNullOrEmpty()` i `orEmpty()`, które można bezpiecznie wywołać na dowolnym `String?`.

---

Prawa strona `?:` może być dowolnym wyrażeniem, także `return`. Daje to zwięzły sposób na wyjście z funkcji, gdy tylko okaże się, że wartości brakuje:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Wszystkie poznane narzędzia dobrze się ze sobą łączą: parametry nullable i typy zwracane opisują *gdzie* wartość może być nieobecna, a `?.`, `?:`, `let`, smart casty i `toIntOrNull` obsługują taki przypadek bez żadnej awarii.
