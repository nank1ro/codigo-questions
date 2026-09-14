Odczytywanie wartości z tablicy po jednym indeksie naraz jest uciążliwe:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**Destrukturyzacja** wykonuje tę samą pracę w jednej linijce. Po lewej stronie `=` piszesz wzorzec, który wygląda jak sama tablica, a każda nazwa wewnątrz niego otrzymuje element na tej samej pozycji:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
Wzorzec nie musi obejmować całej tablicy: nadmiarowe elementy są po prostu ignorowane, a nazwa bez pasującego elementu staje się `undefined`.

---

Destrukturyzacja jest najbardziej przydatna dokładnie tam, gdzie pojawia się tablica: argument funkcji albo wynik wywołania. Zamiast trzymać tablicę przy sobie i indeksować ją wszędzie, rozpakowujesz ją raz i nadajesz częściom prawdziwe nazwy:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
Nic nie jest kopiowane ani zmieniane w oryginalnej tablicy, wzorzec jedynie z niej czyta.

---

Czasami ważny jest tylko jeden element głęboko wewnątrz tablicy. Możesz zostawić pozycję pustą we wzorcu, zachowując przecinek, który ją oddziela: taka pusta pozycja nazywa się **dziurą** i pomija element bez nadawania mu nazwy:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
Policz przecinki, a nie nazwy: każdy przecinek przesuwa wzorzec o jedną pozycję do przodu, niezależnie od tego, czy przed nim stoi nazwa.

---

Tablica nie zawsze jest tak długa, jak oczekuje wzorzec. Zapisanie `= value` po nazwie nadaje jej **wartość domyślną**, używaną zawsze, gdy tablica nie ma nic na tej pozycji:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
Wartość domyślna jest obliczana tylko wtedy, gdy jest potrzebna, więc może być nawet wywołaniem funkcji, a wartość domyślną można nadać dowolnej pozycji, nie tylko ostatniej.

---

Wzorzec może też stać po lewej stronie zwykłego przypisania, bez `const` ani `let` z przodu, a wtedy zapisuje do zmiennych, które już istnieją. Zamienia to podmianę dwóch wartości miejscami w jedną linijkę, bez zmiennej tymczasowej:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
Prawa strona jest budowana najpierw, więc obie stare wartości są już bezpieczne wewnątrz tablicy tymczasowej, gdy następuje przypisanie. Uważaj na średnik w poprzedniej linijce: linijka zaczynająca się od `[` zostałaby w przeciwnym razie odczytana jako indeks tego, co przed nią.

---

Obiekty też można destrukturyzować, za pomocą nawiasów klamrowych zamiast kwadratowych. Tutaj pozycja nic nie znaczy: każda nazwa jest dopasowywana do **klucza** o tej samej pisowni:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
Podmiana `age` i `name` miejscami we wzorcu niczego nie zmienia, a klucze, których wzorzec nie wymienia, są po prostu pomijane. Nazwa bez pasującego klucza staje się `undefined`.

---

Wzorce obiektów i wartości domyślne łączą się dokładnie tak jak tablicowe, co czyni je schludnym sposobem na odczytanie obiektu konfiguracji, którego klucze mogą być, ale nie muszą, obecne:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
Ponieważ cały wzorzec to jedna instrukcja, funkcja może rozpakować wszystko, czego potrzebuje, ze swojego argumentu już w pierwszej linijce.

---

Wzorzec obiektu nazywa swoje zmienne od kluczy, co jest niewygodne, gdy klucze są zagadkowe albo już zajęte. Zapis `key: newName` **zmienia nazwę** zmiennej:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
Czytaj to jako „weź `n`, nazwij je `name`”. Dwukropek nie deklaruje typu, a samo `n` nigdy nie zostaje utworzone jako zmienna, tylko `name`. Nazwa o zmienionej nazwie wciąż może otrzymać wartość domyślną, zapisaną po niej: `{ n: name = "unknown" }`.

---

