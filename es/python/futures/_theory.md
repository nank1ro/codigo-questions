Algunas operaciones toman tiempo: leer un archivo, llamar a un servidor, esperar un temporizador. Python puede ejecutar ese código de forma **asíncrona** con el módulo `asyncio`, de modo que una tarea puede esperar sin bloquear a las demás.

Una función definida con `async def` es una **función corrutina**. Llamarla no ejecuta su cuerpo: retorna un **objeto corrutina** que describe el trabajo por hacer. `asyncio.run(coro)` inicia un bucle de eventos, ejecuta la corrutina hasta completarla y detiene el bucle:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` es el punto de entrada de un programa asíncrono y se llama una sola vez, desde código síncrono normal.

---

Una corrutina puede tomar parámetros y hacer `return` de un valor exactamente como una función normal. El valor no está disponible cuando se crea el objeto corrutina, sino solo cuando la corrutina ya se ha ejecutado. `asyncio.run` retorna lo que la corrutina haya retornado:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Todo lo que sabes sobre funciones sigue aplicando dentro de `async def`: variables locales, condiciones, bucles y múltiples sentencias `return`.

---

`await` pausa la corrutina actual hasta que la operación esperada se completa y entonces entrega su resultado. Mientras la corrutina está pausada, el bucle de eventos queda libre para ejecutar otras corrutinas. `await` solo está permitido dentro de un `async def`.

`asyncio.sleep(seconds)` es el awaitable más simple: espera el tiempo indicado sin bloquear el bucle. A diferencia de `time.sleep`, debe esperarse con `await`:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
El programa imprime `ready`, espera 50 milisegundos e imprime `go`. Escribir `asyncio.sleep(0.05)` sin `await` crea el objeto corrutina pero nunca lo ejecuta, así que no ocurre ninguna espera.

---

Llamar a una función corrutina no es suficiente para ejecutarla. La llamada solo construye un objeto corrutina; el cuerpo se ejecuta cuando ese objeto se espera con `await` o se pasa a `asyncio.run`:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python incluso lo advierte: `RuntimeWarning: coroutine 'hello' was never awaited`. Un `await` olvidado es el error asíncrono más común: el código parece llamado pero nunca se ejecuta, y cualquier variable que debería contener su resultado contiene en su lugar un objeto corrutina.

---

Las corrutinas se llaman entre sí con `await`. Una corrutina puede esperar con `await` a cualquier otra corrutina, recibir su valor de retorno y continuar, exactamente como una cadena de llamadas a funciones:
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
Solo la corrutina más externa pasa por `asyncio.run`; cada una de las internas se alcanza con `await`. Si `total` fuera un `def` normal, no podría usar `await` en absoluto: la palabra clave `async` se propaga a cada función de la cadena que necesita esperar.

---

Esperar corrutinas una tras otra las ejecuta de forma **secuencial**: tres esperas de 10 milisegundos toman 30 milisegundos. `asyncio.gather` ejecuta varias corrutinas de forma **concurrente**: mientras una duerme, las otras avanzan, de modo que las tres esperas juntas toman alrededor de 10 milisegundos. Retorna una lista con los resultados en el mismo orden que los argumentos:
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
`gather` en sí debe esperarse con `await`, y recibe las corrutinas como argumentos separados. Para pasar una lista, desempaquétala: `asyncio.gather(*coroutines)`.

---

La concurrencia rinde cuando la cantidad de operaciones no es fija. Construye los objetos corrutina en una list comprehension, desempaquétalos en `gather` y espera con `await` todo el lote de una vez:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Diez urls siguen tomando unos 20 milisegundos en total en lugar de 200, y los resultados se mantienen en el orden de las urls.

---

Con `gather`, las corrutinas se turnan en cada `await`. Una corrutina se ejecuta hasta que espera algo que aún no está listo, y entonces el bucle cambia a otra. Los efectos secundarios como `print` ocurren por lo tanto en el orden en que las corrutinas **se reanudan**, no en el orden en que se pasaron:
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
Esto imprime `b`, luego `a` y luego `['a', 'b']`: `b` se despierta primero, pero la lista de resultados mantiene el orden de los argumentos.

---

Un pequeño programa asíncrono sigue una forma fija: importar `asyncio`, definir las funciones corrutina, definir una corrutina `main` que las espere con `await` y, finalmente, llamar a `asyncio.run(main())` una vez al final.

---

`asyncio.create_task(coro)` envuelve una corrutina en una **Task** y la programa para ejecutarse en segundo plano. A diferencia de `await`, retorna de inmediato, así que la corrutina actual puede seguir trabajando mientras la tarea se ejecuta. La tarea en realidad arranca la próxima vez que la corrutina actual se pausa en un `await`. Esperar la tarea con `await` más adelante da su resultado:
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
Esto imprime primero `main continues`, porque `background` solo arranca cuando `main` hace `await`, y luego `task started` y `task done`.

---

Una tarea sigue ejecutándose haya o no alguien esperándola. Créala temprano, haz otro trabajo y hazle `await` solo en el punto donde se necesita su resultado: la espera es más corta porque parte de la tarea ya se ejecutó en segundo plano. Una tarea también puede consultarse con `task.done()`, que retorna `True` una vez que terminó.

---

Una excepción lanzada dentro de una corrutina no aparece donde se creó el objeto corrutina: se lanza en el `await` que la ejecuta, o por `asyncio.run` en el caso de la más externa. `try`/`except` debe por lo tanto envolver el **`await`**:
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
Una excepción que nadie captura se propaga a través de cada `await` hasta `asyncio.run`, que vuelve a lanzarla en el código síncrono, exactamente como una pila de llamadas normal.

---

Cuando una de las corrutinas pasadas a `gather` lanza una excepción, esta se propaga a la línea `await asyncio.gather(...)` y los resultados de las demás se pierden, aunque siguen ejecutándose. Pasar `return_exceptions=True` cambia esto: `gather` nunca lanza una excepción, y el objeto de excepción ocupa el lugar del resultado faltante en la lista:
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
Cada elemento puede comprobarse después con `isinstance(result, Exception)` para separar los fallos de los valores.

---

`asyncio.wait_for(awaitable, timeout)` espera algo con `await` pero se rinde después de `timeout` segundos: la operación se cancela y se lanza un `TimeoutError`, que puede capturarse como cualquier excepción:
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
Con un timeout de `0.1` el mismo código imprimiría `done`. `asyncio.TimeoutError` es otro nombre para el `TimeoutError` integrado.

---

Manejar una corrutina que falla sigue el patrón síncrono: la corrutina lanza una excepción, quien llama envuelve el `await` en `try`/`except` y decide qué hacer con el objeto de error, por ejemplo imprimir su mensaje con `print(e)`.

---

Las piezas se combinan de forma natural. Para ejecutar muchas operaciones de manera concurrente, cada una con su propio límite de tiempo, envuelve cada una en una pequeña corrutina que aplique `wait_for` y capture el `TimeoutError`, y luego haz `gather` de los envoltorios:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` retorna entonces un valor para cada trabajo que terminó a tiempo y `None` para cada uno que no, en el orden original, y todo el lote toma como máximo unos `limit` segundos.
