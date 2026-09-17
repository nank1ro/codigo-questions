Eine **Ausnahme (Exception)** ist Pythons Art zu sagen, dass eine Anweisung nicht ausgeführt werden kann. Eine Division durch null, die Umwandlung von `"abc"` in eine ganze Zahl oder der Zugriff auf einen fehlenden Wörterbuchschlüssel lösen jeweils eine aus. Wenn nichts sie behandelt, stoppt das Programm genau dort und gibt einen **Traceback** aus:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
Der Traceback listet die Zeilen auf, die ausgeführt wurden, und die letzte Zeile nennt den **Ausnahmetyp** (`ZeroDivisionError`) und seine Meldung (`division by zero`). Diese letzte Zeile solltest du zuerst lesen.

Um das Programm am Leben zu halten, packe die riskante Anweisung in einen `try`-Block und beschreibe die Wiederherstellung in einem `except`-Block:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python führt den `try`-Block aus; wird die genannte Ausnahme ausgelöst, springt es direkt zum passenden `except`-Block und macht mit dem Rest des Programms weiter.

---

Der `try`-Block stoppt bei der **ersten** Anweisung, die eine Ausnahme auslöst; die Zeilen danach werden übersprungen und die Steuerung geht zum `except`-Block über. Nichts im `try`-Block wird rückgängig gemacht, halte ihn also so kurz wie möglich:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
Ein `return` innerhalb von `except` funktioniert wie jedes andere `return`, was `try`/`except` zu einer natürlichen Methode macht, um einen Ersatzwert zurückzugeben, statt abzustürzen.

---

Eine Ausnahme, auf die kein `except`-Block passt, reist weiter nach außen: aus der Zeile heraus, aus der Funktion, die sie ausgeführt hat, aus deren Aufrufer und so weiter. Wenn nichts sie abfängt, bevor sie die oberste Ebene des Programms erreicht, gibt Python den Traceback aus und der Prozess endet mit einem Exit-Status ungleich null. Die Zeilen nach der fehlgeschlagenen Anweisung laufen nie.

---

Eine `except`-Klausel fängt nur den Typ, den sie nennt, und dessen Unterklassen. Das ist der Sinn der Sache: Alles andere reist weiter nach außen, sodass ein Fehler, den du nicht erwartet hast, immer noch als Traceback auftaucht, statt verschluckt zu werden.

`int(text)` löst eine **`ValueError`** aus, wenn der Text keine ganze Zahl beschreibt; das ist also der Typ, den man beim Einlesen von Benutzereingaben nennt:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
`ValueError` hier zu nennen ist eine Entscheidung, keine Formalität: `int(None)` löst einen `TypeError` aus, den diese Funktion absichtlich **nicht** abfängt, denn `None` zu übergeben ist ein Programmierfehler und sollte sichtbar bleiben.

---

Den schmalsten Typ zu wählen, der den erwarteten Fehler abdeckt, macht Fehlerbehandlung vertrauenswürdig. Eine Funktion, die Text liest, sollte sich von schlechtem Text erholen (`ValueError`), darf aber nicht verbergen, dass sie mit der falschen Art von Argument aufgerufen wurde (`TypeError`) — dieser Fehler gehört zum Aufrufer, also lass ihn durch.

---

Auf einen `try`-Block können **mehrere** `except`-Klauseln folgen, die jeweils einen anderen Fehler mit einer anderen Wiederherstellung behandeln. Python vergleicht die ausgelöste Ausnahme von oben nach unten mit ihnen und führt die **erste** passende aus; die übrigen werden übersprungen:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Da der erste Treffer gewinnt, kommt es auf die Reihenfolge an, wenn die Typen verwandt sind: Eine Klausel für einen allgemeinen Typ über einer Klausel für einen spezifischeren würde immer gewinnen und die spezielle Klausel unerreichbar machen.

---

Wenn mehrere Fehler dieselbe Wiederherstellung verdienen, ist es kürzer, sie als Tupel in einer Klausel aufzulisten, als den Block zu wiederholen:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Die Klammern sind erforderlich: `except ValueError, ZeroDivisionError:` ist in Python 3 ein Syntaxfehler. Ein Tupel ist trotzdem eine explizite Liste von Typen.

---

`except:` ohne Typ dahinter ist ein **nacktes except** (bare except). Es passt auf alles, auch auf Ausnahmen, die mit der Operation, die du absichern wolltest, nichts zu tun haben. Die Regel ist also einfach: Nenne immer die Typen, von denen du dich wirklich erholen kannst.

---

