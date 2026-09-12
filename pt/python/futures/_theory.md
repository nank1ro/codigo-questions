Algumas operações levam tempo: ler um arquivo, chamar um servidor, esperar por um temporizador. Python pode executar esse código de forma **assíncrona** com o módulo `asyncio`, de modo que uma tarefa possa esperar sem bloquear as outras.

Uma função definida com `async def` é uma **função corrotina**. Chamá-la não executa o seu corpo: ela retorna um **objeto de corrotina** que descreve o trabalho a fazer. `asyncio.run(coro)` inicia um loop de eventos, roda a corrotina até o fim e para o loop:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` é o ponto de entrada de um programa assíncrono e é chamado uma vez, a partir de código síncrono regular.

---

Uma corrotina pode receber parâmetros e `return` um valor exatamente como uma função normal. O valor não está disponível quando o objeto de corrotina é criado, mas apenas quando a corrotina já foi executada. `asyncio.run` retorna aquilo que a corrotina retornou:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Tudo o que você sabe sobre funções continua valendo dentro de `async def`: variáveis locais, condições, laços e múltiplas instruções `return`.

---

`await` pausa a corrotina atual até que a operação aguardada seja concluída e então devolve o seu resultado. Enquanto a corrotina está pausada, o loop de eventos fica livre para rodar outras corrotinas. `await` só é permitido dentro de um `async def`.

`asyncio.sleep(seconds)` é o awaitable mais simples: ele espera pelo tempo dado sem bloquear o loop. Diferente de `time.sleep`, ele precisa ser aguardado:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
O programa exibe `ready`, espera 50 milissegundos e exibe `go`. Escrever `asyncio.sleep(0.05)` sem `await` cria o objeto de corrotina, mas nunca o executa, então nenhuma espera acontece.

---

Chamar uma função corrotina não é suficiente para executá-la. A chamada apenas constrói um objeto de corrotina; o corpo roda quando esse objeto é aguardado ou passado a `asyncio.run`:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python até emite um aviso sobre isso: `RuntimeWarning: coroutine 'hello' was never awaited`. Um `await` esquecido é o bug assíncrono mais comum: o código parece chamado, mas nunca executa, e qualquer variável que deveria guardar o seu resultado guarda em vez disso um objeto de corrotina.

---

Corrotinas chamam umas às outras com `await`. Uma corrotina pode aguardar qualquer outra corrotina, receber o seu valor de retorno e continuar, exatamente como uma cadeia de chamadas de função:
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
Apenas a corrotina mais externa passa por `asyncio.run`; cada uma interna é alcançada com `await`. Se `total` fosse um `def` comum, ela não poderia usar `await` de forma alguma: a palavra-chave `async` se espalha para cada função da cadeia que precisa esperar.

---

Aguardar corrotinas uma após a outra as executa **sequencialmente**: três esperas de 10 milissegundos levam 30 milissegundos. `asyncio.gather` roda várias corrotinas **concorrentemente**: enquanto uma dorme, as outras progridem, então as três esperas juntas levam cerca de 10 milissegundos. Ele retorna uma lista com os resultados na mesma ordem dos argumentos:
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
O próprio `gather` precisa ser aguardado, e ele recebe as corrotinas como argumentos separados. Para passar uma lista, desempacote-a: `asyncio.gather(*coroutines)`.

---

A concorrência compensa quando o número de operações não é fixo. Construa os objetos de corrotina numa list comprehension, desempacote-os no `gather` e aguarde o lote inteiro de uma vez:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Dez urls ainda levam cerca de 20 milissegundos no total em vez de 200, e os resultados permanecem na ordem das urls.

---

Com `gather`, as corrotinas se alternam a cada `await`. Uma corrotina roda até aguardar algo que não está pronto, então o loop troca para outra. Efeitos colaterais como `print` acontecem, portanto, na ordem em que as corrotinas **retomam**, não na ordem em que foram passadas:
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
Isso exibe `b`, depois `a`, depois `['a', 'b']`: `b` acorda primeiro, mas a lista de resultados mantém a ordem dos argumentos.

---

Um pequeno programa assíncrono segue uma forma fixa: importe `asyncio`, defina as funções corrotinas, defina uma corrotina `main` que as aguarde e, por fim, chame `asyncio.run(main())` uma vez no final.

---

`asyncio.create_task(coro)` envolve uma corrotina numa **Task** e a agenda para rodar em segundo plano. Diferente de `await`, ele retorna imediatamente, então a corrotina atual pode continuar trabalhando enquanto a tarefa roda. A tarefa na verdade começa na próxima vez que a corrotina atual pausa num `await`. Aguardar a tarefa mais tarde dá o seu resultado:
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
Isso exibe `main continues` primeiro, porque `background` só começa quando `main` aguarda, e depois `task started` e `task done`.

---

Uma tarefa continua rodando haja ou não alguém esperando por ela. Crie-a cedo, faça outro trabalho e faça `await` dela apenas no ponto em que o seu resultado for necessário: a espera é mais curta porque parte da tarefa já rodou em segundo plano. Uma tarefa também pode ser inspecionada com `task.done()`, que retorna `True` assim que ela termina.

---

Uma exceção lançada dentro de uma corrotina não aparece onde o objeto de corrotina foi criado: ela é lançada no `await` que a executa, ou pelo `asyncio.run` para a mais externa. O `try`/`except` precisa, portanto, envolver o **`await`**:
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
Uma exceção que ninguém captura se propaga por cada `await` até o `asyncio.run`, que a relança no código síncrono, exatamente como uma pilha de chamadas normal.

---

Quando uma das corrotinas passadas ao `gather` lança uma exceção, ela se propaga para a linha `await asyncio.gather(...)` e os resultados das outras são perdidos, embora continuem rodando. Passar `return_exceptions=True` muda isso: o `gather` nunca lança, e o objeto de exceção toma o lugar do resultado ausente na lista:
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
Cada elemento pode então ser verificado com `isinstance(result, Exception)` para separar as falhas dos valores.

---

`asyncio.wait_for(awaitable, timeout)` aguarda algo, mas desiste depois de `timeout` segundos: a operação é cancelada e um `TimeoutError` é lançado, que pode ser capturado como qualquer exceção:
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
Com um timeout de `0.1`, o mesmo código exibiria `done`. `asyncio.TimeoutError` é outro nome para o `TimeoutError` embutido.

---

Tratar uma corrotina que falha segue o padrão síncrono: a corrotina lança uma exceção, quem chama envolve o `await` num `try`/`except` e decide o que fazer com o objeto de erro, por exemplo exibir a sua mensagem com `print(e)`.

---

As peças se combinam naturalmente. Para rodar muitas operações concorrentemente, cada uma com o seu próprio limite de tempo, envolva cada uma numa pequena corrotina que aplica `wait_for` e captura o `TimeoutError`, e então faça `gather` dos invólucros:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` então retorna um valor para cada job que terminou a tempo e `None` para cada um que não terminou, na ordem original, e o lote inteiro leva cerca de `limit` segundos no máximo.
