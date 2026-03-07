> Komputery doskonale nadają się do zadań powtarzalnych.

Najprostsza forma powtarzania używa słowa kluczowego `while`.
Powtarza blok kodu tak długo, jak _wyrażenie boolowskie_ kontrolujące jest prawdziwe:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
Wyrażenie boolowskie jest sprawdzane raz na początku pętli i
ponownie przed każdą kolejną iteracją przez blok.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Tutaj utworzyliśmy zmienną `x`, przypisując jej wartość początkową __3__.

Następnie użyliśmy instrukcji `while`, która będzie wykonywać blok kodu dopóki warunek `x > 0` jest `true`.

Wewnątrz bloku kodu **NIE** możemy zapomnieć o dodaniu linii `x--`.
Dekrementuje ona wartość `x`, w przeciwnym razie pętla będzie nieskończona.

---

Przeanalizujmy ten fragment kodu.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Inicjalizujemy zmienną `counter` wartością __0__.
- __[2]__: Wyrażenie warunkowe dla _while_ mówi: "powtarzaj instrukcje w treści tak długo, jak counter jest mniejszy niż _100_".
- __[3]__: Operator `+=` dodaje _10_ do `counter` i przypisuje wynik do `counter` w jednej operacji.

Wynik powyższego kodu to _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Istnieje drugi sposób użycia _while_, w połączeniu ze słowem kluczowym `do`.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
Jak widać, `do-while` jest bardzo podobna do pętli `while`, z wyjątkiem jednej ważnej różnicy:
> ciało pętli jest wykonywane raz przed sprawdzeniem warunku.

Innymi słowy, ciało `do-while` zawsze wykonuje się przynajmniej raz, nawet jeśli wyrażenie warunkowe początkowo daje `false`.

Dla kontrastu, ciało pętli `while` nigdy nie zostanie uruchomione, jeśli warunek da `false` za pierwszym razem.

---

Pętla _while_ obsługuje trzy strukturalne wyrażenia skoku:
- `break` kończy najbliższą otaczającą pętlę.
- `continue` przechodzi do następnego kroku najbliższej otaczającej pętli.
- `return` domyślnie zwraca z najbliższej otaczającej funkcji lub funkcji anonimowej (_zobaczymy to później, gdy będziemy mówić o funkcjach_).

Oto przykład użycia `continue` w pętli _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

Jak widać w __[1]__, gdy `i` jest równe _2_, pomijamy i _kontynuujemy_ do następnego kroku. W rzeczywistości liczba 2 nigdy nie jest wyświetlana.

---

Oto przykład użycia `break` w pętli _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

Jak widać w __[1]__, gdy `i` jest równe _2_, _przerywamy_ pętlę. W rzeczywistości liczby 2 i 3 nigdy nie są wyświetlane.
