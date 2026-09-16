---
language: javascript
exerciseType: 1
difficulty: 2
title: 애너그램
---

# --description--

한 단어가 다른 단어의 재배열일 때 두 단어는 애너그램입니다. 즉, 정확히 같은 문자를 사용하며 각 문자가 같은 횟수로 나타나고 오직 순서만 다릅니다. `listen`과 `silent`는 애너그램이고, `stone`과 `tones`도 애너그램입니다.

단어는 결코 자기 자신의 애너그램이 아닙니다. 두 단어가 완전히 같으면 재배열된 것이 없으므로 답은 `false`입니다. 두 단어는 모두 소문자로 주어지며 `a`부터 `z`까지의 문자만을 담고 있습니다.

# --instructions--

두 단어 `first`와 `second`를 받아 두 단어가 서로의 애너그램이면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isAnagram`를 작성하세요.

예시:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- 두 단어가 완전히 같으면 애너그램이 아닙니다.
- 길이가 다른 단어는 결코 애너그램이 아닙니다.
- 모든 문자는 두 단어에서 같은 횟수로 나타나야 합니다.

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
function isAnagram(first, second) {
  
}
```

# --asserts--

단어 "listen"과 "silent"는 애너그램입니다

```javascript
tryCatch(isAnagram("listen", "silent") === true);
```

단어 "stone"과 "tones"는 애너그램입니다

```javascript
tryCatch(isAnagram("stone", "tones") === true);
```

단어는 자기 자신의 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("stone", "stone") === false);
```

길이가 다른 단어는 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("abc", "abcd") === false);
```

같은 문자라도 개수가 다르면 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("aab", "abb") === false);
```

단어 "anagram"과 "nagaram"는 애너그램입니다

```javascript
tryCatch(isAnagram("anagram", "nagaram") === true);
```

길이가 같고 문자가 다른 두 단어는 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("rat", "car") === false);
```

두 빈 단어는 동일하므로 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("", "") === false);
```

서로 다른 한 문자 두 개는 애너그램이 아닙니다

```javascript
tryCatch(isAnagram("a", "b") === false);
```

단어 "evil"과 "vile"는 애너그램입니다

```javascript
tryCatch(isAnagram("evil", "vile") === true);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isAnagram(first, second) {
  if (first === second) {
    return false;
  }

  const sortLetters = (word) => word.split("").sort().join("");

  return sortLetters(first) === sortLetters(second);
}
```
