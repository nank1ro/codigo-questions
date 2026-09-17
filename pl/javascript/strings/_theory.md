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

---

Metoda `split(separator)` dzieli łańcuch na **tablicę** fragmentów, przecinając przy każdym wystąpieniu `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// wypisuje [ 'I', 'like', 'JavaScript' ]
```
Przeciwieństwem jest metoda tablicy `join(separator)`, która skleja fragmenty z powrotem w łańcuch:
```javascript
console.log(words.join("-"));
// wypisuje I-like-JavaScript
```

---

Dane wprowadzone przez użytkownika często mają dodatkowe spacje wokół nich. Metoda `trim()` zwraca kopię łańcucha z usuniętymi białymi znakami z **obu** końców:
```javascript
let input = "   hello   ";
console.log(input.trim());
// wypisuje hello
```
`trimStart()` usuwa tylko wiodące białe znaki, a `trimEnd()` tylko końcowe.
Spacje w środku łańcucha nigdy nie są ruszane.

---

Metoda `replace(search, replacement)` zwraca nowy łańcuch, w którym **pierwsze** wystąpienie `search` jest zamienione na `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// wypisuje blue red
```
Aby zamienić **wszystkie** wystąpienia, użyj `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// wypisuje blue blue
```

---

Metoda `repeat(count)` zwraca łańcuch powtórzony `count` razy:
```javascript
console.log("ab".repeat(3));
// wypisuje ababab
console.log("ab".repeat(0));
// wypisuje pusty string
```

---

Metoda `padStart(targetLength, padString)` dodaje `padString` na **początku** łańcucha, dopóki nie osiągnie `targetLength` znaków. `padEnd()` robi to samo na końcu:
```javascript
console.log("7".padStart(3, "0"));
// wypisuje 007
console.log("Tea".padEnd(6, "."));
// wypisuje Tea...
```
Jeśli łańcuch jest już wystarczająco długi, jest zwracany bez zmian.
Liczby nie mają metod łańcuchowych, więc najpierw przekształć je za pomocą `String(number)`.

---

Dwa łańcuchy są równe za pomocą `===` tylko wtedy, gdy mają dokładnie te same znaki, w tej samej wielkości liter:
```javascript
console.log("hello" === "hello");
// wypisuje true
console.log("hello" === "Hello");
// wypisuje false
```
Operatory `<` i `>` porównują łańcuchy alfabetycznie, znak po znaku.
Wielkie litery są mniejsze od małych, więc `"Zoo" < "apple"` to `true`.

---

Łańcuchy są **niemutowalne**: po utworzeniu łańcuch nigdy nie może zostać zmieniony.
Przypisanie do indeksu nic nie robi, a każda metoda łańcucha zwraca **nowy** łańcuch zamiast modyfikować oryginał:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// wypisuje hello
word.toUpperCase();
console.log(word);
// wypisuje hello
```
Aby zachować wynik, przypisz go z powrotem do zmiennej:
```javascript
word = word.toUpperCase();
```

---

Wywołanie `split("")` z pustym separatorem zamienia łańcuch w tablicę jego pojedynczych znaków.
Tablice mają metodę `reverse()`, więc możesz odwrócić łańcuch, dzieląc go, odwracając i łącząc z powrotem:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// wypisuje cba
```
