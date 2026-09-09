W JavaScripcie funkcja jest **wartością**: możesz zapisać ją w zmiennej, umieścić w tablicy i przekazać innej funkcji jako argument. Funkcja, która przyjmuje funkcję jako argument albo zwraca funkcję, nazywa się **funkcją wyższego rzędu**. Przekazana funkcja nazywa się **callbackiem**, ponieważ odbiorca *wywołuje ją zwrotnie*, gdy jej potrzebuje:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Zwróć uwagę, że `shout` przekazujemy **bez nawiasów**: `twice(shout, "hi")` przekazuje samą funkcję, natomiast `twice(shout("hi"), "hi")` najpierw wywołałoby `shout` i przekazało jego wynik, łańcuch `"HI!"`, którego nie da się wywołać.

---

Funkcje wyższego rzędu pozwalają oddzielić *co robić z każdym elementem* od *jak przechodzić po elementach*. Część przechodząca jest napisana raz, a callback decyduje o reszcie:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
Callback dostaje po jednym elemencie naraz. Może to być funkcja strzałkowa napisana w miejscu, jak wyżej, albo dowolna funkcja zapisana w zmiennej. Dokładnie tak działają wewnątrz wbudowane metody tablic, które poznasz dalej.

---

Wbudowana metoda `map` robi to, co `transform`: wywołuje callback dla każdego elementu i zbiera wyniki w **nowej tablicy**. `forEach` również wywołuje callback dla każdego elementu, ale niczego nie zbiera i zawsze zwraca `undefined`; używaj jej tylko dla efektów ubocznych, takich jak wypisywanie:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Częstym błędem jest zapisanie wyniku `forEach` albo dołączenie po niej kolejnej metody: nie ma czego łączyć, ponieważ zwraca `undefined`. Zasada: używaj `map`, gdy potrzebujesz nowych wartości, a `forEach`, gdy chcesz tylko coś *zrobić*.

---

Kolejne dwie metody wyższego rzędu pokrywają większość codziennych potrzeb.
`filter(callback)` zwraca nową tablicę zawierającą tylko te elementy, dla których callback zwraca `true`; callback odpowiadający w ten sposób tak lub nie nazywa się **predykatem**.
`reduce(callback, initialValue)` łączy wszystkie elementy w jedną wartość: callback dostaje **akumulator** (dotychczasowy wynik) oraz bieżący element i zwraca nowy akumulator. Drugi argument `reduce` to początkowy akumulator:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Ponieważ `filter` i `map` zwracają tablice, możesz je łączyć i zakończyć przez `reduce`: `numbers.filter(...).map(...).reduce(...)`.

---

Trzy metody odpowiadają na pytania o tablicę za pomocą predykatu:
- `find(predicate)` zwraca **pierwszy** element, dla którego predykat jest `true`, albo `undefined`, gdy takiego nie ma
- `some(predicate)` zwraca `true`, jeśli **co najmniej jeden** element spełnia predykat
- `every(predicate)` zwraca `true`, jeśli spełniają go **wszystkie** elementy (i `true` dla pustej tablicy)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Wszystkie trzy zatrzymują się, gdy tylko odpowiedź jest znana, więc nigdy nie sprawdzają więcej elementów, niż trzeba.

---

