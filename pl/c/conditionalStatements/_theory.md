Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest pewien warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną boolowską `nice_weather` i wykonać akcję zabawy na zewnątrz `if`, gdy ta zmienna jest `true`, na przykład:
```c
bool nice_weather = true;
if (nice_weather) {
    // baw się na dworze
}
```

---

Kontynuujmy poprzedni przykład.
```c
bool nice_weather = true;
if (nice_weather) {
    // baw się na dworze
}
```
Widzieliśmy, że instrukcja `if` wykonuje blok kodu tylko wtedy, gdy warunek jest `true`.
Inną ważną rzeczą do rozważenia są **nawiasy klamrowe** `{}`, które oznaczają blok kodu.

---

Właśnie zobaczyliśmy, jak wykonać blok kodu, gdy warunek jest spełniony; teraz zobaczmy, jak wykonać inny blok kodu, gdy pierwszy warunek nie jest spełniony.
Wychodzimy bawić się na zewnątrz, gdy pogoda jest ładna; w przeciwnym razie zostajemy w domu.
W C możemy użyć instrukcji `else`, na przykład:
```c
bool nice_weather = false;
if (nice_weather) {
    // baw się na dworze
} else {
    // zostań w domu
}
```

---

Załóżmy, że mamy kolejny warunek do sprawdzenia, jak w tym przykładzie:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
a wynik tego kodu to `the number is 3`.
Najpierw sprawdźmy, czy liczba jest równa 2 – to jest fałsz.
Przejdźmy więc do drugiej instrukcji i sprawdźmy, czy `num` jest równe 3 – będąc prawdą, wykonujemy następny blok kodu, drukując `the number is 3`

---

Możemy dodać tyle instrukcji `else if`, ile chcemy – nie ma żadnych ograniczeń
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
a wynik tego kodu to `the number is 4`.

---

Możemy również zagnieżdżać instrukcję warunkową (`if`, `else if` lub `else`) wewnątrz innej instrukcji warunkowej, aby stworzyć bardziej złożoną strukturę.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
a wynik tego kodu to `the number is 4`.

---

Czas przełożyć składnię instrukcji `if` na praktykę: słowo kluczowe, warunek w nawiasach oraz blok kodu ujęty w nawiasy klamrowe.
```c
if (condition) {
    // wykonuje się, gdy warunek jest prawdziwy
}
```

---

Literały logiczne w C to `true` i `false`: pisane małymi literami, bez cudzysłowów, zdefiniowane w `<stdbool.h>`, a nie wbudowane w sam język. Zapisanie `True` nie skompiluje się jako warunek — działa tylko forma pisana małymi literami, a gdy ma wartość `true`, blok się wykonuje.

---

C nie ma osobnego testu logicznego: warunek jest prawdziwy, gdy jego wartość jest różna od zera. `false` z `<stdbool.h>` to po prostu `0`, więc blok zabezpieczony takim warunkiem nigdy się nie wykonuje.

---

Instrukcja `if` w C składa się z trzech części: słowa kluczowego `if`, warunku w nawiasach oraz bloku w nawiasach klamrowych. Nawiasy są wymagane — to dzięki nim kompilator wie, gdzie kończy się warunek.

---

Każda instrukcja warunkowa zaczyna się od słowa kluczowego, które informuje kompilator, że przed podjęciem decyzji, co wykona się dalej, trzeba sprawdzić warunek.

---

Warunek będący literałem `true` jest zawsze prawdziwy, więc blok się wykonuje, a jego `printf` działa dokładnie tak, jak zostało napisane.

---

Warunek będący literałem `false` nigdy nie jest prawdziwy, więc blok jest całkowicie pomijany i nic w jego wnętrzu się nie wykonuje.

---

Warunki to wartości, które sprawdza instrukcja `if`: gdy warunek ma wartość `true`, blok się wykonuje, gdy `false` — jest pomijany.

---

Nawias otwierający może znajdować się w tej samej linii co warunek albo w linii poniżej. C ignoruje złamanie linii, więc oba style kompilują się do dokładnie tego samego programu.

---

Nawiasy wokół warunku są częścią składni `if` w C, a nie opcjonalnym grupowaniem: `if true { ... }` się nie skompiluje.

---

`"false"` w cudzysłowie to ciąg znaków, a nie wartość logiczna — a ciąg znaków w warunku to niezerowy adres, który liczy się jako prawda. Tylko `false` bez cudzysłowu powstrzymuje wykonanie bloku.

---

Odstępy między elementami linii `if` są w C dowolne: `if(true){` oraz `if (true) {` to dla kompilatora ta sama instrukcja, liczy się tylko kolejność elementów.

---

Blok kodu nie jest ograniczony do jednej instrukcji. Każda instrukcja między nawiasami klamrowymi wykonuje się kolejno, w takiej kolejności, w jakiej została zapisana.

---

Zmienna logiczna może być użyta bezpośrednio jako warunek, bez potrzeby porównania. Ponieważ `online` ma już wartość `true`, samo napisanie `if (online)` wystarczy, by wykonać blok.

---

Zmienna typu `bool` działa jako warunek, ponieważ `if` sprawdza jedynie wartość przechowywaną w niej w danym momencie. Gdy w `online` znajduje się `false`, `if (online)` zachowuje się dokładnie tak jak `if (false)`.

---

Warunkowy jest wyłącznie kod znajdujący się między nawiasami klamrowymi instrukcji `if`. Wszystko, co zostało napisane po nawiasie zamykającym, wykonuje się bezwarunkowo, niezależnie od tego, jaki był warunek.

---

Nie ma stałego limitu tego, ile instrukcji może zawierać blok kodu — jedna linia czy sto, wszystkie wykonują się razem, gdy warunek ma wartość `true`.

---

Odczytanie zmiennej logicznej jako warunku działa tak samo jak literał: skoro `online` ma wartość `true`, blok się wykonuje, a jego `printf` działa.

---

Gdy `online` ma zamiast tego wartość `false`, warunek jest fałszywy, więc blok jest całkowicie pomijany i nic z wnętrza tych nawiasów nie zostaje wydrukowane.
