---
language: javascript
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

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function clockTime(hours, minutes) {
  
}
```

# --asserts--

Ósma rano to wskazanie `08:00`

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

Pojedyncze cyfry są uzupełniane do dwóch, więc dziewięć minut po jedenastej to wskazanie `11:09`

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

Dokładnie jeden pełny dzień godzin przewija się na `00:00`

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

Minuty powyżej 60 przenoszą się na godziny

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

Ujemna godzina przekręca zegar wstecz za północ

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

Ujemna liczba minut również przekręca zegar wstecz

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

Więcej niż cały dzień wstecz nadal przewija zegar

```javascript
tryCatch(clockTime(-25, 0) === "23:00");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function clockTime(hours, minutes) {
  // % zachowuje znak lewego operandu, więc dodaj cały dzień przed ponownym
  // zawinięciem, aby wylądować w zakresie 0..1439.
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
