**Wyrażenie regularne** (w skrócie **regex**) to niewielki wzorzec opisujący kształt tekstu. Służy do odpowiadania na pytania typu „czy ten łańcuch zawiera liczbę?” albo „gdzie pojawia się słowo `cat`?”.

W JavaScripcie najkrótszym sposobem zapisania go jest **literał wyrażenia regularnego**: wzorzec między dwoma ukośnikami.
```javascript
const pattern = /cat/;
```
Zwykłe znaki we wzorcu pasują do samych siebie, więc `/cat/` pasuje do trzech liter `c`, `a`, `t` w dowolnym miejscu łańcucha.

Najprostszą rzeczą, jaką można zrobić ze wzorcem, jest zapytanie, czy pojawia się on w łańcuchu. Metoda **`test`** przyjmuje tekst i zwraca `true` lub `false`:
```javascript
console.log(/cat/.test("the cat sleeps"));
// prints true
console.log(/cat/.test("the dog sleeps"));
// prints false
```
Zauważ, że `test` szuka wzorca *gdziekolwiek* w łańcuchu; cały łańcuch nie musi pasować.

---

Wzorce stają się użyteczne, gdy opisują *rodzaj* znaku zamiast jednego dokładnego znaku. Kilka **sekwencji ucieczki** pokrywa większość potrzeb:
- `\d` dowolna cyfra, od `0` do `9`
- `\w` dowolny znak słowa: litera, cyfra lub `_`
- `\s` dowolny biały znak: spacja, tabulator, znak nowej linii

```javascript
console.log(/\d/.test("room 12"));
// prints true
console.log(/\d/.test("lobby"));
// prints false
```
**Kwantyfikator** mówi, ile razy poprzedni fragment może się powtórzyć. Najczęstszy to `+`, oznaczający „jeden lub więcej”:
```javascript
console.log(/\d+/.test("42"));
// prints true
```
Zatem `/\d/` pasuje do pojedynczej cyfry, a `/\d+/` pasuje do ciągu cyfr. Dla zwykłego `test` oba zachowują się tak samo, ponieważ oba wymagają jedynie obecności jednej cyfry.

---

Literał taki jak `/\d+/` jest stały od momentu jego zapisania. Gdy wzorzec musi zostać **zbudowany w czasie działania**, użyj **konstruktora `RegExp`**, który przyjmuje wzorzec jako łańcuch znaków:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// prints true
```
Czyha tu jedna pułapka. Wewnątrz łańcucha znaków ukośnik odwrotny rozpoczyna sekwencję ucieczki dla *łańcucha*, więc znika, zanim wyrażenie regularne w ogóle go zobaczy. Aby umieścić prawdziwy ukośnik odwrotny we wzorcu, trzeba go podwoić:
```javascript
const digits = new RegExp("\\d+");
// the same pattern as /\d+/
```
Zapisanie zamiast tego `new RegExp("\d+")` daje wzorzec `/d+/`, który pasuje do litery `d`, a nie do cyfry.

Gdy wzorzec jest znany podczas pisania kodu, preferuj literał; jest krótszy i nie wymaga podwajania ukośników odwrotnych.

---

Jeszcze dwa elementy składowe pozwalają opisać niemal dowolny kształt tekstu.

**Klasa znaków** to zbiór znaków między nawiasami kwadratowymi; pasuje dokładnie do jednego z nich. Myślnik zapisuje zakres, a `^` na początku neguje zbiór:
```javascript
/[aeiou]/   // one vowel
/[a-z]/     // one lowercase letter
/[A-Z0-9]/  // one uppercase letter or one digit
/[^0-9]/    // one character that is not a digit
```
**Kwantyfikatory** mówią, ile razy powtarza się poprzedni fragment: `+` jeden lub więcej, `*` zero lub więcej, `?` zero lub jeden, a `{n}` dokładnie `n` razy.

Wreszcie, **kotwice** wiążą wzorzec z końcami tekstu: `^` oznacza „tu się zaczyna”, a `$` oznacza „tu się kończy”. Bez nich wzorzec może pasować gdziekolwiek wewnątrz łańcucha, więc `/\d{2}/.test("abc12def")` daje `true`. Z obiema kotwicami cały łańcuch musi pasować:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// prints false
console.log(/^\d{2}$/.test("12"));
// prints true
```

