Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy wyjść na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `niceWeather` i wykonać akcję wyjścia na zewnątrz `if` ta zmienna jest `true`, jak:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

Kontynuujmy poprzedni przykład.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
// prints 10
```
Skrócony zapis powyższego kodu to:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
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