Wartości domyślne mają jedną zasadę, która zaskakuje wszystkich: dotyczą one **wyłącznie** `undefined`. Klucz, który istnieje i zawiera `null`, `0`, `""` albo `false`, jest prawdziwą wartością, więc wzorzec ją bierze, a wartość domyślna nie jest nigdy używana:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` zachowuje się tutaj tak samo jak `0`, mimo że w odpowiedzi API często oznacza „brak wartości”. Gdy `null` też musi zostać zastąpiony, najpierw zdestrukturyzuj, a potem wróć do wartości zastępczej za pomocą `??`.

---

Tam, gdzie klucz zawiera inny obiekt lub tablicę, wzorzec może po prostu iść dalej i opisać również ten kształt:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
Uważaj, co tworzy taka linijka: `address: { city }` znaczy „wejdz do `address`”, a nie „daj mi `address`”, więc tylko `city` staje się zmienną. Aby uzyskać oba, wymień klucz dwa razy: `const { address, address: { city } } = user;`. Wzorce tablic i obiektów swobodnie zagnieżdżają się w sobie, jak w `{ tags: [first] }`.

---

Wzięcie głowy tablicy i zachowanie ogona to tak powszechna potrzeba, że wzorce mają na nią własną składnię. Trzy kropki przed ostatnią nazwą czynią ją **elementem rest** i zbiera ona wszystkie pozostałe elementy do zupełnie nowej tablicy:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
Element rest musi być ostatni we wzorcu i nie może mieć wartości domyślnej: gdy nic nie zostaje, jest po prostu pustą tablicą.

---

Wzorce obiektów też mają rest i tam zbiera on każdy klucz, którego wzorzec nie wymienił, do nowego obiektu:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
To najkrótszy sposób na zbudowanie kopii obiektu bez jednego z jego kluczy: oryginał nie jest nigdy dotykany, a obiekt rest jest świeżym obiektem przechowującym pozostałe wartości.

---

Wzorzec może zastąpić nazwę parametru w deklaracji funkcji, więc rozpakowanie następuje w momencie wywołania:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
Wewnątrz ciała nie ma wcale zmiennej obiektu, są tylko `width` i `height`. Wywołujący przekazuje jeden obiekt, ale sygnatura dokumentuje dokładnie, które klucze funkcja odczytuje, a klucze mogą przyjść w dowolnej kolejności.

---

Zdestrukturyzowany parametr z wartościami domyślnymi tworzy zgrabny obiekt opcji, ale wciąż się psuje, gdy wywołujący nie przekazuje niczego: odczytanie klucza z `undefined` rzuca `TypeError`. Nadanie całemu wzorcowi wartości domyślnej `{}` naprawia to:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
Czytaj tę linijkę od zewnątrz do środka: `= {}` dostarcza pusty obiekt, gdy brakuje argumentu, a każda wewnętrzna wartość domyślna wypełnia potem swój własny klucz.

---

`Object.entries(obj)` zamienia obiekt w tablicę par `[key, value]`. Umieść wzorzec tablicy w nagłówku pętli `for...of`, a każda para zostanie rozpakowana w miarę działania pętli:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
To czytelny sposób na przejście po obiekcie: bez indeksu, bez wyszukiwania, tylko dwie nazwy, na których ci zależy. `Object.keys` i `Object.values` dają tylko jedną stronę każda, `Object.entries` daje obie.

---

Wszystko, co dotąd widzieliśmy, należy do jednej składni, więc elementy swobodnie się łączą: wzorzec obiektu może zagnieżdżać inny wzorzec obiektu, który może zawierać klucz o zmienionej nazwie z wartością domyślną, obok wzorca tablicy kończącego się elementem rest. Jedna linijka opisuje wtedy cały kształt, jakiego funkcja oczekuje:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
Zachowaj czytelność: wzorzec, który nie mieści się już w kilku linijkach, to zwykle znak, że funkcja oczekuje za dużo.
