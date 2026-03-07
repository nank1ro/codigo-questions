Wiemy, jak powtarzać kod za pomocą pętli `while`.
Jak ten program powtarzający instrukcje, aby wyświetlić `hello`
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
Ale możemy zrobić to samo za pomocą pętli `for`:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

W pętli `for` możemy określić, ile razy chcemy, aby nasza pętla się wykonała

---

Możemy używać `<` do pętli aż do następnej liczby wyłącznie, lub `<=` do pętli aż do następnej liczby włącznie

---

Zmienna o nazwie `i` to zmienna licznikowa.
Możemy nadać jej dowolną nazwę.
Zlicza, na której iteracji pętli aktualnie się znajdujemy

---

W JavaScript mamy również pętlę `forEach`.
W rzeczywistości `forEach` wywołuje podane domknięcie na każdym elemencie sekwencji w tej samej kolejności co pętla `for`:
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
Używanie metody `forEach` różni się od pętli `for` na dwa ważne sposoby:
1. Instrukcji `break` lub `continue` nie można używać do zakończenia bieżącego wywołania domknięcia ciała lub do pomijania kolejnych wywołań.
2. Użycie instrukcji `return` w domknięciu ciała spowoduje jedynie wyjście z domknięcia, a nie z zewnętrznego zakresu, i nie pominie kolejnych wywołań.
UWAGA: `=>` to tak zwana _funkcja strzałkowa_ i jest to skrócona składnia funkcji ES6, która zastępuje nawiasy klamrowe {} i zwraca wartość (jeśli potrzeba)
