In Python ist eine Funktion ein **Wert**, genau wie eine Zahl oder eine Zeichenkette. Du kannst sie in einer Variablen speichern, in eine Liste legen oder an eine andere Funktion übergeben. Nur die Klammern rufen sie auf: `shout` ist die Funktion selbst, `shout("hi")` ist ihr Ergebnis:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Eine Funktion, die eine andere Funktion als Parameter erhält oder eine zurückgibt, heißt **Funktion höherer Ordnung**. Innerhalb von ihr wird der Parameter wie jede andere Funktion mit Klammern aufgerufen:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Eine Funktion als Argument zu übergeben lässt den Aufrufer entscheiden, **was** getan wird, während die Funktion höherer Ordnung entscheidet, **wie oft** oder **auf was**. Der Funktionsparameter kann so oft wie nötig aufgerufen werden, und sein Ergebnis kann ihm wieder zugeführt werden:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Jedes Callable funktioniert: eine `def`-Funktion, eine eingebaute Funktion wie `len` oder eine lambda.

---

Die eingebaute Funktion `map(func, iterable)` ruft `func` für jedes Element auf und erzeugt die Ergebnisse, eines pro Element. Sie gibt ein träges *map object* zurück, also wickle es in `list()`, um die Werte zu sehen:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Du kannst jedes Callable übergeben, nicht nur eine lambda: eine eingebaute Funktion wie `len` oder eine Methode aus ihrer Klasse wie `str.upper`, die die Zeichenkette als erstes Argument erhält:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

Die eingebaute Funktion `filter(func, iterable)` behält nur die Elemente, für die `func` einen wahren Wert zurückgibt. Wie `map` gibt sie ein träges Objekt zurück, das in eine Liste umgewandelt werden muss:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
Die an `filter` übergebene Funktion heißt **Prädikat**: Sie nimmt ein Element entgegen und beantwortet eine Ja/Nein-Frage dazu. Übergibst du stattdessen `None`, behält `filter` die Elemente, die von sich aus wahr sind, und verwirft `0`, `""` und `None`.

---

`sorted(iterable, key=func)` ordnet die Elemente nach dem Wert, den `func` für jedes von ihnen zurückgibt, ohne die Elemente selbst zu verändern. Mit `reverse=True` erhältst du das Größte zuerst:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
Die Sortierung ist **stabil**: Elemente mit gleichen Schlüsseln behalten ihre ursprüngliche Reihenfolge. Die `key`-Funktion wird einmal pro Element aufgerufen und ihre Ergebnisse dienen nur dem Vergleich, daher enthält die Ausgabe weiterhin die ursprünglichen Wörter, nicht ihre Längen.

---

Die `key`-Funktion kann einen **beliebigen Teil** eines Elements auswählen. Bei einer Liste von Tupeln sortiert `lambda s: s[1]` nach dem zweiten Eintrag jedes Tupels; bei einer Liste von Wörterbüchern sortiert `lambda d: d["age"]` nach einem Wert:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` und `max` akzeptieren denselben `key`-Parameter, daher gibt `max(pairs, key=lambda p: p[1])` `('a', 3)` zurück: das ganze Tupel, nicht nur die Zahl.

---

Eine Funktion kann auch eine Funktion **zurückgeben**. Definiere eine innere Funktion mit `def` und gib sie zurück, ohne sie aufzurufen:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
Die innere Funktion verwendet `greeting` auch dann weiter, wenn `make_greeter` bereits fertig ist: Sie **merkt sich** die Variablen des Gültigkeitsbereichs, in dem sie erstellt wurde. So eine Funktion heißt **Closure**. Jeder Aufruf von `make_greeter` erstellt eine neue, unabhängige Closure mit ihrem eigenen `greeting`.

---

Eine Closure kann die Variablen der umgebenden Funktion lesen, aber eine Zuweisung an eine von ihnen erstellt stattdessen eine **neue lokale** Variable. Um die äußere Variable zu aktualisieren, deklariere sie mit `nonlocal` innerhalb der inneren Funktion:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` würde `count` auf Modulebene suchen, wo es nicht existiert. Mit `nonlocal` aktualisiert jeder Aufruf der zurückgegebenen Funktion dasselbe `count`, sodass die Closure den Zustand zwischen den Aufrufen trägt, wie ein winziges Objekt.

---

`reduce(func, iterable, initial)` aus dem Modul `functools` faltet eine Sequenz zu einem **einzelnen Wert** zusammen. Es ruft `func` mit dem bisherigen Ergebnis und dem nächsten Element auf, beginnend mit `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
Die Schritte sind `0 + 1`, dann `1 + 2`, dann `3 + 3`. Lässt du `initial` weg, wird das erste Element als Startwert verwendet, aber dann wirft eine leere Sequenz einen `TypeError`, gib also einen Anfangswert an, wann immer die Sequenz leer sein kann.

---

`partial(func, *fixed)` aus `functools` baut eine neue Funktion, bei der einige Argumente **bereits ausgefüllt** sind. Beim Aufruf des Ergebnisses gibst du die übrigen an:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Positionale Argumente an `partial` füllen die ersten Parameter; Schlüsselwortargumente legen einen Parameter über seinen Namen fest und können beim Aufruf noch überschrieben werden. Ein partial ist ein gewöhnliches Callable, daher kannst du es an `map`, `sorted` oder jede andere Funktion höherer Ordnung übergeben.

---

`partial` ist praktisch bei eingebauten Funktionen mit Optionen. `int(text, base=16)` zerlegt eine hexadezimale Zeichenkette; legst du die Basis fest, entsteht ein Konverter mit einem Argument, der zu `map` passt:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
Das partial-Objekt merkt sich, was es umhüllt: `hex_to_int.func` ist `int` und `hex_to_int.keywords` ist `{'base': 16}`.

---

Ein **Decorator** ist eine Funktion höherer Ordnung, die eine Funktion entgegennimmt und eine neue zurückgibt, die sie umhüllt, meist um Verhalten vor oder nach dem ursprünglichen Aufruf hinzuzufügen:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` ist der Name, mit dem die Funktion definiert wurde. Den Decorator anzuwenden ist nur ein Aufruf: `greet = announce(greet)`. Die `@`-Syntax in der Zeile **über** einem `def` macht genau das:
```python
@announce
def greet(name):
    return "Hello, " + name
```
Der Decorator muss definiert sein, bevor du ihn mit `@` verwendest, denn die Ersetzung geschieht, sobald das `def` ausgeführt wird.

---

Ein Decorator, der nur ein Argument akzeptiert, ist wenig nützlich. Um **jede** Funktion zu umhüllen, sammelt der Wrapper jedes positionale Argument in `*args` und jedes Schlüsselwortargument in `**kwargs` und reicht sie unverändert weiter:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
Im Wrapper ist `args` ein Tupel und `kwargs` ein Wörterbuch; das `*` und `**` im Aufruf entpacken sie wieder in einzelne Argumente.

---

`any(iterable)` gibt `True` zurück, wenn **mindestens ein** Element wahr ist, `all(iterable)`, wenn **jedes** Element wahr ist. Sie passen natürlich zu einem **Generatorausdruck**: einer List Comprehension ohne die eckigen Klammern, die die Werte einzeln erzeugt, statt eine Liste zu bauen:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Da die Werte träge erzeugt werden, stoppt `any` beim ersten `True` und `all` beim ersten `False`, ohne den Rest auszuwerten. `sum` akzeptiert ebenfalls einen Generatorausdruck: `sum(1 for age in ages if age >= 18)` zählt die Erwachsenen.
