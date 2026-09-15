Wiesz już, że `extends` czyni jedną klasę potomną drugiej. To, co to słowo kluczowe naprawdę daje, to **dziedziczenie**: klasa potomna dostaje za darmo każdą właściwość i metodę klasy nadrzędnej i może dodawać na nich własne.

Elementem, który czyni dziedziczenie użytecznym, jest **`super`**. Wewnątrz konstruktora klasy potomnej `super(...)` wywołuje konstruktor klasy nadrzędnej, dzięki czemu rodzic może skonfigurować tę część obiektu, do której należy:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
Tutaj `super(name)` przekazuje `name` do `Animal`, które je zapisuje, a `Dog` musi już martwić się tylko o `breed`.

---

Klasa potomna nie musi ponownie definiować niczego, co dostarcza już klasa nadrzędna. Metody również są dziedziczone, więc instancja klasy potomnej może wywoływać je tak, jakby były jej własnymi:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// wypisuje Max makes a sound
```
Gdy klasa potomna deklaruje własny konstruktor, wywołanie `super(...)` wewnątrz niego jest **obowiązkowe**: bez tego obiekt nigdy nie zostaje zainicjowany, a JavaScript rzuca `ReferenceError`. Klasa potomna bez żadnego konstruktora jest w porządku, ponieważ JavaScript pisze za nią taki, który przekazuje każdy argument do klasy nadrzędnej.

---

Zasada dotycząca `super()` jest ostrzejsza niż „wywołaj go gdzieś”. W konstruktorze klasy potomnej słowo `this` nie istnieje, dopóki `super()` nie zostanie wykonane, ponieważ to konstruktor klasy nadrzędnej tworzy obiekt. Dotknięcie `this` przed tą linią rzuca wyjątek:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
Dlatego `super(...)` powinno być **pierwszą instrukcją** każdego konstruktora klasy potomnej, który używa `this`.

---

Gdy klasa potomna definiuje metodę, którą ma już klasa nadrzędna, wygrywa wersja z klasy potomnej. Nazywa się to **nadpisywaniem**:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// wypisuje Woof
```
Nadpisywanie nie usuwa wersji z klasy nadrzędnej, tylko ją ukrywa. Wewnątrz metody klasy potomnej `super.nazwaMetody(...)` nadal się do niej dociera, co pozwala rozszerzyć zachowanie klasy nadrzędnej zamiast je zastępować:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// wypisuje Woof!
```
Zwróć uwagę na różnicę: `super(...)` wywołuje **konstruktor** klasy nadrzędnej, a `super.nazwa(...)` wywołuje **metodę** klasy nadrzędnej.

---

Do tej pory każda właściwość była tworzona wewnątrz konstruktora. **Pole klasy** pozwala zadeklarować je bezpośrednio w ciele klasy, z opcjonalną wartością początkową:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// wypisuje 0
```
Pola są przypisywane każdej nowej instancji, zanim wykona się ciało konstruktora, więc konstruktor może już na nich polegać. Pole bez wartości nadal jest deklarowane, po prostu zaczyna jako `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Zwróć uwagę na składnię: żadnego `let`, żadnego `const`, żadnego `this` w deklaracji, a linia kończy się średnikiem.

---

Kolejność ma znaczenie, gdy klasy po sobie dziedziczą. Deklaracja `class` **nie** jest hoistowana tak, jak `function`: nazwa istnieje dopiero od linii, w której zapisano klasę. Dlatego klasa potomna musi pojawić się *po* klasie nadrzędnej, po której dziedziczy, w przeciwnym razie klauzula `extends` kończy się błędem `ReferenceError`.

---

Niektóre zachowania należą do samej klasy, a nie do pojedynczej instancji. Konwersja między dwiema jednostkami, na przykład, nie potrzebuje obiektu, na którym miałaby pracować. Oznaczenie metody jako **`static`** umieszcza ją na klasie:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// wypisuje 8
```
Metodę statyczną wywołuje się na nazwie klasy, nigdy na instancji: `new MathUtils().double(4)` rzuca `TypeError`, ponieważ instancje nie otrzymują statycznych składowych. Wewnątrz metody statycznej `this` odnosi się do klasy, więc jedna metoda statyczna może wywołać inną za pomocą `this.innaStatyczna(...)`.

---

