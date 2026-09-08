Czasami potrzebujesz maleńkiej funkcji tylko raz, na przykład żeby podwoić liczbę.
Pisanie pełnego bloku `def` wydaje się wtedy zbyt rozbudowane.
Python oferuje krótszą formę: wyrażenie **lambda**, _anonimową_ funkcję zapisaną w jednej linii:
```python
lambda x: x * 2
```
Składnia to `lambda parametry: wyrażenie`.
Lambda nie ma nazwy, ale możesz zapisać ją w zmiennej i wywołać jak każdą inną funkcję:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Zauważ, że ciało lambdy nie ma słowa kluczowego `return`.
Ciało to **pojedyncze wyrażenie**, którego wartość jest zwracana automatycznie:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Lambda może przyjmować **więcej niż jeden parametr**.
Oddziel je przecinkami, dokładnie tak jak w funkcji `def`:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Ponieważ ciało musi być pojedynczym wyrażeniem, lambda **nie może zawierać instrukcji**.
Żadnego `return`, żadnych bloków `if`, pętli ani przypisań:
```python
# SyntaxError
increment = lambda x: return x + 1
```
Jeśli potrzebujesz czegoś z tego, napisz zwykłą funkcję `def`.

---

Parametry lambdy również obsługują **wartości domyślne**:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Nie musisz nawet zapisywać lambdy: możesz **wywołać ją od razu**.
Umieść lambdę w nawiasach, a następnie dodaj argumenty:
```python
print((lambda x: x + 1)(4))  # 5
```

---

Lambdy naprawdę błyszczą jako **argumenty przekazywane do innych funkcji**.
`sorted()` przyjmuje parametr `key`: funkcję wywoływaną dla każdego elementu, której wynik decyduje o kolejności.
Lambda pasuje tu idealnie:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

Lambda użyta w `key` może wybrać dowolną część elementu.
Dla listy list, `lambda p: p[1]` sortuje według drugiego elementu każdej wewnętrznej listy.

---

`map()` stosuje funkcję do **każdego elementu** listy.
Zwraca specjalny _obiekt map_, więc opakuj go w `list()`, aby zobaczyć wartości:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` zachowuje tylko te elementy, dla których funkcja zwraca `True`:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Wypisanie obiektu `map` bezpośrednio nie pokazuje jego wartości: otrzymasz coś w rodzaju `<map object at 0x7f2b1c>`.
Dopiero `list()` (albo pętla) zamienia go w oczekiwane wartości.

---

Lambdy nie ograniczają się do funkcji wbudowanych: **twoje własne funkcje** też mogą przyjmować funkcję jako parametr i ją wywoływać.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` i `min()` również przyjmują funkcję `key`, tak jak `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**Kiedy powinieneś preferować `def`?**
Lambda świetnie sprawdza się jako krótka, jednorazowa funkcja przekazywana jako argument.
Jeśli logika wymaga nazwy, kilku linii, docstringa lub jest używana w wielu miejscach, funkcja `def` jest czytelniejsza.
Ostatnia sztuczka: `sorted()` przyjmuje też `reverse=True`, aby najpierw uzyskać największe wartości:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
