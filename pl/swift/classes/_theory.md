Swift jest obiektowym językiem programowania, co oznacza, że manipuluje konstruktami programistycznymi zwanymi obiektami.
Obiekt można traktować jako pojedynczą strukturę danych zawierającą zarówno dane, jak i funkcje; funkcje obiektu nazywane są jego metodami.
Na przykład, gdy wywołujesz:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift sprawdza, czy `dictName` ma metodę `removeValue()` (którą posiadają wszystkie słowniki) i wykonuje tę metodę, jeśli ją znajdzie.

---

_Struktury_ i _klasy_ to ogólne, elastyczne konstrukty, które stają się blokami budulcowymi kodu programu.
Podstawowa klasa lub struktura składa się wyłącznie ze słowa kluczowego `class` lub `struct` i jej nazwy, na przykład:
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

Dodajmy coś do naszej klasy `Animal`

---

Zdefiniowanie klasy nie tworzy obiektu.
Aby to zrobić, musimy utworzyć __instancję__ klasy

---

Gdy klasa posiada własne funkcje, te funkcje są nazywane __metodami__.

---

Struktury i klasy w Swift mają wiele wspólnych cech. Obie mogą:
- Definiować właściwości do przechowywania wartości
- Definiować metody zapewniające funkcjonalność
- Definiować indeksy dolne umożliwiające dostęp do ich wartości przy użyciu składni indeksu dolnego
- Definiować inicjalizatory ustawiające ich stan początkowy
- Być rozszerzane w celu rozbudowania funkcjonalności poza domyślną implementację
- Być zgodne z protokołami w celu zapewnienia standardowej funkcjonalności określonego rodzaju

Jednak klasy mają dodatkowe możliwości, których struktury nie posiadają:
- Dziedziczenie umożliwia jednej klasie przejęcie cech innej klasy
- Rzutowanie typów umożliwia sprawdzanie i interpretowanie typu instancji klasy w czasie wykonywania
- Deinicjalizatory umożliwiają instancji klasy zwolnienie przydzielonych zasobów
- Zliczanie referencji pozwala na więcej niż jedno odwołanie do instancji klasy

---

Możesz uzyskać dostęp do właściwości instancji używając _składni z kropką_.
W składni z kropką nazwę właściwości piszesz bezpośrednio po nazwie instancji, oddzieloną kropką `.`, bez żadnych spacji:
```swift
someInstance.someProperty
```
Używając tej samej składni możemy również zaktualizować wartość właściwości

---

Jedną z zalet struktur jest to, że posiadają automatycznie generowany inicjalizator memberwise, którego można użyć do inicjalizacji właściwości składowych nowych instancji struktury.
Wartości początkowe dla właściwości nowej instancji można przekazać do inicjalizatora memberwise według nazwy
