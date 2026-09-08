**Komentarz** to tekst w kodzie źródłowym przeznaczony dla ludzi, a nie dla kompilatora. Kompilator wyrzuca komentarze, zanim zbuduje program, więc możesz ich używać, aby wyjaśnić, po co jest dany kod, zostawiać przypomnienia albo odnotować decyzję.

Najczęstszym rodzajem jest **komentarz jednolinijkowy**: wszystko od `//` do końca tej linii jest ignorowane.
```c
// Greet the user
printf("Hello\n");
```
Pierwsza linia nie robi nic, gdy program działa; dane wyjściowe generuje tylko `printf`.

---

Ponieważ kompilator usuwa komentarze całkowicie, dodanie lub usunięcie komentarza nigdy nie zmienia działania programu. Wykonywany jest tylko kod, który **nie** jest zakomentowany.

Dzięki temu `//` to szybki sposób na wyłączenie linii kodu bez jej usuwania. Nazywa się to **zakomentowaniem**:
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
Druga linia jest teraz komentarzem, więc `total` pozostaje `10`. Usunięcie `//` przywraca linię do życia.

Zakomentowanie jest przydatne podczas eksperymentów, ale pamiętaj o sprzątaniu: kod, który pozostaje zakomentowany przez długi czas, tylko myli tego, kto będzie go czytał jako następny.

---

Gdy komentarz potrzebuje więcej niż jednej linii, C oferuje **komentarz wielolinijkowy** (nazywany także komentarzem blokowym): zaczyna się od `/*` i kończy na `*/`, a wszystko pomiędzy jest ignorowane, łącznie ze zmianami linii.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Komentarz blokowy może być też krótki i zmieścić się w jednej linii: `/* na przykład tak */`.

W przeciwieństwie do `//`, które kończy się na końcu linii, komentarz `/*` kończy się dopiero na `*/`. Jeśli zapomnisz go zamknąć, kompilator potraktuje cały następny kod jako część komentarza.

---

Komentarze blokowe **nie zagnieżdżają się**. Kompilator kończy komentarz `/*` na pierwszym napotkanym `*/`, niezależnie od tego, ile `/*` pojawiło się przed nim:
```c
/* outer /* inner */ still code */
```
Tutaj komentarz kończy się zaraz po `inner`, więc `still code */` jest kompilowane jako kod i powoduje błąd.

Ma to znaczenie, gdy chcesz zakomentować blok, który już zawiera komentarz `/* */`: wewnętrzne `*/` zamknęłoby twój zewnętrzny komentarz zbyt wcześnie. W takim przypadku umieść zamiast tego `//` przed każdą linią.

---

Komentarz nie potrzebuje własnej linii: może następować po kodzie w tej samej linii. To **komentarz końcowy** i dobre miejsce na krótką uwagę o tej konkretnej instrukcji:
```c
int retries = 3; // give up after three attempts
```
Zarówno `//`, jak i `/* */` działają jako komentarze końcowe, ale uważaj na `/*`: ponieważ kończy się dopiero na `*/`, niedomknięte `/*` na końcu linii pochłonie kolejne linie i program przestanie się kompilować.

---

Częstym zastosowaniem komentarzy blokowych jest **komentarz nagłówkowy**: krótki blok umieszczony bezpośrednio nad funkcją, który mówi, co funkcja robi, co oznaczają jej parametry i co zwraca.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Każdy, kto wywołuje `to_seconds`, może teraz przeczytać nagłówek zamiast ciała funkcji. Trzymaj nagłówek obok funkcji, aby aktualizować je razem.

---

Kompilator zastępuje każdy komentarz pojedynczą spacją. Oznacza to, że komentarz `/* */` może pojawić się wszędzie tam, gdzie może pojawić się spacja, nawet w środku instrukcji lub wyrażenia:
```c
int area = width /* cm */ * height /* cm */;
```
Czasem jest to przydatne do opisania operandów lub argumentów wywołania. Komentarz `//` nie może tego zrobić, ponieważ zakomentowałby resztę linii, łącznie z kodem znajdującym się po nim.

---

Programiści używają kilku konwencjonalnych słów kluczowych na początku komentarza, aby oznaczyć niezakończoną pracę:

- `TODO` oznacza coś, co wciąż trzeba napisać
- `FIXME` oznacza kod, o którym wiadomo, że jest błędny i musi zostać poprawiony

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Edytory i narzędzia potrafią wypisać takie znaczniki, więc zaległa praca jest łatwa do znalezienia. Gdy praca jest gotowa, usuń znacznik: nieaktualny `TODO` wprowadza w błąd.

---

Dobry komentarz wyjaśnia **dlaczego** kod coś robi, a nie **co** robi. Kod sam pokazuje, co się dzieje; powtarzanie tego słowami dodaje szum i dezaktualizuje się, gdy tylko kod się zmieni:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
Tego, czego czytelnik nie może się domyślić, to powód stojący za liczbami:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Jeśli komentarz tylko powtarza treść linii poniżej, usuń go albo zastąp wyjaśnieniem powodu.

---

Podsumowując: używaj `//` do krótkich notatek i komentarzy końcowych, `/* */` do dłuższych bloków i komentarzy nagłówkowych, oznaczaj niedokończoną pracę przez `TODO` lub `FIXME` oraz usuwaj zakomentowany kod i nieaktualne znaczniki, gdy nie są już potrzebne.