Eine Ausnahme ist ein Objekt, und `as` bindet es an einen Namen, damit der Handler sich es ansehen kann:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — das verwenden auch `print(e)` und ein f-Slot — liefert die Meldung, mit der die Ausnahme erzeugt wurde, und `type(e).__name__` liefert den Klassennamen als Text. Der Name, den `as` bindet, existiert nur innerhalb des `except`-Blocks; Python löscht ihn, wenn der Block endet.

---

Auf einen `try`-Block kann ein `else`-Block folgen, der **nur dann läuft, wenn der `try`-Block ohne Auslösung durchlief**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
`print(number * 2)` in den `try`-Block zu setzen würde auch funktionieren, aber dann würde ein `ValueError`, den das Ausgeben selbst auslöst, für einen Umwandlungsfehler gehalten. `else` hält den `try`-Block auf die eine abgesicherte Anweisung beschränkt und nimmt alles auf, was im Erfolgsfall passieren soll.

---

Ein `finally`-Block läuft **immer, was auch passiert**: nach einem sauberen `try`-Block, nach einem `except`-Block, sogar während eine Ausnahme, die niemand abgefangen hat, nach außen reist, und sogar wenn der `try`- oder `except`-Block ein `return` ausführt:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Beide Wege geben `done` aus, bevor der Wert die Funktion verlässt. Diese Garantie ist der Zweck von `finally`: eine Datei schließen, eine Sperre freigeben, eine Einstellung zurücksetzen. Die vollständige Form ist `try` / `except` / `else` / `finally`; ein `try` braucht mindestens ein `except` oder ein `finally`, und `else` funktioniert nur zusammen mit einem `except`.

---

Auch dein eigener Code kann Ausnahmen auslösen, mit der `raise`-Anweisung, gefolgt von einem Ausnahmeobjekt:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` stoppt die Funktion sofort, genau wie ein eingebauter Fehler es täte. Stattdessen einen Fehlerwert zurückzugeben — `-1`, `None`, `False` — vergisst ein Aufrufer leicht; eine Ausnahme kann nicht versehentlich ignoriert werden.

Wähle den Typ, der das Problem beschreibt: `ValueError`, wenn das Argument den richtigen Typ hat, aber einen unmöglichen Wert, `TypeError`, wenn es ganz den falschen Typ hat. Der an die Ausnahme übergebene Text ist ihre Meldung.

---

Eine Handvoll eingebauter Ausnahmen deckt die meisten alltäglichen Fehler ab:

| Ausnahme | Ausgelöst, wenn | Beispiel |
|---|---|---|
| `ValueError` | der Typ stimmt, aber der Wert ist unmöglich | `int("abc")` |
| `TypeError` | der Typ selbst ist falsch | `"x" + 1` |
| `ZeroDivisionError` | eine Division oder Modulo hat einen Nulldivisor | `1 / 0` |
| `KeyError` | ein Wörterbuch hat keinen solchen Schlüssel | `{"a": 1}["b"]` |
| `IndexError` | ein Sequenzindex ist außerhalb des Bereichs | `[1, 2][5]` |

Zu einer dieser Ausnahmen zu greifen, statt einen neuen Typ zu erfinden, hält deine Fehler für jeden lesbar, der Python kennt.

---

Manchmal soll ein Handler auf einen Fehler reagieren, ohne die Verantwortung dafür zu übernehmen: ihn mitprotokollieren, ihn mitzählen, etwas schließen — und dann den Aufrufer damit umgehen lassen. Ein `raise` allein innerhalb eines `except`-Blocks **löst die behandelte Ausnahme erneut aus**, mit ihrem ursprünglichen Typ, ihrer Meldung und ihrem Traceback unversehrt:
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
Würdest du stattdessen `raise ValueError(...)` schreiben, entstünde eine neue Ausnahme mit einem neuen Traceback — es wäre nicht mehr derselbe Fehler, den du gefangen hast, und genau diese Identität bewahrt ein alleinstehendes `raise`.

---

Wenn kein eingebauter Typ passt, definiere deinen eigenen, indem du von `Exception` erbst. Ein leerer Körper genügt meist — der Name ist die Botschaft an den Leser:
```python
class ConfigError(Exception):
    pass
```
Sie verhält sich wie jede andere Ausnahme: `raise ConfigError("bad port")` löst sie aus, und `except ConfigError:` fängt sie ab.

Einen Fehler auf niedriger Ebene in deinen eigenen Typ zu übersetzen ist üblich, und der ursprüngliche Fehler sollte dabei nicht verloren gehen. `raise NewError(...) from original` **verkettet** beide: Es speichert `original` im `__cause__`-Attribut der neuen Ausnahme, und der Traceback zeigt beide unter *The above exception was the direct cause of the following exception* an:
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
Ohne `from e` hängen die beiden weiterhin implizit zusammen, aber `from` sagt laut heraus, dass der erste Fehler den zweiten verursacht hat.
