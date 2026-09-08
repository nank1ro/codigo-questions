**String** to sekwencja znaków ujęta w cudzysłów, na przykład `"hello"` lub `'hello'`.
Każdy łańcuch ma właściwość `length`, która mówi, ile znaków zawiera:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
Spacje i znaki interpunkcyjne również liczą się jako znaki.

---

Każdy znak w łańcuchu ma **indeks**, zaczynając od `0`.
Pojedynczy znak możesz odczytać za pomocą nawiasów kwadratowych lub metody `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
Ostatni znak znajduje się pod indeksem `length - 1`:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

Łańcuchy mają wiele wbudowanych **metod**. Dwie z najprostszych zmieniają wielkość każdej litery:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
```
Obie metody nie przyjmują argumentów, więc pamiętaj o nawiasach.

---

Aby sprawdzić, czy łańcuch zawiera inny łańcuch, użyj tych metod, które zawsze zwracają wartość logiczną:
- `includes(text)` to `true`, jeśli `text` występuje gdziekolwiek
- `startsWith(text)` to `true`, jeśli łańcuch zaczyna się od `text`
- `endsWith(text)` to `true`, jeśli łańcuch kończy się na `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
Porównanie rozróżnia wielkość liter: `"Hello".includes("h")` to `false`.

---

Metoda `indexOf()` zwraca indeks, pod którym fragment tekstu **pierwszy raz** pojawia się w łańcuchu.
Jeśli tekst nie zostanie znaleziony, zwraca `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

Metoda `slice(start, end)` wycina fragment łańcucha, od indeksu `start` do (ale bez) indeksu `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
```
Jeśli pominiesz `end`, fragment sięga do końca łańcucha.
Ujemny indeks liczy się od końca: `word.slice(-3)` to `"ipt"`.
Metoda `substring(start, end)` działa tak samo, ale nie akceptuje ujemnych indeksów.

---

`indexOf()` i `slice()` dobrze ze sobą współpracują: znajdź, gdzie coś się znajduje, a potem przetnij tam łańcuch.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// prints 45
```
