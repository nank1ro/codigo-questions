Some operations take time: reading a file, calling a server, waiting for a timer. Python can run such code **asynchronously** with the `asyncio` module, so that one task can wait without blocking the others.

A function defined with `async def` is a **coroutine function**. Calling it does not run its body: it returns a **coroutine object** that describes the work to do. `asyncio.run(coro)` starts an event loop, runs the coroutine to completion and stops the loop:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` is the entry point of an asynchronous program and is called once, from regular synchronous code.

---

A coroutine can take parameters and `return` a value exactly like a normal function. The value is not available when the coroutine object is created, only once the coroutine has been run. `asyncio.run` returns whatever the coroutine returned:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Everything you know about functions still applies inside `async def`: local variables, conditions, loops and multiple `return` statements.

---

`await` pauses the current coroutine until the awaited operation completes, then gives back its result. While the coroutine is paused, the event loop is free to run other coroutines. `await` is only allowed inside an `async def`.

`asyncio.sleep(seconds)` is the simplest awaitable: it waits for the given time without blocking the loop. Unlike `time.sleep`, it must be awaited:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
The program prints `ready`, waits 50 milliseconds and prints `go`. Writing `asyncio.sleep(0.05)` without `await` creates the coroutine object but never runs it, so no waiting happens.

---

Calling a coroutine function is not enough to run it. The call only builds a coroutine object; the body runs when that object is awaited or passed to `asyncio.run`:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python even warns about it: `RuntimeWarning: coroutine 'hello' was never awaited`. A forgotten `await` is the most common asynchronous bug: the code looks called but never executes, and any variable that should hold its result holds a coroutine object instead.

---

Coroutines call each other with `await`. A coroutine can await any other coroutine, receive its return value and keep going, exactly like a chain of function calls:
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
Only the outermost coroutine goes through `asyncio.run`; every inner one is reached with `await`. If `total` were a plain `def`, it could not use `await` at all: the `async` keyword spreads to every function in the chain that needs to wait.

---

Awaiting coroutines one after another runs them **sequentially**: three waits of 10 milliseconds take 30 milliseconds. `asyncio.gather` runs several coroutines **concurrently**: while one is sleeping, the others make progress, so the three waits together take about 10 milliseconds. It returns a list with the results in the same order as the arguments:
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
`gather` itself must be awaited, and it takes the coroutines as separate arguments. To pass a list, unpack it: `asyncio.gather(*coroutines)`.

---

Concurrency pays off when the number of operations is not fixed. Build the coroutine objects in a list comprehension, unpack them into `gather` and await the whole batch at once:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Ten urls still take about 20 milliseconds in total instead of 200, and the results stay in the order of the urls.

---

With `gather`, coroutines take turns at every `await`. A coroutine runs until it awaits something that is not ready, then the loop switches to another one. Side effects such as `print` therefore happen in the order in which the coroutines **resume**, not in the order they were passed:
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
This prints `b`, then `a`, then `['a', 'b']`: `b` wakes up first, but the results list keeps the argument order.

---

A small asynchronous program follows a fixed shape: import `asyncio`, define the coroutine functions, define a `main` coroutine that awaits them, and finally call `asyncio.run(main())` once at the end.

---

`asyncio.create_task(coro)` wraps a coroutine in a **Task** and schedules it to run in the background. Unlike `await`, it returns immediately, so the current coroutine can keep working while the task runs. The task actually starts the next time the current coroutine pauses at an `await`. Awaiting the task later gives its result:
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
This prints `main continues` first, because `background` only starts when `main` awaits, and then `task started` and `task done`.

---

A task keeps running whether or not someone is waiting for it. Create it early, do other work, and `await` it only at the point where its result is needed: the wait is shorter because part of the task has already run in the background. A task can also be inspected with `task.done()`, which returns `True` once it has finished.

---

An exception raised inside a coroutine does not appear where the coroutine object was created: it is raised at the `await` that runs it, or by `asyncio.run` for the outermost one. `try`/`except` therefore has to wrap the **`await`**:
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
An exception that nobody catches propagates through every `await` up to `asyncio.run`, which re-raises it in the synchronous code, exactly like a normal call stack.

---

When one of the coroutines passed to `gather` raises, the exception propagates to the `await asyncio.gather(...)` line and the results of the others are lost, although they keep running. Passing `return_exceptions=True` changes this: `gather` never raises, and the exception object takes the place of the missing result in the list:
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
Each element can then be checked with `isinstance(result, Exception)` to separate failures from values.

---

`asyncio.wait_for(awaitable, timeout)` awaits something but gives up after `timeout` seconds: the operation is cancelled and a `TimeoutError` is raised, which can be caught like any exception:
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
With a timeout of `0.1` the same code would print `done`. `asyncio.TimeoutError` is another name for the built-in `TimeoutError`.

---

Handling a failing coroutine follows the synchronous pattern: the coroutine raises, the caller wraps the `await` in `try`/`except` and decides what to do with the error object, for example printing its message with `print(e)`.

---

The pieces combine naturally. To run many operations concurrently, each with its own time limit, wrap every one in a small coroutine that applies `wait_for` and catches the `TimeoutError`, then `gather` the wrappers:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` then returns a value for each job that finished in time and `None` for each one that did not, in the original order, and the whole batch takes about `limit` seconds at most.
