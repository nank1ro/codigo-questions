Python jest obiektowym językiem programowania, co oznacza, że operuje na konstruktach programistycznych zwanych obiektami.
Możesz myśleć o obiekcie jako o pojedynczej strukturze danych, która zawiera zarówno dane, jak i funkcje; funkcje obiektu są nazywane jego metodami.
Na przykład, gdy wywołujesz:
```python
dict_name.items()
```
Python sprawdza, czy `my_dict` ma metodę `items()` (którą mają wszystkie słowniki) i wykonuje tę metodę, jeśli ją znajdzie.

---

Podstawowa klasa składa się tylko ze słowa kluczowego `class` i nazwy klasy, na przykład:
```python
class ClassName:
    pass
```

---

Zastąpmy `pass` czymś innym.
Metoda `__init__()` jest wymagana dla klas i służy do __inicjalizacji__ tworzonych przez nią obiektów.
`__init__()` zawsze przyjmuje co najmniej jeden argument, `self`, który odnosi się do tworzonego obiektu.
Możesz myśleć o `__init__()` jak o metodzie, która uruchamia każdy obiekt tworzony przez klasę.

---

Oczywiście metoda `__init__()` może przyjmować więcej parametrów niż tylko `self`

---

Pierwszy argument `__init__()` służy do odwoływania się do obiektu instancji i zgodnie z konwencją argument ten nosi nazwę `self`.
Jeśli dodasz dodatkowe argumenty (na przykład `gender` i `legs` dla swojego zwierzęcia), ustawienie każdego z nich jako równego `self.gender` i `self.legs` w ciele `__init__()` sprawi, że podczas tworzenia obiektu instancji klasy `Animal` będziesz musiał podać dla każdej instancji płeć i liczbę nóg, które zostaną skojarzone z tworzoną instancją

---

Zdefiniowanie klasy nie tworzy obiektu.
Aby to zrobić, musimy utworzyć __instancję__ klasy

---

Gdy klasa ma własne funkcje, te funkcje są nazywane __metodami__. Widziałeś już jedną taką metodę: `__init__()`.
Możesz jednak definiować własne metody!
