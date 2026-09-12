어떤 작업은 바로 끝나지 않습니다: 파일 다운로드, 데이터베이스 읽기, 타이머 대기 같은 일들입니다. JavaScript는 이런 작업이 실행되는 동안 멈추지 않습니다. 대신 **`Promise`**를 건네줍니다: **나중에** 사용할 수 있게 될 값을 대변하는 객체입니다.

**`async`**가 붙은 함수는 항상 프로미스를 반환합니다. 함수가 무엇을 반환하든 그것이 프로미스 안의 값이 됩니다:
```javascript
async function fetchNumber() {
  return 42;
}
```
프로미스에서 값을 꺼낼 때는 **`await`**를 사용합니다. `await`는 프로미스가 값을 가질 때까지 함수를 잠시 멈췄다가, 값이 생기면 평범한 값을 돌려줍니다. `await`는 `async` 함수 안에서만 사용할 수 있습니다:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
`await`가 없다면 `n`에는 프로미스 자체가 담기고, `console.log(n)`은 숫자 대신 `Promise { 42 }`를 출력합니다.

---

함수 앞에 `async`를 붙이면 함수가 돌려주는 것이 달라집니다: 본문은 여전히 평범한 값을 계산하지만, 호출자는 그 값을 감싼 프로미스를 받습니다.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
두 함수는 같은 코드를 담고 있습니다. 결과를 읽는 방식만 다를 뿐입니다. `shoutLater("hi")`가 `"HI"`를 돌려주게 하려면 다른 `async` 함수 안에서 await해야 합니다.

함수에 `async`를 붙이는 것은 기다릴 것이 없을 때는 아무 비용도 들지 않으며, 나중에 그 안에서 `await`를 쓸 수 있게 해주는 장치입니다.

---

값이 정말로 나중에 도착한다면, **`new Promise`**로 프로미스를 직접 만듭니다. `new Promise`는 함수 하나를 받는데, 이 함수는 **`resolve`** 콜백을 전달받습니다: 값이 준비되면 `resolve(value)`를 호출하고, 프로미스는 그 값으로 이행(fulfilled)됩니다.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)`는 `callback`이 `ms`밀리초 후에 실행되도록 예약하고 즉시 반환하므로, 그 사이에 아무것도 막히지 않습니다.

`new Promise`에 전달된 함수는 즉시 실행되지만, `resolve`가 호출되기 전까지 프로미스는 **대기(pending)** 상태로 머뭅니다. 프로미스를 await하면 값을 얻습니다:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

프로미스는 항상 세 상태 중 하나입니다:

- **대기(pending)**: 작업이 아직 진행 중입니다;
- **이행(fulfilled)**: 작업이 성공했고 프로미스가 값을 담고 있습니다;
- **거부(rejected)**: 작업이 실패했고 프로미스가 에러를 담고 있습니다.

프로미스는 대기 상태로 시작하며 상태는 최대 한 번 바뀝니다. 일단 이행되거나 거부되면 **처리(settled)**된 것이며 다시는 바뀌지 않습니다.

`async` 함수를 호출하는 것은 결코 기다리지 않습니다: 작업을 시작하고 대기 중인 프로미스를 즉시 돌려주므로, 호출 다음 줄은 작업이 끝나기 전에 실행됩니다. 이 프로미스는 평범한 객체일 뿐 그 안의 값이 아니므로, `await`를 잊어버리는 실수가 아주 흔한 것입니다.

---

`await`만이 프로미스를 읽는 유일한 방법은 아닙니다. 모든 프로미스에는 **`.then(callback)`** 메서드가 있습니다: 프로미스가 이행되는 즉시 콜백이 값을 전달받습니다.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`**는 이미 `value`로 이행된 프로미스를 만듭니다. 값은 손에 있지만 프로미스를 반환해야 할 때 유용합니다.

`.then`은 콜백이 반환하는 것으로 이행되는 **새** 프로미스를 반환하므로, 호출을 **체이닝**할 수 있습니다. 각 단계는 이전 단계의 결과를 다룹니다:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

`async` 함수는 다른 함수와 마찬가지로 위에서 아래로 읽힙니다: `await`는 대기 중인 프로미스가 이행될 때까지 함수를 잠시 멈출 뿐이고, 그다음 줄에서 실행이 계속됩니다.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
마지막 줄에 주목하세요: `async` 함수도 여전히 **호출**되어야 합니다. 괄호 없이 `main`만 쓰면 작업을 정의할 뿐 결코 시작하지 않고, 아무것도 출력되지 않습니다.

---

비동기 작업은 실패할 수도 있습니다. `new Promise`에 주어진 함수는 두 번째 콜백 **`reject`**를 전달받습니다: `reject(error)`를 호출하면 프로미스가 이행 대신 거부(rejected) 상태가 됩니다.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
항상 `Error` 객체로 거부하세요: `Error`는 `message`와 스택 트레이스를 담고 있지만, 문자열만으로는 그렇지 않습니다.

거부는 **`.catch(callback)`**으로 읽습니다. `.then`의 거울상입니다. **`Promise.reject(error)`**는 이미 거부된 프로미스를 만드는데, `Promise.resolve`가 이행된 프로미스를 만드는 것과 같습니다:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
`resolve`와 `reject`를 둘 다 호출하거나 두 번 호출해도 아무 일도 일어나지 않습니다: 첫 번째 호출만 효과가 있습니다.

---

