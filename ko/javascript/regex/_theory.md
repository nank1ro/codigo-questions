**정규 표현식**(또는 **정규식**, regex)은 텍스트의 모양을 기술하는 작은 패턴입니다. "이 문자열에 숫자가 들어 있을까?"나 "단어 `cat`은 어디에 나타날까?" 같은 질문에 답할 때 사용합니다.

JavaScript에서 가장 짧게 쓰는 방법은 **정규식 리터럴**, 즉 두 슬래시 사이에 패턴을 넣는 것입니다.
```javascript
const pattern = /cat/;
```
패턴의 일반 문자는 자기 자신과 일치하므로, `/cat/`은 문자열 어디에서든 `c`, `a`, `t` 세 글자와 일치합니다.

패턴으로 할 수 있는 가장 간단한 일은 문자열에 나타나는지 묻는 것입니다. **`test`** 메서드는 텍스트를 받아 `true` 또는 `false`를 반환합니다:
```javascript
console.log(/cat/.test("the cat sleeps"));
// true 출력
console.log(/cat/.test("the dog sleeps"));
// false 출력
```
`test`는 문자열 *어딘가에서* 패턴을 찾는다는 점에 유의하세요. 문자열 전체가 일치할 필요는 없습니다.

---

패턴은 정확히 한 문자 대신 문자의 *종류*를 기술할 때 유용해집니다. 몇 가지 **이스케이프 시퀀스**가 대부분의 필요를 해결해 줍니다:
- `\d` 임의의 숫자, `0`부터 `9`까지
- `\w` 임의의 단어 문자: 문자, 숫자 또는 `_`
- `\s` 임의의 공백 문자: 스페이스, 탭, 줄바꿈

```javascript
console.log(/\d/.test("room 12"));
// true 출력
console.log(/\d/.test("lobby"));
// false 출력
```
**수량자**는 앞 조각이 몇 번 반복될 수 있는지를 나타냅니다. 가장 흔한 것은 "하나 이상"을 뜻하는 `+`입니다:
```javascript
console.log(/\d+/.test("42"));
// true 출력
```
즉 `/\d/`는 숫자 하나와 일치하고 `/\d+/`는 숫자의 연속과 일치합니다. 단순한 `test`에서는 둘이 같게 동작하는데, 둘 다 숫자 하나만 있으면 되기 때문입니다.

---

`/\d+/` 같은 리터럴은 한 번 쓰면 고정됩니다. 패턴을 **실행 시점에 만들어야** 한다면 패턴을 문자열로 받는 **`RegExp` 생성자**를 사용하세요:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// true 출력
```
함정이 하나 있습니다. 문자열 안에서 백슬래시는 *문자열*의 이스케이프 시퀀스를 시작하므로, 정규식이 보기도 전에 사라집니다. 패턴에 진짜 백슬래시를 넣으려면 두 번 써야 합니다:
```javascript
const digits = new RegExp("\\d+");
// /\d+/와 동일한 패턴
```
대신 `new RegExp("\d+")`라고 쓰면 패턴 `/d+/`가 되는데, 이것은 숫자가 아니라 문자 `d`와 일치합니다.

코드를 쓰는 시점에 패턴을 알고 있다면 리터럴을 선호하세요. 더 짧고 백슬래시를 두 배로 쓸 필요도 없기 때문입니다.

---

구성 요소 두 가지를 더 알면 거의 모든 모양의 텍스트를 기술할 수 있습니다.

**문자 클래스**는 대괄호 사이에 놓인 문자들의 집합이며, 그중 정확히 하나와 일치합니다. 대시는 범위를 쓰고, 맨 앞의 `^`는 집합을 부정합니다:
```javascript
/[aeiou]/   // 모음 하나
/[a-z]/     // 소문자 하나
/[A-Z0-9]/  // 대문자 하나 또는 숫자 하나
/[^0-9]/    // 숫자가 아닌 문자 하나
```
**수량자**는 앞 조각이 몇 번 반복되는지를 나타냅니다: `+`는 하나 이상, `*`는 0개 이상, `?`는 0개 또는 1개, `{n}`은 정확히 `n`번입니다.

마지막으로 **앵커**는 패턴을 텍스트의 끝에 묶습니다: `^`는 "여기서 시작"을, `$`는 "여기서 끝"을 뜻합니다. 앵커가 없으면 패턴은 문자열 안 어디에서든 일치할 수 있으므로 `/\d{2}/.test("abc12def")`는 `true`입니다. 앵커가 양쪽에 있으면 문자열 전체가 일치해야 합니다:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// false 출력
console.log(/^\d{2}$/.test("12"));
// true 출력
```

