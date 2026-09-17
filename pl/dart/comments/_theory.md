> Zanim zacznę, chciałem powiedzieć, że jestem bardzo szczęśliwy mogąc uczyć cię Dart.
Przy tej okazji chcę ci przekazać, że aplikacja, której używasz, została napisana właśnie w Dart, przy użyciu frameworka Flutter. Dlatego to dla mnie zaszczyt móc dzielić się swoją wiedzą na temat tego języka.

Dart, podobnie jak wiele innych języków programowania, pozwala na dokumentowanie kodu.
Dzięki temu możesz pisać dowolny tekst obok kodu.
Komentarze są ignorowane przez kompilator.

Dart obsługuje komentarze _jednoliniowe_, _wieloliniowe_ i _dokumentacyjne_.

Oto jak napisać komentarz _jednoliniowy_:
```dart
// To jest komentarz. Nie jest wykonywany.
```

---

Możesz łączyć komentarze _jednoliniowe_, aby tworzyć komentarze _wieloliniowe_.
```dart
// To jest
// komentarz wieloliniowy
```

---

Możesz też tworzyć bloki komentarzy, czyli komentarze _wieloliniowe_.
Komentarze _wieloliniowe_ zaczynają się od `/*` i kończą na `*/`.
```dart
/*
To jest komentarz
wieloliniowy
*/
```

---

Oprócz tych dwóch sposobów pisania komentarzy, Dart zawiera _komentarze dokumentacyjne_.

_Komentarze dokumentacyjne_ to komentarze wieloliniowe lub jednoliniowe, które zaczynają się od `///` lub `/**.` Użycie `///` w kolejnych liniach ma taki sam efekt jak wieloliniowy komentarz dokumentacyjny.

_Komentarze dokumentacyjne_ są bardzo przydatne, ponieważ umożliwiają generowanie dokumentacji.
Warto dodawać _komentarze dokumentacyjne_ do kodu, aby było jasne, co robi dany blok kodu.

W _komentarzu dokumentacyjnym_ analizator traktuje nazwy ujęte w nawiasy kwadratowe jako odwołania do innych elementów API.
Używając nawiasów kwadratowych można odwoływać się do _klas_, _metod_, _pól_, _zmiennych_, _funkcji_ i _parametrów_.

Oto przykład:
```dart
/// Udomestykowany południowoamerykański wielbłądowaty (Lama glama).
///
/// Tak jak każde inne zwierzę, lamy muszą jeść,
/// więc nie zapomnij dać im [feed] trochę [Food].
class Llama {
  String? name;

  /// Karmi twoją lamę [food].
  ///
  /// Typowa lama zjada jedną belę siana tygodniowo.
  void feed(Food food) {
    // ...
  }

  /// Ćwiczy twoją lamę przez [activity] przez
  /// [timeLimit] minut.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

W wygenerowanej dokumentacji `[feed]` staje się linkiem do dokumentacji metody `feed`, a `[Food]` staje się linkiem do dokumentacji klasy `Food`.
Natomiast `[activity]` i `[timeLimit]` stają się linkami do dokumentacji odpowiednio `activity` i `timeLimit`.
