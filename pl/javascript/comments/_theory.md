**Komentarz** to notatka zapisana wewnątrz kodu źródłowego dla osób, które go czytają. JavaScript całkowicie ignoruje komentarze, więc nigdy nie zmieniają one tego, co robi program.

Najprostszy komentarz to **komentarz jednolinijkowy**: zaczyna się od `//` i trwa do końca linii.
```javascript
// Greets the user
console.log("Hello");
```
Używaj komentarzy, aby wyjaśnić, do czego służy fragment kodu albo dlaczego został napisany w taki sposób. Zwróć uwagę, że w przeciwieństwie do niektórych innych języków, `#` **nie** rozpoczyna komentarza w JavaScripcie.

---

Komentarz nie potrzebuje własnej linii: może znajdować się za kodem w tej samej linii. To **komentarz w linii** (nazywany też komentarzem końcowym) i jest dobrym miejscem na krótką notatkę o tej konkretnej instrukcji:
```javascript
const retries = 3; // give up after three attempts
```
Wszystko od `//` do końca linii jest ignorowane, a kod przed nim wykonuje się normalnie.

---

Ponieważ komentarze są ignorowane, dodanie lub usunięcie komentarza nigdy nie zmienia tego, co robi program. Wykonuje się tylko kod, który **nie** jest zakomentowany.

Dzięki temu `//` to szybki sposób na wyłączenie linii kodu bez jej usuwania. Nazywa się to **zakomentowaniem**:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
Druga linia jest teraz komentarzem, więc `total` pozostaje `10`. Usunięcie `//` przywraca linię do życia.

Zakomentowywanie jest wygodne, gdy eksperymentujesz, ale pamiętaj o porządkach: kod, który długo pozostaje zakomentowany, tylko wprowadza w błąd kolejną osobę, która go przeczyta.

---

Gdy komentarz potrzebuje więcej niż jednej linii, JavaScript oferuje **komentarz wielolinijkowy** (nazywany też komentarzem blokowym): zaczyna się od `/*` i kończy na `*/`, a wszystko pomiędzy jest ignorowane, łącznie ze znakami nowej linii.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Komentarz blokowy może też być krótki i zmieścić się w jednej linii: `/* like this */`.

---

Niezależnie od tego, jakiego rodzaju komentarza użyjesz, zasada jest ta sama: tekst w środku **nie jest kodem**. `console.log` wewnątrz komentarza nigdy niczego nie wypisze, a kod napisany po `//` w tej samej linii nigdy się nie wykona, nawet gdy linia zaczyna się prawdziwym kodem:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Gdy nie masz pewności, co program wypisze, usuń w myślach wszystkie komentarze i przeczytaj to, co zostało.

---

W przeciwieństwie do `//`, który kończy się na końcu linii, komentarz `/*` kończy się dopiero na `*/`. Jeśli zapomnisz go zamknąć, JavaScript potraktuje cały dalszy kod jako część komentarza i zgłosi błąd składni:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Zarówno `//`, jak i `/* */` działają jako komentarze w linii, ale przy `/*` zawsze upewnij się, że `*/` jest na miejscu.

---

Komentarze blokowe w JavaScripcie **nie mogą być zagnieżdżane**: komentarz kończy się na **pierwszym** napotkanym `*/`, niezależnie od tego, ile `/*` było wcześniej.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Tutaj komentarz kończy się tuż po `inner`, więc `still a comment */` jest odczytywane jako kod i powoduje błąd składni. Pamiętaj o tym, gdy zakomentowujesz blok, który już zawiera komentarz `/* */`: użyj `//` w każdej linii albo najpierw usuń wewnętrzny komentarz.

---

Aby zakomentować kilka linii naraz, obejmij je jednym komentarzem blokowym zamiast dodawać `//` do każdej linii:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Ponieważ linie wewnątrz bloku są ignorowane, `total` nigdy się nie zmienia. Pamiętaj, że działa to tylko wtedy, gdy żadna z tych linii nie zawiera `*/`.

---