---

`test`는 맞는지 아닌지만 알려줍니다. 일치한 텍스트 그 자체를 얻으려면 문자열에 대해 **`match`**를 호출하세요:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
아무것도 일치하지 않으면 `match`는 `null`을 반환합니다. 일치하는 것이 있으면 배열과 비슷한 결과를 반환합니다:
- `match[0]`은 일치한 텍스트입니다
- `match.index`는 일치가 시작되는 위치입니다
- `match.input`은 검색한 전체 문자열입니다

```javascript
console.log(match[0]);
// 42 출력
console.log(match.index);
// 6 출력
```
결과가 `null`일 수 있으므로 `match[0]`을 읽기 전에 확인하세요.

---

패턴이 없을 때 `match`는 `null`을 반환하므로, `match[0]`을 바로 읽으면 `TypeError: Cannot read properties of null`이 발생합니다. 방어 코드를 두세요:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
널 병합 연산자는 같은 방어 코드를 한 줄로 씁니다. `match`가 `null`일 때 `match?.[0]`은 `undefined`이기 때문입니다:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

패턴의 일부를 괄호로 감싸면 **캡처 그룹**이 만들어집니다: 그 부분이 일치시킨 텍스트는 따로 보관되므로 다시 읽을 수 있습니다.

그룹은 `match[0]` 다음에 나타나며, 여는 괄호를 기준으로 왼쪽에서 오른쪽으로 번호가 매겨집니다:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// 2026-09-12 출력
console.log(match[1]);
// 2026 출력
console.log(match[3]);
// 12 출력
```
즉 `match[0]`은 항상 전체 일치이고, `match[1]`, `match[2]`, ...은 그룹입니다. 전혀 일치하지 않는 패턴 부분에 속한 그룹은 `match` 전체가 `null`을 반환하게 만듭니다.

---

필요한 것만 캡처하세요. 그룹은 조각을 다시 읽는 방법일 뿐만 아니라, 패턴의 어느 부분이 중요한지 읽는 이에게 알려 줍니다. 분만 원하는 시각 패턴에서는 분만 그룹으로 감싸고 나머지는 그룹 없이 두세요:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// 35 출력
```
패턴 전체는 여전히 일치해야 하므로 시와 초도 여전히 필요합니다. 단지 캡처되지 않을 뿐입니다. 그룹이 적으면 `match[1]`, `match[2]` 등을 읽을 때 짚어 둘 번호도 적어집니다.

---

괄호를 세는 일은 지치는 일이고, 패턴 중간에 그룹을 추가하면 그 뒤의 모든 번호가 다시 매겨집니다. **이름 있는 그룹**은 두 문제를 모두 피합니다: 여는 괄호 바로 뒤에 `?<name>`을 쓰고 그 조각을 `match.groups`에서 읽으세요:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// 2026 출력
console.log(match.groups.month);
// 09 출력
```
이름 있는 그룹도 여전히 번호를 가지므로 `match[1]`은 계속 동작하지만, `match.groups.year`는 그 값이 무엇을 뜻하는지 알려 줍니다. 패턴에 이름 있는 그룹이 전혀 없으면 `match.groups`는 `undefined`입니다.

---

지금까지 본 것은 모두 첫 번째 일치에서 멈췄습니다. 리터럴의 닫는 슬래시 뒤에 쓰는 **플래그**는 이 동작과 검색의 다른 세부 사항을 바꿉니다:
- `g` global: 첫 번째뿐만 아니라 모든 일치를 찾습니다
- `i` 대소문자를 무시합니다. 따라서 `/cat/i`는 `Cat`과 `CAT`도 일치시킵니다

`g` 플래그와 함께 쓰면 `match`는 다르게 동작합니다: `index`도 그룹도 없이 일치한 **문자열**들만 담은 평범한 배열을 반환하고, 일치가 없으면 `null`을 반환합니다:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// [ '1', '22', '333' ] 출력
console.log(numbers.length);
// 3 출력
```
플래그는 `/cat/gi`처럼 어떤 순서로든 조합할 수 있습니다. `RegExp` 생성자에서는 두 번째 인자로 씁니다: `new RegExp("\\d+", "g")`.

---