---

`test` odpowiada tylko tak lub nie. Aby uzyskać sam dopasowany tekst, wywołaj **`match`** na łańcuchu:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Gdy nic nie pasuje, `match` zwraca `null`. Gdy coś pasuje, zwraca wynik podobny do tablicy:
- `match[0]` to dopasowany tekst
- `match.index` to pozycja, na której dopasowanie się zaczyna
- `match.input` to cały przeszukiwany łańcuch

```javascript
console.log(match[0]);
// prints 42
console.log(match.index);
// prints 6
```
Ponieważ wynik może być `null`, sprawdź go przed odczytaniem `match[0]`.

---

Ponieważ `match` zwraca `null`, gdy wzorzec nie występuje, odczytanie od razu `match[0]` rzuca `TypeError: Cannot read properties of null`. Zabezpiecz to:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
Operator scalania nullish zapisuje tę samą ochronę w jednej linii, ponieważ `match?.[0]` daje `undefined`, gdy `match` jest `null`:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Nawiasy wokół części wzorca tworzą **grupę przechwytującą**: tekst dopasowany przez tę część jest odkładany na bok, aby można było go później odczytać.

Grupy pojawiają się po `match[0]`, numerowane od lewej do prawej według ich nawiasu otwierającego:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// prints 2026-09-12
console.log(match[1]);
// prints 2026
console.log(match[3]);
// prints 12
```
Zatem `match[0]` to zawsze całe dopasowanie, a `match[1]`, `match[2]`, ... to grupy. Grupa będąca częścią wzorca, który w ogóle nie pasuje, sprawia, że całe `match` zwraca `null`.

---

Przechwytuj tylko to, czego potrzebujesz. Grupa to nie tylko sposób na odczytanie fragmentu; mówi też czytelnikowi, która część wzorca jest ważna. We wzorcu czasu, w którym chcesz tylko minut, pogrupuj same minuty i zostaw resztę bez grupowania:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// prints 35
```
Cały wzorzec nadal musi pasować, więc godziny i sekundy są nadal wymagane; po prostu nie są przechwytywane. Mniej grup oznacza mniej liczb do śledzenia przy odczytywaniu `match[1]`, `match[2]` i tak dalej.

---

Liczenie nawiasów męczy, a dodanie grupy w środku wzorca zmienia numerację wszystkiego, co następuje po niej. **Nazwana grupa** unika obu problemów: zapisz `?<name>` zaraz po nawiasie otwierającym i odczytaj fragment z `match.groups`:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// prints 2026
console.log(match.groups.month);
// prints 09
```
Nazwane grupy nadal mają numery, więc `match[1]` nadal działa, ale `match.groups.year` mówi, co oznacza wartość. Gdy wzorzec w ogóle nie ma nazwanej grupy, `match.groups` to `undefined`.

---

Wszystko dotychczas zatrzymywało się na pierwszym dopasowaniu. **Flagi**, zapisywane po zamykającym ukośniku literału, zmieniają to i inne szczegóły wyszukiwania:
- `g` globalna: znajduje każde dopasowanie, nie tylko pierwsze
- `i` ignoruje wielkość liter, więc `/cat/i` pasuje także do `Cat` i `CAT`

Z flagą `g` metoda `match` zachowuje się inaczej: zwraca zwykłą tablicę dopasowanych **łańcuchów znaków**, bez `index` i bez grup, albo `null`, gdy nie ma dopasowania:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// prints [ '1', '22', '333' ]
console.log(numbers.length);
// prints 3
```
Flagi można łączyć w dowolnej kolejności, jak w `/cat/gi`. W konstruktorze `RegExp` trafiają do drugiego argumentu: `new RegExp("\\d+", "g")`.

---

