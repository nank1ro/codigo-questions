有些操作需要时间：读取文件、调用服务器、等待计时器。Python 可以用 `asyncio` 模块**异步地**运行这样的代码，让一个任务可以在不阻塞其他任务的情况下等待。

用 `async def` 定义的函数是一个**协程函数**。调用它并不会运行函数体：它返回一个描述要做的工作的**协程对象**。`asyncio.run(coro)` 启动一个事件循环，把协程运行完毕，然后停止该循环：
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` 是异步程序的入口，只从普通的同步代码中调用一次。

---

协程可以像普通函数一样接收参数并 `return` 一个值。这个值在协程对象被创建时还不可用，只有协程运行之后才能得到。`asyncio.run` 会返回协程返回的值：
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
你关于函数所知的一切在 `async def` 内部依然适用：局部变量、条件、循环和多个 `return` 语句。

---

`await` 会暂停当前协程，直到被等待的操作完成，然后交回它的结果。在协程暂停期间，事件循环可以自由地运行其他协程。`await` 只能用在 `async def` 内部。

`asyncio.sleep(seconds)` 是最简单的可等待对象：它等待给定的时间而不阻塞事件循环。与 `time.sleep` 不同，它必须用 `await` 等待：
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
程序打印 `ready`，等待 50 毫秒，然后打印 `go`。写 `asyncio.sleep(0.05)` 而不加 `await` 会创建协程对象但从不运行它，因此不会发生任何等待。

---

调用协程函数并不足以运行它。调用只是构建一个协程对象；函数体在该对象被 await 或传给 `asyncio.run` 时才会运行：
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python 甚至会对此发出警告：`RuntimeWarning: coroutine 'hello' was never awaited`。忘记 `await` 是最常见的异步错误：代码看起来被调用了，却从未执行，而本应保存其结果的变量保存的却是一个协程对象。

---

协程之间用 `await` 相互调用。一个协程可以 await 任何其他协程，接收它的返回值并继续执行，就像一条函数调用链：
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
只有最外层的协程通过 `asyncio.run` 运行；内部的每一个协程都用 `await` 到达。如果 `total` 是普通的 `def`，它就完全不能使用 `await`：`async` 关键字会蔓延到链上每一个需要等待的函数。

---

一个接一个地 await 协程会**顺序地**运行它们：三次 10 毫秒的等待需要 30 毫秒。`asyncio.gather` 会**并发地**运行多个协程：当一个在休眠时，其他协程继续推进，所以三次等待加起来大约只需要 10 毫秒。它返回一个列表，结果的顺序与参数的顺序相同：
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
`gather` 本身也必须被 await，并且它把协程作为单独的参数接收。要传入一个列表，请将其解包：`asyncio.gather(*coroutines)`。

---

当操作的数量不固定时，并发就派上了用场。用列表推导构建协程对象，把它们解包传给 `gather`，然后一次性 await 整批协程：
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
十个 url 总共仍只需约 20 毫秒而不是 200 毫秒，并且结果保持与 url 相同的顺序。

---

使用 `gather` 时，协程在每一个 `await` 处轮流执行。一个协程一直运行到它 await 一个尚未就绪的东西，然后事件循环切换到另一个。因此，`print` 之类的副作用按照协程**恢复**的顺序发生，而不是它们被传入的顺序：
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
它打印 `b`，然后是 `a`，接着是 `['a', 'b']`：`b` 先醒来，但结果列表保持参数的顺序。

---

一个小的异步程序遵循固定的形状：导入 `asyncio`，定义协程函数，定义一个 await 它们的 `main` 协程，最后在结尾调用一次 `asyncio.run(main())`。

---

`asyncio.create_task(coro)` 把一个协程包装成一个 **Task**，并调度它在后台运行。与 `await` 不同，它立即返回，所以当前协程可以在任务运行期间继续工作。任务实际上在当前协程下一次在 `await` 处暂停时才启动。之后再 await 该任务就能得到它的结果：
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
它先打印 `main continues`，因为 `background` 只有在 `main` await 时才启动，然后打印 `task started` 和 `task done`。

---

无论有没有人在等待它，任务都会持续运行。尽早创建它，做其他工作，只在需要其结果的地方才 `await` 它：等待会更短，因为任务的一部分已经在后台运行过了。任务还可以用 `task.done()` 来检查，它一旦完成就返回 `True`。

---

在协程内部抛出的异常不会出现在协程对象被创建的地方：它在运行该协程的 `await` 处被抛出，对于最外层的协程则由 `asyncio.run` 抛出。因此 `try`/`except` 必须包裹 **`await`**：
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
没有人捕获的异常会穿过每一个 `await` 一路传播到 `asyncio.run`，后者在同步代码中把它重新抛出，与普通的调用栈完全一样。

---

当传给 `gather` 的协程中有一个抛出异常时，该异常会传播到 `await asyncio.gather(...)` 这一行，其他协程的结果会丢失，尽管它们仍在继续运行。传入 `return_exceptions=True` 会改变这一点：`gather` 从不抛出异常，异常对象会顶替列表中缺失的结果：
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
之后可以用 `isinstance(result, Exception)` 检查每个元素，把失败与值区分开。

---

`asyncio.wait_for(awaitable, timeout)` 等待某个东西，但在 `timeout` 秒后放弃：操作被取消，并抛出一个 `TimeoutError`，它可以像任何异常一样被捕获：
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
如果超时为 `0.1`，同样的代码会打印 `done`。`asyncio.TimeoutError` 是内置 `TimeoutError` 的另一个名字。

---

处理失败的协程遵循同步的模式：协程抛出异常，调用者把 `await` 包在 `try`/`except` 中，并决定如何处理这个错误对象，例如用 `print(e)` 打印它的消息。

---

这些部件可以自然地组合起来。要并发运行许多操作，且每个操作都有自己的时限，可以把每一个包装在一个应用 `wait_for` 并捕获 `TimeoutError` 的小协程中，然后 `gather` 这些包装协程：
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` 然后会为每个按时完成的任务返回一个值，为每个未按时完成的任务返回 `None`，顺序保持原样，而整批任务最多耗时约 `limit` 秒。
