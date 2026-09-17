**Wyjątek** to sposób, w jaki Kotlin zgłasza, że instrukcja nie może zostać wykonana. Zamiana `"abc"` na liczbę, dzielenie liczby całkowitej przez zero i odczyt poza końcem listy — wszystkie te operacje go zgłaszają.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Ten program wypisuje `before`, a następnie się zatrzymuje. `toInt()` nie potrafi odczytać `"abc"`, więc **zgłasza** `NumberFormatException`; nic w programie się nim nie zajmuje, więc Kotlin kończy program raportem błędu, a `after` nigdy nie jest wypisywany.

Wyjątek możesz też zgłosić samodzielnie za pomocą słowa kluczowego `throw`:
```kotlin
throw Exception("something went wrong")
```

Wyjątek, którego nikt nie obsłuży, to nie ostrzeżenie: to koniec działania programu.

---

Aby utrzymać program przy życiu, umieść ryzykowną instrukcję w bloku `try`, a sposób naprawy opisz w bloku `catch`:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin wykonuje blok `try`; gdy tylko któraś instrukcja wewnątrz niego zgłosi wyjątek, reszta bloku jest pomijana, a sterowanie przechodzi do bloku `catch`. Nazwa w nawiasie — tutaj `e` — to obiekt wyjątku, a `Exception` to przechwytywany typ.

Gdy blok `catch` zakończy działanie, program normalnie kontynuuje od linii następującej po całej konstrukcji `try`/`catch`.

---

Przechwycenie `Exception` obejmuje wszystko, co rzadko jest tym, czego chcesz: literówka gdzie indziej w bloku również zostałaby po cichu pochłonięta. Zamiast tego podaj **dokładny typ**, od którego wiesz, jak się odbudować.

Każda awaria ma swój własny typ. `"abc".toInt()` zgłasza `NumberFormatException`, więc to właśnie ten typ należy przechwycić:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Jeśli wewnątrz bloku zostanie zgłoszony inny rodzaj wyjątku, ten `catch` nie pasuje i wyjątek wędruje dalej poza funkcję.

---

Po jednym `try` może następować kilka bloków `catch`, z których każdy obsługuje inny typ:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin sprawdza bloki **od góry do dołu** i wykonuje pierwszy, którego typ pasuje. Wykonywany jest zawsze tylko jeden blok.

Kolejność ma więc znaczenie. `NumberFormatException` i `IndexOutOfBoundsException` to oba rodzaje `Exception`, więc `catch (e: Exception)` zapisany jako pierwszy pasowałby do każdej awarii, a bloki poniżej nigdy by się nie wykonały. Najbardziej konkretny typ zapisz jako pierwszy, a najbardziej ogólny jako ostatni.

---

Na końcu można dodać blok `finally`. Wykonuje się on **niezależnie od tego, co się stanie**: po udanym `try`, po tym, jak `catch` naprawi sytuację, a nawet gdy wyjątek w ogóle nie zostanie przechwycony.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
To czyni go odpowiednim miejscem na sprzątanie, które nie może zostać pominięte, na przykład zamknięcie pliku. `try` wymaga co najmniej `catch` albo `finally`, ale może mieć oba.

---

W Kotlinie `try` to nie tylko instrukcja: to **wyrażenie**, które daje wartość. Tą wartością jest ostatnie wyrażenie tego bloku, który się wykonał — bloku `try`, gdy nic nie zawiodło, bloku `catch`, gdy jednak zawiodło.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
To idiomatyczna forma w Kotlinie. Zamiast deklarować `var`, przypisywać mu wartość w dwóch miejscach i liczyć, że każda ścieżka go ustawi, dostajesz pojedynczy `val`, który zawsze przechowuje użyteczną wartość.

Zwróć uwagę, że blok `finally` nigdy nie zmienia wartości: wykonuje się wyłącznie dla swoich efektów ubocznych.

---

Ponieważ `try` jest wyrażeniem, można go użyć wszędzie tam, gdzie oczekiwana jest wartość — także jako całe ciało funkcji zapisanej za pomocą `=`:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Oba bloki muszą zwracać wartość tego samego typu, tutaj `Int`. Zapisz wartość zastępczą jako ostatnie wyrażenie bloku `catch`; w żadnym z bloków nie ma `return`.

---

Zgłaszanie i przechwytywanie wyjątków nie jest darmowe, dlatego dla typowych konwersji Kotlin oferuje tańszy wariant, który zamiast zgłaszać wyjątek, po prostu zwraca `null`: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
W połączeniu z operatorem elvis `?:`, który dostarcza wartość zastępczą, gdy wartość po jego lewej stronie to `null`, cały `try`/`catch` skraca się do jednej linii:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Sięgaj po `try`/`catch`, gdy awaria jest naprawdę wyjątkowa; sięgaj po `toIntOrNull()`, gdy spodziewasz się nieprawidłowych danych wejściowych.

---