Flaga `g` daje każdy dopasowany łańcuch, ale wyrzuca grupy. Gdy potrzebujesz grup *każdego* dopasowania, użyj **`matchAll`**. Zwraca on iterator pełnych obiektów dopasowania, z których każdy jest dokładnie taki jak wynik zwykłego `match`:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// prints a -> 1
// prints b -> 2
```
`matchAll` wymaga flagi `g`; bez niej rzuca `TypeError`. Ponieważ zwraca iterator, rozwiń go za pomocą `[...text.matchAll(pattern)]`, gdy chcesz otrzymać prawdziwą tablicę, i zauważ, że nie daje niczego, gdy wzorzec nigdy nie pasuje.

---

**`replace`** zwraca nowy łańcuch z dopasowaniem zamienionym na coś innego. Oryginalny łańcuch nigdy nie jest zmieniany.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// prints the dog sleeps
```
Wewnątrz łańcucha zastępującego kilka sekwencji ma specjalne znaczenie:
- `$1`, `$2`, ... tekst przechwycony przez grupę 1, grupę 2, ...
- `$<name>` tekst przechwycony przez nazwaną grupę
- `$&` całe dopasowanie

To właśnie czyni z `replace` narzędzie do przepisywania, a nie tylko do zamiany:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// prints 12/09/2026
```
Bez flagi `g` zastępowane jest tylko **pierwsze** dopasowanie.

---

Aby przepisać **każde** dopasowanie zamiast pierwszego, masz dwie opcje:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// prints a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// prints a# b#
```
**`replaceAll`** jest czytelniejszy z obu i akceptuje także zwykły łańcuch jako wzorzec. Gdy podasz mu wyrażenie regularne, musi ono **koniecznie** mieć flagę `g`, w przeciwnym razie rzuca `TypeError`; dokładnie to zapobiega cichej pomyłce polegającej na napisaniu `replace` i naprawieniu tylko pierwszego dopasowania.

---

Zastępnik nie musi być łańcuchem znaków. Gdy przekażesz **funkcję**, jest ona wywoływana raz na dopasowanie, a cokolwiek zwróci, zostaje wstawione w miejsce tego dopasowania.

Funkcja otrzymuje najpierw całe dopasowanie, potem każdą grupę przechwytującą:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// prints 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// prints Ann Lee
```
To jedyny sposób na obliczenie zastępnika na podstawie dopasowanego tekstu, czego samo `$1` nie potrafi.

---

**`split`** tnie łańcuch na tablicę. Gdy podasz zwykły łańcuch, tnie na tym dokładnym tekście, ale gdy podasz wyrażenie regularne, tnie na każdym dopasowaniu wzorca, co pozwala jednemu wywołaniu obsłużyć różne separatory:
```javascript
console.log("a, b;c".split(", "));
// prints [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// prints [ 'a', 'b', 'c' ]
```
Same separatory nie są częścią wyniku. Uważaj na separator na początku lub końcu łańcucha: daje on pusty łańcuch znaków w tablicy, ponieważ po tej stronie znajduje się puste pole.

---

Ostatnia flaga dopełnia zbiór. Domyślnie `^` i `$` oznaczają początek i koniec **całego łańcucha**, więc wzorzec zakotwiczony za pomocą `^` może pasować tylko na samym początku, nawet gdy tekst ma kilka linii.

Flaga **`m`** (multiline) zmienia to: `^` i `$` pasują wtedy także tuż po i tuż przed każdym znakiem nowej linii, więc każda linia jest zakotwiczona osobno:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// prints [ 'note a' ]
console.log(text.match(/^note.*/gm));
// prints [ 'note a', 'note c' ]
```
Tutaj ważne są dwa szczegóły. Domyślnie `.` nie pasuje do znaku nowej linii (zmienia to tylko flaga `s`), więc `.*` sam zatrzymuje się na końcu linii. A `match` z flagą `g` zwraca `null`, a nie pustą tablicę, gdy nic nie pasuje, więc paruj go z `?? []`, gdy obiecasz zwrócić tablicę.
