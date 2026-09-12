読み込み、サーバーへの呼び出し、タイマーの待機など、時間のかかる操作があります。Python は `asyncio` モジュールでそのようなコードを**非同期に**実行でき、あるタスクが他のタスクを妨げることなく待機できます。

`async def` で定義された関数は**コルーチン関数**です。呼び出しても本体は実行されません：実行すべき作業を記述する**コルーチンオブジェクト**を返します。`asyncio.run(coro)` はイベントループを開始し、コルーチンを最後まで実行して、ループを停止します：
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` は非同期プログラムのエントリーポイントであり、通常の同期コードから一度だけ呼び出されます。

---

コルーチンは、通常の関数と全く同じように引数を取ったり `return` で値を返したりできます。その値は、コルーチンオブジェクトが作られた時点では得られず、コルーチンが実行されて初めて得られます。`asyncio.run` はコルーチンが返した値をそのまま返します：
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
関数について知っていることはすべて `async def` の中でもそのまま当てはまります：ローカル変数、条件分岐、ループ、複数の `return` 文です。

---

`await` は現在のコルーチンを、await された操作が完了するまで一時停止させ、その結果を受け渡します。コルーチンが一時停止している間、イベントループは他のコルーチンを自由に実行できます。`await` を書けるのは `async def` の中だけです。

`asyncio.sleep(seconds)` は最も単純な awaitable です：ループを妨げることなく指定された時間待機します。`time.sleep` とは異なり、await される必要があります：
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
プログラムは `ready` を表示し、50ミリ秒待ってから `go` を表示します。`await` を付けずに `asyncio.sleep(0.05)` と書くと、コルーチンオブジェクトが作られるだけで実行はされないため、待機は一切起こりません。

---

コルーチン関数を呼び出すだけでは実行されません。呼び出しはコルーチンオブジェクトを作るだけです。本体は、そのオブジェクトが await されるか、`asyncio.run` に渡されたときに実行されます：
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python は `RuntimeWarning: coroutine 'hello' was never awaited` という警告まで出します。忘れられた `await` は最もよくある非同期のバグです：コードは呼び出されたように見えるのに決して実行されず、結果を受け取るはずの変数には代わりにコルーチンオブジェクトが入ります。

---

コルーチンは `await` でお互いを呼び出します。コルーチンは他のコルーチンを await し、その戻り値を受け取って処理を続けられます。関数呼び出しの連鎖と全く同じです：
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
`asyncio.run` を通すのは最も外側のコルーチンだけで、内側のものはすべて `await` で到達します。もし `total` が普通の `def` だったら、`await` を一切使えません：待機が必要なチェーン内のすべての関数に `async` キーワードが広がるのです。

---

コルーチンを次々に await すると、**逐次的に**実行されます：10ミリ秒の待機3回には30ミリ秒かかります。`asyncio.gather` は複数のコルーチンを**並行して**実行します：1つがスリープしている間に他のものが進行するため、3つの待機全体で約10ミリ秒しかかかりません。結果を、引数と同じ順序のリストで返します：
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
`gather` 自体も await する必要があり、コルーチンは個別の引数として渡します。リストを渡すには展開します：`asyncio.gather(*coroutines)`

---

操作の数が固定でないときこそ、並行処理が役立ちます。リスト内包表記でコルーチンオブジェクトを作り、それを `gather` に展開して、バッチ全体を一度に await します：
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
10個の URL でも合計では 200ミリ秒ではなく約20ミリ秒しかかからず、結果は URL の順序のまま保たれます。

---

`gather` では、コルーチンは `await` のたびに順番を交代します。コルーチンは準備のできていないものを await するところまで実行され、その後ループが別のコルーチンに切り替えます。そのため `print` のような副作用は、渡された順序ではなく、コルーチンが**再開**する順序で起こります：
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
これは `b`、次に `a`、最後に `['a', 'b']` を出力します：`b` が先に目覚めますが、結果のリストは引数の順序を保ちます。

---

小さな非同期プログラムは決まった形に従います：`asyncio` をインポートし、コルーチン関数を定義し、それらを await する `main` コルーチンを定義し、最後に `asyncio.run(main())` を一度だけ呼び出します。

---

`asyncio.create_task(coro)` はコルーチンを**タスク**に包み、バックグラウンドで実行されるようスケジュールします。`await` とは異なり、すぐに戻るため、タスクが実行されている間も現在のコルーチンは作業を続けられます。タスクが実際に始まるのは、現在のコルーチンが次に `await` で一時停止するときです。後でタスクを await するとその結果が得られます：
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
これは最初に `main continues` を出力します。`background` は `main` が await するときに初めて始まるからです。その後、`task started` と `task done` が出力されます。

---

タスクは、誰かが待っているかどうかに関係なく実行を続けます。早めに作成し、他の作業を行い、その結果が必要になる時点でのみ `await` します。タスクの一部はすでにバックグラウンドで実行されているため、待ち時間は短くなります。タスクは `task.done()` で状態を確認することもでき、完了すれば `True` を返します。

---

コルーチンの中で発生した例外は、コルーチンオブジェクトを作った場所には現れません：それを実行する `await` の位置で発生するか、最も外側のコルーチンなら `asyncio.run` が発生させます。そのため `try`/`except` は**`await`** を包まなければなりません：
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
誰にも捕捉されない例外は、すべての `await` を通って `asyncio.run` まで伝わり、同期コードの中で再スローされます。通常のコールスタックと全く同じです。

---

`gather` に渡したコルーチンの1つが例外を発生させると、その例外は `await asyncio.gather(...)` の行に伝わり、他のコルーチンは実行を続けているのに、その結果は失われます。`return_exceptions=True` を渡すとこれが変わります：`gather` は決して例外を発生させず、リストの中で失われた結果の代わりに例外オブジェクトが入ります：
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
その後、各要素を `isinstance(result, Exception)` でチェックすれば、失敗と値を区別できます。

---

`asyncio.wait_for(awaitable, timeout)` は対象を await しますが、`timeout` 秒後には諦めます。操作はキャンセルされ、`TimeoutError` が発生します。これは他の例外と同じように捕捉できます：
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
タイムアウトが `0.1` なら、同じコードは `done` を出力します。`asyncio.TimeoutError` は組み込みの `TimeoutError` の別名です。

---

失敗するコルーチンの処理は同期のパターンに従います：コルーチンが例外を発生させ、呼び出し側が `await` を `try`/`except` で包み、エラーオブジェクトをどうするか決めます。たとえば `print(e)` でそのメッセージを出力します。

---

これらの部品は自然に組み合わさります。多くの操作を並行して実行し、それぞれに個別の時間制限を付けるには、各操作を `wait_for` を適用して `TimeoutError` を捕捉する小さなコルーチンで包み、そのラッパーを `gather` します：
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
そうすると、`gather(*[guarded(job(x), limit) for x in items])` は、時間内に終わったジョブにはその値を、終わらなかったジョブには `None` を、元の順序で返します。バッチ全体にかかる時間は最大でも約 `limit` 秒です。
