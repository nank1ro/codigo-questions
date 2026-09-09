C nie ma interpolacji łańcuchów: tekst i wartości łączy `printf` za pomocą **łańcucha formatującego**, w którym każdy specyfikator `%` jest zastępowany odpowiadającym mu argumentem. Najczęstsze specyfikatory to:
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
Specyfikator musi pasować do typu argumentu: wypisanie `double` przez `%d` albo `int` przez `%s` nie konwertuje wartości, tylko wypisuje śmieci lub powoduje awarię.

---

`sprintf` działa dokładnie tak jak `printf`, ale zamiast pisać na ekran zapisuje sformatowany tekst do tablicy `char`, zwanej **buforem**, wraz z kończącym `'\0'`:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
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
printf("%s\n", message); // prints "Hello, Ada!"
```
W tych ćwiczeniach `string.h` jest już dołączony nad twoim kodem, więc do porównania wyniku można użyć `strcmp`.

---

`%x` wypisuje liczbę całkowitą szesnastkowo małymi literami, a `%X` robi to samo wielkimi literami. `%c` przyjmuje całkowity kod znaku i wypisuje znak, który on oznacza, więc `%c` z `65` wypisuje `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

Liczba między `%` a literą ustawia minimalną **szerokość** pola. Wartość jest dopełniana spacjami z lewej strony, a **flagi** umieszczone zaraz po `%` zmieniają to dopełnianie:
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
Wartość dłuższa niż szerokość nigdy nie jest obcinana, pole po prostu się powiększa.

---

Szerokość i flagi działają z każdym specyfikatorem, więc `%02x` wypisuje liczbę całkowitą szesnastkowo dopełnioną zerami do dwóch cyfr. Tak właśnie zapisuje się kolory w postaci `#rrggbb`:
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

Kropka, po której następuje liczba, ustawia **precyzję**. Dla `%f` jest to liczba miejsc po przecinku, zaokrąglona; dla `%s` jest to maksymalna liczba wypisywanych znaków:
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
Szerokość i precyzję można łączyć: `%8.2f` wypisuje dwa miejsca po przecinku wyrównane do prawej na 8 kolumnach.

---

Precyzja to zwykły sposób kontrolowania tego, jak `double` wygląda w łańcuchu. Stosunek taki jak `0.425` staje się procentem po pomnożeniu przez `100` i wypisaniu z jednym miejscem po przecinku oraz `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf` i `printf` **zwracają** liczbę zapisanych znaków, nie licząc kończącego `'\0'`. Jest to długość właśnie zbudowanego łańcucha, bez osobnego wywołania `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf` nie wie, jak duży jest bufor. `snprintf` przyjmuje rozmiar bufora jako drugi argument i nigdy nie zapisuje więcej niż `size - 1` znaków plus `'\0'`, w razie potrzeby obcinając tekst. Zwraca długość, jaką miałby **kompletny** tekst, więc wynik większy lub równy `size` oznacza, że wyjście zostało obcięte:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer` daje rozmiar tablicy w bajtach, co dla tablicy `char` jest liczbą jej elementów.

---

Porównanie wartości zwróconej przez `snprintf` z rozmiarem bufora mówi, czy wszystko się zmieściło. To bezpieczny wzorzec budowania łańcuchów o nieznanej długości:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

Łańcuch można budować w kilku krokach, zapisując każdy fragment zaraz po poprzednim. Wartość zwracana mówi, gdzie kończy się tekst, więc `buffer + n` to adres znaku kończącego i kolejne `sprintf` może kontynuować od tego miejsca:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
Dodawanie każdej zwróconej wartości do `n` sprawia, że `n` pozostaje równe całkowitej długości dotychczas zbudowanego tekstu.

---

Łańcuchy można też łączyć bez łańcucha formatującego. `strcat` z `string.h` dopisuje kopię swojego drugiego argumentu na koniec pierwszego, który musi mieć dość wolnego miejsca, a `strncat` dopisuje co najwyżej podaną liczbę znaków:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
Obie zawsze dodają kończące `'\0'` po dopisanych znakach.

---

Gdy nie ma nic do sformatowania, `puts` wypisuje łańcuch zakończony znakiem nowej linii. W przeciwieństwie do `printf` nie interpretuje `%`, więc tekst jest wypisywany dokładnie tak, jak został zapisany:
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
`puts` to właściwy wybór dla stałego tekstu, a `printf` wtedy, gdy trzeba wstawić wartości.

---

`strncat` przydaje się, gdy trzeba dopisać tylko część łańcucha albo gdy dopisywany fragment musi być ograniczony do maksymalnej długości:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
Gdy limit jest większy niż łańcuch, dopisywany jest cały łańcuch.

---

Wszystko razem: wiersz raportu łączy pole tekstowe wyrównane do lewej, separator i liczbę wyrównaną do prawej ze stałą liczbą miejsc po przecinku, zapisany przez `snprintf`, dzięki czemu nigdy nie przepełnia bufora:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
Dopóki każda wartość mieści się w swojej szerokości, wszystkie wiersze mają tę samą długość, więc kolumny są równe, gdy wiersze są wypisywane jeden pod drugim.
