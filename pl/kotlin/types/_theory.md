Każda wartość w Kotlinie ma **typ**, który mówi kompilatorowi, jakie to dane i co można z nimi robić.
Podstawowe typy to:
- `Int`: liczba całkowita, jak `42` czy `-7`
- `Long`: liczba całkowita, która może być znacznie większa niż `Int`
- `Double`: liczba z częścią dziesiętną, jak `3.14`
- `Float`: liczba dziesiętna, która używa połowy pamięci `Double`, ale jest mniej precyzyjna
- `Char`: pojedynczy znak w apostrofach, jak `'a'`
- `Boolean`: `true` albo `false`
- `String`: tekst w cudzysłowach, jak `"Hello"`

Podobnie jak w lekcjach o zmiennych, możesz jawnie podać typ za pomocą dwukropka po nazwie:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Wartości jednego typu nie można zapisać w zmiennej innego typu: `val age: Int = "36"` to błąd kompilacji.

---

Przez większość czasu nie zapisujesz typu: Kotlin **wywnioskowuje** go z przypisywanej wartości, według kilku reguł dotyczących literałów:
- liczba całkowita, jak `42`, to `Int`
- liczba z kropką dziesiętną, jak `3.14`, to `Double`
- tekst w cudzysłowach to `String`
- znak w apostrofach to `Char`
- `true` i `false` to `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Aby sprawdzić, co wywnioskował Kotlin, możesz wypisać nazwę typu dowolnej wartości za pomocą `::class.simpleName`:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Literał dziesiętny nigdy nie jest wnioskowany jako `Float`: `val ratio = 0.5` to `Double`.

---

`Int` może przechowywać liczby całkowite do około dwóch miliardów, a dokładniej do `Int.MAX_VALUE`, czyli `2147483647`.
Literał całkowity zbyt duży dla `Int` jest automatycznie wnioskowany jako `Long`, a dla dowolnego literału możesz wymusić `Long` sufiksem `L`:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
Analogicznie sufiks `f` zamienia literał dziesiętny w `Float`: `val ratio = 0.5f`.
Długie liczby są trudne do odczytania, więc Kotlin pozwala wstawić podkreślniki `_` w dowolnym miejscu między cyframi; kompilator je ignoruje:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin nigdy nie konwertuje typów liczbowych sam z siebie przy przypisaniu wartości, nawet z mniejszego typu na większy: zapisanie `Int` w zmiennej `Long` lub `Double` to błąd kompilacji.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Każdy typ liczbowy ma **funkcje konwersji**, które tworzą nową wartość potrzebnego typu: `toInt()`, `toLong()`, `toDouble()`, `toFloat()`, a aby uzyskać tekst, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Przejście z liczby dziesiętnej na całkowitą **obcina**: `toInt()` po prostu odrzuca część dziesiętną, więc `3.99.toInt()` to `3`, a `(-3.99).toInt()` to `-3`.

---

Typy operandów decydują o tym, jak działa dzielenie. Gdy oba są typu `Int`, operator `/` wykonuje **dzielenie całkowite**: wynikiem jest `Int`, a reszta jest odrzucana.
Gdy co najmniej jeden operand jest typu `Double`, `/` wykonuje dzielenie zmiennoprzecinkowe i zachowuje część dziesiętną:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Aby uzyskać wynik dziesiętny z dwóch zmiennych `Int`, musisz przekonwertować co najmniej jedną z nich **przed** dzieleniem: `(7 / 2).toDouble()` to `3.0`, ponieważ dzielenie całkowite już się odbyło.

---

Gdy funkcja musi zwrócić wynik dziesiętny obliczony z liczb całkowitych, przekonwertuj operandy na `Double` przed dzieleniem i zadeklaruj typ zwracany jako `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Pamiętaj, że `sum()` i `size` z `List<Int>` też są wartościami `Int`, więc wymagają tej samej konwersji.

---

Każdy `Char` jest przechowywany jako liczba, jego **kod**. Właściwość `code` daje `Int` stojący za znakiem, a `toChar()` działa odwrotnie, zamieniając `Int` w `Char` o tym kodzie:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Litery mają kolejne kody, więc dodawanie do kodu przesuwa po alfabecie.
Zauważ, że kod `'7'` to `55`, a nie `7`: aby odczytać cyfrę, którą reprezentuje `Char`, użyj `digitToInt()`, która zwraca `7`.

---

Ponieważ kod `Char` to `Int`, możesz wykonywać na nim arytmetykę i przekonwertować wynik z powrotem na `Char`. W ten sposób przesuwasz się po alfabecie:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin pozwala też dodać `Int` bezpośrednio do `Char`: `'a' + 1` to `'b'`, a różnica między dwoma znakami `'d' - 'a'` to `Int` `3`.

---

Tekst wpisany przez użytkownika zawsze przychodzi jako `String`, nawet gdy wygląda jak liczba. Aby wykonywać na nim obliczenia, musisz go **przetworzyć**: `toInt()` zamienia `"42"` w `Int` `42`, a `toDouble()` zamienia `"3.5"` w `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Nie każdy tekst jest liczbą: `"4x2".toInt()` rzuca `NumberFormatException` i zatrzymuje program.
Bezpieczne alternatywy `toIntOrNull()` i `toDoubleOrNull()` zwracają `null` zamiast rzucać wyjątek, więc — jak już wiesz z lekcji o nullowalności — możesz podać wartość domyślną za pomocą `?:`:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` kończy się sukcesem tylko wtedy, gdy cały tekst jest poprawną liczbą całkowitą, z opcjonalnym znakiem:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Dla tekstu dziesiętnego użyj `toDoubleOrNull()`, które przyjmuje `"3.5"` i analogicznie zwraca `Double?`.

---

`Int` ma stały rozmiar, więc ma najmniejszą i największą wartość: `Int.MIN_VALUE` to `-2147483648`, a `Int.MAX_VALUE` to `2147483647`.
Przekroczenie granicy **nie** powoduje błędu: wartość po cichu **zawija się** do drugiego końca zakresu, zjawisko to nazywa się przepełnieniem (overflow).
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Gdy wynik może przekroczyć dwa miliardy, użyj `Long`, którego granica `Long.MAX_VALUE` wynosi około dziewięciu kwintylionów. Pamiętaj o konwersji przed operacją: `Int.MAX_VALUE.toLong() + 1` to `2147483648`.

---

`Double` przechowuje liczby dziesiętne w postaci binarnej, więc niektórych wartości nie da się zapisać dokładnie i w ostatnich cyfrach pojawiają się drobne błędy:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Aby wyświetlić stałą liczbę miejsc dziesiętnych, użyj `String.format` z ciągiem formatującym: `"%.2f"` znaczy "liczba dziesiętna z 2 cyframi po kropce". Wynikiem jest `String`, zaokrąglony do tylu cyfr:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` to typ na szczycie hierarchii: każda wartość w Kotlinie to `Any`, więc zmienna typu `Any` może przechowywać `Int`, `String`, `Boolean` albo cokolwiek innego.
Aby sprawdzić, co faktycznie przechowuje, używasz operatora `is`, który zwraca `true`, gdy wartość ma dany typ:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Gdy sprawdzenie się powiedzie, kompilator wykonuje **smart cast**: wewnątrz `if` (lub gałęzi `when`) możesz użyć wartości jako tego typu, bez żadnej konwersji:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
