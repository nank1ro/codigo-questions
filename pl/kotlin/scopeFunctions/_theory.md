**Funkcje zasięgu** wykonują blok kodu *wewnątrz kontekstu obiektu*. Nie dodają one do języka żadnych nowych możliwości: sprawiają jedynie, że kod działający na jednym obiekcie jest krótszy i łatwiejszy do odczytania. Kotlin ma ich pięć: `let`, `run`, `with`, `apply` i `also`.

Różnią się one tylko w **dwóch** punktach: jak obiekt jest wskazywany wewnątrz bloku i co zwraca wywołanie. Zaczniemy od `let`: wewnątrz jego bloku obiekt nazywa się `it`, a wywołanie zwraca **wynik ostatniego wyrażenia** bloku.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Bez `let` potrzebowałbyś tymczasowej zmiennej; z nim obiekt jest dostępny pod krótką nazwą `it` tak długo, jak trwa blok.

---

Ponieważ `let` zwraca wartość swojego ostatniego wyrażenia, jest wygodnym sposobem na **zamianę wartości w coś innego** bez nazywania zmiennej pomocniczej:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Wewnątrz bloku możesz używać `it` tyle razy, ile potrzebujesz:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` staje się naprawdę przydatny po bezpiecznym wywołaniu. `?.let { ... }` wykonuje blok **tylko** wtedy, gdy wartość nie jest `null`, a wewnątrz bloku `it` jest wartością non-null, więc dodatkowe sprawdzenie nie jest potrzebne:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Gdy wartość jest `null`, całe wyrażenie ma wartość `null` i blok nigdy się nie wykonuje, dlatego operator Elvisa `?:` jest naturalnym partnerem do podania wartości domyślnej:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Wewnątrz bloku `let` nie musisz nazywać obiektu `it`: parametrowi lambdy możesz nadać własną nazwę, co pozwala zachować czytelność kodu, gdy bloki są zagnieżdżone albo gdy nazwa `it` niewiele mówi.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
Takie nazywanie działa dla każdej funkcji zasięgu, która używa `it`, czyli dla `let` i `also`.

---

`apply` porusza się po obu osiach naraz: wewnątrz jego bloku obiektem jest odbiornik `this` (dzięki czemu jego składowe można używać **bez żadnego prefiksu**), a wywołanie zwraca **sam obiekt**, a nie wynik bloku.

To połączenie czyni `apply` narzędziem do **konfigurowania** obiektu dokładnie w miejscu, w którym go tworzysz:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` i `port` wewnątrz bloku to `this.host` i `this.port`; ponieważ `apply` oddaje skonfigurowany `Server`, można go od razu przypisać do zmiennej.

---

`apply` nie jest ograniczone do obiektów, które właśnie utworzono: działa na każdym obiekcie, a ponieważ oddaje ten obiekt z powrotem, całe wyrażenie można użyć wszędzie tam, gdzie oczekiwany jest obiekt.
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
Blok jest zwykłym blokiem kodu, więc może zawierać dowolną liczbę instrukcji.

---

`also` jest lustrzanym odbiciem `apply`: obiekt jest wskazywany jako `it`, a wywołanie zwraca **sam obiekt**. Ponieważ wynik bloku jest wyrzucany, `also` służy do **efektów ubocznych**, takich jak logowanie czy sprawdzanie, i można go wstawić w środku łańcucha bez zmieniania tego, co łańcuch wytwarza:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Odczytaj to jako *„i jeszcze zrób z tym coś”*: wartość płynie dalej do następnego kroku nietknięta.

---

Gdy blok potrzebuje obiektu jako **argumentu** czegoś innego, `also` czyta się lepiej niż `apply`: `it` można przekazać bezpośrednio dalej, podczas gdy `this` musiałby zostać zapisany wprost.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
Wartością wyrażenia jest nadal `"ada"`: `also` tylko przygląda się, jak przepływa.

---

`run` to `let` z innym sposobem nazywania obiektu: wewnątrz bloku obiektem jest `this`, więc jego składowe nie potrzebują prefiksu, a wywołanie zwraca **wynik ostatniego wyrażenia**.

Pasuje wtedy, gdy odczytujesz kilka składowych tego samego obiektu, aby obliczyć jedną wartość:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Porównaj to z `apply`, które używa `this` w dokładnie ten sam sposób, ale oddaje z powrotem obiekt zamiast wyniku bloku.

---

`with` wykonuje tę samą pracę co `run`, ale **nie** jest rozszerzeniem: obiekt przekazuje się jako pierwszy argument zamiast być odbiornikiem wywołania po kropce.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Wewnątrz bloku obiektem jest `this`, a wywołanie zwraca ostatnie wyrażenie, dokładnie jak w `run`. Wybieraj `with`, gdy masz już obiekt non-null i chcesz zgrupować na nim kilka wywołań; wybieraj `run`, gdy obiekt pochodzi z łańcucha albo może wymagać bezpiecznego wywołania (`obj?.run { ... }`).

---

Wszystkie pięć funkcji zasięgu mamy już na stole, a każda z nich to tylko punkt na dwóch osiach:
- `let` - obiektem jest `it`, zwraca wynik bloku
- `run` - obiektem jest `this`, zwraca wynik bloku
- `with` - obiektem jest `this` (przekazywany jako argument), zwraca wynik bloku
- `apply` - obiektem jest `this`, zwraca obiekt
- `also` - obiektem jest `it`, zwraca obiekt

Wybierz wiersz, którego potrzebujesz: `it` czyta się lepiej, gdy przekazujesz obiekt dalej do czegoś innego, `this` czyta się lepiej, gdy dotykasz wielu jego składowych; zwracaj wynik bloku, gdy chcesz uzyskać nową wartość, a obiekt, gdy chcesz dalej z nim pracować.
