**주석**은 소스 코드 안에 코드를 읽는 사람을 위해 적어 두는 메모입니다. JavaScript는 주석을 완전히 무시하므로, 주석이 프로그램의 동작을 바꾸는 일은 없습니다.

가장 단순한 주석은 **한 줄 주석**입니다. `//`로 시작해서 그 줄의 끝까지 이어집니다.
```javascript
// Greets the user
console.log("Hello");
```
주석은 어떤 코드가 무엇을 위한 것인지, 또는 왜 그렇게 작성되었는지를 설명할 때 사용하세요. 다른 일부 언어와 달리 JavaScript에서 `#`는 주석을 시작하지 **않는다**는 점에 유의하세요.

---

주석이 반드시 자기만의 줄을 차지할 필요는 없습니다. 같은 줄에서 코드 뒤에 올 수도 있습니다. 이것이 **인라인 주석**(또는 후행 주석)이며, 그 문장에 대한 짧은 메모를 적기에 좋은 자리입니다:
```javascript
const retries = 3; // give up after three attempts
```
`//`부터 줄 끝까지는 모두 무시되고, 그 앞의 코드는 평소처럼 실행됩니다.

---

주석은 무시되기 때문에, 주석을 추가하거나 지워도 프로그램의 동작은 절대 달라지지 않습니다. 주석 처리되지 **않은** 코드만 실행됩니다.

덕분에 `//`는 코드를 지우지 않고 한 줄을 꺼 두는 빠른 방법이 됩니다. 이것을 **주석 처리**라고 부릅니다:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
두 번째 줄은 이제 주석이므로 `total`은 `10`으로 남습니다. `//`를 없애면 그 줄이 다시 살아납니다.

주석 처리는 실험하는 동안에는 편리하지만 정리하는 것을 잊지 마세요. 오래 주석 처리된 채로 남은 코드는 다음에 읽는 사람을 혼란스럽게 할 뿐입니다.

---

주석에 한 줄보다 더 많은 공간이 필요할 때 JavaScript는 **여러 줄 주석**(블록 주석이라고도 함)을 제공합니다. `/*`로 시작해 `*/`로 끝나며, 그 사이의 모든 것은 줄바꿈까지 포함해 무시됩니다.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
블록 주석은 짧게 한 줄에 둘 수도 있습니다: `/* like this */`.

---

어떤 종류의 주석을 쓰든 규칙은 같습니다. 그 안의 글자는 **코드가 아닙니다**. 주석 안의 `console.log`는 아무것도 출력하지 않고, 같은 줄에서 `//` 뒤에 쓴 코드는 그 줄이 진짜 코드로 시작하더라도 절대 실행되지 않습니다:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
프로그램이 무엇을 출력할지 확신이 서지 않을 때는, 먼저 머릿속에서 모든 주석을 지우고 남은 것을 읽어 보세요.

---

줄 끝에서 멈추는 `//`와 달리 `/*` 주석은 `*/`를 만나야만 끝납니다. 닫는 것을 잊으면 JavaScript는 뒤따르는 모든 코드를 주석의 일부로 취급하고 문법 오류를 보고합니다:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
`//`와 `/* */` 둘 다 인라인 주석으로 쓸 수 있지만, `/*`를 쓸 때는 항상 `*/`가 있는지 확인하세요.

---

JavaScript의 블록 주석은 **중첩할 수 없습니다**. 앞에 `/*`가 몇 개 있었든, 주석은 만나는 **첫 번째** `*/`에서 끝납니다.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
여기서 주석은 `inner` 바로 뒤에서 끝나므로 `still a comment */`는 코드로 읽혀 문법 오류를 일으킵니다. 이미 `/* */` 주석이 들어 있는 블록을 주석 처리할 때 이 점을 기억하세요. 각 줄에 `//`를 쓰거나, 안쪽 주석을 먼저 지우세요.

---

여러 줄을 한 번에 주석 처리하려면 각 줄에 `//`를 붙이는 대신 하나의 블록 주석으로 감싸세요:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
블록 안의 줄들은 무시되므로 `total`은 전혀 바뀌지 않습니다. 이 방법은 그 줄들 중 어느 것에도 `*/`가 들어 있지 않을 때만 통한다는 점을 기억하세요.

---

