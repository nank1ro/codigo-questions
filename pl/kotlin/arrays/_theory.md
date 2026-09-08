**Array** przechowuje stałą liczbę wartości tego samego typu pod jedną nazwą zmiennej.
Tworzysz go za pomocą `arrayOf`, odczytujesz element za pomocą nawiasów kwadratowych i **indeksu** zaczynającego się od `0`, a liczbę elementów uzyskujesz za pomocą `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
Ostatni element znajduje się pod indeksem `size - 1`.

---

`arrayOf(1, 2, 3)` tworzy `Array<Int>`, w którym każdy element jest opakowanym obiektem.
Dla typów prymitywnych Kotlin oferuje dedykowane, wydajniejsze typy, takie jak `IntArray`, `DoubleArray` i `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Możesz też zbudować tablicę o zadanym rozmiarze za pomocą lambdy **inicjalizującej**, która otrzymuje każdy indeks, albo wypełniony zerami `IntArray`:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Każdy array ma dwie przydatne właściwości do pracy z indeksami:
- `indices` to zakres prawidłowych indeksów, od `0` do ostatniego
- `lastIndex` to indeks ostatniego elementu, czyli `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Nawet gdy tablica jest zadeklarowana za pomocą `val`, jej **elementy** można zastąpić, przypisując wartość do indeksu:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Aby odwiedzić każdy element, możesz użyć pętli `for` lub `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Zwróć uwagę, że `n` i `it` to kopie wartości tylko do odczytu i nie można im nic ponownie przypisać, więc aby zmodyfikować elementy, potrzebujesz ich indeksu.

---

Aby sprawdzić, czy tablica zawiera wartość, użyj `in` lub `contains`, oba zwracają `Boolean`.
`indexOf` zwraca indeks pierwszego wystąpienia, albo `-1`, gdy wartości nie ma:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Wypisanie tablicy bezpośrednio nie pokazuje jej elementów, wypisuje coś w rodzaju `[Ljava.lang.String;@1b6d3586`.
Użyj `joinToString`, aby zbudować czytelny ciąg znaków, opcjonalnie z niestandardowym separatorem (domyślny to `", "`), albo `contentToString`, aby uzyskać elementy w nawiasach kwadratowych:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Tablice można sortować **w miejscu** (in place) albo kopiować do nowej posortowanej kolekcji:
- `sort()` i `sortDescending()` porządkują samą tablicę i nic nie zwracają
- `reverse()` odwraca kolejność samej tablicy
- `sorted()`, `sortedDescending()` i `reversed()` pozostawiają tablicę nietkniętą i zwracają nową `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Tablice liczbowe mają wbudowane funkcje agregujące:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` i `min()` rzucają wyjątek na pustej tablicy, użyj `maxOrNull()` i `minOrNull()`, gdy tablica może być pusta.

---

Główna różnica między tablicą a `MutableList` polega na tym, że tablica ma **stały rozmiar**: po utworzeniu możesz zastępować jej elementy, ale nigdy nie możesz dodać ani usunąć żadnego, nie ma funkcji `add`.
Wyrażenia takie jak `nums + 4` nie powiększają `nums`, tylko tworzą zupełnie nową tablicę:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Wybieraj `MutableList`, gdy liczba elementów zmienia się w czasie, a tablicę, gdy jest znana z góry albo gdy potrzebujesz wydajności typów prymitywnych.

---

Tablice obsługują te same funkcje transformacji co listy. `filter` zachowuje elementy spełniające warunek, a `map` przekształca każdy element.
Obie zwracają nową `List`, a nie tablicę:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Ponieważ wynik jest listą, wypisanie jej bezpośrednio pokazuje jej elementy.

---

Gdy podczas pętli potrzebujesz zarówno indeksu, jak i wartości, użyj `withIndex()` i zdestrukturyzuj każdą parę, albo `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Tablice i listy łatwo się nawzajem konwertują:
- `toList()` i `toMutableList()` kopiują tablicę do listy
- `toTypedArray()` kopiuje listę do `Array<T>`
- `toIntArray()` kopiuje listę `Int` do `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Każda konwersja tworzy **kopię**, więc zmiana wyniku nie wpływa na oryginał.

---

W przeciwieństwie do list, dwie tablice o tych samych elementach **nie** są równe przy `==`: tablice porównuje się przez referencję, więc `==` jest `true` tylko dla tego samego obiektu tablicy.
Aby porównać zawartość, użyj `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Ponieważ tablice mają stały rozmiar, wzięcie części tablicy oznacza utworzenie nowej tablicy:
- `copyOf()` kopiuje całą tablicę, `copyOf(n)` kopiuje pierwsze `n` elementów
- `copyOfRange(from, to)` kopiuje elementy od indeksu `from` do `to` **wyłącznie**
- `sliceArray(range)` kopiuje elementy pod indeksami zakresu, z obydwoma końcami włącznie
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
