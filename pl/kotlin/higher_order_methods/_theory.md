**Metoda wyższego rzędu** to metoda, która przyjmuje funkcję jako argument. Kolekcje Kotlina oferują ich wiele, a funkcja, którą przekazujesz, to zwykle **lambda**: mała funkcja anonimowa zapisana w nawiasach klamrowych.
`map` jest najczęstsza: wywołuje lambdę na każdym elemencie i zwraca **nową listę** z wynikami, pozostawiając oryginał nietknięty:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Gdy lambda ma jeden parametr, nie musisz go deklarować: Kotlin nazywa go `it`. Lambdę zapisuje się po nazwie metody, poza nawiasami okrągłymi, które można pominąć, gdy lambda jest jedynym argumentem. To składnia **trailing lambda** i jest używana w każdym ćwiczeniu tego tematu.

---

`filter` przyjmuje lambdę zwracającą `Boolean`, nazywaną **predykatem**, i zwraca nową listę zawierającą tylko te elementy, dla których predykat jest `true`:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Zamiast `it` możesz nadać parametrowi nazwę, po której następuje strzałka `->`. Nazwany parametr sprawia, że dłuższe lambdy są czytelniejsze, i jest wymagany, gdy lambda jest zagnieżdżona w innej, ponieważ wewnętrzne `it` przesłania zewnętrzny element:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` uruchamia lambdę raz dla każdego elementu i nic nie zwraca. To odpowiednik pętli `for` w stylu wyższego rzędu, używany do efektów ubocznych, takich jak wypisywanie:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` daje dodatkowo pozycję każdego elementu. Jego lambda ma **dwa** parametry, więc muszą być nazwane: `it` istnieje tylko dla lambd z dokładnie jednym parametrem.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, potem 1: b
}
```

---

`reduce` łączy wszystkie elementy w jedną wartość. Jego lambda przyjmuje dwa parametry: **akumulator** (dotychczasowy wynik) i kolejny element. Zaczyna od pierwszego elementu jako akumulatora i uruchamia lambdę dla każdego pozostałego elementu:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` rzuca wyjątek na pustej liście, bo nie ma pierwszego elementu, od którego można zacząć. `fold` to naprawia: przekazujesz **wartość początkową** akumulatora jako argument, a lambda uruchamia się dla każdego elementu, łącznie z pierwszym:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Przy `fold` akumulator może mieć nawet inny typ niż elementy, na przykład gdy budujesz `String` z listy liczb.

---

Niektóre metody wyższego rzędu odpowiadają na pytanie o kolekcję, zamiast budować nową. Wszystkie przyjmują predykat:
- `any` zwraca `true`, jeśli spełnia go **co najmniej jeden** element
- `all` zwraca `true`, jeśli spełnia go **każdy** element
- `none` zwraca `true`, jeśli nie spełnia go **żaden** element
- `count` zwraca, **ile** elementów go spełnia
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Na pustej liście `any` zwraca `false`, a `all` i `none` zwracają `true`: nie ma elementu, który łamałby regułę.

---

Metody agregujące zamieniają całą kolekcję w jedną wartość:
- `sum()` sumuje listę liczb, natomiast `sumOf` sumuje wartość, którą lambda oblicza dla każdego elementu
- `maxByOrNull` i `minByOrNull` zwracają **element**, dla którego lambda daje największą lub najmniejszą wartość, albo `null` na pustej liście
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Zwróć uwagę na różnicę wobec `maxOf { it.length }`, które zwraca największą **wartość** (`6`) zamiast elementu, który ją wytworzył.

---

`sortedBy` zwraca nową listę uporządkowaną według wartości, którą lambda oblicza dla każdego elementu, od najmniejszej w górę. `sortedByDescending` porządkuje od największej w dół. Gdy porównywać chcesz same elementy, `sorted()` i `sortedDescending()` nie potrzebują lambdy:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
Sortowanie jest **stabilne**: elementy o tym samym kluczu zachowują swoją pierwotną kolejność względną. Oryginalna lista nigdy nie jest modyfikowana.

---

