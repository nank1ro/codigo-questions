**Map** przechowuje **pary klucz-wartość**: każda wartość jest zapisywana pod kluczem, a ty używasz tego klucza, aby ponownie znaleźć wartość.
Tworzysz pusty Map za pomocą `new Map()`, dodajesz parę za pomocą `set(key, value)` i odczytujesz wartość za pomocą `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// wypisuje 30
```
Wywołanie `set()` z kluczem, który już istnieje, zastępuje jego wartość.

---

Map ma jeszcze kilka istotnych metod i właściwości:
- `has(key)` zwraca `true`, jeśli klucz istnieje
- `delete(key)` usuwa parę z tym kluczem
- `size` to liczba przechowywanych par

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// wypisuje true
stock.delete("pear");
console.log(stock.size);
// wypisuje 1
```
Zauważ, że `size` jest właściwością, a nie metodą, więc nie ma nawiasów.

---

Zapytanie Map o klucz, którego nie zawiera, nie jest błędem: `get()` po prostu zwraca `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// wypisuje undefined
```
Dlatego istnieje `has()`: pozwala odróżnić brakujący klucz od klucza, którego wartość akurat wynosi `undefined`.
`set()` zwraca sam Map, więc wywołania można łączyć w łańcuch:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

W zwykłym obiekcie każdy klucz jest zamieniany na ciąg znaków: `user[1]` i `user["1"]` to ten sam klucz.
Map zachowuje **typ** swoich kluczy, więc liczba, ciąg znaków, wartość logiczna, a nawet obiekt mogą być osobnymi kluczami:
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// wypisuje 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// wypisuje klucz obiektu
```
Klucze będące obiektami są porównywane przez tożsamość: tylko dokładnie ten sam obiekt otrzymuje z powrotem wartość.

---

Map zapamiętuje kolejność, w jakiej dodawano pary, i możesz go przeglądać za pomocą `for...of`.
Metoda `entries()` zwraca każdą parę jako tablicę `[key, value]`, którą możesz od razu rozpakować w pętli:
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// wypisuje apple: 3
// wypisuje pear: 5
```
Przeglądanie bezpośrednio Map, `for (const [name, qty] of stock)`, robi dokładnie to samo.

---

Gdy potrzebujesz tylko jednej strony par, użyj w pętli `keys()` lub `values()` zamiast `entries()`:
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// wypisuje tea
// wypisuje cake
for (const price of prices.values()) {
  console.log(price);
}
// wypisuje 2
// wypisuje 4
```

---

Zamiast wielokrotnie wywoływać `set()`, możesz zbudować Map za jednym razem, przekazując **tablicę par** do `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// wypisuje 2
```
Ponieważ `Object.entries(obj)` zwraca dokładnie taką tablicę par, jest to najszybszy sposób na zamianę obiektu w Map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// wypisuje 30
```

---

Map i zwykłe obiekty przechowują wartości pod kluczami, ale różnią się pod kilkoma ważnymi względami:
- klucze obiektu są zawsze ciągami znaków (lub symbolami), klucze Map mogą być **dowolnego** typu
- Map zachowuje dokładną **kolejność wstawiania** swoich par
- Map zna swój własny `size`, podczas gdy dla obiektu potrzebujesz `Object.keys(obj).length`
- Map zaczyna naprawdę pusty, podczas gdy obiekt dziedziczy klucze takie jak `toString` ze swojego prototypu

---

Map nie ma metod tablicowych, takich jak `sort()` czy `filter()`. Aby ich użyć, przekonwertuj Map (lub jego klucze albo wartości) na tablicę za pomocą `Array.from()` lub operatora rozproszenia `...`:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// wypisuje [ [ 'Bob', 25 ], [ 'Ann', 30 ] ]
let names = [...ages.keys()];
console.log(names);
// wypisuje [ 'Bob', 'Ann' ]
let values = [...ages.values()];
console.log(values);
// wypisuje [ 25, 30 ]
```
Odwrotna konwersja, `Object.fromEntries(ages)`, zamienia Map z powrotem w zwykły obiekt.

---

Podobnie jak tablice, Map ma metodę `forEach()`, która wywołuje funkcję dla każdej pary.
Uważaj na kolejność parametrów: callback otrzymuje najpierw **wartość**, a potem klucz:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// wypisuje apple x3
// wypisuje pear x5
```

---

`delete(key)` zwraca `true`, gdy para została usunięta, i `false`, gdy klucza tam nie było.
Aby usunąć **wszystkie** pary naraz, wywołaj `clear()`:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// wypisuje true
console.log(cart.delete("pen"));
// wypisuje false
cart.clear();
console.log(cart.size);
// wypisuje 0
```

---

Kiedy więc warto sięgnąć po `Map` zamiast po zwykły obiekt?
- Użyj **Map**, gdy klucze są dodawane i usuwane w czasie działania programu, gdy nie są ciągami znaków, albo gdy potrzebujesz `size` i niezawodnego porządku
- Użyj **obiektu** dla stałego rekordu ze znanymi nazwami pól, jak `{ name, email }`, oraz zawsze, gdy trzeba przekonwertować dane do JSON, ponieważ `JSON.stringify()` ignoruje zawartość Map
