Zacznijmy od operatora porównania **równości** `==`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są równe, na przykład:
```javascript
console.log(2 == 2); 
// wypisuje true
console.log(2 == 3);
// wypisuje false
```

---

Kontynuujmy z operatorem porównania **nierówności** `!=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są **NIERÓWNE**, na przykład:
```javascript
console.log(2 != 2);
// wypisuje false
console.log(2 != 3); 
// wypisuje true
```
Jest to dokładne przeciwieństwo operatora *równości*

---

Kontynuujmy z operatorem porównania **większości** `>`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe od drugiego, na przykład:
```javascript
console.log(2 > 2);
// wypisuje false
console.log(3 > 2);
// wypisuje true
```

---

Kontynuujmy z operatorem porównania **mniejszości** `<`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```javascript
console.log(2 < 2);
// wypisuje false
console.log(2 < 3);
// wypisuje true
```

---

Kontynuujmy z operatorem porównania **większy lub równy** `>=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```javascript
console.log(2 >= 2); 
// wypisuje true
console.log(3 >= 2);
// wypisuje true
console.log(3 >= 4);
// wypisuje false
```

---

Kontynuujmy z operatorem porównania **mniejszy lub równy** `<=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```javascript
console.log(2 <= 2); 
// wypisuje true
console.log(3 <= 2);
// wypisuje false
console.log(3 <= 4);
// wypisuje true
```

---

Teraz przyjrzyjmy się operatorom **logicznym**, zacznijmy od pierwszego zwanego __AND__ `&&`.
Zwraca on pierwszy operand, który przyjmuje wartość *false*, lub ostatni, jeśli wszystkie są *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// wypisuje false
console.log(1 == 1 && 1 == 1.0);
// wypisuje true
```

---

Kontynuujmy z operatorem logicznym **lub** `||`.
Zwraca on pierwszy operand, który przyjmuje wartość *true*, lub ostatni, jeśli wszystkie są *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// wypisuje true
console.log(1 == 2 || 1 == 3);
// wypisuje false
```

---

Zakończmy z operatorem logicznym **negacji** `!`.
Zwraca on wartość logiczną będącą odwrotnością stanu logicznego wyrażenia.
```javascript
console.log(!true);
// wypisuje false
console.log(!false);
// wypisuje true
console.log(!(2 == 2));
// wypisuje false
```

---

`==` porównuje obie strony po przekonwertowaniu ich do wspólnego typu, więc `"5" == 5` daje `true`. Ścisły operator `===` pomija tę konwersję i wymaga, aby typy również się zgadzały.
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

`!=` konwertuje przed porównaniem, tak samo jak `==`, więc `"5" != 5` daje `false`. Jego ścisły odpowiednik `!==` traktuje ciąg znaków i liczbę jako różne, niezależnie od tego, co zawierają.
```javascript
console.log("5" !== 5); // true
```

---

Gdy obie strony są ciągami znaków, `>` porównuje je znak po znaku według kolejności kodów, a nie według długości, więc `"b" > "a"` daje `true`, podobnie jak `"apple" > "ant"`.

---

`>=` jest spełnione przez którąkolwiek z połówek swojej nazwy: `8 >= 8` daje `true`, ponieważ obie wartości są równe, podczas gdy bardziej rygorystyczne `8 > 8` daje `false`.

---

Każde porównanie z udziałem `NaN` zwraca `false`, nawet te przeciwstawne: zarówno `NaN < 3`, jak i `NaN >= 3` dają `false`, więc nieudane `<` nie zawsze oznacza, że lewa strona jest większa.

---

Gdy jedna strona jest ciągiem znaków, a druga liczbą, `<=` najpierw konwertuje ciąg znaków na liczbę, więc `"7" <= 8` daje `true`.