`static` działa także na polach. **Właściwość statyczna** jest przechowywana raz, na klasie, a nie raz na instancję, co czyni ją naturalnym miejscem dla współdzielonego licznika lub stałej:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// wypisuje 3.14
```
Ponieważ istnieje tylko jedna kopia, każda instancja, która ją aktualizuje, aktualizuje tę samą wartość. Wewnątrz konstruktora sięgasz do niej przez nazwę klasy, `Circle.PI`, a nie przez `this`: `this.PI` szukałoby właściwości w instancji, nie znalazłoby nic i dałoby ci `undefined`.

---

Bardzo częstym zastosowaniem metody statycznej jest **fabryka**: metoda, która buduje instancję z danych w innym kształcie i ją zwraca. Trzyma `new` w jednym miejscu i nadaje konstrukcji nazwę, która mówi, co robi:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// wypisuje 120
```
Fabrykę można wywołać, zanim jeszcze istnieje jakakolwiek instancja, czego zwykła metoda nie potrafi.

---

**Getter** to metoda, która jest odczytywana jak właściwość. Napisz przed nią `get` i opuść nawiasy w miejscu wywołania:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// wypisuje 12
```
`r.area` uruchamia metodę i zwraca jej wynik, więc jest to liczba. Dodanie nawiasów próbowałoby wtedy wywołać tę liczbę, co kończy się niepowodzeniem.

Lustrzanym odbiciem jest **setter**, deklarowany za pomocą `set`, który uruchamia się, gdy właściwość jest przypisywana. Przyjmuje dokładnie jeden parametr:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

Prawdziwa wartość settera polega na tym, że może odmówić. Między przypisaniem a zapisaną wartością masz szansę sprawdzić, ograniczyć lub odrzucić to, co nadchodzi:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// wypisuje 3, setter odrzucił 50
```
Getter i setter o tej samej nazwie tworzą jedną właściwość, więc nie mogą nią być jednocześnie zwykłe pole: zapisana wartość mieszka pod inną nazwą, z konwencją tej samej nazwy z wiodącym podkreślnikiem.

---

Wiodący podkreślnik w `_temperature` to tylko konwencja: nic nie powstrzymuje świata zewnętrznego przed napisaniem `v._level = 999` i przejściem prosto obok twojego settera. **Pole prywatne** jest wymuszane przez sam język. Jego nazwa zaczyna się od `#`, musi być zadeklarowane w ciele klasy i może być odczytane lub zapisane tylko z wnętrza tej klasy:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// wypisuje 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Dwa szczegóły łatwo przewrócą. Znak `#` jest częścią nazwy, więc zawsze piszesz `this.#code`, nigdy `this.code`. A pole prywatne nie pojawia się w `Object.keys` ani w `console.log` instancji.

---

Metody też mogą być prywatne. Poprzedź nazwę znakiem `#`, a metoda zniknie z publicznej powierzchni klasy, wciąż będąc wywoływalną z dowolnej innej metody za pomocą `this.#nazwa(...)`:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// wypisuje $7
```
W ten sposób trzymasz kroki pomocnicze z dala od API: wywołujący widzi `print`, a nie szczegół formatowania, który się za nim kryje. Prywatne pola i prywatne metody razem dają klasie wyraźne wnętrze i zewnętrze.

---

Wypisanie obiektu zwykle daje coś nieprzydatnego. Ilekroć JavaScript potrzebuje ciągu znaków, a dostaje obiekt, wywołuje metodę **`toString`** obiektu, a domyślna zwraca `[object Object]`. Zdefiniowanie własnej to zastępuje:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// wypisuje $7
```
Ta sama metoda jest używana przez konkatenację ciągów znaków oraz przez `String(value)`. Jeśli chcesz też rozsądną **liczbę**, zdefiniuj `[Symbol.toPrimitive](hint)`, który otrzymuje `"string"`, `"number"` lub `"default"` i decyduje, co zwrócić; gdy istnieje, wygrywa z `toString`.

---

Operator **`instanceof`** pyta, czy obiekt został zbudowany z danej klasy lub z dowolnej klasy, która po niej dziedziczy:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript nie ma słowa kluczowego `abstract`, ale tę samą ideę zapisuje się ręcznie: klasa bazowa definiuje kształt, a każda metoda, którą klasa potomna *musi* dostarczyć, po prostu rzuca wyjątek:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Klasa potomna, która zapomni nadpisać `area`, głośno zawodzi przy pierwszym użyciu, zamiast po cichu zwracać `undefined`.

---

`for...of` i operator spread `...` nie działają na dowolnym obiekcie: działają na **obiektach iterowalnych**, obiektach, które dostarczają metodę zapisaną pod specjalnym kluczem `Symbol.iterator`. Daj swojej klasie tę metodę, a dołączy do klubu:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// wypisuje [ 'a', 'b' ]
```
Znak `*` przed nazwą czyni ją **generatorem**: funkcją, która przekazuje wartości pojedynczo za pomocą `yield` i pauzuje między nimi. To najkrótszy sposób spełnienia protokołu iteracji i działa dla wartości, które są obliczane, a nie przechowywane.
