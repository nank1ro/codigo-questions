어떤 작업에는 시간이 걸립니다: 파일 읽기, 서버 호출, 타이머 대기 같은 일들입니다. Python은 `asyncio` 모듈로 이런 코드를 **비동기적으로** 실행할 수 있으므로, 하나의 작업이 다른 작업을 막지 않고 기다릴 수 있습니다.

`async def`로 정의한 함수는 **코루틴 함수**입니다. 호출한다고 해서 본문이 실행되는 것은 아니고, 해야 할 작업을 나타내는 **코루틴 객체**가 반환됩니다. `asyncio.run(coro)`는 이벤트 루프를 시작하고, 코루틴을 끝까지 실행한 뒤 루프를 종료합니다:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run`은 비동기 프로그램의 진입점이며, 평범한 동기 코드에서 딱 한 번 호출됩니다.

---

코루틴은 일반 함수와 똑같이 매개변수를 받고 `return`으로 값을 반환할 수 있습니다. 이 값은 코루틴 객체가 만들어질 때가 아니라 코루틴이 실행된 후에야 얻을 수 있습니다. `asyncio.run`은 코루틴이 반환한 값을 그대로 반환합니다:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
함수에 대해 아는 모든 것은 `async def` 안에서도 그대로 적용됩니다: 지역 변수, 조건문, 반복문, 여러 개의 `return` 문 등이 그렇습니다.

---

`await`는 현재 코루틴을 일시 중지했다가 기다리던 작업이 끝나면 그 결과를 돌려줍니다. 코루틴이 일시 중지된 동안 이벤트 루프는 다른 코루틴을 자유롭게 실행할 수 있습니다. `await`는 `async def` 안에서만 사용할 수 있습니다.

`asyncio.sleep(seconds)`는 가장 간단한 awaitable입니다: 루프를 막지 않으면서 주어진 시간만큼 기다립니다. `time.sleep`과 달리 반드시 await해야 합니다:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
이 프로그램은 `ready`를 출력하고, 50밀리초를 기다린 뒤 `go`를 출력합니다. `await` 없이 `asyncio.sleep(0.05)`라고 쓰면 코루틴 객체만 만들어질 뿐 실행되지 않으므로 아무런 대기도 일어나지 않습니다.

---

코루틴 함수를 호출하는 것만으로는 실행되지 않습니다. 호출은 코루틴 객체를 만들 뿐이며, 본문은 그 객체가 await되거나 `asyncio.run`에 전달될 때 실행됩니다:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python은 이에 대해 `RuntimeWarning: coroutine 'hello' was never awaited` 경고까지 내줍니다. 잊어버린 `await`는 가장 흔한 비동기 버그입니다: 코드는 호출된 것처럼 보이지만 실행되지 않고, 결과를 담아야 할 변수에는 대신 코루틴 객체가 들어갑니다.

---

코루틴은 `await`로 서로를 호출합니다. 코루틴은 다른 어떤 코루틴이든 await하고 그 반환값을 받아 계속 진행할 수 있습니다. 함수 호출의 연쇄와 똑같습니다:
```python
import asyncio

async def fetch_price(item):
    await asyncio.sleep(0.01)  # simulates a slow lookup
    return 10

async def total(item, quantity):
    price = await fetch_price(item)
    return price * quantity

print(asyncio.run(total("pen", 3)))  # 30
```
`asyncio.run`을 거치는 것은 가장 바깥쪽 코루틴뿐이며, 안쪽 코루틴은 모두 `await`로 도달합니다. 만약 `total`이 평범한 `def`라면 `await`를 전혀 사용할 수 없습니다: `async` 키워드는 기다려야 하는 연쇄상의 모든 함수로 번져나갑니다.

---

코루틴을 하나씩 차례로 await하면 **순차적으로** 실행됩니다: 10밀리초 대기 세 번은 30밀리초가 걸립니다. `asyncio.gather`는 여러 코루틴을 **동시에** 실행합니다: 하나가 잠자는 동안 다른 코루틴이 진행되므로, 세 번의 대기는 함께였을 때 약 10밀리초가 걸립니다. `gather`는 인수와 같은 순서로 결과가 담긴 리스트를 반환합니다:
```python
import asyncio

async def double(n):
    await asyncio.sleep(0.01)
    return n * 2

async def main():
    results = await asyncio.gather(double(1), double(2), double(3))
    print(results)  # [2, 4, 6]

asyncio.run(main())
```
`gather` 자체도 await해야 하며, 코루틴들을 개별 인수로 받습니다. 리스트를 전달하려면 언패킹하세요: `asyncio.gather(*coroutines)`.

---

연산 개수가 정해져 있지 않을 때 동시성이 빛을 발합니다. 리스트 컴프리헨션으로 코루틴 객체를 만들고, `gather`에 언패킹해서 전달한 뒤 한꺼번에 await하세요:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
열 개의 url도 200밀리초 대신 총 약 20밀리초가 걸리며, 결과는 url 순서를 그대로 유지합니다.

---

`gather`에서 코루틴들은 `await`마다 순서를 번갈아 가며 실행됩니다. 코루틴은 준비되지 않은 것을 await할 때까지 실행되다가, 루프가 다른 코루틴으로 전환합니다. 따라서 `print` 같은 부수 효과는 코루틴에 전달된 순서가 아니라 코루틴이 **재개되는** 순서로 일어납니다:
```python
import asyncio