`take(n)` zwraca nową listę z pierwszymi `n` elementami, a `drop(n)` zwraca nową listę **bez** pierwszych `n` elementów. Żadna z nich nie przyjmuje lambdy, ale często łączy się je w łańcuch po metodzie, która ją przyjmuje:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` i `dropWhile` to wersje z predykatem: biorą lub odrzucają elementy od początku **dopóki** predykat jest `true`, i zatrzymują się na pierwszym elemencie, który go nie spełnia:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` dzieli kolekcję na `Map`: lambda oblicza **klucz** każdego elementu, a każdemu kluczowi przypisana jest lista elementów, które go wytworzyły, w ich pierwotnej kolejności:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
Wynik ma typ `Map<K, List<T>>`, gdzie `K` to typ zwracany przez lambdę, a `T` to typ elementów. Klucze pojawiają się w kolejności, w jakiej zostały napotkane po raz pierwszy.

---

Gdy lambda zwraca **listę** dla każdego elementu, `map` tworzy listę list. `flatMap` robi to samo, ale następnie scala wszystkie te listy w jedną płaską:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
Kolejność jest zachowana: najpierw idą wszystkie wartości wytworzone przez pierwszy element, potem te z drugiego i tak dalej. Jeśli masz już listę list, `flatten()` scala je bez lambdy.

---

`zip` łączy elementy dwóch list pozycja po pozycji. Bez lambdy zwraca listę wartości `Pair`, których połówki odczytuje się przez `.first` i `.second`; z lambdą oba elementy z każdej pozycji są do niej przekazywane, a wyniki zbierane są na liście:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
Wynik jest tak długi jak **krótsza** z dwóch list: nadmiarowe elementy dłuższej są pomijane.

---

Kształt lambdy musi pasować do tego, czego oczekuje metoda:
- metody działające na jednym elemencie naraz (`map`, `filter`, `sortedBy`, `groupBy`...) przyjmują lambdę **jednoparametrową**, w której dostępne jest `it`
- `reduce`, `fold`, `forEachIndexed` i `zip` z lambdą przekazują **dwie** wartości, więc parametry muszą być jawnie nazwane za pomocą `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: jeden parametr, it jest dostępne
numbers.reduce { acc, n -> acc + n }    // ok: dwa parametry, nazwane
numbers.reduce { it + 1 }               // błąd: it nie istnieje przy dwóch parametrach
```
Nazywanie parametrów jest zawsze dozwolone, nawet przy jednym: `numbers.map { n -> n * 2 }`.

---

Metody wyższego rzędu można **łączyć w łańcuch**: każda zwraca nową kolekcję, na której pracuje następna, dzięki czemu całe obliczenie czyta się jak potok od lewej do prawej:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Mapy również mają metody wyższego rzędu. `mapValues` zachowuje klucze i zastępuje każdą wartość wynikiem lambdy, która otrzymuje **wpis** z `.key` i `.value`:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

W łańcuchu typ `it` zmienia się na każdym kroku: po `filter` na `List<String>` nadal masz napisy, ale po `map { it.length }` masz `List<Int>`, więc kolejna lambda widzi liczby.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Każdy krok zwraca **nową** listę i nigdy nie rusza poprzedniej, więc łańcuch można rozbić na nazwane wartości pośrednie bez zmiany wyniku.

---

Lambda może zawierać kolejne wywołanie wyższego rzędu. Wewnątrz wewnętrznej lambdy `it` odnosi się do **wewnętrznego** elementu i przesłania zewnętrzny, więc nazwij jawnie parametr zewnętrzny, aby oba pozostały dostępne:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` tworzy `Pair`. Tutaj zewnętrzna lambda pracuje na wpisie mapy, a wewnętrzna na parach z listy tego wpisu.

---

`Map` można przetwarzać jak listę wpisów: `filter` i `map` działają bezpośrednio na mapie i otrzymują każdy wpis z `.key` i `.value`. `filter` na mapie zwraca mapę, a `map` zwraca listę. Metody sortujące, takie jak `sortedBy`, nie są zdefiniowane na mapie: przejdź najpierw przez `scores.entries`, czyli kolekcję wpisów:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` to zbiór wszystkich wpisów; `scores.keys` i `scores.values` dają tylko jedną ze stron.
