Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy wyjść na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `niceWeather` i wykonać akcję wyjścia na zewnątrz `if` ta zmienna jest `true`, jak:
```javascript
var niceWeather = true;
if (niceWeather) {
    // baw się na dworze
}
```

---

Kontynuujmy poprzedni przykład.
```javascript
var niceWeather = true;
if (niceWeather) {
    // baw się na dworze
}
```
Widzieliśmy, że instrukcja `if` wykonuje blok kodu tylko wtedy, gdy warunek jest `true`.
Kolejną ważną rzeczą do rozważenia są **nawiasy klamrowe** `{}`, które oznaczają blok kodu.

---

Właśnie zobaczyliśmy, jak wykonać blok kodu, jeśli warunek jest spełniony. Teraz zobaczmy, jak wykonać inny blok kodu, gdy pierwszy warunek nie jest spełniony.
Wychodzimy na zewnątrz, jeśli pogoda jest ładna; w przeciwnym razie zostajemy w domu.
W JavaScript możemy użyć instrukcji `else`, jak:
```javascript
var niceWeather = true;
if (niceWeather) {
    // baw się na dworze
} else {
    // zostań w domu
}
```

---

Załóżmy, że mamy kolejny warunek do sprawdzenia, jak w tym przykładzie:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
a wynik tego kodu to `the number is 3`.
Przede wszystkim sprawdźmy, czy liczba jest równa 2 — to jest fałsz.
Przejdźmy zatem do drugiej instrukcji i sprawdźmy, czy `num` jest równe 3. Ponieważ jest to prawda, wykonujemy następujący blok kodu, drukując `the number is 3`

---

Możemy dodać tyle instrukcji `else if`, ile chcemy — nie ma żadnych ograniczeń
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
a wynik tego kodu to `the number is 4`.

---

Możemy również zagnieździć instrukcję warunkową (`if`, `else if` lub `else`) wewnątrz innej instrukcji warunkowej, aby stworzyć bardziej złożoną strukturę.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
a wynik tego kodu to `the number is 4`.

---

Trójargumentowy operator warunkowy to specjalny operator z trzema częściami, który ma postać `pytanie ? odpowiedź1 : odpowiedź2`.
Jest to skrót do ewaluacji jednego z dwóch wyrażeń w zależności od tego, czy `pytanie` jest prawdziwe czy fałszywe.
Jeśli `pytanie` jest prawdziwe, ewaluuje `odpowiedź1` i zwraca jej wartość; w przeciwnym razie ewaluuje `odpowiedź2` i zwraca jej wartość.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// wypisuje 10
```
Skrócony zapis powyższego kodu to:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// wypisuje 10
```
`c` jest ustawione równe `a`, ponieważ warunek `a < b` był prawdziwy

---

Operator _nil-coalescing_ `a ?? b` rozpakowuje opcjonalne `a`, jeśli zawiera wartość, lub zwraca wartość domyślną `b`, jeśli `a` jest `nil`.
Wyrażenie `a` jest zawsze typu opcjonalnego.
Wyrażenie `b` musi pasować do typu przechowywanego wewnątrz a.
Operator nil-coalescing jest skrótem dla poniższego kodu:
```javascript
a != nil ? a! : b;
```

---

`if` to słowo kluczowe wprowadzające instrukcję warunkową w JavaScript. Nie ma tu słowa kluczowego `elif` — drugi warunek wprowadza się za pomocą `else if`, zapisywanego jako dwa oddzielne wyrazy.

---

Literały logiczne w JavaScript pisane są małymi literami: `true` i `false`, a nie `True`/`False`, ani jako ciągi znaków `"true"`/`"false"`.

---

Aby blok kodu się nie wykonał, warunek w nawiasach musi przyjąć wartość `false`.

---

Odstęp między `if` a jego nawiasami ma charakter czysto kosmetyczny: `if(true)` i `if (true)` to dla JavaScript ta sama instrukcja.

---

To nawiasy klamrowe grupują kilka instrukcji w jeden blok. Bez nich `if` kontroluje tylko pojedynczą instrukcję, która po nim następuje, więc `if (true) console.log("Hello!");` jest poprawnym kodem JavaScript.

---

Warunek jest obliczany jednorazowo, zanim rozpocznie się blok. JavaScript nie sprawdza go ponownie podczas wykonywania instrukcji między nawiasami klamrowymi.

---

Warunek `false` powoduje całkowite pominięcie bloku, a program kontynuuje od pierwszej instrukcji po nawiasie zamykającym.

---

Warunek nie musi być wartością logiczną: JavaScript konwertuje na nią to, co znajdzie, więc `if (1)` wykonuje swój blok, a `if (0)` — nie. Literał `true` w ogóle nie wymaga konwersji.

---

Blok kodu nie jest ograniczony do jednej linii — każda instrukcja wewnątrz nawiasów klamrowych wykonuje się po kolei, gdy warunek ma wartość `true`.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
a wynikiem jest `First line`, a następnie `Second line`.

---

Instrukcje wewnątrz bloku wykonują się jedna po drugiej, od góry do dołu, więc dwa wywołania `console.log` w tym samym bloku wypisują tekst w dwóch osobnych liniach.

---

Wcinanie instrukcji wewnątrz bloku to jedynie konwencja poprawiająca czytelność. JavaScript o tym, co należy do bloku, decyduje na podstawie nawiasów klamrowych, nigdy na podstawie wcięcia.

---

Instrukcje takie jak `if`, `else if` i `else`, które wykonują lub pomijają kod w zależności od tego, czy warunek ma wartość `true`, czy `false`, nazywane są **instrukcjami warunkowymi**.

---

Zmienna logiczna, nawet taka zbudowana z negacji `!`, jak `isAfternoon`, może być użyta bezpośrednio jako warunek `if`, bez potrzeby porównania.

---

Warunek instrukcji `if` zawsze umieszcza się wewnątrz nawiasów `()`, znajdujących się bezpośrednio po słowie kluczowym `if` i przed otwierającym nawiasem klamrowym.

---

Blok może zawierać dowolną liczbę instrukcji, a może też nie zawierać żadnej: `if (true) {}` jest poprawnym kodem JavaScript, który po prostu nic nie robi.

---

Blok kodu instrukcji `if` to zbiór poleceń wewnątrz nawiasów klamrowych `{ }` — część, która faktycznie się wykonuje, gdy warunek ma wartość `true`.
