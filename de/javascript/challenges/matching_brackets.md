---
language: javascript
exerciseType: 1
difficulty: 3
title: Passende Klammern
---

# --description--

Text, der Code, Formeln oder Markup enthält, ist voller Klammern, und jede öffnende Klammer braucht eine schließende derselben Art. Ein String ist ausgeglichen, wenn sich seine Klammern paarweise entsprechen und wie die Schichten einer Zwiebel verschachteln: `{[()]}` ist ausgeglichen, `{[(])}` dagegen nicht, weil das runde Paar vor dem eckigen Paar geschlossen wird, in dem es liegt.

Hier zählen drei Paare: runde `()`, eckige `[]` und geschweifte `{}`. Jedes andere Zeichen im String wird ignoriert. Eine schließende Klammer muss die zuletzt geöffnete Klammer schließen, die noch offen ist, und wenn der String endet, darf keine Klammer offen geblieben sein.

# --instructions--

Schreiben Sie eine Funktion `isBalanced`, die einen String entgegennimmt und `true` zurückgibt, wenn alle darin enthaltenen Klammern übereinstimmen und korrekt verschachtelt sind, und andernfalls `false`.

Beispiele:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Ein leerer String ist ausgeglichen.
- Zeichen, die keine Klammern sind, werden ignoriert.
- Eine schließende Klammer muss zu der zuletzt geöffneten Klammer passen, die noch offen ist.
- Wenn der String endet, darf keine Klammer offen geblieben sein.

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

Ein leerer String ist ausgeglichen

```javascript
tryCatch(isBalanced("") === true);
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```javascript
tryCatch(isBalanced("()") === true);
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```javascript
tryCatch(isBalanced("{[()]}") === true);
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```javascript
tryCatch(isBalanced("{what is (42)}[?]") === true);
```

Nebeneinander stehende Paare sind ausgeglichen

```javascript
tryCatch(isBalanced("()[]{}") === true);
```

Ein String ohne jegliche Klammern ist ausgeglichen

```javascript
tryCatch(isBalanced("no brackets in here at all") === true);
```

Ein überkreuztes Paar ist nicht ausgeglichen

```javascript
tryCatch(isBalanced("{[(])}") === false);
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```javascript
tryCatch(isBalanced("(") === false);
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```javascript
tryCatch(isBalanced(")(") === false);
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```javascript
tryCatch(isBalanced("(([]{[}]))") === false);
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

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
