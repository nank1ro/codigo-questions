**문자열**은 `"hello"`나 `'hello'`처럼 따옴표로 감싼 문자의 나열입니다.
모든 문자열에는 포함된 문자 수를 알려주는 `length` 속성이 있습니다:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
공백과 문장 부호도 문자로 계산됩니다.

---

문자열의 각 문자에는 `0`부터 시작하는 **인덱스**가 있습니다.
대괄호나 `charAt()` 메서드로 문자 하나를 읽을 수 있습니다:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
마지막 문자는 인덱스 `length - 1`에 있습니다:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

문자열에는 다양한 내장 **메서드**가 있습니다. 그중 가장 간단한 두 가지는 모든 글자의 대소문자를 바꿉니다:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
```
두 메서드 모두 인자를 받지 않으므로 괄호를 잊지 마세요.

---

문자열이 다른 문자열을 포함하는지 확인하려면 다음 메서드를 사용하세요. 모두 불리언 값을 반환합니다:
- `includes(text)`는 `text`가 어디든 나타나면 `true`
- `startsWith(text)`는 문자열이 `text`로 시작하면 `true`
- `endsWith(text)`는 문자열이 `text`로 끝나면 `true`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
비교는 대소문자를 구분합니다: `"Hello".includes("h")`는 `false`입니다.

---

`indexOf()` 메서드는 지정한 텍스트가 문자열에서 **처음** 나타나는 인덱스를 반환합니다.
텍스트를 찾을 수 없으면 `-1`을 반환합니다:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

`slice(start, end)` 메서드는 인덱스 `start`부터 인덱스 `end` 직전까지(포함하지 않음)의 문자열 조각을 추출합니다:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
```
`end`를 생략하면 문자열 끝까지 잘라냅니다.
음수 인덱스는 끝에서부터 셉니다: `word.slice(-3)`은 `"ipt"`입니다.
`substring(start, end)` 메서드도 동일하게 동작하지만 음수 인덱스는 받지 않습니다.

---

`indexOf()`와 `slice()`는 함께 잘 작동합니다. 무언가의 위치를 찾은 다음, 그 지점에서 문자열을 자르는 것입니다.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// prints 45
```
