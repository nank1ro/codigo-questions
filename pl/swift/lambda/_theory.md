**Domknięcie** to blok kodu, który możesz przekazywać i wywoływać później, jak funkcja bez nazwy.
Pełna składnia wyrażenia domknięcia umieszcza parametry i typ zwracany wewnątrz nawiasów klamrowych, po których następuje słowo kluczowe `in` i treść:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Podobnie jak każda inna wartość, domknięcie może być przechowywane w stałej, a następnie wywoływane przy użyciu nazwy tej stałej:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Zapisywanie każdego typu wewnątrz domknięcia jest często niepotrzebne. Gdy stała ma jawny **typ funkcyjny**, Swift wnioskuje typy parametrów i typ zwracany, więc przed `in` wystarczy podać tylko nazwy parametrów:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
Typ `(Int) -> Int` czyta się jako "funkcja, która przyjmuje `Int` i zwraca `Int`".
Gdy treść to pojedyncze wyrażenie, słowo kluczowe `return` również można pominąć, nazywa się to **niejawnym zwracaniem**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift idzie o krok dalej: wewnątrz domknięcia możesz odwoływać się do argumentów za pomocą **skróconych nazw argumentów** `$0`, `$1`, `$2` i tak dalej, bez deklarowania jakiegokolwiek parametru ani słowa kluczowego `in`.
`$0` to pierwszy argument, `$1` drugi:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
Typy nadal pochodzą z adnotacji `(Int, Int) -> Int`.

---

Ponieważ domknięcia są wartościami, funkcja może przyjąć jedno z nich jako parametr. Typ parametru to po prostu typ funkcyjny:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
Funkcja `apply` nie wie, co robi `operation`, wie tylko, że przyjmuje `Int` i zwraca `Int`, i wywołuje ją jak każdą inną funkcję.

---

Gdy domknięcie jest **ostatnim** argumentem funkcji, możesz zapisać je po nawiasie zamykającym wywołanie. To jest składnia **trailing closure**:
```swift
print(apply(5) { $0 + 1 }) // 6
```
Jeśli domknięcie jest jedynym argumentem, nawiasy można całkowicie pominąć:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Obie formy wywołują dokładnie tę samą funkcję, składnia trailing jest po prostu łatwiejsza do odczytania, gdy domknięcie jest długie.

---

Domknięcia pokazują swoją siłę w metodach tablicowych, które przyjmują jedno z nich jako argument. `map` wywołuje domknięcie na każdym elemencie i zwraca nową tablicę z wynikami:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
Oryginalna tablica nie zostaje zmieniona. Ponieważ `map` przyjmuje pojedyncze domknięcie jako argument, składnia trailing closure jest zwykłym sposobem jej wywoływania.

---

`filter` zachowuje tylko te elementy, dla których domknięcie zwraca `true`. Domknięcie otrzymuje jeden element i musi zwrócić `Bool`:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Elementy zachowują swoją oryginalną kolejność, a wynikiem jest nowa tablica tego samego typu elementów.

---

`reduce` łączy wszystkie elementy w jedną wartość. Przyjmuje wartość początkową i domknięcie z dwoma argumentami: wartością zgromadzoną do tej pory i bieżącym elementem. Domknięcie zwraca nową zgromadzoną wartość:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Tutaj `$0` zaczyna jako `1`, potem staje się `1 * 1`, `1 * 2`, `2 * 3` i wreszcie `6 * 4`.
Ponieważ `map`, `filter` i `reduce` zwracają wartości, można je łączyć w łańcuch: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` zwraca nową posortowaną tablicę. Domknięcie otrzymuje dwa elementy i zwraca `true`, gdy pierwszy powinien znaleźć się **przed** drugim:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
Domknięcie może porównywać cokolwiek, na przykład `words.sorted { $0.count < $1.count }` porządkuje ciągi znaków od najkrótszego do najdłuższego.

---

Domknięcie może korzystać ze zmiennych zadeklarowanych poza jego treścią. **Przechwytuje** je: zmienna nadal istnieje tak długo, jak istnieje domknięcie, nawet po zakończeniu funkcji, która ją zadeklarowała.
Dzięki temu funkcja może zbudować domknięcie z własnym, prywatnym stanem:
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int` to typ domknięcia bez parametrów, które zwraca `Int`. Każde wywołanie zwróconego domknięcia zwiększa to samo przechwycone `count`:
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

Zwracanie domknięcia to wygodny sposób na budowanie dostosowanych funkcji. Parametry funkcji zewnętrznej są przechwytywane przez domknięcie, które ona zwraca:
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
Typ zwracany `(Int) -> Int` opisuje domknięcie, a skrót `$0` odnosi się do argumentu tego domknięcia, a nie `makeAdder`.

---

Domknięcie zapisane w stałej może być przekazane wszędzie tam, gdzie oczekiwany jest argument-domknięcie, przy użyciu etykiety argumentu parametru:
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

Każde wywołanie funkcji zwracającej domknięcie tworzy **nową** przechwyconą zmienną. Dwa domknięcia zbudowane przez osobne wywołania nie współdzielą swojego stanu:
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
Stan jest współdzielony tylko między wywołaniami tego samego domknięcia.

---

Domyślnie domknięcie przekazane do funkcji może być używane tylko podczas działania tej funkcji. Jeśli funkcja przechowuje domknięcie albo zwraca inne domknięcie, które go używa, domknięcie **ucieka** (escapes) z funkcji, a jego parametr musi być oznaczony `@escaping`:
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
Bez `@escaping` kompilator zgłasza błąd, ponieważ zwrócone domknięcie używałoby `task` już po zakończeniu działania `twice`.

---

Domknięcia można przechowywać w tablicach jak każdą inną wartość. Typem elementu jest typ funkcyjny:
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
Przechodzenie po takiej tablicy i wywoływanie po kolei każdego domknięcia tworzy mały **potok** (pipeline) przekształceń.
