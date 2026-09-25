---
language: javascript
exerciseType: 1
difficulty: 3
title: Сбалансированные скобки
---

# --description--

Текст, в котором есть код, математика или разметка, полон скобок, и каждой открывающей скобке нужна закрывающая того же вида. Строка сбалансирована, когда её скобки образуют пары и вкладываются друг в друга, как слои луковицы: `{[()]}` сбалансирована, а `{[(])}` — нет, ведь круглая пара закрывается раньше квадратной пары, внутри которой она находится.

Здесь учитываются три пары: круглые `()`, квадратные `[]` и фигурные `{}`. Все остальные символы строки игнорируются. Закрывающая скобка должна закрывать последнюю из ещё открытых скобок, а к концу строки не должно остаться ни одной незакрытой скобки.

# --instructions--

Напишите функцию `isBalanced`, которая принимает строку и возвращает `true`, если все скобки в ней образуют пары и правильно вложены, и `false` в противном случае.

Примеры:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Пустая строка сбалансирована.
- Символы, не являющиеся скобками, игнорируются.
- Закрывающая скобка должна соответствовать последней из ещё открытых скобок.
- К концу строки не должно оставаться ни одной открытой скобки.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function isBalanced(text) {
  
}
```

# --asserts--

Пустая строка сбалансирована

```javascript
tryCatch(isBalanced("") === true);
```

Одна пара круглых скобок сбалансирована

```javascript
tryCatch(isBalanced("()") === true);
```

Три вида пар, вложенные друг в друга, сбалансированы

```javascript
tryCatch(isBalanced("{[()]}") === true);
```

Скобки вперемешку с другим текстом остаются сбалансированными

```javascript
tryCatch(isBalanced("{what is (42)}[?]") === true);
```

Пары, стоящие друг за другом, сбалансированы

```javascript
tryCatch(isBalanced("()[]{}") === true);
```

Строка вовсе без скобок сбалансирована

```javascript
tryCatch(isBalanced("no brackets in here at all") === true);
```

Перекрёстная пара не сбалансирована

```javascript
tryCatch(isBalanced("{[(])}") === false);
```

Открывающая скобка, которая никогда не закрывается, не сбалансирована

```javascript
tryCatch(isBalanced("(") === false);
```

Закрывающая скобка раньше любой открывающей не сбалансирована

```javascript
tryCatch(isBalanced(")(") === false);
```

Перекрёстные пары в глубине строки не сбалансированы

```javascript
tryCatch(isBalanced("(([]{[}]))") === false);
```

Лишняя закрывающая скобка в конце строки не сбалансирована

```javascript
tryCatch(isBalanced("())") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isBalanced(text) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const char of text) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char in pairs) {
      if (stack.pop() !== pairs[char]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
```
