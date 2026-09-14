Jede Ganzzahl wird im Speicher als Reihe von **Bits** gespeichert, jedes davon entweder `0` oder `1`. Die Zahl `12` wird als `00001100` gespeichert und die Zahl `10` als `00001010`.
**Bitweise Operatoren** wirken auf diese einzelnen Bits statt auf die Zahl als Ganzes. Der **Und**-Operator `&` vergleicht die beiden Werte Bit für Bit und behält nur dort eine `1`, wo *beide* Bits `1` sind:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// prints "8"
```
Bitmuster schreibt man üblicherweise als hexadezimale Literale wie `0x0C`, weil jede Hexziffer genau vier Bits darstellt. Verwende für die Bitarbeit immer `unsigned`-Typen und gib sie mit `%u` aus.

---

Der **Oder**-Operator `|` vergleicht die beiden Werte Bit für Bit und behält eine `1`, wo *mindestens ein* Bit `1` ist:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// prints "14"
```
`|` ist die übliche Art, zwei Bitmuster zu einem zu verschmelzen.

---

Der **XOR**-Operator `^` (exklusives Oder) behält nur dort eine `1`, wo die beiden Bits *verschieden* sind:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// prints "6"
```
Daraus folgt eine nützliche Eigenschaft: Wendet man dasselbe XOR zweimal an, erhält man den ursprünglichen Wert zurück.

---

Der **Nicht**-Operator `~` nimmt einen einzelnen Operanden und dreht jedes seiner Bits um: jedes `0` wird zu `1` und jedes `1` wird zu `0`.
Ein `unsigned int` enthält 32 Bits, daher dreht `~0x0Fu` alle 32 um und erzeugt eine sehr große Zahl. Um nur das Byte zu behalten, das dich interessiert, kombiniere `~` mit `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// prints "240"
```
`~` bindet stärker als `&`, wird also zuerst angewendet.
Verwechsle `~` nicht mit dem logischen `!`: `!` betrachtet den gesamten Wert und liefert `0` oder `1`, während `~` jedes Bit umschreibt.

---

Der **Links-Shift**-Operator `<<` verschiebt jedes Bit um eine Anzahl von Stellen nach links und füllt die frei gewordenen Stellen rechts mit Nullen:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// prints "12"
```
Verschiebt man um `n` nach links, multipliziert das den Wert mit 2 hoch `n`.
Zwei Fehler machen ein C-Programm undefiniert: das Links-Schieben eines negativen Werts und das Verschieben um einen Betrag, der gleich oder größer als die Breite des Typs ist (32 bei `unsigned int`). Mit **unsigned**-Werten zu arbeiten bewahrt dich vor dem ersten.

---

Der **Rechts-Shift**-Operator `>>` verschiebt jedes Bit nach rechts; die Bits, die am rechten Ende herausfallen, werden verworfen. Bei einem unsigned-Wert werden die frei gewordenen Stellen links mit Nullen gefüllt:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// prints "3"
```
Verschiebt man einen unsigned-Wert um `n` nach rechts, teilt das ihn durch 2 hoch `n` und verwirft den Rest.
Das Rechts-Schieben eines *negativen* Werts ist nicht portabel, was ein weiterer Grund ist, die Bitarbeit auf `unsigned`-Typen zu betreiben.

---

Jeder binäre bitweise Operator hat eine Form als **zusammengesetzte Zuweisung**, die eine Variable an Ort und Stelle aktualisiert: `&=`, `|=`, `^=`, `<<=` und `>>=`.
```c
unsigned int x = 12;
x &= 10;  // same as x = x & 10;
x |= 1;   // same as x = x | 1;
x ^= 3;   // same as x = x ^ 3;
x <<= 1;  // same as x = x << 1;
x >>= 2;  // same as x = x >> 2;
```
Sie sind besser lesbar, als den Variablennamen zu wiederholen, und sind die übliche Art, die Bits einer Flag-Variablen zu ändern.

---

Eine **Maske** ist ein Wert, dessen Bits den Teil eines anderen Werts auswählen, der dich interessiert. Kombiniert mit `&` behält eine Maske die Bits, die in der Maske `1` sind, und setzt alle anderen auf Null:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// prints "11"
```
`0x0F` behält die unteren vier Bits, das sogenannte untere **Nibble**, und `0xFF` behält die unteren acht Bits, ein ganzes Byte.

