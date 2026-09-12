Alcune operazioni richiedono tempo: leggere un file, chiamare un server, attendere un timer. Python può eseguire questo tipo di codice **in modo asincrono** con il modulo `asyncio`, così che un'attività possa attendere senza bloccare le altre.

Una funzione definita con `async def` è una **funzione coroutine**. Chiamarla non esegue il suo corpo: restituisce un **oggetto coroutine** che descrive il lavoro da svolgere. `asyncio.run(coro)` avvia un event loop, esegue la coroutine fino al completamento e ferma il loop:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` è il punto di ingresso di un programma asincrono e viene chiamato una sola volta, da codice sincrono normale.

---

Una coroutine può ricevere parametri e restituire un valore con `return` esattamente come una funzione normale. Il valore non è disponibile quando l'oggetto coroutine viene creato, ma solo una volta che la coroutine è stata eseguita. `asyncio.run` restituisce ciò che la coroutine ha restituito:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Tutto ciò che sai sulle funzioni vale anche dentro `async def`: variabili locali, condizioni, cicli e più istruzioni `return`.

---

`await` mette in pausa la coroutine corrente finché l'operazione attesa non è completata, poi ne restituisce il risultato. Mentre la coroutine è in pausa, l'event loop è libero di eseguire altre coroutine. `await` è consentito solo dentro un `async def`.

`asyncio.sleep(seconds)` è l'awaitable più semplice: attende per il tempo indicato senza bloccare il loop. A differenza di `time.sleep`, deve essere atteso con `await`:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
Il programma stampa `ready`, attende 50 millisecondi e stampa `go`. Scrivere `asyncio.sleep(0.05)` senza `await` crea l'oggetto coroutine ma non lo esegue mai, quindi non avviene alcuna attesa.

---

Chiamare una funzione coroutine non basta per eseguirla. La chiamata costruisce soltanto un oggetto coroutine; il corpo viene eseguito quando quell'oggetto viene atteso con `await` o passato a `asyncio.run`:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python lo segnala persino con un avviso: `RuntimeWarning: coroutine 'hello' was never awaited`. Un `await` dimenticato è il bug asincrono più comune: il codice sembra chiamato ma non viene mai eseguito, e ogni variabile che dovrebbe contenere il suo risultato contiene invece un oggetto coroutine.

---

Le coroutine si chiamano tra loro con `await`. Una coroutine può attendere qualsiasi altra coroutine, riceverne il valore di ritorno e continuare, esattamente come una catena di chiamate di funzione:
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
Solo la coroutine più esterna passa attraverso `asyncio.run`; ogni coroutine interna viene raggiunta con `await`. Se `total` fosse un `def` normale, non potrebbe usare `await` affatto: la parola chiave `async` si estende a ogni funzione della catena che deve attendere.

---

Attendere le coroutine una dopo l'altra le esegue **in modo sequenziale**: tre attese di 10 millisecondi richiedono 30 millisecondi. `asyncio.gather` esegue più coroutine **in modo concorrente**: mentre una dorme, le altre progrediscono, così le tre attese insieme richiedono circa 10 millisecondi. Restituisce una lista con i risultati nello stesso ordine degli argomenti:
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
Anche `gather` stesso deve essere atteso, e prende le coroutine come argomenti separati. Per passare una lista, scompattala: `asyncio.gather(*coroutines)`.

---

La concorrenza dà i suoi frutti quando il numero di operazioni non è fisso. Costruisci gli oggetti coroutine in una list comprehension, scompattali in `gather` e attendi l'intero blocco in una volta sola:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Dieci url richiedono comunque circa 20 millisecondi in totale invece di 200, e i risultati restano nell'ordine degli url.

---

Con `gather`, le coroutine si alternano a ogni `await`. Una coroutine viene eseguita finché non attende qualcosa che non è ancora pronto, poi il loop passa a un'altra. Gli effetti collaterali come `print` avvengono quindi nell'ordine in cui le coroutine **riprendono**, non nell'ordine in cui sono state passate:
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
Questo stampa `b`, poi `a`, poi `['a', 'b']`: `b` si risveglia per prima, ma la lista dei risultati mantiene l'ordine degli argomenti.

---

Un piccolo programma asincrono segue una forma fissa: importare `asyncio`, definire le funzioni coroutine, definire una coroutine `main` che le attende e infine chiamare `asyncio.run(main())` una sola volta alla fine.

---

`asyncio.create_task(coro)` avvolge una coroutine in un **Task** e la pianifica per l'esecuzione in background. A differenza di `await`, restituisce subito, così la coroutine corrente può continuare a lavorare mentre il task è in esecuzione. Il task in realtà parte la volta successiva in cui la coroutine corrente si ferma su un `await`. Attendere il task in seguito ne restituisce il risultato:
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
Questo stampa prima `main continues`, perché `background` parte solo quando `main` attende, e poi `task started` e `task done`.

---

Un task continua a essere eseguito che qualcuno lo attenda o meno. Crealo per tempo, fai altro lavoro e attendilo con `await` solo nel punto in cui serve il suo risultato: l'attesa è più breve perché parte del task è già stata eseguita in background. Un task può anche essere ispezionato con `task.done()`, che restituisce `True` una volta terminato.

---

Un'eccezione sollevata dentro una coroutine non appare nel punto in cui l'oggetto coroutine è stato creato: viene sollevata dall'`await` che la esegue, oppure da `asyncio.run` per quella più esterna. `try`/`except` deve quindi avvolgere **l'`await`**:
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
Un'eccezione che nessuno cattura si propaga attraverso ogni `await` fino a `asyncio.run`, che la rilancia nel codice sincrono, esattamente come un normale stack di chiamate.

---

Quando una delle coroutine passate a `gather` solleva un'eccezione, l'eccezione si propaga alla riga `await asyncio.gather(...)` e i risultati delle altre vanno perduti, sebbene le coroutine continuino a essere eseguite. Passare `return_exceptions=True` cambia le cose: `gather` non solleva mai, e l'oggetto eccezione prende il posto del risultato mancante nella lista:
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
Ogni elemento può quindi essere controllato con `isinstance(result, Exception)` per separare i fallimenti dai valori.

---

`asyncio.wait_for(awaitable, timeout)` attende qualcosa ma rinuncia dopo `timeout` secondi: l'operazione viene annullata e viene sollevata una `TimeoutError`, che può essere catturata come qualsiasi eccezione:
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
Con un timeout di `0.1` lo stesso codice stamperebbe `done`. `asyncio.TimeoutError` è un altro nome per la `TimeoutError` integrata.

---

Gestire una coroutine che fallisce segue lo schema sincrono: la coroutine solleva, chi la chiama avvolge l'`await` in `try`/`except` e decide cosa fare dell'oggetto errore, ad esempio stamparne il messaggio con `print(e)`.

---

I pezzi si combinano naturalmente. Per eseguire molte operazioni in modo concorrente, ciascuna con il proprio limite di tempo, avvolgi ognuna in una piccola coroutine che applica `wait_for` e cattura la `TimeoutError`, poi passa i wrapper a `gather`:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` restituisce quindi un valore per ogni job terminato in tempo e `None` per ciascuno che non ci è riuscito, nell'ordine originale, e l'intero blocco richiede al massimo circa `limit` secondi.
