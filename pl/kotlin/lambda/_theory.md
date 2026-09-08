**Lambda** to mała funkcja bez nazwy, zapisywana bezpośrednio jako wyrażenie w nawiasach klamrowych.
Najpierw podaje się parametry, potem strzałkę `->`, a potem ciało:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Lambda to wartość jak każda inna: można zapisać ją w zmiennej i wywołać później z nawiasami, dokładnie jak funkcję:
```kotlin
println(add(2, 3)) // 5
```
Lambda bez parametrów w ogóle nie ma strzałki: `val hello = { println("Hello!") }`.

---

Każda lambda ma **typ funkcyjny**, zapisywany jako typy parametrów w nawiasach, strzałka i typ zwracany.
Lambda `{ a: Int, b: Int -> a + b }` ma typ `(Int, Int) -> Int`: przyjmuje dwie wartości `Int` i zwraca `Int`.
Gdy zadeklarujesz typ funkcyjny na zmiennej, typy parametrów wewnątrz lambdy można pominąć, ponieważ kompilator już je zna:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Lambda, która niczego nie zwraca, ma typ zwracany `Unit`.

---

Ciało lambdy może zajmować kilka linii. Nie ma słowa kluczowego `return`: wartością zwracaną przez lambdę jest wartość **ostatniego wyrażenia**.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Ponieważ `if` jest w Kotlinie wyrażeniem, może być ostatnią linią i decydować o wyniku:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Gdy lambda ma dokładnie **jeden** parametr, możesz pominąć jego deklarację: Kotlin nadaje mu nazwę `it`.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` istnieje tylko wtedy, gdy parametr nie jest zadeklarowany wprost, i tylko w lambdach z jednym parametrem.
Dzięki niej krótkie lambdy pozostają zwięzłe, ale przy dłuższych ciałach czytelniejsza jest prawdziwa nazwa.

---

Lambdy są najczęściej używane jako argumenty innych funkcji. Kolekcje oferują wiele funkcji przyjmujących lambdę:
- `forEach` wykonuje lambdę raz dla każdego elementu
- `map` buduje nową listę z wynikiem lambdy dla każdego elementu
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Gdy lambda jest **ostatnim** argumentem, można przenieść ją poza nawiasy; a gdy jest jedynym argumentem, nawiasy można całkowicie pominąć. Nazywa się to składnią **trailing lambda** i jest to zwykły sposób jej zapisu:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Lambda zwracająca `Boolean` nazywa się **predykatem**. Kilka funkcji kolekcji przyjmuje taki predykat:
- `filter` zachowuje tylko elementy, dla których predykat jest `true`
- `count` zwraca, ile elementów go spełnia
- `any` i `all` mówią, czy jakiś lub każdy element go spełnia
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Wywołania można **łączyć w łańcuch**: każda funkcja zwraca nową listę, na której pracuje następna.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Lambdy obsługują także sortowanie i agregację:
- `sortedBy` zwraca nową listę uporządkowaną według wartości, którą lambda oblicza dla każdego elementu; `sortedByDescending` działa odwrotnie
- `reduce` łączy wszystkie elementy w jedną wartość: lambda otrzymuje dotychczasowy wynik częściowy i następny element
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` zaczyna od pierwszego elementu jako `acc`, a następnie wykonuje lambdę dla każdego pozostałego elementu.

---

W przypadku `reduce` kształt wyniku zależy od lambdy. Działa każda operacja łącząca dwie wartości: suma, iloczyn, zachowanie większej z nich.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Zauważ, że `reduce` rzuca wyjątek na pustej liście, ponieważ nie ma pierwszego elementu, od którego można zacząć.

---

Lambda może używać zmiennych zadeklarowanych wokół niej, nawet po tym, jak otaczający kod wykonuje się dalej. Nazywa się to **domknięciem**: lambda *przechwytuje* zmienne, których potrzebuje.
W przeciwieństwie do wielu innych języków Kotlin pozwala lambdzie **modyfikować** przechwyconą zmienną `var`:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Każde wywołanie `onClick` aktualizuje tę samą zmienną `clicks`, którą widzi zewnętrzny kod.

---

Ponieważ lambda jest wartością, funkcja może ją **zwracać**. Typem zwracanym jest typ funkcyjny:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
Zwracana lambda przechwytuje `factor`, więc każde wywołanie `multiplier` buduje inną funkcję.
Funkcje, które przyjmują lub zwracają inne funkcje, nazywane są **funkcjami wyższego rzędu**.

---

Zwracana lambda może przechwycić zmienną `var` zadeklarowaną wewnątrz funkcji. Ta zmienna żyje dalej po tym, jak funkcja zwróciła, i tylko lambda może się do niej dostać: to stan prywatny.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Każde wywołanie `makeGreeter()` deklaruje świeże `calls`, więc dwa liczniki powitań liczą niezależnie.

---

Możesz pisać własne funkcje wyższego rzędu: parametr z typem funkcyjnym przyjmuje dowolną lambdę o tym kształcie, a wewnątrz funkcji wywołujesz ją jak zwykłą funkcję.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
To umieszczenie parametru funkcyjnego **na końcu** sprawia, że składnia trailing lambda jest dostępna dla wywołujących.

---

Gdy funkcja, której potrzebujesz, już istnieje, nie ma potrzeby owijania jej w lambdę: **referencja do funkcji** `::name` zamienia nazwaną funkcję w wartość o pasującym typie funkcyjnym.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Do funkcji składowych tworzy się referencje przez ich typ, na przykład `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

**Funkcja anonimowa** to funkcja zadeklarowana słowem `fun`, ale bez nazwy. To inny sposób utworzenia wartości funkcyjnej:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
W przeciwieństwie do lambdy może jawnie deklarować swój typ zwracany i używa `return` do wytworzenia wartości.
Funkcje anonimowe i lambdy są wymienne: obie można przekazywać do `map`, `filter` lub dowolnej funkcji przyjmującej typ funkcyjny.

---

Funkcje wyższego rzędu mogą zarówno przyjmować, jak i zwracać funkcje. Klasycznym przykładem jest **kompozycja**: budowanie nowej funkcji, która uruchamia jedną funkcję i przekazuje jej wynik do drugiej.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
Zwracana lambda przechwytuje zarówno `first`, jak i `second`, więc działa dalej długo po tym, jak `andThen` zwróciła.

---

Niektóre funkcje przyjmują **lambdę z odbiornikiem**: wewnątrz lambdy `this` to konkretny obiekt, więc można wywoływać jego składowe bezpośrednio, bez nazywania go.
`buildString` to częsty przykład: wewnątrz jej lambdy `this` to `StringBuilder`, więc `append` można wywołać, jakby była lokalną funkcją:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` zwraca końcowy ciąg znaków. To wygodna alternatywa dla łączenia za pomocą `+` w pętli.
