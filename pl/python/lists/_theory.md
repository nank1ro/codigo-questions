Listy to typ danych, który pozwala przechowywać kolekcję różnych informacji jako sekwencję pod jedną nazwą zmiennej.
Lista przechowuje wiele wartości dowolnego typu i używa **indeksów** do ich rozróżniania.
Możesz przypisać elementy do listy za pomocą wyrażenia postaci:
```python
list_name = [item1, item2]
```

---

Możesz uzyskać dostęp do pojedynczego elementu listy za pomocą jego indeksu.
Indeks jest jak adres, który identyfikuje miejsce elementu na liście.
Indeks pojawia się bezpośrednio po nazwie listy, w nawiasach kwadratowych, tak jak tutaj:
```python
list_name[index]
```

Indeksy listy zaczynają się od `0`, **nie** od `1`! Dostęp do pierwszego elementu listy uzyskujesz w ten sposób: `list_name[0]`.
Drugi element listy ma indeks 1: `list_name[1]`.

---

Indeks listy zachowuje się jak każda inna nazwa zmiennej! Może być używany zarówno do odczytu, jak i do przypisywania wartości.
Widziałeś, jak uzyskać dostęp do indeksu listy w ten sposób:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
Tak wygląda przypisanie:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

Podobnie jak ciągi znaków, listy mają **długość**.
Długość listy to liczba elementów, które zawiera

---

Lista nie musi mieć stałej długości.
Możesz dodawać elementy na końcu listy w dowolnym momencie!
Aby dodać element do listy, używamy słowa kluczowego `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Czasami chcesz uzyskać dostęp tylko do części listy.
Rozważmy następujący kod:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Najpierw tworzymy listę o nazwie `numbers`.
Następnie bierzemy podsekcję listy i przechowujemy ją w liście slice.
Robimy to, definiując indeksy, które chcemy uwzględnić po nazwie listy: `numbers[1:3]`.
W Pythonie, gdy w ten sposób określamy część listy, uwzględniamy element z pierwszym indeksem, `1`, ale wykluczamy element z drugim indeksem, `3`.

---

Możesz wycinać ciąg znaków dokładnie tak samo jak listę! W rzeczywistości możesz myśleć o ciągach znaków jako o listach znaków: każdy znak jest kolejnym elementem listy, zaczynając od indeksu `0`.
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
Jeśli wycięty fragment listy obejmuje pierwszy lub ostatni element listy (lub ciągu znaków), indeks tego elementu nie musi być podany.

---

Elementy listy mogą być dowolnego typu:
```python
list_name = ["one", 2, True]
```
W rzeczywistości powyżej mamy, w kolejności, ciąg znaków, liczbę całkowitą i wartość logiczną.
Ale możemy też mieć listy zawierające listy!

---

Czasem trzeba wyszukać element na liście.
W Pythonie możemy użyć metody `index()`:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
Powyższy kod drukuje pierwszy indeks zawierający ciąg `"Zac"`, w tym przypadku `1`.
Możemy również wstawiać elementy do listy na określony indeks za pomocą metody `insert()`:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
Powyższy kod wstawia `"Ali"` na indeks `1`, co przesuwa wszystko po tym indeksie o 1

---

W Pythonie możemy bardzo prosto iterować po liście za pomocą słów kluczowych `for..in`:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
Po słowie kluczowym `for` następuje nazwa zmiennej, której zostanie przypisana wartość każdego elementu listy po kolei.

---

**Krotki** są podobne do list, ale znacznie szybsze.
Jednak wartości krotek nie mogą być zmieniane.
Zwykle używamy krotek dla danych **tylko do odczytu**, które pozostają stałe podczas działania programu.
Aby utworzyć krotkę, używamy okrągłych nawiasów `()`

---

Możemy też przekonwertować krotkę na listę za pomocą funkcji `list()`

---

Podobnie możemy przekonwertować listę na krotkę