Twoje własne funkcje mogą odrzucać złe dane wejściowe w taki sam sposób jak biblioteka standardowa, za pomocą `throw`. Biblioteka udostępnia już typ dla najczęstszego przypadku: `IllegalArgumentException` oznacza „wartość, którą mi przekazałeś, jest niedopuszczalna”.

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` kończy działanie funkcji natychmiast — `return` znajdujący się poniżej nigdy nie zostaje wykonany. To wywołujący decyduje, co z tym zrobić:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Zgłoszenie wyjątku jest lepsze niż ciche zwrócenie zmyślonej wartości: błędna odpowiedź wędruje daleko, a wyjątek zatrzymuje się przy pierwszym wywołującym, który jest gotów go obsłużyć.

---

Każdy wyjątek niesie ze sobą tekst, z jakim został utworzony. Wewnątrz bloku `catch` odczytujesz go poprzez właściwość `message` obiektu wyjątku:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` jest nullowalne, ponieważ wyjątek może zostać utworzony bez żadnego tekstu; `e.message ?: "unknown"` daje bezpieczną wartość zastępczą, gdy potrzebujesz zwykłego `String`.

Wypisuj raczej `e.message` niż sam obiekt wyjątku: własny tekst obiektu zawiera też nazwę klasy, co jest szumem dla osoby czytającej wynik.

---

Pisanie `if (...) throw IllegalArgumentException(...)` przy każdym argumencie robi się uciążliwe, więc Kotlin dostarcza dwa skróty, które czyta się jak zwykłe zdania:

```kotlin
require(n >= 0) { "n must not be negative" }   // zgłasza IllegalArgumentException
check(started) { "not started" }               // zgłasza IllegalStateException
```
Obie funkcje przyjmują warunek i blok tworzący komunikat, i obie zgłaszają wyjątek **gdy warunek jest fałszywy**. Jedyną różnicą jest typ wyjątku, a ta różnica jest wiadomością dla czytelnika:

* `require` pilnuje **argumentów** przekazanych przez wywołującego i kończy się niepowodzeniem z `IllegalArgumentException`.
* `check` pilnuje **stanu** obiektu lub programu i kończy się niepowodzeniem z `IllegalStateException`.

Blok jest obliczany tylko wtedy, gdy warunek zawiedzie, więc budowanie komunikatu nic nie kosztuje na szczęśliwej ścieżce.

---

Gdy żaden z wbudowanych typów dobrze nie opisuje twojej awarii, zadeklaruj własny. Wyjątek to zwykła klasa, która rozszerza `Exception` i przekazuje swój tekst do klasy nadrzędnej:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Ta pojedyncza linia to kompletny typ wyjątku. Jest zgłaszany i przechwytywany tak jak każdy inny, a `e.message` zwraca tekst, z jakim został utworzony:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
Zyskujesz precyzję: wywołujący może przechwycić samodzielnie `InsufficientFundsException`, a każdą inną awarię puścić dalej.

---

`runCatching` wykonuje blok i nigdy nie pozwala wyjątkowi się wydostać. Zamiast tego zwraca `Result` — obiekt przechowujący **albo** wartość zwróconą przez blok, **albo** zgłoszony przez niego wyjątek:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
Wartość odczytuje się później, a ty decydujesz, czym ma się stać awaria:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` zamienia awarię w `null`, podczas gdy `getOrElse { ... }` wykonuje blok, aby zbudować wartość zastępczą. Nic nie jest zgłaszane w miejscu wywołania, więc awarię można przenieść i obsłużyć później.

---

Ponieważ `Result` jest zwykłą wartością, można go przechować w `val` i odpytywać dowolną liczbę razy:

```kotlin
val result = runCatching { "abc".toInt() }

println(result.getOrElse { 0 })  // 0
println(result.getOrNull())      // null
println(result.isSuccess)        // false
```
`try`/`catch` nie potrafi tego zrobić. Tam wynik jest obsługiwany tylko raz, w miejscu awarii, a potem znika. `Result` zachowuje awarię, dzięki czemu kod, który na nią reaguje, nie musi znajdować się tam, gdzie się wydarzyła.

---

`Result` można też sprawdzić bez jego rozpakowywania. `onFailure` wykonuje swój blok tylko wtedy, gdy wynik zawiera wyjątek, `onSuccess` — tylko wtedy, gdy zawiera wartość, a **oba zwracają ten sam `Result`**, dzięki czemu wywołania można łączyć w łańcuch:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Wewnątrz bloku wyjątek (lub wartość) jest dostępny jako `it`, więc `it.message` to tekst awarii.

To układ „zaloguj i działaj dalej”: zgłoś problem tam, gdzie się wydarzył, a potem kontynuuj, bez wczesnego `return` i bez `var` ustawianego w dwóch miejscach.

---

To, gdzie umieścisz `try`, decyduje, ile pracy niszczy pojedyncza zła wartość. Owiń nią **całą pętlę**, a pierwsza awaria porzuci resztę partii; owiń nią **ciało**, a straci się tylko ten jeden element:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // pomiń tę wartość
    }
}
println(total) // 8
```
Świetnie łączy się to z walidującą funkcją, która zgłasza wyjątek: funkcja ustala jedną regułę i odrzuca wszystko, co ją łamie, a pętla decyduje, że odrzucenie kosztuje tylko jeden element.