async def step(name, delay):
    await asyncio.sleep(delay)
    print(name)
    return name

async def main():
    print(await asyncio.gather(step("a", 0.03), step("b", 0.01)))

asyncio.run(main())
```
이 코드는 `b`, 그다음 `a`, 그다음 `['a', 'b']`를 출력합니다: `b`가 먼저 깨어나지만 결과 리스트는 인수 순서를 유지합니다.

---

작은 비동기 프로그램은 정해진 형태를 따릅니다: `asyncio`를 import하고, 코루틴 함수들을 정의하고, 이들을 await하는 `main` 코루틴을 정의한 다음, 마지막에 `asyncio.run(main())`을 한 번 호출합니다.

---

`asyncio.create_task(coro)`는 코루틴을 **태스크**로 감싸 백그라운드에서 실행되도록 예약합니다. `await`와 달리 즉시 반환되므로, 태스크가 실행되는 동안 현재 코루틴도 계속 작업할 수 있습니다. 태스크는 실제로 현재 코루틴이 다음 `await`에서 일시 중지될 때 시작됩니다. 나중에 태스크를 await하면 그 결과를 얻습니다:
```python
import asyncio

async def background():
    print("task started")
    await asyncio.sleep(0.01)
    return "task done"

async def main():
    task = asyncio.create_task(background())
    print("main continues")
    print(await task)

asyncio.run(main())
```
`background`는 `main`이 await할 때 비로소 시작되므로, 이 코드는 먼저 `main continues`를 출력하고 그다음 `task started`와 `task done`을 출력합니다.

---

태스크는 기다려 주는 사람이 있든 없든 계속 실행됩니다. 미리 만들어 두고 다른 작업을 하다가, 결과가 필요한 지점에서만 `await`하세요: 태스크의 일부가 이미 백그라운드에서 실행되었으므로 기다림이 짧아집니다. 태스크는 `task.done()`으로 확인할 수도 있는데, 이는 끝나면 `True`를 반환합니다.

---

코루틴 안에서 발생한 예외는 코루틴 객체를 만든 곳에 나타나지 않습니다: 예외는 그것을 실행하는 `await`에서 발생하고, 가장 바깥쪽 코루틴의 경우 `asyncio.run`에서 발생합니다. 따라서 `try`/`except`는 **`await`**를 감싸야 합니다:
```python
import asyncio

async def load(path):
    await asyncio.sleep(0.01)
    if path == "":
        raise FileNotFoundError("empty path")
    return "contents"

async def safe_load(path):
    try:
        return await load(path)
    except FileNotFoundError:
        return ""

print(asyncio.run(safe_load("")))  # prints an empty line
```
아무도 잡지 않은 예외는 모든 `await`를 타고 `asyncio.run`까지 전파되어 동기 코드에서 다시 발생합니다. 보통의 호출 스택과 똑같습니다.

---

`gather`에 전달한 코루틴 중 하나가 예외를 발생시키면, 예외는 `await asyncio.gather(...)` 줄로 전파되고 나머지 코루틴들은 계속 실행되지만 그 결과는 사라집니다. `return_exceptions=True`를 전달하면 이 동작이 바뀝니다: `gather`는 절대 예외를 발생시키지 않고, 리스트에서 빠진 결과 자리에 예외 객체가 들어갑니다:
```python
import asyncio

async def ok():
    return 1

async def fail():
    raise ValueError("bad")

async def main():
    results = await asyncio.gather(ok(), fail(), return_exceptions=True)
    print(results)  # [1, ValueError('bad')]

asyncio.run(main())
```
그다음 각 요소를 `isinstance(result, Exception)`으로 검사해 실패와 값을 구분할 수 있습니다.

---

`asyncio.wait_for(awaitable, timeout)`은 무언가를 await하다가 `timeout`초가 지나면 포기합니다: 작업은 취소되고 `TimeoutError`가 발생하며, 이는 다른 예외처럼 잡을 수 있습니다:
```python
import asyncio

async def slow():
    await asyncio.sleep(0.05)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=0.01)
        print(result)
    except TimeoutError:
        print("timed out")

asyncio.run(main())  # timed out
```
타임아웃이 `0.1`이라면 같은 코드는 `done`을 출력합니다. `asyncio.TimeoutError`는 내장 `TimeoutError`의 다른 이름입니다.

---

실패하는 코루틴을 다루는 방법은 동기 패턴을 따릅니다: 코루틴이 예외를 발생시키면, 호출자는 `await`를 `try`/`except`로 감싸고 오류 객체를 어떻게 처리할지 결정합니다. 예를 들어 `print(e)`로 메시지를 출력하는 식입니다.

---

이 조각들은 자연스럽게 결합됩니다. 많은 작업을 각자의 시간 제한과 함께 동시에 실행하려면, 각 작업을 `wait_for`를 적용하고 `TimeoutError`를 잡는 작은 코루틴으로 감싼 뒤 그 wrapper들을 `gather`하세요:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])`는 제시간에 끝난 각 작업의 값과 그렇지 못한 각 작업의 `None`을 원래 순서대로 반환하며, 전체 배치는 최대 `limit`초 정도가 걸립니다.
