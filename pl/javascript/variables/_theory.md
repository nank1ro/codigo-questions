Zmienne są kontenerami do przechowywania wartości danych.
Każda zmienna w JavaScript jest obiektem.
Aby utworzyć zmienną, musimy nadać jej **nazwę**, pamiętając, że nie może ona zawierać spacji.
Zmienna jest tworzona w momencie pierwszego przypisania do niej wartości.
W JavaScript stałe deklaruje się za pomocą słów kluczowych `let` lub `const`, a zmienne za pomocą słowa kluczowego `var`.
Wartości stałej nie można zmienić po jej ustawieniu, podczas gdy zmienna może w przyszłości przyjąć inną wartość.
Przykład tworzenia zmiennej o nazwie `x`:
```javascript
var x = 1;
```
W ten sposób przypisaliśmy wartość `1` do zmiennej o nazwie `x`.
Jeśli wydrukujemy zmienną `x`, otrzymamy liczbę `1`:
```javascript
console.log(x);
// prints 1
```

---

Zmienne są tak nazywane, ponieważ przechowywane przez nie wartości mogą się zmieniać.
Możemy zaktualizować `x`, używając `=` i podając nową wartość.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

Możemy również nadawać zmiennym wartości innych zmiennych.
Tutaj możemy nadać zmiennej `y` wartość `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

Kiedy aktualizujemy zmienną, zapomina ona swoją poprzednią wartość.
Tutaj możemy wyświetlić zmienną `x` dwa razy i zobaczyć, jak aktualizuje się jej wartość.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

W JavaScript zmienne łańcuchowe można deklarować zarówno za pomocą podwójnych, jak i pojedynczych cudzysłowów:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

Jeśli chcemy nazwy zmiennej składającej się z wielu słów, używamy **camelCase**.
Jest to praktyka pisania wyrażeń, w której każde słowo w środku wyrażenia zaczyna się od wielkiej litery
