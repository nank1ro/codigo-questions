Funkcja nie musi mieć nazwy. **Wyrażenie funkcyjne** tworzy funkcję jako wartość, którą można zapisać w zmiennej i wywoływać przez nią:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
**Funkcja strzałkowa** to krótszy sposób zapisania tego samego: opuszczasz słowo kluczowe `function` i wstawiasz "grubą strzałkę" `=>` między listą parametrów a ciałem:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Funkcje strzałkowe zwykle zapisuje się w `const`, więc nazwy nie da się przez pomyłkę przypisać ponownie, a wywołuje się je dokładnie tak samo jak każdą inną funkcję.

---

Funkcje strzałkowe stają się krótsze w dwóch typowych przypadkach.
Gdy ciało to **pojedyncze wyrażenie**, możesz opuścić klamry i słowo kluczowe `return`: wartość wyrażenia jest zwracana automatycznie (**niejawny return**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
Gdy jest **dokładnie jeden parametr**, możesz też opuścić nawiasy wokół niego:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
Przy zerze parametrów albo przy dwóch lub więcej nawiasy są wymagane: `() => 42` oraz `(a, b) => a + b`.

---

Z niejawnym return wiąże się jedna pułapka. Funkcję strzałkową, której ciało zaczyna się od `{`, czyta się jako **ciało blokowe**, nigdy jako literał obiektu:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Tu `{ name: name }` to blok zawierający etykietę `name:`, po której następuje wyrażenie `name`. Nic nie jest zwracane, więc wywołanie daje `undefined`.
Aby zwrócić literał obiektu w jednej linii, owiń go w **nawiasy okrągłe**, dzięki czemu JavaScript potraktuje go jako wyrażenie:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Owijanie literału obiektu w nawiasy okrągłe to standardowy sposób tworzenia obiektów jednolinijkową funkcją strzałkową, na przykład gdy zamieniasz kilka wartości w rekord:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
Funkcja strzałkowa bez parametrów zaczyna się od pustej pary nawiasów `()`:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Funkcje strzałkowe sprawdzają się przede wszystkim jako **callbacki**: funkcje przekazywane jako argumenty do innych funkcji. Najczęstszym przykładem są metody tablic.
`map(callback)` zwraca nową tablicę z wynikiem callbacka dla każdego elementu, a `filter(callback)` zwraca nową tablicę zawierającą tylko te elementy, dla których callback zwraca `true`:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Obie zwracają nową tablicę i pozostawiają oryginał nietkniętym, więc można je łączyć w łańcuch: `numbers.filter(...).map(...)`.

---

Jeszcze dwie metody tablic przyjmują callback.
`forEach(callback)` wywołuje callback raz dla każdego elementu i nic nie zwraca; używa się jej do efektów ubocznych, takich jak wypisywanie.
`reduce(callback, initialValue)` zwija tablicę do pojedynczej wartości: callback otrzymuje dotychczasową skumulowaną wartość oraz bieżący element i zwraca nową skumulowaną wartość:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` porządkuje tablicę w miejscu za pomocą callbacka, który otrzymuje dwa elementy i zwraca liczbę ujemną, gdy pierwszy powinien być pierwszy, dodatnią, gdy drugi powinien być pierwszy, albo `0`, gdy są równe. Dla liczb `(a, b) => a - b` sortuje rosnąco, a `(a, b) => b - a` malejąco.
`find(callback)` zwraca pierwszy element, dla którego callback zwraca `true`, albo `undefined`, gdy takiego nie ma:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

Parametry funkcji strzałkowej obsługują te same możliwości co parametry zwykłej funkcji.
**Wartość domyślna** jest używana, gdy argument zostanie pominięty lub jest równy `undefined`:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Zauważ, że parametr z wartością domyślną zawsze wymaga nawiasów, nawet gdy jest jedyny: `name = "World" => ...` to błąd składni.

---

**Parametr reszty** `...name` zbiera dowolną liczbę argumentów do tablicy i działa również w funkcjach strzałkowych:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Zwykłe funkcje mają też ukryty obiekt przypominający tablicę, `arguments`, przechowujący wszystkie otrzymane argumenty. Funkcje strzałkowe **nie**: wewnątrz strzałki `arguments` odnosi się do `arguments` otaczającej funkcji albo w ogóle nie istnieje. Gdy w funkcji strzałkowej potrzebujesz "wszystkich argumentów", użyj parametru reszty.

---

Funkcja zapamiętuje zmienne zakresu, w którym została **utworzona**, nawet po tym, jak ten zakres skończył się wykonywać. Nazywa się to **domknięciem**.
Klasycznym przykładem jest twórca liczników: każde wywołanie `makeCounter` tworzy świeży `count` i zwraca funkcję strzałkową, która nadal używa tego samego `count`:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Nikt inny nie może odczytać ani zresetować `count`: żyje on tylko wewnątrz zwróconej funkcji. Drugie wywołanie `makeCounter()` tworzy niezależny licznik z własnym `count`.

---

Ponieważ funkcja jest wartością, funkcja strzałkowa może **zwracać inną funkcję strzałkową**. Połączenie dwóch strzałek w łańcuch to zwięzły sposób zapisania funkcji budującej funkcje:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Czytaj od lewej do prawej: `makeAdder` przyjmuje `amount` i zwraca `(n) => n + amount`, funkcję strzałkową, która przechwytuje `amount` dzięki domknięciu. `makeAdder(1)(5)` od razu wywołuje zwróconą funkcję.
