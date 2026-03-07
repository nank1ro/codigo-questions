Tablice to typ danych, którego możesz używać do przechowywania kolekcji różnych informacji jako sekwencji pod jedną nazwą zmiennej.
Tablica przechowuje wiele wartości jednego typu i używa **indeksów** do ich rozróżniania.
Możesz przypisać elementy do tablicy wyrażeniem w postaci:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` to typ danych, którego będziesz używać dla tablicy, na przykład `int`, `double` itp.
`array_name` to nazwa zmiennej przechowującej elementy.
`array_size` to maksymalny rozmiar tablicy.
Na końcu, `item1` i `item2` to wartości, które chcemy zapisać w tablicy

---

Możesz uzyskać dostęp do pojedynczego elementu tablicy za pomocą jego indeksu.
Indeks jest jak adres, który identyfikuje miejsce elementu w tablicy.
Indeks pojawia się bezpośrednio po nazwie tablicy, w nawiasach kwadratowych, w następujący sposób:
```
list_name[index];
```

Indeksy tablicy zaczynają się od `0`, **nie** od `1`! Dostęp do pierwszego elementu tablicy uzyskujesz w ten sposób: `list_name[0]`.
Drugi element tablicy ma indeks 1: `list_name[1]`.

---

Indeks listy zachowuje się jak każda inna nazwa zmiennej! Może być używany zarówno do odczytu, jak i do przypisywania wartości.
Widziałeś, jak uzyskać dostęp do indeksu listy w ten sposób:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Gets the value 5
```
Tak działa przypisanie:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // prints the new value 1
```

---

Możesz obliczyć długość tablicy w bajtach, uzyskując `sizeof` tablicy, a następnie podzielić ją przez rozmiar jednego elementu.
Działa to dlatego, że każdy element tablicy ma ten sam typ, a zatem ten sam rozmiar.
Wynikowa *długość* to liczba zawartych w niej elementów

---

Tablica w języku C musi mieć stałą długość.
Nie możesz dodawać elementów na końcu tablicy po zadeklarowaniu jej rozmiaru.

---

W programowaniu w C możesz tworzyć tablice tablic.
Takie tablice są znane jako tablice wielowymiarowe, na przykład:
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
