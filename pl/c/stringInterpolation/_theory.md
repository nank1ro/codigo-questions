C nie ma interpolacji łańcuchów: tekst i wartości łączy `printf` za pomocą **łańcucha formatującego**, w którym każdy specyfikator `%` jest zastępowany odpowiadającym mu argumentem. Najczęstsze specyfikatory to:
```c
printf("%d\n", 42);      // wypisuje "42" (int, %i oznacza to samo)
printf("%f\n", 2.5);     // wypisuje "2.500000" (double, domyślnie 6 miejsc po przecinku)
printf("%s\n", "hi");    // wypisuje "hi" (ciąg znaków)
printf("%c\n", 'A');     // wypisuje "A" (pojedynczy znak)
printf("%x\n", 255);     // wypisuje "ff" (int szesnastkowo małymi literami)
printf("100%%\n");       // wypisuje "100%" (dosłowny znak procentu)
```
Specyfikator musi pasować do typu argumentu: wypisanie `double` przez `%d` albo `int` przez `%s` nie konwertuje wartości, tylko wypisuje śmieci lub powoduje awarię.

---

`sprintf` działa dokładnie tak jak `printf`, ale zamiast pisać na ekran zapisuje sformatowany tekst do tablicy `char`, zwanej **buforem**, wraz z kończącym `'\0'`:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // wypisuje "3-7"
```
Bufor musi zostać zadeklarowany przed wywołaniem i musi być dość duży na cały tekst plus znak kończący, inaczej `sprintf` zapisze poza jego końcem.

---

Funkcja, która buduje łańcuch, zwykle otrzymuje bufor jako parametr i wypełnia go przez `sprintf`. Tablica należy do wywołującego, który po wywołaniu może odczytać wynik:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // wypisuje "Hello, Ada!"
```
W tych ćwiczeniach `string.h` jest już dołączony nad twoim kodem, więc do porównania wyniku można użyć `strcmp`.

---

`%x` wypisuje liczbę całkowitą szesnastkowo małymi literami, a `%X` robi to samo wielkimi literami. `%c` przyjmuje całkowity kod znaku i wypisuje znak, który on oznacza, więc `%c` z `65` wypisuje `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // wypisuje "1f 1F B"
```

---

Liczba między `%` a literą ustawia minimalną **szerokość** pola. Wartość jest dopełniana spacjami z lewej strony, a **flagi** umieszczone zaraz po `%` zmieniają to dopełnianie:
```c
printf("[%5d]\n", 42);  // wypisuje "[   42]" wyrównane do prawej na 5 kolumnach
printf("[%-5d]\n", 42); // wypisuje "[42   ]", flaga - wyrównuje do lewej
printf("[%05d]\n", 42); // wypisuje "[00042]", flaga 0 dopełnia zerami
printf("[%+d]\n", 42);  // wypisuje "[+42]", flaga + zawsze pokazuje znak
```
Wartość dłuższa niż szerokość nigdy nie jest obcinana, pole po prostu się powiększa.

---

Szerokość i flagi działają z każdym specyfikatorem, więc `%02x` wypisuje liczbę całkowitą szesnastkowo dopełnioną zerami do dwóch cyfr. Tak właśnie zapisuje się kolory w postaci `#rrggbb`:
```c
printf("%02x\n", 5);   // wypisuje "05"
printf("%02x\n", 255); // wypisuje "ff"
```

---

Kropka, po której następuje liczba, ustawia **precyzję**. Dla `%f` jest to liczba miejsc po przecinku, zaokrąglona; dla `%s` jest to maksymalna liczba wypisywanych znaków:
```c
printf("%.2f\n", 3.14159);    // wypisuje "3.14"
printf("%.3s\n", "formatting"); // wypisuje "for"
```
Szerokość i precyzję można łączyć: `%8.2f` wypisuje dwa miejsca po przecinku wyrównane do prawej na 8 kolumnach.

---

Precyzja to zwykły sposób kontrolowania tego, jak `double` wygląda w łańcuchu. Stosunek taki jak `0.425` staje się procentem po pomnożeniu przez `100` i wypisaniu z jednym miejscem po przecinku oraz `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out to "42.5%"
```

---

`sprintf` i `printf` **zwracają** liczbę zapisanych znaków, nie licząc kończącego `'\0'`. Jest to długość właśnie zbudowanego łańcucha, bez osobnego wywołania `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // wypisuje "3"
```

---

`sprintf` nie wie, jak duży jest bufor. `snprintf` przyjmuje rozmiar bufora jako drugi argument i nigdy nie zapisuje więcej niż `size - 1` znaków plus `'\0'`, w razie potrzeby obcinając tekst. Zwraca długość, jaką miałby **kompletny** tekst, więc wynik większy lub równy `size` oznacza, że wyjście zostało obcięte:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // wypisuje "formatt 10"
```
`sizeof buffer` daje rozmiar tablicy w bajtach, co dla tablicy `char` jest liczbą jej elementów.

---

Porównanie wartości zwróconej przez `snprintf` z rozmiarem bufora mówi, czy wszystko się zmieściło. To bezpieczny wzorzec budowania łańcuchów o nieznanej długości:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out przechowuje tylko pierwsze size - 1 znaków tekstu
}
```

---

Łańcuch można budować w kilku krokach, zapisując każdy fragment zaraz po poprzednim. Wartość zwracana mówi, gdzie kończy się tekst, więc `buffer + n` to adres znaku kończącego i kolejne `sprintf` może kontynuować od tego miejsca:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer to "Hello, world", n wynosi 12
```
Dodawanie każdej zwróconej wartości do `n` sprawia, że `n` pozostaje równe całkowitej długości dotychczas zbudowanego tekstu.

---

Łańcuchy można też łączyć bez łańcucha formatującego. `strcat` z `string.h` dopisuje kopię swojego drugiego argumentu na koniec pierwszego, który musi mieć dość wolnego miejsca, a `strncat` dopisuje co najwyżej podaną liczbę znaków:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text to "Hi!!!"
strncat(text, "abcdef", 2); // text to "Hi!!!ab"
```
Obie zawsze dodają kończące `'\0'` po dopisanych znakach.

---

Gdy nie ma nic do sformatowania, `puts` wypisuje łańcuch zakończony znakiem nowej linii. W przeciwieństwie do `printf` nie interpretuje `%`, więc tekst jest wypisywany dokładnie tak, jak został zapisany:
```c
puts("Done");      // wypisuje "Done" i znak nowej linii
puts("50% off");   // wypisuje "50% off" i znak nowej linii
printf("50% off"); // niezdefiniowane: % off nie jest prawidłowym specyfikatorem
```
`puts` to właściwy wybór dla stałego tekstu, a `printf` wtedy, gdy trzeba wstawić wartości.

---

`strncat` przydaje się, gdy trzeba dopisać tylko część łańcucha albo gdy dopisywany fragment musi być ograniczony do maksymalnej długości:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name to "file.ba"
```
Gdy limit jest większy niż łańcuch, dopisywany jest cały łańcuch.

---

Wszystko razem: wiersz raportu łączy pole tekstowe wyrównane do lewej, separator i liczbę wyrównaną do prawej ze stałą liczbą miejsc po przecinku, zapisany przez `snprintf`, dzięki czemu nigdy nie przepełnia bufora:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out to "Ada   |  9.5"
```
Dopóki każda wartość mieści się w swojej szerokości, wszystkie wiersze mają tę samą długość, więc kolumny są równe, gdy wiersze są wypisywane jeden pod drugim.
