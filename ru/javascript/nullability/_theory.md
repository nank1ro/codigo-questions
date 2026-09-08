В JavaScript есть два разных способа сказать «здесь нет значения».
`undefined` означает, что значение **не было задано вовсе**. Переменная, объявленная без значения, содержит `undefined`, как и свойство, отсутствующее в объекте:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` — это значение, которое **вы** присваиваете намеренно, чтобы сказать «здесь пусто, и я это знаю»:
```javascript
let owner = null;
console.log(owner);
// prints null
```
Итак, `undefined` — это обычно язык, сообщающий вам, что чего-то не хватает, а `null` — способ программиста заявить, что значение пусто намеренно.

---

Функции дают `undefined` ещё в двух ситуациях.
Когда вы вызываете функцию с **меньшим числом аргументов**, чем она объявляет, пропущенные параметры содержат `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Когда функция завершается **без `return`** (или с пустым `return;`), её вызов даёт `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Обратите внимание, что явная передача `null` — не то же самое, что пропуск аргумента: `greet(null)` выводит `null`, потому что `null` — это настоящее значение, переданное функции.

---

Оператор `typeof` возвращает тип значения в виде строки. Для `undefined` он отвечает `"undefined"`, как и ожидается:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Для `null`, однако, он отвечает `"object"`. Это ошибка из самой первой версии JavaScript, которую так и не исправили, потому что слишком много кода от неё зависит:
```javascript
console.log(typeof null);
// prints object
```
Итак, `typeof` — надёжный способ обнаружить `undefined`, но не `null`. Чтобы проверить на `null`, сравните с ним напрямую: `value === null`.

---

Как сравниваются между собой `null` и `undefined`? Это зависит от оператора.
**Нестрогое** равенство `==` считает их одним и тем же, но отличными от любого другого значения, включая `0`, `""` и `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
**Строгое** равенство `===` сравнивает ещё и тип, а у `null` и `undefined` разные типы:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

В большинстве случаев вам неважно, *какой именно* из двух маркеров «нет значения» вы получили: вы просто хотите знать, есть ли значение.
Поскольку `null == undefined` даёт `true` и ничто другое не равно нестрого `null`, сравнение `value == null` — стандартный приём, чтобы поймать **оба** значения сразу:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
Это единственный случай, когда `==` предпочитают `===`: запись `value === null || value === undefined` делает ровно то же самое, только длиннее.
Значения вроде `0`, `""` и `false` — *не* `null`: это настоящие значения, которые просто оказываются falsy.

---

Чтение свойства у `null` или `undefined` — это ошибка, которая останавливает программу:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` — это `undefined`, а у `undefined` нет свойств. Оператор **опциональной цепочки** `?.` решает эту проблему: если значение слева от него равно `null` или `undefined`, всё выражение останавливается и вычисляется в `undefined` вместо выбрасывания ошибки:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Когда слева всё же есть значение, `?.` ведёт себя в точности как обычная точка `.`. Можно объединять несколько: `user.address?.street?.name` возвращает `undefined`, как только какое-либо звено отсутствует.

---

Опциональная цепочка не ограничивается свойствами через точку. Есть ещё две формы.
`?.[]` читает элемент или вычисляемый ключ только тогда, когда слева есть значение:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` вызывает функцию, только если она существует, что удобно для опциональных колбэков:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
В любой форме проверка применяется к значению **непосредственно перед** `?.`: `post?.tags?.[0]` безопасно, даже когда сам `post` равен `null` или `undefined`.

---

Когда вы знаете, что значение может отсутствовать, обычно вы хотите подставить на его место **значение по умолчанию**. Это делают два оператора, и они различаются в том, что считают «отсутствующим».
`a || b` возвращает `b` всякий раз, когда `a` **falsy**: не только `null` и `undefined`, но и `0`, `""`, `false` и `NaN`.
Оператор **нулевого слияния** `a ?? b` возвращает `b`, только когда `a` равно `null` или `undefined`, и сохраняет любое другое значение:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Используйте `??`, когда `0`, `""` или `false` — легитимные значения, которые нужно сохранить, и `||`, когда вы действительно хотите заменить каждое falsy-значение.

---

Очень распространённый шаблон — «заполнить это свойство, только если оно ещё не задано». Записанный с `??`, он повторяет имя:
```javascript
options.timeout = options.timeout ?? 1000;
```
Оператор **нулевого присваивания** `??=` делает то же самое за один шаг: он присваивает правую часть, только когда левая часть сейчас `null` или `undefined`, и не трогает любое другое значение:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` остаётся `0`, потому что `0` — не nullish; `timeout` не существовало, поэтому оно получает `1000`. Та же идея существует для `||` в виде `||=`, который перезаписывает каждое falsy-значение.

---

**Параметр по умолчанию** даёт параметру значение, когда вызывающий его не предоставляет. Правило точное: значение по умолчанию используется только тогда, когда аргумент равен `undefined`, что включает и его пропуск. Передача `null` **не** запускает значение по умолчанию, потому что `null` — это значение:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Параметры по умолчанию следуют правилу `undefined`, тогда как `??` покрывает и `null`, и `undefined`: выбирайте то, что соответствует тому, как ваша функция будет вызываться.

---

Опциональная цепочка и проверка `== null` хорошо работают вместе: цепочка читает вложенное значение без выбрасывания ошибки, а проверка решает, что делать, когда результат отсутствует:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Внутри последнего `return` обычная точка `.` безопасна, потому что проверка уже доказала, что каждое звено существует.

---

Многие встроенные методы сообщают «ничего не найдено», возвращая `undefined`. Метод массивов `find(callback)` — типичный пример: он возвращает первый элемент, для которого колбэк равен `true`, или `undefined`, когда ни один элемент не подходит:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Чтение `found.price` здесь выбросило бы ошибку, поэтому `?.` и `??` — естественные спутники `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` и `undefined` ведут себя по-разному, когда объект преобразуется в JSON с помощью `JSON.stringify()`.
В JSON есть значение `null`, но нет `undefined`, поэтому свойство со значением `undefined` просто **пропускается**, а свойство `null` сохраняется:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Внутри массивов позиции не могут исчезнуть, поэтому там `undefined` становится `null`:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Проверка `obj.key === undefined` не может различить две ситуации: свойство не существует, или оно существует и содержит значение `undefined`.
`Object.hasOwn(obj, key)` отвечает только на первый вопрос: он возвращает `true`, когда у объекта есть **собственное** свойство с именем `key`, каковым бы ни было его значение:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
«Собственное» означает объявленное на самом объекте: унаследованные члены, такие как `toString`, доступны у каждого объекта, но `Object.hasOwn(config, "toString")` даёт `false`.
