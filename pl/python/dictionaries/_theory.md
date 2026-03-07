**Słowniki** są podobne do list i krotek, ale dostęp do wartości uzyskuje się przez wyszukiwanie *klucza*, a nie indeksu.
Klucz może być dowolnym ciągiem znaków lub liczbą.
Słowniki są otoczone nawiasami klamrowymi, na przykład:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
To jest słownik o nazwie `d` z trzema *parami klucz-wartość*.
Klucz `key1` wskazuje na wartość `1`, `key2` na `2` i tak dalej.

---

Dostęp do wartości słownika za pomocą klucza działa tak samo jak dostęp do wartości listy za pomocą indeksu:
```python
user['age']
# pobiera wartość age ze słownika user
```

---

Podobnie jak listy, słowniki są _mutowalne_.
Oznacza to, że można je zmieniać po ich utworzeniu.
Jedną z zalet tego jest możliwość dodawania nowych _par klucz/wartość_ do słownika po jego utworzeniu w taki sposób:
```python
dict_name[new_key_name] = new_value
```

---

Długość `len()` słownika to liczba _par klucz-wartość_, które zawiera.
Każda para liczy się tylko raz, nawet jeśli wartość jest listą. (Zgadza się: wewnątrz słowników można też umieszczać listy!)

---

Ponieważ słowniki są mutowalne, można je zmieniać na wiele sposobów. Elementy można usuwać ze słownika za pomocą polecenia `del`:
```python
del dict_name[key_name]
```
usunie klucz `key_name` i jego skojarzoną wartość ze słownika.

---

Co jeśli chcemy wylistować wszystkie klucze słownika?
Do tego służy metoda `keys()`.

---

Co jeśli chcemy wylistować wszystkie wartości słownika?
Do tego służy metoda `values()`.

---

Podobnie jak w listach, możemy iterować po elementach słownika używając słów kluczowych `for..in`.
Aby uzyskać zarówno klucz, jak i wartość w pętli, możemy użyć metody `items()`:
```python
for key, value in dict_name:
    print(key, value)
```

---

Możemy również użyć słowa kluczowego `in`, którego używaliśmy z pętlami, aby sprawdzić, czy słownik zawiera określony __klucz__

---

Aby __dodać__ lub __zmienić__ wartości w słowniku, możemy również użyć metody `update()` z _parami klucz-wartość_, które chcemy dodać w nawiasach klamrowych

---

A co jeśli chcemy __usunąć__ wartość ze słownika?
Do tego służy metoda `pop()`:
```python
dict_name.pop("key_name")
```
