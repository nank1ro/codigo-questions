---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

全字母句是指至少使用一次英文字母表中每个字母的句子。最著名的例子是 "the quick brown fox jumps over the lazy dog"，它把全部 26 个字母装进了九个短单词里。

检查不区分大小写，因此 `A` 和 `a` 算作同一个字母。数字、标点和空格会被忽略：它们不是字母，但也不构成拒绝一个句子的理由。

# --instructions--

编写一个函数 `isPangram`，它接收一个句子，如果该句子是全字母句则返回 `true`，否则返回 `false`。

示例：
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 空句子不是全字母句。
- 只有从 `a` 到 `z` 的 26 个字母才算数。

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

空句子不是全字母句

```javascript
tryCatch(isPangram("") === false);
```

经典句子 "the quick brown fox jumps over the lazy dog" 是全字母句

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

缺少字母 `x` 的句子不是全字母句

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

句子 "the five boxing wizards jump quickly" 是全字母句

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

下划线会被忽略，所以这个句子仍然是全字母句

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

数字会被忽略，所以这个句子仍然是全字母句

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

数字不能代替字母 `e`、`i` 和 `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

全大写的句子也是全字母句

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

混合字母表同一半部分的大小写还不够

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
