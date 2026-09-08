**Set** — это коллекция **уникальных** значений: каждое значение может встречаться не более одного раза, и не существует индекса, по которому можно было бы получить значение по позиции.
Sets идеальны, когда вас интересует только то, *какие* значения присутствуют, а не сколько раз или в каком порядке.
Вы создаёте пустой set с помощью `new Set()`, добавляете значение с помощью `add(value)` и проверяете, присутствует ли значение, с помощью `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

Добавление значения, которое уже есть в set, **ничего** не делает: дубликаты просто игнорируются.
Ещё два важных момента:
- `delete(value)` удаляет значение из set
- `size` — это количество хранимых значений (свойство, поэтому без скобок)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` возвращает сам set, поэтому несколько вызовов можно объединять в цепочку:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Независимо от того, используете вы цепочку вызовов или нет, значение, которое уже присутствует, никогда не добавляется во второй раз, поэтому `size` считает каждое отдельное значение только один раз.

---

Вы можете построить set сразу, передав массив в `new Set()`. Дубликаты в массиве отбрасываются, поэтому это самый быстрый способ найти отличающиеся значения массива:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
Оператор **расширения** `...` работает в обратную сторону и превращает set обратно в массив:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` делает то же самое.

---

Set запоминает порядок, в котором были добавлены значения, и вы можете перебрать его с помощью `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
У sets также есть метод `forEach()`, который вызывает функцию для каждого значения:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
