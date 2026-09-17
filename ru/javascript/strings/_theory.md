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

---

Метод `split(separator)` разбивает строку на **массив** частей, разрезая её на каждом `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// выводит [ 'I', 'like', 'JavaScript' ]
```
Противоположность — метод массива `join(separator)`, который склеивает части обратно в строку:
```javascript
console.log(words.join("-"));
// выводит I-like-JavaScript
```

---

Пользовательский ввод часто содержит лишние пробелы вокруг него. Метод `trim()` возвращает копию строки с удалёнными пробельными символами с **обоих** концов:
```javascript
let input = "   hello   ";
console.log(input.trim());
// выводит hello
```
`trimStart()` удаляет только пробелы в начале, а `trimEnd()` — только в конце.
Пробелы в середине строки никогда не затрагиваются.

---

Метод `replace(search, replacement)` возвращает новую строку, в которой **первое** вхождение `search` заменено на `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// выводит blue red
```
Чтобы заменить **все** вхождения, используйте `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// выводит blue blue
```

---

Метод `repeat(count)` возвращает строку, повторённую `count` раз:
```javascript
console.log("ab".repeat(3));
// выводит ababab
console.log("ab".repeat(0));
// выводит an empty string
```

---

Метод `padStart(targetLength, padString)` добавляет `padString` в **начало** строки, пока она не достигнет `targetLength` символов. `padEnd()` делает то же самое в конце:
```javascript
console.log("7".padStart(3, "0"));
// выводит 007
console.log("Tea".padEnd(6, "."));
// выводит Tea...
```
Если строка уже достаточно длинная, она возвращается без изменений.
У чисел нет строковых методов, поэтому сначала преобразуйте их с помощью `String(number)`.

---

Две строки равны с помощью `===` только если у них полностью совпадают символы, в одном и том же регистре:
```javascript
console.log("hello" === "hello");
// выводит true
console.log("hello" === "Hello");
// выводит false
```
Операторы `<` и `>` сравнивают строки по алфавиту, посимвольно.
Заглавные буквы идут раньше строчных, поэтому `"Zoo" < "apple"` — это `true`.

---

Строки **неизменяемы**: после создания строку никогда нельзя изменить.
Присваивание по индексу ничего не делает, и каждый строковый метод возвращает **новую** строку вместо изменения исходной:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// выводит hello
word.toUpperCase();
console.log(word);
// выводит hello
```
Чтобы сохранить результат, присвойте его обратно переменной:
```javascript
word = word.toUpperCase();
```

---

Вызов `split("")` с пустым разделителем превращает строку в массив её отдельных символов.
У массивов есть метод `reverse()`, поэтому строку можно перевернуть, разбив её, перевернув и снова соединив:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// выводит cba
```
