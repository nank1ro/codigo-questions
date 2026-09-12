Niektóre operacje zajmują czas: czytanie pliku, odwołanie do serwera, oczekiwanie na timer. Python może wykonywać taki kod **asynchronicznie** za pomocą modułu `asyncio`, dzięki czemu jedno zadanie może czekać, nie blokując pozostałych.

Funkcja zdefiniowana za pomocą `async def` to **funkcja asynchroniczna**. Jej wywołanie nie uruchamia ciała funkcji: zwraca **obiekt korutyny**, który opisuje pracę do wykonania. `asyncio.run(coro)` uruchamia pętlę zdarzeń, wykonuje korutynę do końca i zatrzymuje pętlę:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` jest punktem wejścia programu asynchronicznego i jest wywoływany raz, z zwykłego kodu synchronicznego.

---

Korutyna może przyjmować parametry, a `return` zwraca wartość dokładnie jak w zwykłej funkcji. Wartość nie jest dostępna w momencie utworzenia obiektu korutyny, lecz dopiero po wykonaniu korutyny. `asyncio.run` zwraca to, co zwróciła korutyna:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Wszystko, co wiesz o funkcjach, obowiązuje także wewnątrz `async def`: zmienne lokalne, warunki, pętle i wiele instrukcji `return`.

---

`await` wstrzymuje bieżącą korutynę, aż oczekiwana operacja się zakończy, po czym oddaje jej wynik. Dopóki korutyna jest wstrzymana, pętla zdarzeń może swobodnie wykonywać inne korutyny. `await` jest dozwolony tylko wewnątrz `async def`.

`asyncio.sleep(seconds)` to najprostszy awaitable: czeka podany czas, nie blokując pętli. W przeciwieństwie do `time.sleep` musi być użyty z `await`:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
Program wypisuje `ready`, czeka 50 milisekund i wypisuje `go`. Zapisanie `asyncio.sleep(0.05)` bez `await` tworzy obiekt korutyny, ale nigdy go nie wykonuje, więc oczekiwanie nie następuje.

---

Wywołanie funkcji asynchronicznej nie wystarcza, aby ją uruchomić. Wywołanie tylko buduje obiekt korutyny; ciało wykonuje się, gdy ten obiekt jest użyty z `await` lub przekazany do `asyncio.run`:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python ostrzega nawet o tym: `RuntimeWarning: coroutine 'hello' was never awaited`. Zapomniany `await` to najczęstszy błąd asynchroniczny: kod wygląda na wywołany, ale nigdy się nie wykonuje, a każda zmienna, która powinna przechowywać jego wynik, przechowuje zamiast tego obiekt korutyny.

---

Korutyny wywołują się nawzajem za pomocą `await`. Korutyna może użyć `await` na dowolnej innej korutynie, otrzymać jej wartość zwracaną i kontynuować działanie, dokładnie jak łańcuch wywołań funkcji:
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
Przez `asyncio.run` przechodzi tylko najbardziej zewnętrzna korutyna; do każdej wewnętrznej dochodzi się przez `await`. Gdyby `total` było zwykłym `def`, nie mogłoby w ogóle użyć `await`: słowo kluczowe `async` rozprzestrzenia się na każdą funkcję w łańcuchu, która musi czekać.

---

Używanie `await` na korutynach jedna po drugiej wykonuje je **sekwencyjnie**: trzy oczekiwania po 10 milisekund zajmują 30 milisekund. `asyncio.gather` wykonuje kilka korutyn **równolegle**: podczas gdy jedna śpi, inne robią postępy, więc trzy oczekiwania razem zajmują około 10 milisekund. Zwraca listę z wynikami w tej samej kolejności co argumenty:
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
Samo `gather` musi być użyte z `await`, a korutyny przyjmuje jako osobne argumenty. Aby przekazać listę, rozpakuj ją: `asyncio.gather(*coroutines)`.

---

Współbieżność opłaca się, gdy liczba operacji nie jest ustalona. Zbuduj obiekty korutyn w list comprehension, rozpakuj je do `gather` i użyj `await` na całej partii naraz:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Dziesięć adresów URL nadal zajmuje łącznie około 20 milisekund zamiast 200, a wyniki pozostają w kolejności adresów URL.

---

Z `gather` korutyny zmieniają się przy każdym `await`. Korutyna wykonuje się, dopóki nie użyje `await` na czymś, co nie jest gotowe, wtedy pętla przełącza się na inną. Efekty uboczne, takie jak `print`, dzieją się więc w kolejności, w jakiej korutyny **wznawiają działanie**, a nie w kolejności, w jakiej zostały przekazane:
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
Wypisuje to `b`, potem `a`, potem `['a', 'b']`: `b` budzi się pierwsze, ale lista wyników zachowuje kolejność argumentów.

---

Mały program asynchroniczny ma ustalony kształt: zaimportuj `asyncio`, zdefiniuj funkcje asynchroniczne, zdefiniuj korutynę `main`, która używa na nich `await`, a na koniec wywołaj raz `asyncio.run(main())`.

---

`asyncio.create_task(coro)` opakowuje korutynę w **Task** i planuje jej wykonanie w tle. W przeciwieństwie do `await` zwraca natychmiast, więc bieżąca korutyna może dalej pracować, podczas gdy zadanie się wykonuje. Zadanie faktycznie startuje przy najbliższej pauzie bieżącej korutyny na `await`. Późniejsze użycie `await` na zadaniu daje jego wynik:
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
Wypisuje to najpierw `main continues`, ponieważ `background` startuje dopiero, gdy `main` użyje `await`, a potem `task started` i `task done`.

---

Zadanie wykonuje się dalej niezależnie od tego, czy ktoś na nie czeka. Utwórz je wcześnie, rób inną pracę, a `await` użyj dopiero w miejscu, w którym potrzebny jest jego wynik: oczekiwanie jest krótsze, bo część zadania wykonała się już w tle. Zadanie można też sprawdzić za pomocą `task.done()`, która zwraca `True`, gdy już się zakończyło.

---

Wyjątek zgłoszony wewnątrz korutyny nie pojawia się tam, gdzie utworzono obiekt korutyny: jest zgłaszany przy `await`, które go wykonuje, albo przez `asyncio.run` dla najbardziej zewnętrznej. Dlatego `try`/`except` musi obejmować **`await`**:
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
Wyjątek, którego nikt nie łapie, propaguje przez każde `await` aż do `asyncio.run`, które zgłasza go ponownie w kodzie synchronicznym, dokładnie jak zwykły stos wywołań.

---

Gdy jedna z korutyn przekazanych do `gather` zgłosi wyjątek, propaguje się on do linii `await asyncio.gather(...)`, a wyniki pozostałych są tracone, choć one dalej się wykonują. Przekazanie `return_exceptions=True` zmienia to: `gather` nigdy nie zgłasza wyjątku, a obiekt wyjątku zajmuje miejsce brakującego wyniku na liście:
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
Każdy element można wtedy sprawdzić za pomocą `isinstance(result, Exception)`, aby oddzielić błędy od wartości.

---

`asyncio.wait_for(awaitable, timeout)` używa `await` na czymś, ale poddaje się po `timeout` sekundach: operacja jest anulowana i zgłaszany jest `TimeoutError`, który można złapać jak każdy wyjątek:
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
Z limitem czasu `0.1` ten sam kod wypisałby `done`. `asyncio.TimeoutError` to inna nazwa wbudowanego `TimeoutError`.

---

Obsługa zawodzącej korutyny wygląda jak w schemacie synchronicznym: korutyna zgłasza wyjątek, wywołujący obejmuje `await` blokiem `try`/`except` i decyduje, co zrobić z obiektem błędu, na przykład wypisując jego komunikat przez `print(e)`.

---

Elementy łączą się naturalnie. Aby wykonać wiele operacji równolegle, każda z własnym limitem czasu, opakuj każdą z nich w małą korutynę, która stosuje `wait_for` i łapie `TimeoutError`, a potem połącz opakowania przez `gather`:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` zwraca wtedy wartość dla każdego zadania, które zdążyło na czas, i `None` dla każdego, które nie zdążyło, w pierwotnej kolejności, a cała partia zajmuje najwyżej około `limit` sekund.
