**Enumeracja** (lub *enum*) to wspólny typ dla małej grupy powiązanych, stałych wartości: dni tygodnia, kolory kart, możliwe stany zamówienia.
W przeciwieństwie do wielu języków, JavaScript **nie** posiada słowa kluczowego `enum`. Idiomatycznym zamiennikiem jest zwykły obiekt, którego właściwości są składowymi, przekazany do `Object.freeze()`, aby nikt nie mógł go później zmienić:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
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
// prints done
```
Po zamrożeniu obiekt nie może również otrzymać nowych właściwości, a `Object.isFrozen(obj)` mówi, czy obiekt został zamrożony:
```javascript
console.log(Object.isFrozen(Status));
// prints true
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
// prints s
console.log(Size.MEDIUM);
// prints undefined
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
// prints true
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
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Połączenie `Object.values()` z metodą tablicową `includes()` to standardowy sposób sprawdzenia, czy dowolna wartość, na przykład wczytana z danych wejściowych użytkownika, jest prawidłową składową:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