`sort(compare)` sortuje tablicę **w miejscu** za pomocą callbacku, który dostaje dwa elementy i zwraca liczbę ujemną, gdy pierwszy ma być wcześniej, liczbę dodatnią, gdy wcześniej ma być drugi, albo `0`, gdy są równe. Dla liczb `(a, b) => a - b` sortuje rosnąco, a `(a, b) => b - a` malejąco.
Bez komparatora `sort()` zamienia każdy element na **łańcuch** i porównuje je znak po znaku, więc `10` jest przed `9`, bo `"1"` jest mniejsze niż `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Ponieważ `sort` zmienia tablicę, sortuj kopię, gdy potrzebujesz też oryginalnej kolejności: `[...numbers].sort(...)`. Dla łańcuchów użyj komparatora `(a, b) => a.localeCompare(b)`, który porządkuje tekst alfabetycznie.

---

Komparator może patrzeć na dowolną część elementów, więc tablicę obiektów sortuje się według jednej z ich właściwości, po prostu porównując tę właściwość:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Sortowanie kopii zostawia `items` w pierwotnej kolejności.

---

Funkcja wyższego rzędu może też **zwrócić** funkcję. Zwrócona funkcja pamięta zmienne z miejsca, w którym powstała, nawet po zakończeniu funkcji zewnętrznej: nazywa się to **domknięciem**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Każde wywołanie `makeMultiplier` tworzy nową funkcję z własnym `factor`. Tak buduje się rodzinę podobnych funkcji z jednego wzorca. To samo można zapisać funkcjami strzałkowymi: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Domknięcie zachowuje **żywe** połączenie ze zmienną, a nie kopię jej wartości. Gdy w tym samym wywołaniu powstaje kilka funkcji, dzielą one tę samą zmienną, a każda zmiana wprowadzona przez jedną z nich jest widoczna dla pozostałych:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Nikt nie może odczytać ani wyzerować `count` z zewnątrz inaczej niż przez te dwie funkcje: zmienna jest **prywatna**. Drugie wywołanie `makeCounter()` tworzy całkowicie osobne `count`.

---

Ponieważ funkcje są wartościami, możesz napisać funkcję wyższego rzędu, która **łączy** dwie funkcje w jedną nową. `compose(f, g)` zwraca funkcję stosującą najpierw `g`, a potem `f` do wyniku, zgodnie z zapisem matematycznym *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
Kolejność ma znaczenie: `compose(f, g)` uruchamia najpierw `g`, potem `f`. Budowanie programów przez sklejanie w ten sposób małych funkcji nazywa się **komponowaniem funkcji**.

---

Funkcja zwracająca funkcję to również naturalny sposób na **dostosowanie** callbacku. Załóżmy, że masz predykat, a do `filter` potrzebujesz jego przeciwieństwa: zamiast pisać go od nowa, opakuj go:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Ogólne `not(predicate)` zrobiłoby to dla dowolnego predykatu: zwraca nową funkcję, która wywołuje `predicate` z tym samym argumentem i odwraca wynik przez `!`. Predykaty dla `filter`, `find`, `some` i `every` dostają element jako pierwszy argument, więc opakowanie musi przekazać dalej tylko tę jedną wartość.

---

Akumulator `reduce` nie musi być liczbą: może być łańcuchem, tablicą albo obiektem. Zaczynając od pustego obiektu `{}`, możesz zliczać albo grupować rzeczy w jednym przebiegu. Pamiętaj, aby **zwrócić akumulator** z callbacku, inaczej następny krok dostanie `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` odczytuje bieżącą liczbę albo `0`, gdy takiego klucza jeszcze nie ma.

---

Każda funkcja ma metodę `bind`, która zwraca **nową** funkcję z częścią rzeczy ustaloną z góry. Jej pierwszy argument staje się `this` nowej funkcji; pozostałe argumenty trafiają przed te, z którymi nowa funkcja zostanie wywołana (**częściowa aplikacja**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Ustalenie `this` ma znaczenie dla metod. Gdy metodę skopiujemy poza jej obiekt i wywołamy samodzielnie, `this` nie wskazuje już obiektu, więc `this.name` staje się `undefined`. `bind` przypina je do obiektu:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
Oryginalna funkcja nigdy się nie zmienia: `bind` zawsze buduje nową, której `name` to pierwotna nazwa poprzedzona `bound `.

---

Prawdziwe programy łączą te metody w **potok**: odfiltruj interesujące cię elementy, przekształć je na potrzebne wartości i zredukuj do wyniku. Zapisywanie pośrednich tablic w stałych utrzymuje czytelność każdego kroku i pozwala je ponownie wykorzystać:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` zamienia tablicę łańcuchów w jeden łańcuch, w którym elementy są oddzielone przecinkiem i spacją.

---

Domknięcia pozwalają zwróconej funkcji zachować **prywatny stan** między wywołaniami. Klasycznym tak zbudowanym pomocnikiem jest `once(fn)`: zwraca funkcję, która uruchamia `fn` tylko przy pierwszym wywołaniu, zapamiętuje wynik i przy każdym kolejnym wywołaniu zwraca ten sam wynik bez ponownego uruchamiania `fn`:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
Opakowanie potrzebuje dwóch prywatnych zmiennych: czy `fn` już się uruchomiło oraz zapamiętanego wyniku. Obie żyją w domknięciu, niewidoczne z zewnątrz. Aby przekazać do `fn` wszystkie argumenty opakowania, zadeklaruj je z parametrem reszty `(...args)` i wywołaj `fn(...args)`.

---

Wszystko spotyka się w `groupBy(items, keyFn)`: funkcji wyższego rzędu, która dostaje callback ustalający **klucz grupy** każdego elementu i zwraca obiekt przypisujący każdemu kluczowi tablicę elementów o tym kluczu. `reduce` z akumulatorem będącym obiektem wykonuje całą pracę:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Dla każdego elementu wylicz klucz, utwórz tablicę dla tego klucza, jeśli jeszcze nie istnieje (`acc[key] ?? []`), dodaj element i zwróć akumulator. Ponieważ to wywołujący wybiera `keyFn`, ta sama funkcja grupuje słowa po pierwszej literze, osoby po mieście albo liczby po parzystości.
