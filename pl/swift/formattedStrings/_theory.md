A **sformatowany ciąg znaków** to fragment tekstu, w którym niektóre części są uzupełniane wartościami w czasie działania programu: cena, imię, wynik. Swift daje do tego dwa narzędzia.

Pierwszym z nich jest **interpolacja ciągów znaków**, którą już znasz: wszystko zapisane wewnątrz `\( )` jest obliczane i wstawiane do tekstu. Nie musi to być zmienna, może to być dowolne wyrażenie:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
Interpolacja to najszybszy sposób zbudowania ciągu znaków, ale wypisuje liczby dokładnie tak, jak Swift je przechowuje: `3.5` pozostaje `3.5`, nigdy `3.50`. Pełną kontrolę nad cyframi, szerokością i dopełnianiem uzyskamy dzięki `String(format:)`, poznanemu w następnym ćwiczeniu.

---

Drugim narzędziem jest `String(format:)`, które pochodzi z frameworka **Foundation**, więc plik musi zaczynać się od `import Foundation`.

Przyjmuje on **ciąg formatujący**, a po nim wartości do wstawienia. Wewnątrz ciągu formatującego **specyfikator** zaczynający się od `%` oznacza, gdzie trafia każda wartość i jak zostanie zapisana. Specyfikatorem dla liczby całkowitej jest `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` zwraca zwykły `String`, więc możesz go wypisać, zapisać lub zwrócić z funkcji.

---

Dla liczb dziesiętnych (`Double`) specyfikatorem jest `%f`. Sam z siebie wypisuje on zawsze sześć cyfr po kropce:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Aby wybrać liczbę miejsc dziesiętnych, zapisz kropkę i liczbę między `%` a `f`. To jest **precyzja**, a wartość jest zaokrąglana, aby się zmieścić:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` to zwykły wybór dla cen, ponieważ zawsze pokazuje dokładnie dwa miejsca dziesiętne.

---

Liczba między `%` a literą ustawia **minimalną szerokość** pola. Jeśli wartość jest krótsza, spacje są dodawane po lewej, więc jest **wyrównana do prawej**; jeśli jest dłuższa, nic nie jest obcinane:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Szerokość i precyzja łączą się: `%8.2f` znaczy „co najmniej 8 znaków szerokości, z 2 miejscami dziesiętnymi”:
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
To właśnie stałe szerokości wyrównują kolumny tabeli.

---

Domyślnie dopełnianie trafia na lewą stronę. Znak minus tuż po `%` przenosi dopełnianie na prawą stronę, więc wartość jest **wyrównana do lewej**:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
Znak minus to **flaga**: zmienia sposób wypełnienia pola bez zmiany jego szerokości.

---

Inną flagą jest `0`: zamiast spacji pole jest wypełniane zerami po lewej. W ten sposób otrzymujesz liczby jak `007` czy `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Tak jak przy spacjach, wartość dłuższa niż szerokość nigdy nie jest obcinana.

---

Ciąg formatujący może zawierać dowolną liczbę specyfikatorów. Wartości następują w tej samej kolejności, oddzielone przecinkami, a każda musi pasować do typu swojego specyfikatora: `%d` dla `Int`, `%f` dla `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Przekazanie `Double` do `%d` (lub `Int` do `%f`) skompiluje się, ale wypisze bezsensowną liczbę, więc zawsze sprawdzaj, czy specyfikatory i wartości do siebie pasują.

---

Liczby całkowite można też zapisywać w innych systemach zapisu. `%x` wypisze wartość w systemie **szesnastkowym** małymi literami, `%X` wielkimi literami, a `%o` w systemie ósemkowym:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
Szerokość i flaga `0` działają tu również: `%02x` to klasyczny sposób zapisu jednego bajtu koloru, jak w `#ff8000`.

---

Aby wstawić `String` do ciągu formatującego, użyj specyfikatora `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` przyjmuje bezpośrednio `String` ze Swifte. Nie używaj `%s` z ciągiem znaków Swifta: ten specyfikator oczekuje ciągu znaków z języka C i wypisuje śmieci lub powoduje awarię.

---

Ponieważ `%` rozpoczyna specyfikator, dosłowny znak procenta musi być zapisany jako `%%`. Tak formatujesz wartość procentową:
```swift
let ratio = 0.4567
print(String(format: "%.1f%%", ratio * 100)) // 45.7%
```
Najpierw pomnóż stosunek przez `100`, a potem wybierz precyzję: `%.0f%%` daje `46%`, `%.1f%%` daje `45.7%`.

---

Flagi szerokości działają tylko wewnątrz `String(format:)`. Aby samodzielnie dopełnić zwykły ciąg znaków, zbuduj spacje za pomocą `String(repeating:count:)` i dołącz je do tekstu:
```swift
let text = "7"
let spaces = String(repeating: " ", count: 4 - text.count)
print(spaces + text + "|") //    7|
```
Jeśli tekst jest już dłuższy niż szerokość, `4 - text.count` staje się ujemne i `String(repeating:count:)` ulega awarii. Zabezpiecz to przez `max(0, ...)`, dzięki czemu liczba nigdy nie spadnie poniżej zera, a długi tekst pozostanie bez zmian.

---

Foundation ma też gotową funkcję pomocniczą do dopełniania po prawej: `padding(toLength:withPad:startingAt:)`. Wydłuża ona ciąg znaków do podanej długości przez powtarzanie tekstu wypełnienia, a jeśli jest on dłuższy, obcina go:
```swift
import Foundation

let name = "Ada"
print(name.padding(toLength: 8, withPad: " ", startingAt: 0) + "|") // Ada     |
print("Tea".padding(toLength: 6, withPad: ".", startingAt: 0))     // Tea...
```
`startingAt` to indeks wewnątrz tekstu wypełnienia, od którego zaczyna się powtarzanie; przy wypełnieniu z jednego znaku jest to zawsze `0`.

---

Połącz oba narzędzia, aby wypisać tabelę: `padding` wyrównuje tekst każdego wiersza do lewej, a `String(format:)` wyrównuje liczby do prawej ze stałą szerokością i precyzją:
```swift
import Foundation

let items = [("Tea", 2.5), ("Cake", 12.0)]
for (name, price) in items {
    let label = name.padding(toLength: 6, withPad: ".", startingAt: 0)
    print(label + String(format: "%6.2f", price))
}
// Tea...  2.50
// Cake.. 12.00
```
Ponieważ każdy wiersz ma tę samą szerokość, kropki dziesiętne trafiają do tej samej kolumny.
