W C nie ma dedykowanego typu string: **ciąg znaków** to tablica `char`, która kończy się specjalnym znakiem, **terminatorem null** `'\0'`.
Najprostszym sposobem na jego utworzenie jest literał ciągu znaków w cudzysłowie:
```c
char name[] = "Codigo";
```
Kompilator liczy znaki i sam dodaje na końcu `'\0'`.
Aby wyświetlić ciąg znaków, użyj specyfikatora `%s`:
```c
printf("%s\n", name);
// prints "Codigo"
```

---

Terminator null zajmuje miejsce w pamięci: literał `"hi"` zajmuje 3 bajty: `'h'`, `'i'` i `'\0'`.
Gdy sam deklarujesz rozmiar, zawsze zostaw dla niego miejsce:
```c
char word[6] = "hello"; // 5 letters + '\0'
```
Bez terminatora C nie ma jak wiedzieć, gdzie kończy się ciąg znaków.

---

Nagłówek `string.h` udostępnia funkcje działające na ciągach znaków.
`strlen` zwraca liczbę znaków przed terminatorem null (sam terminator nie jest liczony):
```c
strlen("hello"); // 5
```
Funkcja, która otrzymuje ciąg znaków, deklaruje parametr jako `char *text` — wskaźnik na pierwszy znak.
W tych ćwiczeniach `string.h` i `ctype.h` są już dołączone nad twoim kodem.

---

Ponieważ ciąg znaków jest tablicą, każdy znak ma indeks zaczynający się od `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Pojedynczy znak wyświetla się za pomocą `%c`. Znaki można też podmieniać:
```c
word[0] = 'K'; // word is now "Koding"
```

---

Ponieważ każdy ciąg znaków kończy się `'\0'`, możesz go przejść, nie znając wcześniej jego długości: kontynuuj, dopóki bieżący znak nie jest terminatorem.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Tablicy nie można przypisać wartości operatorem `=` po jej deklaracji:
```c
char copy[20];
copy = "Codigo"; // error
```
Aby skopiować ciąg znaków, użyj `strcpy(destination, source)` z `string.h`.
Cel musi być wystarczająco duży, aby pomieścić wszystkie znaki plus `'\0'`.

---

`strcat(destination, source)` dołącza `source` na końcu `destination`:
```c
char text[20] = "Hello";
strcat(text, " World");
// text is now "Hello World"
```
Podobnie jak w `strcpy`, tablica docelowa musi mieć wystarczająco dużo miejsca na wynik.

---

Dwóch ciągów znaków nie można porównać operatorem `==`: porównałoby to ich adresy w pamięci, a nie znaki.
Użyj zamiast tego `strcmp(first, second)`, która zwraca `0`, gdy oba ciągi zawierają dokładnie te same znaki:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // not 0
```

---

`strcmp` porównuje ciągi znak po znaku, używając ich kodów znaków.
Wynik jest ujemny, gdy pierwszy ciąg jest wcześniejszy od drugiego, dodatni, gdy jest późniejszy, i `0`, gdy są równe:
```c
strcmp("a", "b"); // negative
strcmp("b", "a"); // positive
```

---

`strncpy(destination, source, n)` kopiuje co najwyżej `n` znaków.
Jeśli `source` jest dłuższe niż `n`, żaden `'\0'` nie zostaje zapisany: musisz sam zakończyć wynik.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix is "Cod"
```

---

Nagłówek `ctype.h` udostępnia funkcje działające na pojedynczym znaku.
`toupper(c)` zwraca wielką literę, a `tolower(c)` małą; każdy inny znak jest zwracany bez zmian:
```c
char letter = toupper('a'); // 'A'
```

---

Ciąg znaków jest przekazywany do funkcji jako wskaźnik, więc funkcja przyjmująca `char *text` może zmienić znaki wywołującego bezpośrednio.
Połączenie pętli aż do `'\0'` z `toupper` zamienia cały ciąg znaków:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` działa jak `printf`, ale zapisuje sformatowany tekst do tablicy znaków zamiast na ekran:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer is "3 items"
```
Bufor musi być wystarczająco duży na cały tekst i jego `'\0'`.

---

`sprintf` to wygodny sposób na zamianę liczby na tekst: gdy trafi już do bufora, może na niej działać każda funkcja ciągów znaków.
