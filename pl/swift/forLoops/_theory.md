Wiemy już, jak powtarzać kod za pomocą pętli `while`.
Na przykład ten program powtarza instrukcje, aby wyświetlić `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Ale to samo możemy zrobić za pomocą pętli `for`:
```swift
for i in 0..<5 {
    print("hello")
}
```

---

W pętli `for` możemy określić, ile razy chcemy, aby pętla się wykonała

---

Możemy użyć `..<` aby zapętlić się do następnej liczby (wykluczonej), lub `...` aby zapętlić się do następnej liczby (włączonej)

---

Zmienna o nazwie `i` jest zmienną licznikową.
Możemy nadać jej dowolną nazwę.
Zlicza ona, na której powtórzeniu pętli aktualnie jesteśmy

---

Funkcja `stride()` zwraca sekwencję liczb.
Wymaga parametrów _from_, _to_ i _by_.
Oto składnia tej funkcji:
```swift
stride(from:to:by:)
```
Pamiętaj, że wartość `to` jest wykluczona

---

Za pomocą funkcji `stride()` możemy również używać zakresów zamkniętych, korzystając z:
```swift
stride(from:through:by:)
```
W tym przypadku wartość `through` jest włączona

---

W Swift mamy również pętlę `forEach`.
W rzeczywistości `forEach` wywołuje podane domknięcie dla każdego elementu sekwencji w tej samej kolejności co pętla `for-in`:
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
Użycie metody `forEach` różni się od pętli `for-in` na dwa ważne sposoby:
1. Instrukcja `break` lub `continue` nie może być użyta do wyjścia z bieżącego wywołania domknięcia ciała lub do pominięcia kolejnych wywołań.
2. Użycie instrukcji `return` w domknięciu ciała spowoduje jedynie wyjście z domknięcia, a nie z zakresu zewnętrznego, i nie pominie kolejnych wywołań.
