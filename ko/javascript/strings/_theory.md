**문자열**은 `"hello"`나 `'hello'`처럼 따옴표로 감싼 문자의 나열입니다.
모든 문자열에는 포함된 문자 수를 알려주는 `length` 속성이 있습니다:
```javascript
let greeting = "hello";
console.log(greeting.length);
// 5 출력
```
공백과 문장 부호도 문자로 계산됩니다.

---

문자열의 각 문자에는 `0`부터 시작하는 **인덱스**가 있습니다.
대괄호나 `charAt()` 메서드로 문자 하나를 읽을 수 있습니다:
```javascript
let word = "hello";
console.log(word[0]);
// h 출력
console.log(word.charAt(1));
// e 출력
```
마지막 문자는 인덱스 `length - 1`에 있습니다:
```javascript
console.log(word[word.length - 1]);
// o 출력
```

---

문자열에는 다양한 내장 **메서드**가 있습니다. 그중 가장 간단한 두 가지는 모든 글자의 대소문자를 바꿉니다:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// HELLO 출력
console.log(word.toLowerCase());
// hello 출력
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
// true 출력
console.log(file.startsWith("ph"));
// true 출력
console.log(file.endsWith(".jpg"));
// false 출력
```
비교는 대소문자를 구분합니다: `"Hello".includes("h")`는 `false`입니다.

---

`indexOf()` 메서드는 지정한 텍스트가 문자열에서 **처음** 나타나는 인덱스를 반환합니다.
텍스트를 찾을 수 없으면 `-1`을 반환합니다:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// 2 출력
console.log(word.indexOf("z"));
// -1 출력
```

---

`slice(start, end)` 메서드는 인덱스 `start`부터 인덱스 `end` 직전까지(포함하지 않음)의 문자열 조각을 추출합니다:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// Java 출력
console.log(word.slice(4));
// Script 출력
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
// 45 출력
```

---

`split(separator)` 메서드는 `separator`가 나타날 때마다 잘라서 문자열을 조각들의 **배열**로 나눕니다:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// [ 'I', 'like', 'JavaScript' ] 출력
```
그 반대는 배열 메서드 `join(separator)`로, 조각들을 다시 하나의 문자열로 이어붙입니다:
```javascript
console.log(words.join("-"));
// I-like-JavaScript 출력
```

---

사용자 입력에는 앞뒤로 불필요한 공백이 들어있는 경우가 많습니다. `trim()` 메서드는 문자열의 **양쪽** 끝에서 공백을 제거한 사본을 반환합니다:
```javascript
let input = "   hello   ";
console.log(input.trim());
// hello 출력
```
`trimStart()`는 앞쪽 공백만, `trimEnd()`는 뒤쪽 공백만 제거합니다.
문자열 중간에 있는 공백은 절대 건드리지 않습니다.

---

`replace(search, replacement)` 메서드는 `search`가 **처음** 나타난 부분을 `replacement`로 바꾼 새 문자열을 반환합니다:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// blue red 출력
```
**모든** 부분을 바꾸려면 `replaceAll()`을 사용하세요:
```javascript
console.log(text.replaceAll("red", "blue"));
// blue blue 출력
```

---

`repeat(count)` 메서드는 문자열을 `count`번 반복한 결과를 반환합니다:
```javascript
console.log("ab".repeat(3));
// ababab 출력
console.log("ab".repeat(0));
// 빈 문자열 출력
```

---

`padStart(targetLength, padString)` 메서드는 문자열이 `targetLength` 길이에 도달할 때까지 **앞쪽**에 `padString`을 추가합니다. `padEnd()`는 뒤쪽에 대해 같은 일을 합니다:
```javascript
console.log("7".padStart(3, "0"));
// 007 출력
console.log("Tea".padEnd(6, "."));
// Tea... 출력
```
문자열이 이미 충분히 길면 변경 없이 그대로 반환됩니다.
숫자에는 문자열 메서드가 없으므로 먼저 `String(number)`로 변환하세요.

---

두 문자열은 정확히 같은 문자가 같은 대소문자로 이루어져 있을 때만 `===`로 같습니다:
```javascript
console.log("hello" === "hello");
// true 출력
console.log("hello" === "Hello");
// false 출력
```
`<`와 `>` 연산자는 문자열을 한 글자씩 알파벳 순서로 비교합니다.
대문자가 소문자보다 앞에 오므로 `"Zoo" < "apple"`은 `true`입니다.

---

문자열은 **불변**입니다: 한 번 만들어진 문자열은 절대 변경할 수 없습니다.
인덱스에 값을 대입해도 아무 일도 일어나지 않으며, 모든 문자열 메서드는 원본을 수정하는 대신 **새로운** 문자열을 반환합니다:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// hello 출력
word.toUpperCase();
console.log(word);
// hello 출력
```
결과를 유지하려면 변수에 다시 대입하세요:
```javascript
word = word.toUpperCase();
```

---

빈 구분자로 `split("")`을 호출하면 문자열이 한 글자씩 담긴 배열이 됩니다.
배열에는 `reverse()` 메서드가 있으므로, 나누고 뒤집고 다시 합쳐서 문자열을 뒤집을 수 있습니다:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// cba 출력
```
