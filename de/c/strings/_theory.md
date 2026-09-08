C hat keinen eigenen String-Typ: ein **String** ist ein Array aus `char`, das mit einem besonderen Zeichen endet, dem **Null-Terminator** `'\0'`.
Der einfachste Weg, einen zu erstellen, ist ein String-Literal zwischen doppelten Anführungszeichen:
```c
char name[] = "Codigo";
```
Der Compiler zählt die Zeichen und fügt am Ende automatisch das `'\0'` hinzu.
Um einen String auszugeben, verwendest du den Platzhalter `%s`:
```c
printf("%s\n", name);
// gibt "Codigo" aus
```

---

Der Null-Terminator belegt Speicherplatz: das Literal `"hi"` belegt 3 Bytes, `'h'`, `'i'` und `'\0'`.
Wenn du die Größe selbst festlegst, lass immer Platz dafür:
```c
char word[6] = "hello"; // 5 Buchstaben + '\0'
```
Ohne den Terminator hat C keine Möglichkeit zu wissen, wo der String endet.

---

Der Header `string.h` stellt Funktionen bereit, die mit Strings arbeiten.
`strlen` gibt die Anzahl der Zeichen vor dem Null-Terminator zurück (der Terminator selbst wird nicht mitgezählt):
```c
strlen("hello"); // 5
```
Eine Funktion, die einen String empfängt, deklariert den Parameter als `char *text`, einen Zeiger auf das erste Zeichen.
In diesen Übungen sind `string.h` und `ctype.h` bereits oberhalb deines Codes eingebunden.

---

Da ein String ein Array ist, hat jedes Zeichen einen Index, beginnend bei `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Ein einzelnes Zeichen wird mit `%c` ausgegeben. Zeichen können auch ersetzt werden:
```c
word[0] = 'K'; // word ist jetzt "Koding"
```

---

Da jeder String mit `'\0'` endet, kannst du ihn durchlaufen, ohne seine Länge im Voraus zu kennen: mach weiter, solange das aktuelle Zeichen nicht der Terminator ist.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Ein Array kann nach seiner Deklaration nicht mit `=` zugewiesen werden:
```c
char copy[20];
copy = "Codigo"; // Fehler
```
Um einen String zu kopieren, verwende `strcpy(destination, source)` aus `string.h`.
Das Ziel muss groß genug sein, um alle Zeichen plus das `'\0'` aufzunehmen.

---

`strcat(destination, source)` hängt `source` an das Ende von `destination` an:
```c
char text[20] = "Hello";
strcat(text, " World");
// text ist jetzt "Hello World"
```
Wie bei `strcpy` muss das Ziel-Array genug Platz für das Ergebnis haben.

---

Zwei Strings können nicht mit `==` verglichen werden: das würde ihre Adressen im Speicher vergleichen, nicht ihre Zeichen.
Verwende stattdessen `strcmp(first, second)`, das `0` zurückgibt, wenn beide Strings genau dieselben Zeichen enthalten:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // nicht 0
```

---

`strcmp` vergleicht die Strings Zeichen für Zeichen anhand ihrer Zeichencodes.
Das Ergebnis ist negativ, wenn der erste String vor dem zweiten kommt, positiv, wenn er danach kommt, und `0`, wenn sie gleich sind:
```c
strcmp("a", "b"); // negativ
strcmp("b", "a"); // positiv
```

---

`strncpy(destination, source, n)` kopiert höchstens `n` Zeichen.
Wenn `source` länger als `n` ist, wird kein `'\0'` geschrieben: du musst das Ergebnis selbst terminieren.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix ist "Cod"
```

---

Der Header `ctype.h` stellt Funktionen bereit, die mit einem einzelnen Zeichen arbeiten.
`toupper(c)` gibt die Großbuchstaben-Version eines Buchstabens zurück und `tolower(c)` die Kleinbuchstaben-Version; jedes andere Zeichen wird unverändert zurückgegeben:
```c
char letter = toupper('a'); // 'A'
```

---

Ein String wird an eine Funktion als Zeiger übergeben, sodass eine Funktion, die `char *text` empfängt, die Zeichen des Aufrufers direkt verändern kann.
Die Kombination einer Schleife bis `'\0'` mit `toupper` wandelt einen ganzen String um:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` funktioniert wie `printf`, schreibt den formatierten Text aber in ein char-Array statt auf den Bildschirm:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer ist "3 items"
```
Der Puffer muss groß genug für den gesamten Text und sein `'\0'` sein.

---

`sprintf` ist eine praktische Möglichkeit, eine Zahl in Text umzuwandeln: sobald sie in einem Puffer steht, kann jede String-Funktion damit arbeiten.
