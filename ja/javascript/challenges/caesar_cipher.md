---
language: javascript
exerciseType: 1
difficulty: 2
title: シーザー暗号
---

# --description--

ユリウス・カエサルは、暗号術の中でも最も古い手法の1つを使って、自分の私的な手紙を守っていました。その手法とは、メッセージのすべての文字を、アルファベットに沿って固定された数だけ先にある文字に置き換えるというものです。シフトが3の場合、`a`は`d`に、`b`は`e`に、`c`は`f`になります。

アルファベットは円のように振る舞うため、終わりの文字は先頭へ折り返します。シフトが3の場合、`x`は`a`に、`y`は`b`に、`z`は`c`になります。

スペース、カンマ、感嘆符、数字など、英字以外のものはすべて、暗号を通しても変更されずにそのまま通過します。

# --instructions--

メッセージ`text`と整数`shift`を受け取り、エンコードされたメッセージを返す関数`caesarCipher`を書いてください。

例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- メッセージは常に小文字なので、大文字を扱う必要はありません。
- 英字以外の文字は、その位置と値を保ちます。
- シフトが負になることはありません。シフト`0`ではメッセージはそのままになり、シフト`26`でも同じです。

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
function caesarCipher(text, shift) {
  
}
```

# --asserts--

シフト3で"hello"は"khoor"になります。

```javascript
tryCatch(caesarCipher("hello", 3) === "khoor");
```

アルファベットの終わりが折り返されるため、"xyz"は"abc"になります。

```javascript
tryCatch(caesarCipher("xyz", 3) === "abc");
```

シフト0ではメッセージは変わりません。

```javascript
tryCatch(caesarCipher("abc", 0) === "abc");
```

シフト26はアルファベットのちょうど1周なので、メッセージは変わりません。

```javascript
tryCatch(caesarCipher("abc", 26) === "abc");
```

句読点とスペースは変更されずに通過します。

```javascript
tryCatch(caesarCipher("codigo, rocks!", 5) === "htinlt, wthpx!");
```

空のメッセージは空のままです。

```javascript
tryCatch(caesarCipher("", 4) === "");
```

文字と文字の間のスペースはそのまま保持されます。

```javascript
tryCatch(caesarCipher("a b c", 1) === "b c d");
```

数字は、シフト25であっても置き換えられません。

```javascript
tryCatch(caesarCipher("abc 123!", 25) === "zab 123!");
```

シフト13で文全体がエンコードされます。

```javascript
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) === "gur dhvpx oebja sbk whzcf bire gur ynml qbt");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function caesarCipher(text, shift) {
  const a = "a".charCodeAt(0);
  let result = "";

  for (const char of text) {
    const code = char.charCodeAt(0);
    if (char >= "a" && char <= "z") {
      result += String.fromCharCode(a + ((code - a + shift) % 26));
    } else {
      result += char;
    }
  }

  return result;
}
```
