---
language: javascript
exerciseType: 1
difficulty: 2
title: 카이사르 암호
---

# --description--

율리우스 카이사르는 암호학에서 가장 오래된 기법 중 하나로 자신의 개인 편지를 보호했습니다. 그는 메시지의 모든 글자를 알파벳에서 고정된 칸수만큼 뒤에 있는 글자로 바꿨습니다. 이동 거리가 3이면 `a`는 `d`가 되고, `b`는 `e`가 되며, `c`는 `f`가 됩니다.

알파벳은 원처럼 동작하기 때문에 끝에 있는 글자는 다시 처음으로 돌아갑니다. 이동 거리가 3이면 `x`는 `a`가 되고, `y`는 `b`가 되며, `z`는 `c`가 됩니다.

공백, 쉼표, 느낌표, 숫자처럼 글자가 아닌 것들은 이 암호를 거쳐도 그대로 남습니다.

# --instructions--

메시지 `text`와 정수 `shift`를 받아 암호화된 메시지를 반환하는 함수 `caesarCipher`를 작성하세요.

예시:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 메시지는 항상 소문자이므로 대문자를 다룰 필요는 없습니다.
- 글자가 아닌 문자는 자리와 값을 그대로 유지합니다.
- 이동 거리는 절대 음수가 아닙니다. 이동 거리가 `0`이면 메시지는 바뀌지 않으며, `26`이어도 마찬가지입니다.

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

이동 거리가 3이면 "hello"는 "khoor"가 됩니다

```javascript
tryCatch(caesarCipher("hello", 3) === "khoor");
```

알파벳의 끝은 처음으로 돌아가므로 "xyz"는 "abc"가 됩니다

```javascript
tryCatch(caesarCipher("xyz", 3) === "abc");
```

이동 거리가 0이면 메시지는 바뀌지 않습니다

```javascript
tryCatch(caesarCipher("abc", 0) === "abc");
```

이동 거리가 26이면 알파벳을 한 바퀴 도는 것이므로 메시지는 바뀌지 않습니다

```javascript
tryCatch(caesarCipher("abc", 26) === "abc");
```

문장 부호와 공백은 바뀌지 않고 그대로 통과합니다

```javascript
tryCatch(caesarCipher("codigo, rocks!", 5) === "htinlt, wthpx!");
```

빈 메시지는 빈 상태로 남습니다

```javascript
tryCatch(caesarCipher("", 4) === "");
```

글자 사이의 공백은 그대로 유지됩니다

```javascript
tryCatch(caesarCipher("a b c", 1) === "b c d");
```

이동 거리가 25여도 숫자는 이동하지 않습니다

```javascript
tryCatch(caesarCipher("abc 123!", 25) === "zab 123!");
```

이동 거리가 13이면 문장 전체가 암호화됩니다

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
