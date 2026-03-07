Tablice to typ danych, którego możesz używać do przechowywania kolekcji różnych informacji jako sekwencji pod jedną nazwą zmiennej.
Tablica przechowuje wiele wartości jednego lub wielu typów i używa **indeksów** do ich rozróżnienia.
Możesz przypisać elementy do tablicy za pomocą wyrażenia o postaci:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` oznacza typ elementów wewnątrz tablicy, na przykład może to być `Int`, `String`, `Any`...

---

Możesz uzyskać dostęp do pojedynczego elementu tablicy za pomocą jego indeksu.
Indeks jest jak adres, który identyfikuje miejsce elementu w tablicy.
Indeks pojawia się bezpośrednio po nazwie tablicy, w nawiasach kwadratowych, w taki sposób:
```swift
arrayName[index]
```

Indeksy tablicy zaczynają się od `0`, **nie** od `1`! Dostęp do pierwszego elementu tablicy uzyskujesz w ten sposób: `arrayName[0]`.
Drugi element tablicy jest pod indeksem 1: `arrayName[1]`.

---

Indeks tablicy zachowuje się jak każda inna nazwa zmiennej.
Można go używać zarówno do odczytywania, jak i przypisywania wartości.
Zobaczyłeś, jak uzyskać dostęp do indeksu tablicy w taki sposób:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
Tak działa przypisanie:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

Podobnie jak ciągi znaków, tablice mają **długość** `count`.
Długość tablicy to liczba elementów, które zawiera

---

Tablica nie musi mieć stałej długości.
Możesz dodawać elementy na koniec tablicy w dowolnym momencie!
Aby dodać element do tablicy, używamy funkcji `append`:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

Czasami chcesz uzyskać dostęp tylko do części tablicy.
Rozważ następujący kod:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
Najpierw tworzymy tablicę o nazwie `numbers`.
Następnie pobieramy podsekcję tablicy i zapisujemy ją w tablicy slice.
Robimy to, definiując indeksy, które chcemy uwzględnić po nazwie tablicy: `numbers[1...2]`.
W Swift możemy uwzględnić ostatni indeks używając `...`, ale możemy też wykluczyć ostatni indeks używając `..<`

---

W Swift możemy wycinać tablicę według własnych potrzeb!
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
Jeśli wycinek tablicy zawiera pierwszy lub ostatni element tablicy, indeks tego elementu nie musi być uwzględniony

---

Elementy tablicy mogą być dowolnego typu, jeśli określimy typ `Any`:
```swift
var arrayName: [Any] = ["one", 2, true]
```
Mamy tu kolejno: ciąg znaków, liczbę całkowitą i wartość logiczną.
Możemy też mieć tablice zawierające tablice!

---

Czasami musisz wyszukać element w tablicy.
W Swift możemy użyć metody `firstIndex()`:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
Powyższy kod drukuje pierwszy indeks zawierający ciąg `"Zac"`, w tym przypadku `1`.
Możemy również wstawiać elementy do tablicy pod określonym indeksem, używając metody `insert()`:
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
Powyższy kod wstawia `"Ali"` pod indeksem `1`, co przesuwa wszystko po tym indeksie o 1

---

W Swift możemy przeglądać tablicę w bardzo prosty sposób używając słów kluczowych `for..in`:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
Nazwa zmiennej następuje po słowie kluczowym `for` - będzie jej przypisywana wartość każdego kolejnego elementu tablicy.

---

**Krotki** są podobne do tablic, ale możesz nadawać nazwy elementom i używać tych nazw do odwoływania się do nich
Aby utworzyć krotkę, używamy nawiasów okrągłych `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
