**Enumeracja** (lub *enum*) to wspólny typ dla małej grupy powiązanych, stałych wartości: dni tygodnia, kolory kart, możliwe stany zamówienia.
W przeciwieństwie do wielu języków, JavaScript **nie** posiada słowa kluczowego `enum`. Idiomatycznym zamiennikiem jest zwykły obiekt, którego właściwości są składowymi, przekazany do `Object.freeze()`, aby nikt nie mógł go później zmienić:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// wypisuje red
```
Zgodnie z konwencją obiekt jest deklarowany za pomocą `const`, jego nazwa zaczyna się wielką literą, a nazwy składowych są zapisywane w formacie `UPPER_CASE`, dokładnie tak jak inne stałe.

---

Wartość przechowywana w każdej składowej zależy od Ciebie. **Ciągi znaków** są najczęstszym wyborem, ponieważ są czytelne po wypisaniu, zalogowaniu lub zapisaniu do pliku:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// wypisuje done
```
Po zamrożeniu obiekt nie może również otrzymać nowych właściwości, a `Object.isFrozen(obj)` mówi, czy obiekt został zamrożony:
```javascript
console.log(Object.isFrozen(Status));
// wypisuje true
```

---

Po co w ogóle zamrażać obiekt? Zamrożony obiekt odrzuca każdą zmianę: przypisanie do istniejącej składowej, dodanie nowej lub usunięcie którejś nie ma żadnego efektu.
To, jak objawia się to odrzucenie, zależy od trybu, w którym działa Twój kod:
- w **trybie niestryktnym** (sloppy mode, domyślnym dla zwykłych skryptów) przypisanie jest **po cichu ignorowane**
- w **trybie strykt** (strict mode, plikach zaczynających się od `"use strict"`, modułach ES i ciałach klas) **rzuca** ono wyjątek `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// wypisuje s
console.log(Size.MEDIUM);
// wypisuje undefined
```
Tak czy inaczej, enumeracja zachowuje zdefiniowane przez Ciebie wartości, czego dokładnie oczekujesz od zestawu stałych.

---

Składowe mogą również przechowywać **liczby**. Wartości liczbowe są przydatne, gdy składowe mają naturalny porządek, ponieważ można je porównywać zwykłymi operatorami:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// wypisuje true
```
Kompromisem jest czytelność: wypisanie `Priority.HIGH` pokazuje `3`, co mówi znacznie mniej niż powiedziałby ciąg znaków `"high"`.

---

Ponieważ enumeracja jest po prostu obiektem, standardowe metody obiektowe pozwalają ją zbadać:
- `Object.keys(Enum)` zwraca tablicę z **nazwami** składowych
- `Object.values(Enum)` zwraca tablicę z **wartościami** składowych
- `Object.entries(Enum)` zwraca tablicę par `[nazwa, wartość]`

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// wypisuje [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// wypisuje [ 'red', 'blue' ]
```
Połączenie `Object.values()` z metodą tablicową `includes()` to standardowy sposób sprawdzenia, czy dowolna wartość, na przykład wczytana z danych wejściowych użytkownika, jest prawidłową składową:
```javascript
console.log(Object.values(Color).includes("red"));
// wypisuje true
console.log(Object.values(Color).includes("pink"));
// wypisuje false
```

---

Enumeracje naturalnie łączą się z instrukcją `switch`, która porównuje jedną wartość z listą etykiet `case` i uruchamia kod pierwszej pasującej.
Każda gałąź kończy się `return` lub `break`, a opcjonalna gałąź `default` uruchamia się, gdy nic nie pasuje:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// wypisuje go
```
Zawsze porównuj ze składowymi (`Light.RED`), nigdy z surowymi wartościami (`"red"`): jeśli wartość kiedykolwiek się zmieni, `switch` nadal będzie działać.

---

Przejście od wartości z powrotem do nazwy jej składowej nazywa się **wyszukiwaniem odwrotnym**. Przejdź przez nazwy za pomocą `Object.keys()` i wybierz pierwszą, której wartość pasuje, używając metody tablicowej `find()`, która zwraca pierwszy element, dla którego funkcja zwrotna zwraca `true` (lub `undefined`, jeśli żaden nie pasuje):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// wypisuje HIGH
```
`Priority[key]` odczytuje składową, której nazwa jest przechowywana w zmiennej `key`, tę samą notację nawiasową, której używasz dla dowolnego obiektu.

---

Składowe będące ciągami znaków mają jedną słabość: jako składowa akceptowany jest każdy ciąg znaków o tym samym tekście.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// wypisuje true
```
Gdy chcesz mieć składowe równe **tylko** samym sobie, użyj `Symbol`. `Symbol(description)` tworzy zupełnie nową wartość, różną od każdego innego symbolu, nawet takiego utworzonego z tym samym opisem:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// wypisuje true
console.log(Suit.HEARTS === Symbol("hearts"));
// wypisuje false
console.log(typeof Suit.HEARTS);
// wypisuje symbol
```
Przekazywany tekst jest jedynie etykietą do celów debugowania; możesz go odczytać z powrotem za pomocą właściwości `description` (`Suit.HEARTS.description` to `"hearts"`).

---

Wartości enumeracji są często używane jako **klucze** innego obiektu, na przykład aby zmapować każdą składową na etykietę lub cenę. Wewnątrz literału obiektu, ujęcie klucza w nawiasy kwadratowe `[ ]` powoduje obliczenie wyrażenia i użycie jego wyniku jako klucza (**klucz obliczany**). Działa to zarówno ze składowymi typu string, jak i symbol:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// wypisuje Completed
```
Bez nawiasów, `Status.DONE: "Completed"` byłoby błędem składni, a `"Status.DONE"` byłoby zwykłym kluczem tekstowym.

---

Gdy każda składowa potrzebuje kilku danych lub własnych metod, rolę enumeracji może pełnić **klasa**. Każda składowa jest instancją klasy, przechowywaną we właściwości `static`, czyli właściwości należącej do samej klasy, a nie do każdej instancji:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// wypisuje Earth
```
Wywołaj `Object.freeze(Planet)` po klasie, aby uniemożliwić komukolwiek dodawanie lub zastępowanie składowych, i zamroź każdą instancję w konstruktorze za pomocą `Object.freeze(this)`, aby same składowe pozostały tylko do odczytu.
