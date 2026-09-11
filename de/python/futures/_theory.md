Einige Operationen dauern Zeit: das Lesen einer Datei, der Aufruf eines Servers, das Warten auf einen Timer. Python kann solchen Code mit dem Modul `asyncio` **asynchron** ausführen, sodass eine Aufgabe warten kann, ohne die anderen zu blockieren.

Eine mit `async def` definierte Funktion ist eine **Coroutine-Funktion**. Ihr Aufruf führt den Körper nicht aus: Er gibt ein **Coroutine-Objekt** zurück, das die auszuführende Arbeit beschreibt. `asyncio.run(coro)` startet eine Event-Loop, führt die Coroutine bis zu ihrem Ende aus und stoppt die Loop:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` ist der Einstiegspunkt eines asynchronen Programms und wird einmal aus normalem synchronem Code aufgerufen.

---

Eine Coroutine kann Parameter entgegennehmen und genau wie eine normale Funktion einen Wert mit `return` zurückgeben. Der Wert ist nicht verfügbar, wenn das Coroutine-Objekt erzeugt wird, sondern erst, wenn die Coroutine ausgeführt wurde. `asyncio.run` gibt zurück, was die Coroutine zurückgegeben hat:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Alles, was du über Funktionen weißt, gilt auch innerhalb von `async def`: lokale Variablen, Bedingungen, Schleifen und mehrere `return`-Anweisungen.

---

`await` pausiert die aktuelle Coroutine, bis der awaited Vorgang abgeschlossen ist, und gibt dann sein Ergebnis zurück. Während die Coroutine pausiert, ist die Event-Loop frei, andere Coroutinen auszuführen. `await` ist nur innerhalb eines `async def` erlaubt.

`asyncio.sleep(seconds)` ist das einfachste Awaitable: Es wartet die angegebene Zeit, ohne die Loop zu blockieren. Anders als `time.sleep` muss es awaited werden:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
Das Programm gibt `ready` aus, wartet 50 Millisekunden und gibt `go` aus. `asyncio.sleep(0.05)` ohne `await` zu schreiben erzeugt das Coroutine-Objekt, führt es aber nie aus, sodass nicht gewartet wird.

---

Eine Coroutine-Funktion aufzurufen reicht nicht aus, um sie auszuführen. Der Aufruf erzeugt nur ein Coroutine-Objekt; der Körper wird ausgeführt, wenn das Objekt awaited oder an `asyncio.run` übergeben wird:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python warnt sogar davor: `RuntimeWarning: coroutine 'hello' was never awaited`. Ein vergessenes `await` ist der häufigste asynchrone Fehler: Der Code sieht aufgerufen aus, wird aber nie ausgeführt, und jede Variable, die sein Ergebnis halten sollte, enthält stattdessen ein Coroutine-Objekt.

---

Coroutinen rufen einander mit `await` auf. Eine Coroutine kann jede andere Coroutine awaiten, ihren Rückgabewert empfangen und weiterlaufen, genau wie eine Kette von Funktionsaufrufen:
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
Nur die äußerste Coroutine läuft über `asyncio.run`; jede innere wird mit `await` erreicht. Wäre `total` ein normales `def`, könnte es `await` überhaupt nicht verwenden: Das Schlüsselwort `async` breitet sich auf jede Funktion in der Kette aus, die warten muss.

---

Coroutinen nacheinander zu awaiten, führt sie **sequenziell** aus: drei Wartezeiten von 10 Millisekunden dauern 30 Millisekunden. `asyncio.gather` führt mehrere Coroutinen **gleichzeitig** aus: Während eine schläft, machen die anderen Fortschritte, sodass die drei Wartezeiten zusammen etwa 10 Millisekunden dauern. Es gibt eine Liste mit den Ergebnissen in derselben Reihenfolge wie die Argumente zurück:
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
`gather` selbst muss awaited werden, und es nimmt die Coroutinen als separate Argumente entgegen. Um eine Liste zu übergeben, entpacke sie: `asyncio.gather(*coroutines)`.

---

Nebenläufigkeit zahlt sich aus, wenn die Anzahl der Operationen nicht feststeht. Baue die Coroutine-Objekte in einer List Comprehension, entpacke sie in `gather` und awaite die gesamte Gruppe auf einmal:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Zehn urls dauern insgesamt weiterhin nur etwa 20 Millisekunden statt 200, und die Ergebnisse behalten die Reihenfolge der urls bei.

---

Mit `gather` kommen Coroutinen bei jedem `await` abwechselnd zum Zug. Eine Coroutine läuft, bis sie auf etwas awaitet, das noch nicht bereit ist, dann schaltet die Loop zu einer anderen um. Nebeneffekte wie `print` passieren daher in der Reihenfolge, in der die Coroutinen **fortgesetzt** werden, nicht in der Reihenfolge, in der sie übergeben wurden:
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
Das gibt `b` aus, dann `a`, dann `['a', 'b']`: `b` wacht zuerst auf, aber die Ergebnisliste behält die Argumentreihenfolge bei.

---

Ein kleines asynchrones Programm folgt einer festen Form: importiere `asyncio`, definiere die Coroutine-Funktionen, definiere eine `main`-Coroutine, die sie awaitet, und rufe zum Schluss einmal `asyncio.run(main())` auf.

---

`asyncio.create_task(coro)` verpackt eine Coroutine in eine **Task** und plant sie ein, um im Hintergrund zu laufen. Anders als `await` kehrt es sofort zurück, sodass die aktuelle Coroutine weiterarbeiten kann, während die Task läuft. Die Task startet tatsächlich beim nächsten Mal, wenn die aktuelle Coroutine an einem `await` pausiert. Die Task später zu awaiten liefert ihr Ergebnis:
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
Das gibt zuerst `main continues` aus, weil `background` erst startet, wenn `main` awaited, und danach `task started` und `task done`.

---

Eine Task läuft weiter, egal ob jemand auf sie wartet. Erstelle sie früh, erledige andere Arbeit und `await` sie erst an der Stelle, an der ihr Ergebnis gebraucht wird: Das Warten ist kürzer, weil ein Teil der Task bereits im Hintergrund gelaufen ist. Eine Task kann auch mit `task.done()` geprüft werden, was `True` zurückgibt, sobald sie beendet ist.

---

Eine innerhalb einer Coroutine ausgelöste Ausnahme tritt nicht dort auf, wo das Coroutine-Objekt erzeugt wurde: Sie wird an dem `await` ausgelöst, das die Coroutine ausführt, oder von `asyncio.run` bei der äußersten. `try`/`except` muss daher das **`await`** umschließen:
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
Eine Ausnahme, die niemand abfängt, breitet sich durch jedes `await` bis zu `asyncio.run` aus, das sie im synchronen Code erneut auslöst, genau wie ein normaler Aufrufstapel.

---

Wenn eine der an `gather` übergebenen Coroutinen eine Ausnahme auslöst, propagiert die Ausnahme zur Zeile `await asyncio.gather(...)` und die Ergebnisse der anderen gehen verloren, obwohl sie weiterlaufen. `return_exceptions=True` zu übergeben ändert dies: `gather` löst nie eine Ausnahme aus, und das Ausnahmeobjekt nimmt in der Liste den Platz des fehlenden Ergebnisses ein:
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
Jedes Element kann dann mit `isinstance(result, Exception)` geprüft werden, um Fehlschläge von Werten zu trennen.

---

`asyncio.wait_for(awaitable, timeout)` awaited etwas, gibt aber nach `timeout` Sekunden auf: Die Operation wird abgebrochen und ein `TimeoutError` ausgelöst, der wie jede Ausnahme abgefangen werden kann:
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
Mit einem Timeout von `0.1` würde derselbe Code `done` ausgeben. `asyncio.TimeoutError` ist ein anderer Name für die eingebaute `TimeoutError`.

---

Der Umgang mit einer fehlschlagenden Coroutine folgt dem synchronen Muster: Die Coroutine löst eine Ausnahme aus, der Aufrufer umschließt das `await` mit `try`/`except` und entscheidet, was mit dem Fehlerobjekt geschehen soll, zum Beispiel seine Meldung mit `print(e)` auszugeben.

---

Die Bausteine lassen sich natürlich kombinieren. Um viele Operationen gleichzeitig auszuführen, jede mit eigenem Zeitlimit, verpacke jede einzelne in eine kleine Coroutine, die `wait_for` anwendet und den `TimeoutError` abfängt, und `gather` die Wrapper:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` gibt dann für jeden Job, der sich rechtzeitig beendet hat, einen Wert zurück und `None` für jeden anderen, in der ursprünglichen Reihenfolge, und die gesamte Gruppe dauert höchstens etwa `limit` Sekunden.
