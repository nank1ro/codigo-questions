**String** to sekwencja znaków ujęta w cudzysłów, na przykład `"hello"` lub `'hello'`.
Każdy łańcuch ma właściwość `length`, która mówi, ile znaków zawiera:
```javascript
let greeting = "hello";
console.log(greeting.length);
// wypisuje 5
```
Spacje i znaki interpunkcyjne również liczą się jako znaki.

---

Każdy znak w łańcuchu ma **indeks**, zaczynając od `0`.
Pojedynczy znak możesz odczytać za pomocą nawiasów kwadratowych lub metody `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// wypisuje h
console.log(word.charAt(1));
// wypisuje e
```
Ostatni znak znajduje się pod indeksem `length - 1`:
```javascript
console.log(word[word.length - 1]);
// wypisuje o
```

---

Łańcuchy mają wiele wbudowanych **metod**. Dwie z najprostszych zmieniają wielkość każdej litery:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// wypisuje HELLO
console.log(word.toLowerCase());
// wypisuje hello
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
// wypisuje true
console.log(file.startsWith("ph"));
// wypisuje true
console.log(file.endsWith(".jpg"));
// wypisuje false
```
Porównanie rozróżnia wielkość liter: `"Hello".includes("h")` to `false`.

---

Metoda `indexOf()` zwraca indeks, pod którym fragment tekstu **pierwszy raz** pojawia się w łańcuchu.
Jeśli tekst nie zostanie znaleziony, zwraca `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// wypisuje 2
console.log(word.indexOf("z"));
// wypisuje -1
```

---

Metoda `slice(start, end)` wycina fragment łańcucha, od indeksu `start` do (ale bez) indeksu `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// wypisuje Java
console.log(word.slice(4));
// wypisuje Script
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
// wypisuje 45
```