`.then`, `.catch`, `.finally`는 같은 체인의 고리입니다. 거부는 `.catch`를 만날 때까지 모든 `.then`을 건너뜁니다. `.catch` 콜백이 값을 반환하는 순간 체인은 다시 이행되어 평소처럼 계속됩니다.

**`.finally(callback)`**은 체인이 처리될 때 실행되며, 이행되었든 거부되었든 상관없습니다. 콜백은 인자를 받지 않고 반환값은 무시되므로, 값은 계속 흘러 다음 `.then`으로 전달됩니다. 스피너를 숨기는 같은 정리 작업을 하기에 적합한 자리입니다:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

`async` 함수 안에서는 `.catch`가 필요하지 않습니다. 거부된 프로미스를 await하면 에러가 **던져지므로(throws)**, 평범한 `try` / `catch` / `finally` 문이 이를 처리합니다:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
반대 방향도 마찬가지입니다: `async` 함수 안의 `throw`는 호출자를 망가뜨리지 않고, 함수가 반환한 프로미스를 거부합니다.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
어떤 `try` 블록에서와 마찬가지로, 실패한 `await` 뒤의 줄들은 건너뛰어지고, `catch` 블록이 실행되며, `finally` 블록은 두 경우 모두에서 실행됩니다.

---

`await`를 둘러싼 `try` / `catch`의 흔한 용도는 실패를 무난한 기본값으로 바꾸는 것입니다. 그러면 호출자는 에러를 전혀 다룰 필요가 없습니다:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
값이 곧바로 반환되더라도 `measure(path)` 앞의 `await`는 그대로 두세요. `await`가 없으면 프로미스가 `try` 블록을 거치지 않고 함수를 빠져나가므로, 거부가 `catch`를 피해 빠져나가 버립니다.

---

여러 결과가 필요할 때 하나씩 차례로 await하면 시간이 낭비됩니다. 각각은 이전 것이 끝나야 시작되기 때문입니다. **`Promise.all(promises)`**은 이미 실행 중인 프로미스들의 배열을 받아, 모든 값의 배열로 이행되는 프로미스 하나를 반환합니다:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
기억할 만한 규칙 두 가지가 있습니다:

- 값은 끝난 순서가 아니라 **배열의 순서대로** 돌아옵니다;
- 프로미스 중 하나라도 거부되면 `Promise.all`이 반환한 프로미스는 그 첫 번째 에러로 즉시 거부되고, 나머지 값들은 사라집니다.

---

`Promise.all`은 빈 배열을 포함해 어떤 길이의 배열과도 동작합니다: `Promise.all([])`을 await하면 빈 배열이 곧바로 돌아옵니다. 덕분에 "기다릴 것이 없다"는 특별한 경우를 따로 두지 않고도, 실행 중에 만들어진 목록을 안전하게 넘길 수 있습니다.
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
반환되는 배열은 받은 배열과 정확히 같은 개수의 항목을 같은 위치에 담으므로, 다른 배열처럼 반복문으로 순회할 수 있습니다.

---

**순차적** 대기와 **병렬** 대기의 차이는 `await`를 *어디에* 두느냐로 결정됩니다:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
첫 번째 버전에서는 두 번째 다운로드가 첫 번째가 끝나야 시작됩니다. `await`가 그 줄에서 함수를 멈추기 때문입니다. 두 번째에서는 아무것도 await하기 전에 두 호출을 모두 하므로, `Promise.all`이 기다리는 동안 두 다운로드는 이미 실행 중입니다.

두 번째 작업이 정말로 첫 번째의 결과를 필요로 할 때만 순차적인 await를 사용하세요. 그렇지 않다면 모두 먼저 시작한 다음 함께 await하세요.

---

`Promise.all`은 프로미스 하나가 거부되는 순간 포기합니다. 그래도 모든 결과가 필요하다면 **`Promise.allSettled(promises)`**를 사용하세요: 절대 거부되지 않으며, 같은 순서대로 프로미스마다 작은 객체 하나씩으로 이행됩니다:

- 성공한 것들은 `{ status: "fulfilled", value: ... }`입니다;
- 실패한 것들은 `{ status: "rejected", reason: ... }`입니다.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
`status`가 `"fulfilled"`일 때만 `value`를, `"rejected"`일 때만 `reason`을 읽으세요: 다른 쪽 프로퍼티는 그냥 없습니다.

---

**`Promise.race(promises)`**는 프로미스 중 **가장 먼저** 처리되는 것과 함께 처리되며 그 결과를 그대로 가져옵니다: 첫 번째 값으로 이행되거나 첫 번째 에러로 거부됩니다. 나머지는 취소되지 않고 계속 실행되지만, 무엇을 만들어내든 무시됩니다.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
전형적인 용도는 마감 시간입니다: 실제 작업을 잠시 후 실패하는 프로미스와 경주시키면, 결과 또는 타임아웃 에러를 얻습니다.

빈 배열은 조심하세요: `Promise.race([])`는 처리해 줄 것이 아무것도 없으므로 영원히 대기 상태로 머뭅니다.

---

마지막 조각들을 합치면 거의 모든 실제 애플리케이션에서 쓰이는 작은 도구가 됩니다: 마감 시간입니다. `ms`밀리초 후에 거부되는 프로미스를 만들어 실제 작업과 경주시키면, 먼저 처리되는 쪽이 결과를 결정합니다:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
`async` 함수에서 프로미스를 반환해도 괜찮습니다: 함수가 돌려주는 프로미스가 그 프로미스를 따라가므로, 호출자는 프로미스의 프로미스가 아니라 최종 값을 await하게 됩니다.
