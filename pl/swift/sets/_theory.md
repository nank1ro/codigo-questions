**Set** to kolekcja, która przechowuje wartości tego samego typu bez określonej kolejności i, co najważniejsze, **bez duplikatów**: każda wartość występuje co najwyżej raz.
Zbiory są idealne, gdy interesuje Cię tylko to, *które* wartości są obecne, a nie ile razy lub na jakiej pozycji.
Zbiór deklarujesz z typem `Set<Element>` i literałem w stylu tablicy:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
Adnotacja typu jest wymagana: bez niej Swift utworzyłby tablicę.
Jeśli literał zawiera wartość więcej niż raz, zbiór zachowuje tylko jedną kopię:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
Właściwość `count` mówi, ile różnych wartości zawiera zbiór.

---

Podobnie jak tablice, zbiory mogą być stałymi (`let`) lub zmiennymi (`var`). Tylko zbiór `var` można zmienić po utworzeniu.
Aby utworzyć pusty zbiór, wywołujesz inicjalizator typu, ponieważ sam pusty literał `[]` nie powiedziałby Swiftowi, jakiego typu elementów użyć:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
Właściwość `isEmpty` ma wartość `true`, gdy zbiór nie ma elementów, dokładnie tak jak w przypadku tablic.

---

Ponieważ zbiór nigdy nie przechowuje tej samej wartości dwa razy, jego `count` to liczba wartości *różnych*, niezależnie od tego, ile razy każda z nich została zapisana w literale.

---

Aby sprawdzić, czy wartość znajduje się w zbiorze, użyj metody `contains(_:)`, która zwraca `Bool`:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
To sprawdzenie jest bardzo szybkie w przypadku zbioru, nawet przy tysiącach elementów, co jest jednym z głównych powodów, dla których warto preferować zbiór zamiast tablicy przy sprawdzaniu przynależności.

---

Zbiór `var` można modyfikować za pomocą `insert(_:)` i `remove(_:)`:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 już tam jest: nic się nie zmienia
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 tam nie ma: nic się nie zmienia
```
Wstawienie wartości, która już jest obecna, nie ma żadnego efektu, a usunięcie wartości, której nie ma, nie powoduje błędu.
`remove(_:)` zwraca usuniętą wartość jako opcjonalną (`nil`, gdy nic nie zostało usunięte), dzięki czemu możesz sprawdzić, czy usunięcie faktycznie nastąpiło.
Aby całkowicie opróżnić zbiór, wywołaj `removeAll()`.

---

Możesz iterować po zbiorze za pomocą `for`-`in`, ale pamiętaj, że zbiór **nie ma określonej kolejności**: elementy mogą pojawiać się w dowolnej kolejności, a ta kolejność może się zmieniać między uruchomieniami.
Gdy kolejność ma znaczenie, wywołaj najpierw `sorted()`: zwraca on nową **tablicę** z elementami w kolejności rosnącej, pozostawiając zbiór bez zmian.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 w osobnych liniach
}
```

---

Zbiory obsługują klasyczne operacje teorii mnogości. Każda z nich zwraca **nowy** zbiór i pozostawia oryginały niezmienione:
- `a.union(b)` zawiera każdy element, który jest w `a`, w `b`, lub w obu
- `a.intersection(b)` zawiera tylko elementy, które są w **obu** `a` i `b`
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

Dwie kolejne operacje uzupełniają tę rodzinę:
- `a.subtracting(b)` zawiera elementy `a`, których **nie ma** w `b`
- `a.symmetricDifference(b)` zawiera elementy, które są w `a` lub w `b`, ale **nie w obu**
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
W przeciwieństwie do `union` i `intersection`, `subtracting` nie jest symetryczne: `a.subtracting(b)` i `b.subtracting(a)` zazwyczaj się różnią.

---

Zbiory można również porównywać ze sobą. Te metody zwracają `Bool`:
- `a.isSubset(of: b)` ma wartość `true`, gdy każdy element `a` jest również w `b`
- `a.isSuperset(of: b)` ma wartość `true`, gdy `a` zawiera każdy element `b`
- `a.isDisjoint(with: b)` ma wartość `true`, gdy `a` i `b` nie mają wspólnego elementu
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

Zbiory i tablice łatwo konwertują się jedne w drugie.
Przekazanie tablicy do `Set(...)` tworzy zbiór z jej elementów, co jest najszybszym sposobem na **usunięcie duplikatów**:
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} in some order
```
Przekazanie zbioru do `Array(...)` zwraca tablicę, ale ponieważ zbiór nie ma kolejności, elementy pojawiają się w nieprzewidywalnej kolejności.
Dlatego, gdy potrzebujesz uporządkowanego wyniku, zwykle wywołujesz `sorted()` na zbiorze, który już zwraca tablicę:
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
