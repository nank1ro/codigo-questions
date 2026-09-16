---
language: javascript
exerciseType: 1
difficulty: 2
title: アナグラム
---

# --description--

アナグラムとは、一方の単語を並べ替えるともう一方になるような2つの単語のことです。使っている文字がまったく同じで、どの文字も同じ回数だけ現れ、順序だけが異なります。`listen` と `silent` はアナグラムであり、`stone` と `tones` もアナグラムです。

単語がそれ自身のアナグラムになることはありません。2つの単語がまったく同じであれば、何も並べ替えられていないため、答えは `false` です。両方の単語は小文字で与えられ、`a` から `z` の文字だけを含みます。

# --instructions--

2つの単語 `first` と `second` を受け取り、互いにアナグラムであれば `true` を、そうでなければ `false` を返す関数 `isAnagram` を書いてください。

例:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- まったく同じ単語どうしはアナグラムではありません。
- 長さが異なる単語がアナグラムになることはありません。
- すべての文字は、両方の単語で同じ回数だけ現れなければなりません。

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

単語 "listen" と "silent" はアナグラムである

```javascript
tryCatch(isAnagram("listen", "silent") === true);
```

単語 "stone" と "tones" はアナグラムである

```javascript
tryCatch(isAnagram("stone", "tones") === true);
```

単語はそれ自身のアナグラムではない

```javascript
tryCatch(isAnagram("stone", "stone") === false);
```

長さが異なる単語はアナグラムではない

```javascript
tryCatch(isAnagram("abc", "abcd") === false);
```

同じ文字でも出現回数が異なればアナグラムではない

```javascript
tryCatch(isAnagram("aab", "abb") === false);
```

単語 "anagram" と "nagaram" はアナグラムである

```javascript
tryCatch(isAnagram("anagram", "nagaram") === true);
```

同じ長さでも文字が異なる2つの単語はアナグラムではない

```javascript
tryCatch(isAnagram("rat", "car") === false);
```

2つの空の単語は同一であるため、アナグラムではない

```javascript
tryCatch(isAnagram("", "") === false);
```

異なる1文字どうしはアナグラムではない

```javascript
tryCatch(isAnagram("a", "b") === false);
```

単語 "evil" と "vile" はアナグラムである

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
