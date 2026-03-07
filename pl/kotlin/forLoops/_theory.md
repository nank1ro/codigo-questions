> Słowo kluczowe `for` wykonuje blok kodu dla każdej wartości w sekwencji.

Pętla `for` iteruje przez wszystko, co dostarcza iterator.

Składnia `for` jest następująca:
```kotlin
for (item in collection) print(item)
```

Ciało `for` może być również blokiem
```kotlin
for (item in collection) {
    print(item)
}
```

Przy każdym przejściu przez pętlę, `item` otrzymuje następny element w wartościach.

Oto pętla `for` powtarzająca akcję określoną liczbę razy:

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

Wynik pokazuje indeks `i` otrzymujący każdą wartość z zakresu od _1_ do _3_.

---

_Zakres_ to przedział wartości zdefiniowany przez parę punktów końcowych.
Istnieją dwa podstawowe sposoby definiowania zakresów:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ użycie składni `..` uwzględnia oba krańce w wynikowym zakresie.
- __[2]__ `until` wyklucza koniec. Wynik pokazuje, że _3_ nie jest częścią zakresu.

---

Można iterować po zakresie w odwrotnej kolejności.

Prawdopodobnie oczekujesz, że `3..1` zadziała, niestety zespół Kotlin postanowił zaimplementować tę funkcjonalność w inny sposób.

Jeśli spróbujesz uruchomić ten fragment kodu:
```kotlin
for (i in 3..1) println(i)
```

Zobaczysz, że nic nie jest drukowane.
Aby to działało, musimy użyć słowa kluczowego `downTo`:

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` tworzy malejący zakres.

---

Domyślny _krok_ zakresu wynosi __1__, ale możesz jawnie ustawić inną wartość.

Możesz zdefiniować __krok__ swojej pętli `for` używając słowa kluczowego `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

Jak widać, blok kodu wykonuje się z krokiem _2_ zamiast _1_, co całkowicie zmienia nasz wynik.

---

Można również tworzyć zakres _znaków_.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

Można iterować po __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

W powyższym przykładzie wydrukowaliśmy każdy znak + 1, więc `'a'` staje się `'b'`, `'b'` staje się `'c'` i tak dalej.

Jest to możliwe, ponieważ znaki są przechowywane jako liczby odpowiadające ich [kodom ASCII](https://en.wikipedia.org/wiki/ASCII).

Dodanie liczby całkowitej do znaku daje nowy znak odpowiadający nowej wartości kodu.

---

Jeśli po prostu musisz powtórzyć blok kodu `n` razy, możesz użyć funkcji `repeat(times: Int)`.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

Możesz nawet uzyskać dostęp do indeksu za pomocą
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

W Kotlinie możemy używać `for-in` również dla iterowalnych kolekcji, wywołując podane domknięcie na każdym elemencie:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

W Kotlinie mamy również pętlę `forEach`.
Wywołuje ona podane domknięcie na każdym elemencie sekwencji w tej samej kolejności co pętla `for-in`:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

Użycie metody `forEach` różni się od pętli `for-in` na dwa ważne sposoby:
1. Instrukcji `break` lub `continue` nie można użyć do wyjścia z bieżącego wywołania domknięcia ciała lub do pominięcia kolejnych wywołań. (_Faktycznie jest to możliwe z adnotacjami, ale jest to nieco bardziej złożony temat, który teraz nie będziemy omawiać._)
2. Użycie instrukcji `return` w domknięciu ciała spowoduje wyjście tylko z domknięcia, a nie z zewnętrznego zakresu, i nie pominie kolejnych wywołań.
