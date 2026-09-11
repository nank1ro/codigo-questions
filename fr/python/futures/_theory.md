Certaines opérations prennent du temps : lire un fichier, appeler un serveur, attendre un minuteur. Python peut exécuter ce type de code **de manière asynchrone** avec le module `asyncio`, afin qu'une tâche puisse attendre sans bloquer les autres.

Une fonction définie avec `async def` est une **fonction coroutine**. L'appeler n'exécute pas son corps : elle renvoie un **objet coroutine** qui décrit le travail à faire. `asyncio.run(coro)` démarre une boucle d'événements, exécute la coroutine jusqu'à son terme puis arrête la boucle :
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` est le point d'entrée d'un programme asynchrone et est appelé une seule fois, depuis du code synchrone classique.

---

Une coroutine peut prendre des paramètres et `return` une valeur exactement comme une fonction normale. La valeur n'est pas disponible à la création de l'objet coroutine, mais seulement une fois que la coroutine a été exécutée. `asyncio.run` renvoie ce que la coroutine a retourné :
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
Tout ce que vous savez sur les fonctions s'applique toujours à l'intérieur de `async def` : variables locales, conditions, boucles et plusieurs instructions `return`.

---

`await` met en pause la coroutine courante jusqu'à ce que l'opération attendue se termine, puis donne son résultat. Pendant que la coroutine est en pause, la boucle d'événements est libre d'exécuter d'autres coroutines. `await` n'est autorisé qu'à l'intérieur d'un `async def`.

`asyncio.sleep(seconds)` est l'objet awaitable le plus simple : il attend pendant la durée indiquée sans bloquer la boucle. Contrairement à `time.sleep`, il doit être attendu avec `await` :
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
Le programme affiche `ready`, attend 50 millisecondes puis affiche `go`. Écrire `asyncio.sleep(0.05)` sans `await` crée l'objet coroutine mais ne l'exécute jamais, donc aucune attente n'a lieu.

---

Appeler une fonction coroutine ne suffit pas pour l'exécuter. L'appel construit seulement un objet coroutine ; le corps s'exécute quand cet objet est attendu avec `await` ou passé à `asyncio.run` :
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python le signale même par un avertissement : `RuntimeWarning: coroutine 'hello' was never awaited`. Un `await` oublié est le bug asynchrone le plus courant : le code semble appelé mais ne s'exécute jamais, et toute variable censée recevoir son résultat contient à la place un objet coroutine.

---

Les coroutines s'appellent entre elles avec `await`. Une coroutine peut attendre n'importe quelle autre coroutine, recevoir sa valeur de retour et continuer, exactement comme une chaîne d'appels de fonctions :
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
Seule la coroutine la plus externe passe par `asyncio.run` ; toutes les internes sont atteintes avec `await`. Si `total` était un `def` classique, elle ne pourrait pas utiliser `await` du tout : le mot-clé `async` se propage à chaque fonction de la chaîne qui a besoin d'attendre.

---

Attendre des coroutines les unes après les autres avec `await` les exécute **séquentiellement** : trois attentes de 10 millisecondes prennent 30 millisecondes. `asyncio.gather` exécute plusieurs coroutines **de manière concurrente** : pendant que l'une dort, les autres progressent, donc les trois attentes prennent ensemble environ 10 millisecondes. Elle renvoie une liste avec les résultats dans le même ordre que les arguments :
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
`gather` doit elle-même être attendue avec `await`, et elle prend les coroutines comme arguments séparés. Pour passer une liste, décompressez-la : `asyncio.gather(*coroutines)`.

---

La concurrence est payante lorsque le nombre d'opérations n'est pas fixe. Construisez les objets coroutine dans une list comprehension, décompressez-les dans `gather` et attendez-les tous avec `await` en une seule fois :
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
Dix urls prennent toujours environ 20 millisecondes au total au lieu de 200, et les résultats restent dans l'ordre des urls.

---

Avec `gather`, les coroutines se partagent la main à chaque `await`. Une coroutine s'exécute jusqu'à ce qu'elle attende quelque chose qui n'est pas prêt, puis la boucle passe à une autre. Les effets de bord tels que `print` se produisent donc dans l'ordre où les coroutines **reprennent**, et non dans l'ordre où elles ont été passées :
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
Ceci affiche `b`, puis `a`, puis `['a', 'b']` : `b` se réveille en premier, mais la liste des résultats conserve l'ordre des arguments.

---

Un petit programme asynchrone suit une forme fixe : importer `asyncio`, définir les fonctions coroutine, définir une coroutine `main` qui les attend avec `await`, et enfin appeler `asyncio.run(main())` une seule fois à la fin.

---

`asyncio.create_task(coro)` enveloppe une coroutine dans une **Task** et la planifie pour s'exécuter en arrière-plan. Contrairement à `await`, elle renvoie immédiatement, donc la coroutine courante peut continuer à travailler pendant que la tâche s'exécute. La tâche démarre réellement au prochain moment où la coroutine courante se met en pause sur un `await`. Attendre la tâche plus tard avec `await` donne son résultat :
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
Ceci affiche d'abord `main continues`, car `background` ne démarre que lorsque `main` attend avec `await`, puis `task started` et `task done`.

---

Une tâche continue de s'exécuter que quelqu'un l'attende ou non. Créez-la tôt, faites autre chose, et attendez-la avec `await` seulement au moment où son résultat est nécessaire : l'attente est plus courte car une partie de la tâche a déjà été exécutée en arrière-plan. Une tâche peut aussi être inspectée avec `task.done()`, qui renvoie `True` une fois qu'elle est terminée.

---

Une exception levée à l'intérieur d'une coroutine n'apparaît pas là où l'objet coroutine a été créé : elle est levée au `await` qui l'exécute, ou par `asyncio.run` pour la plus externe. `try`/`except` doit donc englober le **`await`** :
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
Une exception que personne n'intercepte se propage à travers chaque `await` jusqu'à `asyncio.run`, qui la relève dans le code synchrone, exactement comme une pile d'appels normale.

---

Quand l'une des coroutines passées à `gather` lève une exception, celle-ci se propage à la ligne `await asyncio.gather(...)` et les résultats des autres sont perdus, bien qu'elles continuent de s'exécuter. Passer `return_exceptions=True` change cela : `gather` ne lève jamais d'exception, et l'objet exception prend la place du résultat manquant dans la liste :
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
Chaque élément peut ensuite être vérifié avec `isinstance(result, Exception)` pour séparer les échecs des valeurs.

---

`asyncio.wait_for(awaitable, timeout)` attend quelque chose avec `await` mais abandonne après `timeout` secondes : l'opération est annulée et une `TimeoutError` est levée, qui peut être interceptée comme n'importe quelle exception :
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
Avec un timeout de `0.1`, le même code afficherait `done`. `asyncio.TimeoutError` est un autre nom de la `TimeoutError` native.

---

Gérer une coroutine qui échoue suit le schéma synchrone : la coroutine lève l'exception, l'appelant englobe le `await` dans un `try`/`except` et décide quoi faire de l'objet erreur, par exemple afficher son message avec `print(e)`.

---

Les pièces se combinent naturellement. Pour exécuter beaucoup d'opérations de manière concurrente, chacune avec sa propre limite de temps, enveloppez chacune dans une petite coroutine qui applique `wait_for` et intercepte la `TimeoutError`, puis passez les enveloppes à `gather` :
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` renvoie alors une valeur pour chaque tâche terminée à temps et `None` pour chacune de celles qui ne l'ont pas été, dans l'ordre d'origine, et le lot entier prend au plus environ `limit` secondes.
