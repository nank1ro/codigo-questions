Zacznijmy od relacyjnego operatora **równości** `==`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy dwa wyrażenia są równe, na przykład:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Przejdźmy do relacyjnego operatora **nierówności** `!=`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy dwa wyrażenia **NIE** są równe, na przykład:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Jest to dokładne przeciwieństwo operatora *równości*

---

Przejdźmy do relacyjnego operatora **większości** `>`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy jedno wyrażenie jest większe od drugiego, na przykład:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Przejdźmy do relacyjnego operatora **mniejszości** `<`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Przejdźmy do relacyjnego operatora **większy lub równy** `>=`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Przejdźmy do relacyjnego operatora **mniejszy lub równy** `<=`.
Zwraca on wartość **logiczną** (`True` lub `False`) określającą, czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Teraz poznajmy operatory **logiczne**, zacznijmy od pierwszego o nazwie `and`.
Zwraca on pierwszy operand, który ma wartość *False*, lub ostatni, jeśli wszystkie mają wartość *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Przejdźmy do logicznego operatora **or**.
Zwraca on pierwszy operand, który ma wartość *True*, lub ostatni, jeśli wszystkie mają wartość *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Zakończmy na logicznym operatorze **not**.
Zwraca on wartość logiczną będącą odwrotnością stanu logicznego wyrażenia.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
