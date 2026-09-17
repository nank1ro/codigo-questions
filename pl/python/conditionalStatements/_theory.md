Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `nice_weather` i wykonać czynność zabawy na zewnątrz `if` ta zmienna jest `True`, jak:
```python
nice_weather = True
if (nice_weather):
    # baw się na dworze
```

---

Kontynuujmy poprzedni przykład.
```python
nice_weather = True
if (nice_weather):
    # baw się na dworze
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
    # baw się na dworze
else:
    # zostań w domu
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

---

Każda instrukcja warunkowa potrzebuje słowa kluczowego `if`, które ją wprowadza. To ono informuje Pythona, że poniższy blok wykonuje się tylko wtedy, gdy warunek jest spełniony.

---

Warunek nie musi być porównaniem — samodzielna wartość logiczna, taka jak `True`, też działa, a blok wykonuje się zawsze, gdy ta wartość to `True`.

---

Tę samą instrukcję można sprawić, by pomijała swój blok, po prostu zmieniając warunek: gdy tylko przyjmie on wartość `False`, Python przeskakuje bezpośrednio nad kodem z wcięciem.

---

Linia `if` w Pythonie składa się z trzech części: słowa kluczowego `if`, warunku oraz dwukropka zamykającego linię. Wszystko, co ma wcięcie po tym dwukropku, stanowi blok.

---

Ponieważ warunek jest tu równy `True`, Python wykonuje linię z wcięciem znajdującą się poniżej i wypisuje `Hello!`.

---

Warunek `False` oznacza, że Python nigdy nie wchodzi do bloku z wcięciem, więc nic w ogóle nie zostaje wydrukowane.

---

Wartość decydująca o tym, czy blok się wykona, nazywana jest warunkiem i zawsze musi przyjmować wartość logiczną, `True` lub `False`.

---

Blok pod `if` nigdy nie może być pusty: Python zgłasza `IndentationError`, gdy po dwukropku nie następuje żadna linia z wcięciem. `pass` to zwykły placeholder używany, gdy nie ma jeszcze nic do wykonania.

---

Dwukropek należy do linii `if`, a nie do bloku: oznacza koniec warunku i zapowiada, że poniższe linie z wcięciem są częścią instrukcji.

---

Gdy warunek ma wartość `False`, Python pomija cały blok z wcięciem i kontynuuje od kolejnej linii, która nie ma wcięcia w ramach `if`.

---

Python nie wymaga nawiasów wokół warunku — `if True:` jest już samodzielną, kompletną instrukcją. Nawiasy pełnią tu funkcję zwykłego grupowania, takiego samego jak w arytmetyce, i nie zmieniają wartości.

---

Blok kodu może zawierać więcej niż jedną linię, a linie wykonują się w kolejności, w jakiej zostały zapisane — instrukcja dodana nad już istniejącą wypisze się jako pierwsza.

---

Zmienna logiczna może być użyta jako warunek zupełnie samodzielnie — nie ma potrzeby wcześniejszego porównywania jej z `True` czy `False`.

---

Gdy warunkiem jest zmienna, `if` odczytuje to, co ta zmienna przechowuje w danym momencie. Zmiana przypisania powyżej wystarczy, by wyłączyć blok, bez dotykania samej linii `if`.

---

Linie z wcięciem należące do instrukcji warunkowej nazywane są jej blokiem kodu — to właśnie wcięcie oznacza ich przynależność do niej.

---

Linia znajdująca się poza wcięciem `if` wykonuje się niezależnie od tego, jaki był warunek, ponieważ nigdy nie była częścią tego bloku.

---

Blok kodu nie jest ograniczony do jednej linii — może być tak krótki lub tak długi, jak wymaga tego logika, o ile wszystkie linie mają spójne wcięcie.

---

Gdy `online` ma wartość `False`, warunek nigdy nie jest spełniony, więc blok jest pomijany i nic nie zostaje wydrukowane.

---

Do bloku `if` należy tylko `print` z wcięciem znajdujący się bezpośrednio po nim; linia zapisana z takim samym wcięciem jak sam `if` już nie.

---

Linia umieszczona po bloku `if`, ale bez dodatkowego wcięcia, nie jest już jego częścią — wykonuje się za każdym razem, niezależnie od tego, jaki był warunek.

---

Blok może zawierać dowolną liczbę instrukcji. Wykonują się one od góry do dołu, a każda z nich musi mieć wcięcie na tym samym poziomie co pozostałe.

---

Przypisanie `True` do zmiennej sprawia, że warunek, który z niej korzysta, jest spełniony, więc znajdujący się pod nim blok się wykonuje.

---

Przypisanie zamiast tego `False` sprawia, że warunek nie jest spełniony, więc blok pod nim jest całkowicie pomijany.

---

Słowo kluczowe `if` rozpoczyna instrukcję warunkową — wraz ze swoim warunkiem decyduje o tym, czy poniższy blok się wykona.

---

`"False"` w cudzysłowie to ciąg znaków, a nie wartość logiczna, a niepusty ciąg znaków zawsze liczy się jako prawda. Tylko samo `False` powstrzymuje wykonanie bloku.
```python
print(bool("False"))  # True
```

---

Wybranie tutaj `True` powoduje wykonanie obu linii w bloku, nie tylko pierwszej — wszystko, co ma wcięcie pod `if`, należy do tego samego bloku.

---

Dwukropek to jedyny element, bez którego linia `if` nie może się obejść: zamyka warunek i otwiera blok. Nawiasy wokół warunku są w Pythonie opcjonalne, więc `if True:` i `if (True):` zachowują się identycznie.

---

Instrukcje takie jak `if`, `elif` i `else`, które wykonują lub pomijają kod na podstawie wartości logicznej, nazywane są zbiorczo instrukcjami warunkowymi.

---

Operator `not` odwraca wartość logiczną: `not True` to `False`, a `not False` to `True`.
```python
is_online = False
print(not is_online)  # True
```

---

`not` tworzy nową wartość logiczną, zamiast modyfikować tę, którą odczytuje, więc po `is_afternoon = not is_morning` zmienna `is_morning` nadal przechowuje swoją pierwotną wartość.

---

Warunek zawsze znajduje się między słowem kluczowym `if` a następującym po nim dwukropkiem, nigdzie indziej w tej linii.

---

Nie ma sztywnego limitu tego, ile linii może zawierać blok `if` — liczy się jedynie to, żeby każda linia miała wcięcie na tym samym poziomie.

---

Literał logiczny jest jak najbardziej dobrym warunkiem: `if True:` za każdym razem wykonuje swój blok. Zapisanie tego jako `if (True):` to dokładnie ta sama instrukcja, ponieważ nawiasy wokół warunku są w Pythonie opcjonalne.

---

Blok kodu instrukcji `if` to grupa linii z wcięciem znajdujących się pod nią, wyróżniona z reszty programu właśnie przez to wcięcie.

---

Warunek zawsze sprowadza się do jednej z dwóch wartości, `True` lub `False` — to właśnie czyni go wartością logiczną.
