**Map** przechowuje **pary klucz-wartość**: każda wartość jest zapisywana pod kluczem, a ty używasz tego klucza, aby ponownie znaleźć wartość.
Tworzysz pusty Map za pomocą `new Map()`, dodajesz parę za pomocą `set(key, value)` i odczytujesz wartość za pomocą `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
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
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
Zauważ, że `size` jest właściwością, a nie metodą, więc nie ma nawiasów.

---

Zapytanie Map o klucz, którego nie zawiera, nie jest błędem: `get()` po prostu zwraca `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
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
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
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
// prints apple: 3
// prints pear: 5
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
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

Zamiast wielokrotnie wywoływać `set()`, możesz zbudować Map za jednym razem, przekazując **tablicę par** do `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Ponieważ `Object.entries(obj)` zwraca dokładnie taką tablicę par, jest to najszybszy sposób na zamianę obiektu w Map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
