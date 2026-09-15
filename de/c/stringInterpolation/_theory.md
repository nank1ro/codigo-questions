C hat keine String-Interpolation: Text und Werte werden von `printf` über einen **Formatstring** kombiniert, wobei jeder `%`-Formatbezeichner durch das passende Argument ersetzt wird. Die gängigsten Formatbezeichner sind:
```c
printf("%d\n", 42);      // gibt "42" aus (int, %i ist dasselbe)
printf("%f\n", 2.5);     // gibt "2.500000" aus (double, standardmäßig 6 Nachkommastellen)
printf("%s\n", "hi");    // gibt "hi" aus (String)
printf("%c\n", 'A');     // gibt "A" aus (einzelnes Zeichen)
printf("%x\n", 255);     // gibt "ff" aus (int als hexadezimale Kleinbuchstaben)
printf("100%%\n");       // gibt "100%" aus (ein literales Prozentzeichen)
```
Der Formatbezeichner muss zum Typ des Arguments passen: Gibt man ein `double` mit `%d` oder einen `int` mit `%s` aus, wird der Wert nicht umgewandelt, sondern es erscheint Datenmüll oder das Programm stürzt ab.

---

`sprintf` funktioniert genau wie `printf`, schreibt den formatierten Text aber nicht auf den Bildschirm, sondern in ein char-Array, einen sogenannten **Puffer**, gefolgt vom abschließenden `'\0'`:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // gibt "3-7" aus
```
Der Puffer muss vor dem Aufruf deklariert werden und groß genug für den gesamten Text plus den Terminator sein, sonst schreibt `sprintf` über sein Ende hinaus.

---

Eine Funktion, die einen String erstellt, erhält den Puffer normalerweise als Parameter und füllt ihn mit `sprintf`. Der Aufrufer besitzt das Array und kann nach dem Aufruf das Ergebnis lesen:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // gibt "Hello, Ada!" aus
```
In diesen Übungen ist `string.h` bereits über deinem Code eingebunden, sodass `strcmp` zum Vergleichen des Ergebnisses verwendet werden kann.

---

`%x` gibt eine Ganzzahl hexadezimal mit Kleinbuchstaben aus, und `%X` macht dasselbe mit Großbuchstaben. `%c` nimmt einen Ganzzahl-Zeichencode und gibt das Zeichen aus, für das er steht, daher gibt `%c` mit `65` `A` aus:
```c
printf("%x %X %c\n", 31, 31, 66); // gibt "1f 1F B" aus
```

---

Eine Zahl zwischen `%` und dem Buchstaben legt die minimale **Breite** des Feldes fest. Der Wert wird links mit Leerzeichen aufgefüllt, und **Flags** direkt nach dem `%` ändern diese Auffüllung:
```c
printf("[%5d]\n", 42);  // gibt "[   42]" rechtsbündig in 5 Spalten aus
printf("[%-5d]\n", 42); // gibt "[42   ]" aus, das --Flag richtet linksbündig aus
printf("[%05d]\n", 42); // gibt "[00042]" aus, das 0-Flag füllt mit Nullen auf
printf("[%+d]\n", 42);  // gibt "[+42]" aus, das +-Flag zeigt das Vorzeichen immer an
```
Ein Wert, der länger als die Breite ist, wird nie abgeschnitten, das Feld wächst einfach mit.

---

Breite und Flags funktionieren mit jedem Formatbezeichner, daher gibt `%02x` eine Ganzzahl als mit Nullen auf zwei Stellen aufgefülltes Hexadezimalformat aus. So werden Farben als `#rrggbb` geschrieben:
```c
printf("%02x\n", 5);   // gibt "05" aus
printf("%02x\n", 255); // gibt "ff" aus
```

---

Ein Punkt gefolgt von einer Zahl legt die **Genauigkeit** fest. Bei `%f` ist sie die Anzahl der Dezimalstellen, gerundet; bei `%s` die maximale Anzahl ausgegebener Zeichen:
```c
printf("%.2f\n", 3.14159);    // gibt "3.14" aus
printf("%.3s\n", "formatting"); // gibt "for" aus
```
Breite und Genauigkeit können kombiniert werden: `%8.2f` gibt zwei Dezimalstellen rechtsbündig in 8 Spalten aus.