---

Bits werden ab `0` nummeriert, beginnend beim rechten Bit, daher ist `1u << n` eine Maske, in der nur Bit `n` eingeschaltet ist.
Um ein einzelnes Bit zu **setzen**, es also einzuschalten, ohne die anderen anzufassen, verknüpfst du den Wert per Oder mit dieser Maske:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// prints "6"
```
War das Bit bereits an, ändert sich der Wert nicht, was das Setzen eines Bits sicher wiederholbar macht.

---

Um ein einzelnes Bit zu **löschen**, es also auszuschalten, verknüpfst du den Wert per Und mit dem *Inversen* der Maske:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// prints "5"
```
`~(1u << 1)` ist ein Wert, bei dem jedes Bit an ist außer Bit `1`, daher lässt das Und alles andere unangetastet.

---

Um ein einzelnes Bit zu **toggeln**, es also zu kippen, egal wie sein aktueller Zustand ist, verknüpfst du den Wert per XOR mit der Maske:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// prints "7"
```
Weil XOR sich selbst rückgängig macht, liefert das erneute Toggeln desselben Bits wieder den ursprünglichen Wert.

---

Um ein einzelnes Bit zu **testen**, verknüpfst du den Wert per Und mit der Maske und prüfst, ob das Ergebnis von `0` verschieden ist:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // prints "1"
printf("%d\n", (value & (1u << 2)) != 0); // prints "0"
```
Das Und ergibt keine `1`: Es ergibt entweder `0` oder die Maske selbst, was bei Bit `3` die `8` ist. Deshalb wird das Ergebnis mit `!= 0` verglichen, statt es als schlichte Antwort zu verwenden.

---

**Flags** sind benannte Masken, die jeweils ein anderes Bit verwenden und sich alle in einer einzigen Variable speichern lassen. Sie werden mit `|` kombiniert und mit `&` wieder ausgelesen:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// prints "1"
```
Ein einzelnes `unsigned int` kann daher 32 unabhängige Ja/Nein-Antworten tragen.

---

Vor C23 gab es keinen Formatbezeichner, der eine Zahl binär ausgab, und Literale wie `0b1010` waren ebenfalls kein Standard-C. Um die Bits anzuzeigen, schreibst du die Schleife selbst: gehe vom höchsten Bit hinunter bis Bit `0` und gib jedes Mal `(value >> i) & 1u` aus.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// prints "0101"
```
Verschiebt man den Wert um `i` nach rechts, bringt das Bit `i` an die rechte Stelle, wo `& 1u` es isoliert.

---

Zu zählen, wie viele Bits eines Werts `1` sind, ist eine klassische Bitschleife: teste das unterste Bit mit `& 1u`, addiere es zu einem Zähler, verschiebe dann den Wert mit `>>=` um eine Stelle nach rechts und wiederhole das, bis nichts mehr übrig ist.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count is 2
```
Die Schleife endet immer, denn ein unsigned-Wert wird zu `0`, wenn man ihn oft genug nach rechts verschiebt.

---

Mehrere kleine Zahlen werden oft in einen größeren Wert gepackt. Um eine davon wieder auszulesen, verschiebe sie zunächst nach unten, sodass sie bei Bit `0` beginnt, und maskiere dann alles oberhalb aus:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// prints "18", the 0x12 byte
```
Erst verschieben, dann maskieren – diese Reihenfolge gilt es zu merken: Die Maske beschreibt das Feld immer erst, wenn es unten angekommen ist.
