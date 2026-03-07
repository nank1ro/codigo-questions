Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest pewien warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną boolowską `nice_weather` i wykonać akcję zabawy na zewnątrz `if`, gdy ta zmienna jest `true`, na przykład:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Kontynuujmy poprzedni przykład.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
