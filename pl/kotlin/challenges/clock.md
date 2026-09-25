---
language: kotlin
exerciseType: 1
difficulty: 2
title: Zegar
---

# --description--

Zegar 24-godzinny pokazuje porę dnia jako `HH:MM`, zaczynając od `00:00` tuż po północy i kończąc na `23:59`, minutę przed kolejną północą. Obie części są zawsze zapisywane dwiema cyframi, więc dziewięć minut po jedenastej rano to wskazanie `11:09`.

Cały dzień trwa 1440 minut. Gdy zegar przekroczy `23:59`, przewija się na `00:00` i zaczyna dzień od nowa, a przekręcenie go wstecz za `00:00` daje `23:59`.

# --instructions--

Napisz funkcję `clockTime`, która przyjmuje dwie liczby całkowite, `hours` i `minutes`, i zwraca wskazanie zegara 24-godzinnego jako napis `"HH:MM"`, przy czym obie części są uzupełnione do dwóch cyfr.

Przykłady:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Każda z liczb może być ujemna lub większa, niż pozwala prawdziwy zegar.
- Oblicz całkowitą liczbę minut jako `hours * 60 + minutes`, a następnie zawiń tę sumę do zakresu od `0` do `1439`, żeby zegar przewijał się w obu kierunkach.
- `clockTime(24, 0)` to dokładnie jeden dzień, więc wskazanie to `"00:00"`.

# --seed--

```kotlin
fun clockTime(hours: Int, minutes: Int): String {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Ósma rano to wskazanie `08:00`

```kotlin
    tryCatch(clockTime(8, 0) == "08:00")
```

Pojedyncze cyfry są uzupełniane do dwóch, więc dziewięć minut po jedenastej to wskazanie `11:09`

```kotlin
    tryCatch(clockTime(11, 9) == "11:09")
```

Dokładnie jeden pełny dzień godzin przewija się na `00:00`

```kotlin
    tryCatch(clockTime(24, 0) == "00:00")
```

Minuty powyżej 60 przenoszą się na godziny

```kotlin
    tryCatch(clockTime(25, 160) == "03:40")
```

Ujemna godzina przekręca zegar wstecz za północ

```kotlin
    tryCatch(clockTime(-1, 15) == "23:15")
```

Ujemna liczba minut również przekręca zegar wstecz

```kotlin
    tryCatch(clockTime(0, -90) == "22:30")
```

Więcej niż cały dzień wstecz nadal przewija zegar

```kotlin
    tryCatch(clockTime(-25, 0) == "23:00")
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun clockTime(hours: Int, minutes: Int): String {
    // % zachowuje znak lewego operandu, ale mod() zawsze zawija do przodu
    // do zakresu 0..1439.
    val total = (hours * 60 + minutes).mod(1440)

    return "%02d:%02d".format(total / 60, total % 60)
}
```