JavaScript에는 세 번째 종류의 주석인 **문서화 주석**이 있으며 **JSDoc** 형식으로 작성합니다. `/**`(별표 두 개)로 시작하는 블록 주석으로, 함수 바로 위에 놓입니다. 그 안의 줄은 보통 ` * `로 시작하고, `@`로 시작하는 특별한 **태그**가 함수를 설명합니다:
- 각 매개변수마다 `@param {type} name description`
- 반환값에는 `@returns {type} description`

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
JavaScript에게는 그저 주석일 뿐이지만, 편집기는 이것을 읽어 중괄호 안에 적힌 타입(`{number}`, `{string}`, `{boolean}`, `{number[]}` ...)과 함께 `greet`의 도움말로 보여 줍니다.

---

JSDoc 주석의 첫 줄은 **요약**입니다. 함수가 무엇을 하는지 알려 주는 짧은 문장으로, 함수를 설명하듯 3인칭으로 씁니다: "Returns...", "Adds...", "Checks...". 그다음 태그를 한 줄에 하나씩 나열합니다:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
주석은 선언 바로 위에, 사이에 빈 줄 없이 놓여야 합니다. 그렇지 않으면 편집기가 그 주석을 함수와 연결하지 않습니다.

---

JSDoc 주석은 **계약**이기도 합니다. 본문이 작성되기도 전에, 함수를 호출하는 쪽에 무엇을 전달해야 하고 무엇을 돌려받는지 알려 줍니다. 주석을 읽는 것만으로 함수를 구현할 수 있는 경우도 많습니다:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
각 `@param`은 같은 순서로 매개변수 하나에 대응하고, `@returns`는 가능한 모든 결과를 설명합니다.

---

JSDoc 주석 안의 순서는 언제나 같습니다. 먼저 요약, 그다음 선언된 순서대로 매개변수마다 `@param` 하나, 마지막에 `@returns`입니다. 여는 `/**`와 닫는 ` */`가 전체를 감싸고, 주석은 자신이 설명하는 함수 바로 위에 놓입니다:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

JavaScript 파일은 **셔뱅**(또는 해시뱅)이라는 특별한 줄로 시작할 수 있습니다. `#!` 뒤에 그 파일을 실행할 프로그램의 경로를 적습니다. 유닉스 계열 시스템에서는 이것 덕분에 `node`를 먼저 입력하지 않고도 `./hello.js`처럼 터미널에서 스크립트를 바로 실행할 수 있습니다:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript는 이 줄을 주석과 똑같이 무시하지만, 그것이 파일의 **맨 첫 줄**일 때만 그렇습니다. 다른 곳에서는 `#!`가 문법 오류입니다. `/usr/bin/env node`는 "이 시스템에서 `node`를 찾아 사용하라"는 뜻입니다.

---

좋은 주석은 코드가 **무엇을** 하는지가 아니라 **왜** 그렇게 하는지를 설명합니다. 무슨 일이 일어나는지는 코드가 이미 보여 주고 있습니다. 그것을 말로 되풀이하면 잡음만 늘고, 코드가 바뀌는 순간 낡은 정보가 됩니다:
```javascript
// set timeout to 30
const timeout = 30;
```
그 숫자 뒤에 있는 이유야말로 읽는 사람이 짐작할 수 없는 것입니다:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
주석이 아래 줄을 그대로 되풀이하기만 한다면, 지우거나 그 이유로 바꾸세요.

---

어떤 주석은 편집기가 이해하는 관례를 따릅니다. 가장 흔한 **표식**은 다음과 같습니다:
- `// TODO: ...` 는 아직 작성해야 할 일이 남았음을 알립니다
- `// FIXME: ...` 는 잘못되었다고 알려져 있어 고쳐야 하는 코드를 알립니다

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
JavaScript에게는 평범한 주석이지만, 편집기가 이것들을 모아 보여 주므로 남은 작업을 찾기 쉽습니다. `TODO`는 보통 진짜 구현이 작성될 때까지 코드가 돌아가게 해 주는 임시 코드 옆에 있습니다. 작업을 끝내면 같은 변경에서 임시 코드를 대체하고 표식도 지우세요. 오래된 `TODO`는 사람을 오해하게 만듭니다.

---

`FIXME`는 `TODO`와 다릅니다. 코드는 이미 존재하지만 잘못되었다고 알려져 있습니다. 좋은 `FIXME`는 버그가 무엇인지 말해 주고, 가능하다면 그것을 보여 주는 예도 덧붙여, 다음 사람이 빠르게 고칠 수 있게 합니다. `TODO`와 마찬가지로 버그를 고치면 표식은 지우되, 여전히 사실인 JSDoc 주석은 그대로 두세요.
