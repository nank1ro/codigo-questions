__Wartość logiczna__ (boolean) to typ danych, który może przechowywać tylko dwie wartości: `true` lub `false`.
W Dart typ boolean jest deklarowany słowem kluczowym `bool`.

```dart
bool isRaining = true;
```

Zmienna `isRaining` przechowuje wartość `true`, co oznacza, że aktualnie pada deszcz.
Wartości logiczne są zawsze pisane małymi literami: `true` i `false`.

---

Możesz drukować wartość logiczną za pomocą `print()`, podobnie jak każdą inną zmienną.
Kiedy drukujesz wartość logiczną, Dart wyświetla tekst `true` lub `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Zmienna logiczna może również przechowywać wartość `false`.
Użyj `false`, gdy coś nie jest prawdą.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Tak jak `true`, `false` musi być napisane małymi literami.

---

__Operator negacji__ `!` (zwany również "not" lub "nie") zmienia wartość logiczną na przeciwną.
Zastosowanie `!` do `true` daje `false`, a zastosowanie `!` do `false` daje `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

Jest to przydatne, gdy chcesz sprawdzić przeciwieństwo warunku.

---

Wartości logiczne są używane w całym programowaniu do reprezentowania warunków i podejmowania decyzji.
Każdorazowo, gdy program musi wybrać między dwiema możliwościami, zaangażowana jest wartość logiczna.

Przykłady:
- Czy użytkownik jest zalogowany? (`isLoggedIn`)
- Czy drzwi są otwarte? (`isDoorOpen`)
- Czy zamówienie zostało wysłane? (`isShipped`)
