Tablice to typ danych, którego możesz używać do przechowywania kolekcji różnych informacji jako sekwencji pod jedną nazwą zmiennej.
Tablica przechowuje wiele wartości jednego lub wielu typów i używa **indeksów** do rozróżniania tych wartości.
Możesz przypisać elementy do tablicy za pomocą wyrażenia w postaci:
```javascript
var arrayName = [item1, item2];
```

---

Możesz uzyskać dostęp do pojedynczego elementu tablicy za pomocą jego indeksu.
Indeks jest jak adres, który identyfikuje miejsce elementu w tablicy.
Indeks pojawia się bezpośrednio po nazwie tablicy, w nawiasach kwadratowych, na przykład:
```javascript
arrayName[index];
```
Indeksy tablicy zaczynają się od `0`, **nie** od `1`! Dostęp do pierwszego elementu tablicy uzyskujesz w ten sposób: `arrayName[0]`.
Drugi element tablicy ma indeks 1: `arrayName[1]`.

---

Indeks tablicy zachowuje się jak każda inna nazwa zmiennej.
Można go używać zarówno do uzyskiwania dostępu, jak i do przypisywania wartości.
Widziałeś, jak uzyskać dostęp do indeksu tablicy w ten sposób:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
Tak działa przypisanie:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Podobnie jak ciągi znaków, tablice mają **długość**.
Długość tablicy to liczba elementów, które zawiera

---

Tablica nie musi mieć stałej długości.
Możesz dodawać elementy na końcu tablicy w dowolnym momencie!
Aby dodać element do tablicy, używamy funkcji `push`:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

Czasami chcesz uzyskać dostęp tylko do fragmentu tablicy.
Rozważ następujący kod:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
Najpierw tworzymy tablicę o nazwie `numbers`.
Następnie pobieramy fragment tablicy i zapisujemy go w tablicy slice.
Robimy to, definiując indeksy, które chcemy uwzględnić, po nazwie tablicy: `numbers.slice(1, 3)`.
Pamiętaj, że prawy indeks jest wykluczony

---

W JavaScript możemy wycinać tablice tak jak chcemy!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
Jeśli fragment tablicy zawiera pierwszy lub ostatni element tablicy, indeks tego elementu nie musi być uwzględniony

---

Elementy tablicy mogą być dowolnego typu.
```javascript
var arrayName = ["one", 2, true];
```
W powyższym przykładzie mamy kolejno: ciąg znaków, liczbę całkowitą i wartość logiczną.
Ale możemy też mieć tablice zawierające inne tablice!

---

Czasami musisz wyszukać element w tablicy.
W JavaScript możemy użyć metody `indexOf()`:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
Powyższy kod drukuje pierwszy indeks, który zawiera ciąg `"Zac"`, w tym przypadku `1`.
Możemy również wstawiać elementy do tablicy na określonym indeksie, używając metody `splice()`:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
Powyższy kod wstawia `"Ali"` na indeksie `1`, co przesuwa wszystko po tym indeksie o 1.
Druga wartość `0` oznacza _deleteCount_, w tym przypadku nie usuwamy żadnego elementu z tablicy; ale gdybyśmy podali `1`, wartość `Zac` zostałaby usunięta z tablicy

---

W JavaScript możemy przechodzić przez tablicę w bardzo prosty sposób, używając słów kluczowych `for..of`:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
Po słowie kluczowym `for` następuje nazwa zmiennej, która będzie kolejno przyjmować wartość każdego elementu tablicy.
