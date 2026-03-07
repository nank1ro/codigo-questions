Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `nice_weather` i wykonać czynność zabawy na zewnątrz `if` ta zmienna jest `True`, jak:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Kontynuujmy poprzedni przykład.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
Widzieliśmy, że instrukcja `if` wykonuje blok kodu tylko wtedy, gdy warunek jest `True`.
Inną ważną rzeczą do rozważenia są **dwukropki** `:` i **wcięcia**, które wskazują początek bloku kodu.
Wcięcie odnosi się do spacji na początku linii kodu.
Podczas gdy w innych językach programowania wcięcie w kodzie służy tylko do czytelności, w Pythonie wcięcie jest niezbędne.
Możesz używać dowolnej liczby spacji (2, 4, 6, 8), przy czym preferowana jest 4.
Tutaj w aplikacji sugerujemy użycie klawisza **TAB** do wcięcia wierszy kodu

---

Właśnie zobaczyliśmy, jak wykonać blok kodu, gdy wystąpi warunek, teraz zobaczmy, jak wykonać inny blok kodu, gdy pierwszy warunek nie jest spełniony.
Idziemy bawić się na zewnątrz, jeśli pogoda jest ładna; w przeciwnym razie zostajemy w domu.
W Pythonie możemy użyć instrukcji `else`, jak:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

Załóżmy, że mamy kolejny warunek do sprawdzenia, jak w tym przykładzie:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
a wynik tego kodu to `the number is 3`.
Przede wszystkim sprawdźmy, czy liczba jest równa 2, to jest fałsz.
Przejdźmy więc do drugiej instrukcji i sprawdźmy, czy `num` jest równe 3, będąc prawdą, wykonujemy następujący blok kodu, drukując `the number is 3`

---

Możemy dodać tyle instrukcji `elif`, ile chcemy, nie ma żadnych ograniczeń
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
a wynik tego kodu to `the number is 4`.

---

Możemy również zagnieżdżać instrukcję warunkową (`if`, `elif` lub `else`) wewnątrz innej instrukcji warunkowej, aby stworzyć bardziej złożoną strukturę.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
a wynik tego kodu to `the number is 4`.
