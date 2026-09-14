---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

A pangram is a sentence that uses every letter of the English alphabet at least once. The best known example is "the quick brown fox jumps over the lazy dog", which fits all 26 letters into nine short words.

The check is case-insensitive, so `A` and `a` count as the same letter. Digits, punctuation and spaces are ignored: they are not letters, but they are not a reason to reject a sentence either.

# --instructions--

Write a function `isPangram` that takes a sentence and returns `true` if the sentence is a pangram and `false` otherwise.

Examples:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- An empty sentence is not a pangram.
- Only the 26 letters from `a` to `z` count.

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
function isPangram(sentence) {
  
}
```

# --asserts--

An empty sentence is not a pangram

```javascript
tryCatch(isPangram("") === false);
```

The classic sentence "the quick brown fox jumps over the lazy dog" is a pangram

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

A sentence missing the letter `x` is not a pangram

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

The sentence "the five boxing wizards jump quickly" is a pangram

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

Underscores are ignored, so the sentence is still a pangram

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

Digits are ignored, so the sentence is still a pangram

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

Digits do not replace the letters `e`, `i` and `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

An uppercase sentence is a pangram too

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

Mixing the cases of the same half of the alphabet is not enough

```javascript
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isPangram(sentence) {
  const letters = new Set();

  for (const char of sentence.toLowerCase()) {
    if (char >= "a" && char <= "z") {
      letters.add(char);
    }
  }

  return letters.size === 26;
}
```