JavaScript ma trzeci rodzaj komentarza, **komentarz dokumentacyjny**, zapisywany w formacie **JSDoc**: to komentarz blokowy zaczynający się od `/**` (dwie gwiazdki), umieszczony bezpośrednio nad funkcją. W środku linie zwykle zaczynają się od ` * `, a specjalne **znaczniki** zaczynające się od `@` opisują funkcję:
- `@param {type} name description` dla każdego parametru
- `@returns {type} description` dla zwracanej wartości

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Dla JavaScriptu to zwykły komentarz, ale edytory go czytają i pokazują jako tekst pomocy dla `greet`, razem z typem zapisanym w nawiasach klamrowych (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

Pierwsza linia komentarza JSDoc to **podsumowanie**: krótkie zdanie mówiące, co robi funkcja. Napisz je w trzeciej osobie, jakbyś opisywał funkcję: "Returns...", "Adds...", "Checks...". Następnie wypisz znaczniki, po jednym w linii:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
Komentarz musi znajdować się bezpośrednio nad deklaracją, bez pustej linii pomiędzy, w przeciwnym razie edytory nie powiążą go z funkcją.

---

Komentarz JSDoc jest też **kontraktem**: mówi temu, kto wywołuje funkcję, co przekazać i czego się spodziewać w zamian, jeszcze zanim ciało funkcji zostanie napisane. Przeczytanie komentarza często wystarczy, aby zaimplementować funkcję:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Każdy `@param` odpowiada jednemu parametrowi, w tej samej kolejności, a `@returns` opisuje każdy możliwy wynik.

---

Kolejność wewnątrz komentarza JSDoc jest zawsze taka sama: najpierw podsumowanie, potem po jednym `@param` na parametr w kolejności ich deklaracji, a na końcu `@returns`. Otwierające `/**` i zamykające ` */` obejmują całość, a komentarz znajduje się bezpośrednio nad funkcją, którą opisuje:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Plik JavaScript może zaczynać się specjalną linią zwaną **shebang** (albo hashbang): `#!` po którym następuje ścieżka do programu, który ma uruchomić plik. W systemach uniksowych pozwala to uruchomić skrypt bezpośrednio z terminala, na przykład `./hello.js`, bez wpisywania `node`:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignoruje tę linię dokładnie tak jak komentarz, ale tylko wtedy, gdy jest ona **pierwszą linią** pliku: w każdym innym miejscu `#!` to błąd składni. `/usr/bin/env node` oznacza "znajdź `node` w tym systemie i użyj go".

---

Dobry komentarz wyjaśnia, **dlaczego** kod coś robi, a nie **co** robi. Kod już pokazuje, co się dzieje; powtarzanie tego słowami dodaje szumu i dezaktualizuje się, gdy tylko kod się zmieni:
```javascript
// set timeout to 30
const timeout = 30;
```
Powód stojący za tą liczbą to coś, czego czytelnik nie zgadnie:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Jeśli komentarz tylko powtarza linię pod nim, usuń go albo zastąp powodem.

---

Niektóre komentarze stosują konwencję, którą rozumieją edytory. Najczęstsze **znaczniki** to:
- `// TODO: ...` oznacza coś, co trzeba jeszcze napisać
- `// FIXME: ...` oznacza kod, o którym wiadomo, że jest błędny i wymaga poprawki

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Dla JavaScriptu to zwyczajne komentarze; edytory je wypisują, dzięki czemu łatwo znaleźć zaległą pracę. `TODO` zwykle stoi obok zaślepki, która utrzymuje działanie kodu, dopóki nie powstanie prawdziwa implementacja. Gdy skończysz pracę, zastąp zaślepkę i usuń znacznik w tej samej zmianie: nieaktualne `TODO` wprowadza w błąd.

---

`FIXME` różni się od `TODO`: kod już istnieje, ale wiadomo, że jest błędny. Dobre `FIXME` mówi, na czym polega błąd, i jeśli to możliwe, podaje przykład, który go pokazuje, aby kolejna osoba mogła go szybko naprawić. Tak jak przy `TODO`, usuń znacznik, gdy błąd zostanie naprawiony, ale zachowaj komentarz JSDoc, który nadal jest prawdziwy.
