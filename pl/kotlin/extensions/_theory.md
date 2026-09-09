**Funkcja rozszerzająca** dodaje nową funkcję do istniejącego typu bez naruszania jego kodu źródłowego.
Piszesz `fun`, potem typ, który chcesz rozszerzyć (**typ odbiorcy**), kropkę i nazwę funkcji:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Wewnątrz funkcji `this` to wartość, na której funkcja jest wywoływana, nazywana **odbiorcą**: w `4.squared()` jest to `4`.
Gdy rozszerzenie już istnieje, wywołujesz je z kropką dokładnie tak jak funkcję, która od początku byłaby częścią `Int`.

---

Rozszerzenia działają na dowolnym typie, nawet takim, do którego nie masz kodu źródłowego. `String` pochodzi z biblioteki standardowej, a mimo to możesz dodać mu nowe funkcje:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Wewnątrz rozszerzenia możesz pominąć `this.`, gdy używasz innych składowych odbiorcy: samo `lowercase()` znaczy `this.lowercase()`, a samo `length` znaczy `this.length`.

---

Funkcja rozszerzająca może przyjmować parametry jak każda inna funkcja. Odbiorca pozostaje po lewej stronie kropki, a parametry trafiają w nawiasy:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
Typ przed kropką jest zwykłym typem, więc w ten sam sposób możesz rozszerzyć `List<Int>`, `Double` albo własną klasę.

---

Rozszerzenie **nie** modyfikuje klasy, którą rozszerza, i nie dodaje do niej nowej składowej. Kompilator po prostu przepisuje wywołanie: `"kotlin".first3()` staje się wywołaniem funkcji, do której `"kotlin"` trafia jako `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
Dlatego możesz rozszerzać klasy finalne takie jak `String` i `Int`: nic w nich się nie zmienia, rozszerzenie żyje wyłącznie w twoim kodzie.

---

Oprócz funkcji możesz dodać **właściwość rozszerzającą**. Deklaruje się ją przez `val`, typ odbiorcy, kropkę i nazwę, a po nich `get()`, które wylicza wartość przy każdym odczycie właściwości:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Właściwość rozszerzająca nie może nic przechowywać: nie ma pola zaplecza, więc inicjalizator w rodzaju `val String.label = "text"` jest błędem kompilacji. Może jedynie wyliczyć swoją wartość na podstawie odbiorcy.
Właściwości rozszerzających nie można deklarować wewnątrz funkcji (lokalne właściwości rozszerzające są niedozwolone), w odróżnieniu od funkcji rozszerzających.

---

Właściwości rozszerzające odczytuje się bez nawiasów, dokładnie tak jak wbudowane `length` w `String`. Są naturalnym wyborem, gdy wartość opisuje odbiorcę, zamiast coś z nim robić:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Zwróć uwagę na nawiasy wokół `-3`: bez nich `-3.isNegative` najpierw odczytałoby właściwość `3`, a potem próbowałoby zanegować `Boolean`, co się nie kompiluje.

---

Typ odbiorcy może być **nullowalny**. Rozszerzenie dla `String?` można wywołać na zmiennej, która może zawierać `null`, a wewnątrz funkcji `this` jest typu `String?`, więc przypadek `null` obsługujesz sam, zwykle operatorem Elvisa `?:` poznanym w lekcjach o nullowalności:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Wywołanie `name.orDash()` na wartości `null` jest bezpieczne: nie potrzeba `?.`, ponieważ sama funkcja akceptuje odbiorcę `null`.

---

Wewnątrz rozszerzenia z nullowalnym odbiorcą możesz też użyć bezpiecznego wywołania `this?.`, aby sięgnąć po składowe wartości tylko wtedy, gdy nie jest ona `null`. Biblioteka standardowa korzysta z tego samego pomysłu w funkcjach takich jak `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Gdy klasa ma już składową o tej samej nazwie i tych samych parametrach co rozszerzenie, **składowa zawsze wygrywa**: rozszerzenie nigdy nie zostanie wywołane, a kompilator ostrzeże, że jest przesłonięte.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Rozszerzenie nie może nadpisać ani zastąpić istniejącego zachowania; może jedynie dodać nowe funkcje i właściwości. Aby zostało wybrane, rozszerzenie potrzebuje nazwy albo listy parametrów, których klasa jeszcze nie ma.

---

Rozszerzenie może działać na całej rodzinie typów naraz dzięki **parametrowi typu**: symbolowi zastępczemu dla typu, zadeklarowanemu w nawiasach ostrych zaraz po `fun`, który Kotlin wypełnia przy każdym wywołaniu. To czyni rozszerzenie **generycznym**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Przy `listOf(1, 2, 3)` symbol `T` to `Int`, przy `listOf("a", "b")` to `String`, więc ta sama funkcja za każdym razem zwraca właściwy typ.

---

Parametru typu można użyć w dowolnym miejscu sygnatury: jako typu zwracanego, jako nullowalnego `T?` albo wewnątrz innego typu. Generyczne rozszerzenie, które może niczego nie znaleźć, zwraca `T?`, jak wbudowane `firstOrNull()`:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Wewnątrz funkcji możesz używać `size`, `isEmpty()` i indeksowania dokładnie jak na każdej liście, ponieważ odbiorcą jest `List<T>`.

---

Możesz też rozszerzyć **companion object** klasy, o ile klasa go deklaruje, choćby pusty. Typ odbiorcy zapisuje się jako `ClassName.Companion`, a rozszerzenie wywołuje się wtedy na nazwie klasy, jak funkcję fabrykującą:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
Klasa i rozszerzenie są deklaracjami najwyższego poziomu, więc muszą być zapisane poza `main`.

---

Rozszerzenie companion object może przyjmować parametry, co czyni je wygodnym miejscem na alternatywne konstruktory przeliczające z innej jednostki lub formatu:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

To, gdzie deklarujesz rozszerzenie, decyduje o tym, gdzie można go używać, czyli o jego **zasięgu**:
- na najwyższym poziomie pliku jest dostępne w całym pliku i w reszcie pakietu
- wewnątrz funkcji jest rozszerzeniem lokalnym, używalnym tylko w tej funkcji
- wewnątrz klasy jest **rozszerzeniem składowym**, używalnym tylko w tej klasie

Rozszerzenie składowe może odczytywać właściwości klasy, w której żyje, więc łączy dwóch odbiorców: instancję klasy i wartość, na której jest wywoływane:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Wewnątrz `greet` `greeting` pochodzi z `Greeter`, a `this` to `String`, na którym funkcja jest wywoływana. Poza klasą `"Ada".greet()` jest błędem kompilacji.

---

Funkcję rozszerzającą z dokładnie **jednym** parametrem można oznaczyć jako `infix`. Funkcję infix można wywołać bez kropki i nawiasów, z odbiorcą po lewej i argumentem po prawej, co czyta się niemal jak zdanie:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin używa tego także w niektórych wbudowanych funkcjach: `1 to "one"` buduje `Pair`, a `1 until 5` buduje zakres.

---

Aby dało się ją oznaczyć jako `infix`, funkcja musi być składową albo rozszerzeniem, musi przyjmować dokładnie jeden parametr, a ten parametr nie może mieć wartości domyślnej. Wszystko inne jest błędem kompilacji:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Wywołania infiksowe mają priorytet pomiędzy arytmetyką a porównaniem: `1 add 2 * 3` to `1 add 6`, natomiast `1 add 2 == 3` porównuje wynik z `3`.
