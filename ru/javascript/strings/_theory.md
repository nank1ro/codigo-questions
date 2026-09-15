**Строка** — это последовательность символов в кавычках, например `"hello"` или `'hello'`.
У каждой строки есть свойство `length`, которое сообщает, сколько символов она содержит:
```javascript
let greeting = "hello";
console.log(greeting.length);
// выводит 5
```
Пробелы и знаки препинания тоже считаются символами.

---

У каждого символа в строке есть **индекс**, начиная с `0`.
Прочитать отдельный символ можно с помощью квадратных скобок или метода `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// выводит h
console.log(word.charAt(1));
// выводит e
```
Последний символ находится по индексу `length - 1`:
```javascript
console.log(word[word.length - 1]);
// выводит o
```

---

У строк есть много встроенных **методов**. Два самых простых меняют регистр каждой буквы:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// выводит HELLO
console.log(word.toLowerCase());
// выводит hello
```
Оба метода не принимают аргументов, поэтому не забывайте про скобки.

---

Чтобы проверить, содержит ли строка другую строку, используйте эти методы — все они возвращают логическое значение:
- `includes(text)` — `true`, если `text` встречается где-либо
- `startsWith(text)` — `true`, если строка начинается с `text`
- `endsWith(text)` — `true`, если строка заканчивается на `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// выводит true
console.log(file.startsWith("ph"));
// выводит true
console.log(file.endsWith(".jpg"));
// выводит false
```
Сравнение чувствительно к регистру: `"Hello".includes("h")` — это `false`.

---

Метод `indexOf()` возвращает индекс, по которому фрагмент текста **впервые** встречается в строке.
Если текст не найден, он возвращает `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// выводит 2
console.log(word.indexOf("z"));
// выводит -1
```

---

Метод `slice(start, end)` извлекает часть строки, от индекса `start` до индекса `end` (не включая его):
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// выводит Java
console.log(word.slice(4));
// выводит Script
```
Если опустить `end`, срез идёт до конца строки.
Отрицательный индекс отсчитывается с конца: `word.slice(-3)` — это `"ipt"`.
Метод `substring(start, end)` работает так же, но не принимает отрицательные индексы.

---

`indexOf()` и `slice()` хорошо работают вместе: найдите, где что-то находится, а затем обрежьте строку в этом месте.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// выводит 45
```
