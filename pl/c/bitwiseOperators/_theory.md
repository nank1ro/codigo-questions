Każda liczba całkowita jest przechowywana w pamięci jako rząd **bitów**, z których każdy ma wartość `0` lub `1`. Liczba `12` jest przechowywana jako `00001100`, a liczba `10` jako `00001010`.
**Operatory bitowe** działają na tych pojedynczych bitach, a nie na liczbie jako całości. Operator **AND** `&` porównuje dwie wartości bit po bicie i zachowuje `1` tylko tam, gdzie *oba* bity mają wartość `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// prints "8"
```
Wzorce bitowe zapisuje się zwykle jako literały szesnastkowe, takie jak `0x0C`, ponieważ każda cyfra szesnastkowa odpowiada dokładnie czterem bitom. Do pracy na bitach zawsze używaj typów `unsigned` i wypisuj je za pomocą `%u`.

---

Operator **OR** `|` porównuje dwie wartości bit po bicie i zachowuje `1` tam, gdzie *co najmniej jeden* z bitów ma wartość `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// prints "14"
```
`|` to zwykły sposób scalania dwóch wzorców bitowych w jeden.

---

Operator **XOR** `^` (alternatywa rozłączna) zachowuje `1` tylko tam, gdzie dwa bity są *różne*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// prints "6"
```
Wynika z tego przydatna własność: dwukrotne zastosowanie tego samego XOR przywraca pierwotną wartość.

---

Operator **NOT** `~` przyjmuje jeden operand i odwraca każdy z jego bitów: każde `0` staje się `1`, a każde `1` staje się `0`.
Typ `unsigned int` przechowuje 32 bity, więc `~0x0Fu` odwraca wszystkie 32 i daje bardzo dużą liczbę. Aby zachować tylko bajt, który Cię interesuje, połącz `~` z `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// prints "240"
```
`~` ma wyższy priorytet niż `&`, więc jest stosowane najpierw.
Nie myl `~` z logicznym `!`: `!` patrzy na całą wartość i odpowiada `0` lub `1`, podczas gdy `~` przepisuje każdy bit.

---

Operator **przesunięcia w lewo** `<<` przesuwa każdy bit o podaną liczbę miejsc w lewo i wypełnia zwolnione miejsca po prawej zerami:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// prints "12"
```
Przesunięcie w lewo o `n` mnoży wartość przez 2 do potęgi `n`.
Dwa błędy czynią program w języku C niezdefiniowanym: przesunięcie w lewo wartości ujemnej oraz przesunięcie o liczbę miejsc równą lub większą niż szerokość typu (32 dla `unsigned int`). Praca na wartościach **unsigned** uwalnia Cię od pierwszego z nich.

---

Operator **przesunięcia w prawo** `>>` przesuwa każdy bit w prawo; bity, które wypadają z prawego końca, są odrzucane. Dla wartości bez znaku zwolnione miejsca po lewej są wypełniane zerami:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// prints "3"
```
Przesunięcie w prawo o `n` dzieli wartość bez znaku przez 2 do potęgi `n`, odrzucając resztę z dzielenia.
Przesunięcie w prawo wartości *ujemnej* nie jest przenośne, co jest jeszcze jednym powodem, aby pracę na bitach prowadzić na typach `unsigned`.

---

Każdy binarny operator bitowy ma formę **przypisania złożonego**, która aktualizuje zmienną w miejscu: `&=`, `|=`, `^=`, `<<=` i `>>=`.
```c
unsigned int x = 12;
x &= 10;  // same as x = x & 10;
x |= 1;   // same as x = x | 1;
x ^= 3;   // same as x = x ^ 3;
x <<= 1;  // same as x = x << 1;
x >>= 2;  // same as x = x >> 2;
```
Są czytelniejsze niż powtarzanie nazwy zmiennej i stanowią typowy sposób zmieniania bitów zmiennej flagowej.

---

**Maska** to wartość, której bity wybierają tę część innej wartości, która Cię interesuje. W połączeniu z `&` maska zachowuje bity, które są `1` w masce, i zeruje wszystkie pozostałe:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// prints "11"
```
`0x0F` zachowuje cztery najniższe bity, nazywane dolnym **nibble**, a `0xFF` zachowuje osiem najniższych bitów, czyli cały bajt.

---

Bity są numerowane od `0`, zaczynając od skrajnie prawego, więc `1u << n` to maska, w której włączony jest tylko bit `n`.
Aby **ustawić** pojedynczy bit, czyli włączyć go bez dotykania pozostałych, wykonaj na wartości operację OR z tą maską:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// prints "6"
```
Jeśli bit był już włączony, wartość się nie zmienia, co czyni ustawianie bitu bezpiecznym do powtarzania.

---

Aby **wyzerować** pojedynczy bit, czyli go wyłączyć, wykonaj na wartości operację AND z *odwrotnością* maski:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// prints "5"
```
`~(1u << 1)` to wartość, w której włączony jest każdy bit oprócz bitu `1`, więc AND pozostawia wszystko inne nietknięte.

---

Aby **przełączyć** pojedynczy bit, czyli odwrócić go niezależnie od jego aktualnego stanu, wykonaj na wartości operację XOR z maską:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// prints "7"
```
Ponieważ XOR cofa sam siebie, ponowne przełączenie tego samego bitu przywraca pierwotną wartość.

---

Aby **sprawdzić** pojedynczy bit, wykonaj na wartości operację AND z maską i sprawdź, czy wynik różni się od `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // prints "1"
printf("%d\n", (value & (1u << 2)) != 0); // prints "0"
```
AND nie daje `1`: daje albo `0`, albo samą maskę, która dla bitu `3` wynosi `8`. Dlatego wynik porównuje się z `!= 0`, zamiast używać go jako zwykłej odpowiedzi.

---

**Flagi** to nazwane maski, z których każda używa innego bitu, i wszystkie można przechowywać w jednej zmiennej. Łączy się je za pomocą `|` i odczytuje za pomocą `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// prints "1"
```
Jeden `unsigned int` może więc nieść 32 niezależne odpowiedzi tak/nie.

---

Przed C23 nie było specyfikatora formatu wypisującego liczbę w systemie binarnym, a literały takie jak `0b1010` również nie były standardowym C. Aby pokazać bity, sam piszesz pętlę: przechodź od najwyższego bitu w dół do bitu `0` i za każdym razem wypisuj `(value >> i) & 1u`.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// prints "0101"
```
Przesunięcie wartości w prawo o `i` wprowadza bit `i` na skrajnie prawe miejsce, gdzie `& 1u` go wyodrębnia.

---

Liczenie, ile bitów wartości ma wartość `1`, to klasyczna pętla bitowa: sprawdź najniższy bit za pomocą `& 1u`, dodaj go do licznika, następnie przesuń wartość o jedno miejsce w prawo za pomocą `>>=` i powtarzaj, dopóki nic nie zostanie.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count is 2
```
Pętla zawsze się kończy, ponieważ wartość bez znaku przesuwana w prawo wystarczająco wiele razy staje się `0`.

---

Kilka małych liczb jest często upakowanych wewnątrz jednej większej wartości. Aby odczytać jedną z nich, najpierw przesuń ją w dół, tak aby zaczynała się od bitu `0`, a następnie zamaskuj wszystko powyżej niej:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// prints "18", the 0x12 byte
```
Najpierw przesunięcie, potem maskowanie — to kolejność, którą należy zapamiętać: maska zawsze opisuje pole, gdy osiągnęło ono dół.