`g` 플래그는 일치한 모든 문자열을 주지만 그룹은 버립니다. *모든* 일치의 그룹이 필요할 때는 **`matchAll`**을 사용하세요. 이것은 완전한 일치 객체들의 이터레이터를 반환하며, 각 객체는 평범한 `match`의 결과와 정확히 같습니다:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// a -> 1 출력
// b -> 2 출력
```
`matchAll`에는 `g` 플래그가 필요하고, 없으면 `TypeError`가 발생합니다. 이터레이터를 반환하므로 진짜 배열이 필요할 때는 `[...text.matchAll(pattern)]`으로 펼치고, 패턴이 한 번도 일치하지 않으면 아무것도 내놓지 않는다는 점에 유의하세요.

---

**`replace`**는 일치한 부분을 다른 것으로 바꾼 새 문자열을 반환합니다. 원본 문자열은 절대 바뀌지 않습니다.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// the dog sleeps 출력
```
치환 문자열 안에서는 몇 가지 시퀀스가 특별한 의미를 가집니다:
- `$1`, `$2`, ... 그룹 1, 그룹 2, ...가 캡처한 텍스트
- `$<name>` 이름 있는 그룹이 캡처한 텍스트
- `$&` 전체 일치

이것이 `replace`를 단순한 맞바꾸기가 아니라 재작성 도구로 만듭니다:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// 12/09/2026 출력
```
`g` 플래그가 없으면 **첫 번째** 일치만 바뀝니다.

---

첫 번째 대신 **모든** 일치를 바꾸려면 방법이 두 가지 있습니다:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// a# b# 출력
console.log("a1 b2".replaceAll(/\d/g, "#"));
// a# b# 출력
```
**`replaceAll`**은 둘 중 더 명확하고, 패턴으로 평범한 문자열도 받습니다. 정규식을 넘길 때는 그 정규식이 `g` 플래그를 **반드시** 가져야 하며, 그렇지 않으면 `TypeError`가 발생합니다. `replace`를 써서 첫 번째 일치만 고치는 소리 없는 버그를 막아 주는 것이 바로 이 장치입니다.

---

치환은 문자열일 필요가 없습니다. **함수**를 넘기면 일치마다 한 번씩 호출되고, 그것이 반환하는 것은 무엇이든 그 일치 자리에 삽입됩니다.

함수는 전체 일치를 먼저 받고, 그다음 각 캡처 그룹을 받습니다:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// 5 5 출력

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// Ann Lee 출력
```
이것이 일치한 텍스트로부터 치환을 계산하는 유일한 방법이며, `$1`만으로는 할 수 없는 일입니다.

---

**`split`**은 문자열을 배열로 자릅니다. 평범한 문자열을 주면 그 텍스트와 정확히 일치하는 지점에서 자르지만, 정규식을 주면 패턴과 일치하는 모든 지점에서 자르므로 호출 한 번으로 제각각인 구분자를 처리할 수 있습니다:
```javascript
console.log("a, b;c".split(", "));
// [ 'a', 'b;c' ] 출력
console.log("a, b;c".split(/[,;]\s*/));
// [ 'a', 'b', 'c' ] 출력
```
구분자 자체는 결과에 포함되지 않습니다. 문자열의 시작이나 끝에 있는 구분자는 주의하세요: 그쪽에는 빈 필드가 있으므로 배열에 빈 문자열이 생깁니다.

---

마지막 플래그 하나로 세트가 완성됩니다. 기본적으로 `^`와 `$`는 **문자열 전체**의 시작과 끝을 뜻하므로, `^`로 앵커된 패턴은 텍스트가 여러 줄이더라도 맨 앞에서만 일치할 수 있습니다.

**`m`**(multiline) 플래그가 이것을 바꿉니다: `^`와 `$`는 이제 모든 줄바꿈 바로 뒤와 바로 앞에서도 일치하므로 각 줄이 저마다 앵커됩니다:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// [ 'note a' ] 출력
console.log(text.match(/^note.*/gm));
// [ 'note a', 'note c' ] 출력
```
여기서 두 가지 세부 사항이 중요합니다. 기본적으로 `.`는 줄바꿈과 일치하지 않으므로(오직 `s` 플래그만 이것을 바꿉니다) `.*`는 저절로 줄 끝에서 멈춥니다. 그리고 `g` 플래그와 함께 쓴 `match`는 아무것도 일치하지 않을 때 빈 배열이 아니라 `null`을 반환하므로, 배열을 반환하겠다고 약속했다면 `?? []`와 짝지으세요.
