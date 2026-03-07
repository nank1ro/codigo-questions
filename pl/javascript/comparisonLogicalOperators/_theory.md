Zacznijmy od operatora porównania **równości** `==`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są równe, na przykład:
```javascript
console.log(2 == 2); 
// prints true
console.log(2 == 3);
// prints false
```

---

Kontynuujmy z operatorem porównania **nierówności** `!=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są **NIERÓWNE**, na przykład:
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3); 
// prints true
```
Jest to dokładne przeciwieństwo operatora *równości*

---

Kontynuujmy z operatorem porównania **większości** `>`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe od drugiego, na przykład:
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

Kontynuujmy z operatorem porównania **mniejszości** `<`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

Kontynuujmy z operatorem porównania **większy lub równy** `>=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```javascript
console.log(2 >= 2); 
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

Kontynuujmy z operatorem porównania **mniejszy lub równy** `<=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```javascript
console.log(2 <= 2); 
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

Teraz przyjrzyjmy się operatorom **logicznym**, zacznijmy od pierwszego zwanego __AND__ `&&`.
Zwraca on pierwszy operand, który przyjmuje wartość *false*, lub ostatni, jeśli wszystkie są *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

Kontynuujmy z operatorem logicznym **lub** `||`.
Zwraca on pierwszy operand, który przyjmuje wartość *true*, lub ostatni, jeśli wszystkie są *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

Zakończmy z operatorem logicznym **negacji** `!`.
Zwraca on wartość logiczną będącą odwrotnością stanu logicznego wyrażenia.
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