---

Die Genauigkeit ist die übliche Möglichkeit festzulegen, wie ein `double` in einem String aussieht. Ein Verhältnis wie `0.425` wird zu einer Prozentangabe, indem man mit `100` multipliziert und eine Dezimalstelle gefolgt von `%%` ausgibt:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out ist "42.5%"
```

---

`sprintf` und `printf` **geben** die Anzahl der geschriebenen Zeichen **zurück**, ohne den abschließenden `'\0'` zu zählen. Das ist die Länge des gerade erstellten Strings, ganz ohne separaten `strlen`-Aufruf:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // gibt "3" aus
```

---

`sprintf` weiß nicht, wie groß der Puffer ist. `snprintf` nimmt die Puffergröße als zweites Argument entgegen und schreibt nie mehr als `size - 1` Zeichen plus das `'\0'`, wobei es den Text bei Bedarf abschneidet. Sein Rückgabewert ist die Länge, die der **vollständige** Text gehabt hätte, bedeutet also ein Ergebnis größer oder gleich `size`, dass die Ausgabe abgeschnitten wurde:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // gibt "formatt 10" aus
```
`sizeof buffer` liefert die Größe des Arrays in Bytes, was bei einem char-Array dessen Anzahl an Elementen ist.

---

Vergleicht man den Rückgabewert von `snprintf` mit der Puffergröße, weiß man, ob alles hineingepasst hat. Das ist das sichere Muster, um Strings unbekannter Länge zu erstellen:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out enthält nur die ersten size - 1 Zeichen von text
}
```

---

Ein String kann in mehreren Schritten erstellt werden, indem man jedes Teil direkt hinter das vorherige schreibt. Der Rückgabewert verrät, wo der Text endet, daher ist `buffer + n` die Adresse des Terminators und das nächste `sprintf` kann von dort weitermachen:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer ist "Hello, world", n ist 12
```
Addiert man jeden Rückgabewert zu `n`, bleibt es gleich der Gesamtlänge des bisher erstellten Texts.

---

Strings lassen sich auch ohne einen Formatstring kombinieren. `strcat` aus `string.h` hängt eine Kopie seines zweiten Arguments an das Ende des ersten an, das genug freien Platz haben muss, und `strncat` hängt höchstens eine gegebene Anzahl von Zeichen an:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text ist "Hi!!!"
strncat(text, "abcdef", 2); // text ist "Hi!!!ab"
```
Beide fügen nach den angehängten Zeichen immer den abschließenden `'\0'` hinzu.

---

Wenn es nichts zu formatieren gibt, gibt `puts` einen String gefolgt von einem Zeilenumbruch aus. Anders als `printf` interpretiert es `%` nicht, daher wird der Text genau so ausgegeben, wie er geschrieben ist:
```c
puts("Done");      // gibt "Done" und einen Zeilenumbruch aus
puts("50% off");   // gibt "50% off" und einen Zeilenumbruch aus
printf("50% off"); // undefiniert: % off ist kein gültiger Formatbezeichner
```
`puts` ist die richtige Wahl für festen Text und `printf`, wenn Werte eingefügt werden müssen.

---

`strncat` ist nützlich, wenn nur ein Teil eines Strings angehängt werden soll oder wenn das angehängte Stück auf eine maximale Länge begrenzt werden muss:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name ist "file.ba"
```
Ist das Limit größer als der String, wird der ganze String angehängt.

---

Zum Schluss alles zusammen: Eine Berichtszeile kombiniert ein linksbündiges Textfeld, einen Trenner und eine rechtsbündige Zahl mit fester Anzahl von Dezimalstellen, geschrieben mit `snprintf`, damit der Puffer nie überläuft:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out ist "Ada   |  9.5"
```
Solange jeder Wert in seine Breite passt, haben alle Zeilen die gleiche Länge, sodass die Spalten fluchten, wenn die Zeilen untereinander ausgegeben werden.
