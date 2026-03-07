Listy to typ danych, którego możesz użyć do przechowywania kolekcji różnych informacji jako sekwencji pod jedną nazwą zmiennej.
Lista przechowuje wiele wartości jednego lub wielu typów i używa **indeksów** do rozróżniania tych wartości.
Możesz przypisać elementy do listy za pomocą wyrażenia o postaci:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` oznacza typ elementów wewnątrz listy, na przykład może to być `Int`, `String`, `Any`...

---

Lista to kolekcja elementów w określonej kolejności. W Kotlinie istnieją dwa typy list:

- `List` nie może być modyfikowana po jej utworzeniu.
- `MutableList` może być modyfikowana po jej utworzeniu, co oznacza, że możesz dodawać, usuwać lub aktualizować jej elementy.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ zgłasza błąd, ponieważ `List`y są _tylko do odczytu_.

Aby utworzyć modyfikowalną listę, użyj słowa kluczowego `mutableListOf`
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

Możesz uzyskać dostęp do pojedynczego elementu listy za pomocą jego indeksu.
Indeks jest jak adres, który identyfikuje miejsce elementu na liście.
Indeks pojawia się bezpośrednio po nazwie listy, w nawiasach kwadratowych, w ten sposób:
```kotlin
listName[index]
```

Indeksy listy zaczynają się od `0`, **nie** od `1`! Dostęp do pierwszego elementu listy uzyskuje się tak: `listName[0]` lub `listName.get(0)` lub nawet `listName.first()`.
Drugi element listy ma indeks __1__: `listName[1]`.

---

Indeks jest w rzeczywistości przesunięciem względem pierwszego elementu. Na przykład, gdy piszesz `list[2]`, nie prosisz o drugi element listy, ale o element, który jest przesunięty o 2 pozycje względem pierwszego elementu. Zatem `list[0]` to pierwszy element (przesunięcie zerowe), `list[1]` to drugi element (przesunięcie o 1), `list[2]` to trzeci element (przesunięcie o 2) i tak dalej.

Indeks listy może być używany zarówno do odczytu, jak i do przypisywania wartości.
Zobaczyłeś, jak uzyskać dostęp do indeksu listy w ten sposób:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
Oto jak działa przypisanie:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

Podobnie jak ciągi znaków, listy mają **długość** pobieraną za pomocą gettera `size`.
Długość listy to liczba elementów, które zawiera

---

Inną przydatną operacją na liście jest metoda `contains`, która pozwala sprawdzić, czy dany element znajduje się na liście.
Na przykład, jeśli masz listę imion, możesz użyć metody `contains`, aby sprawdzić, czy dane imię jest obecne na liście.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

Modyfikowalna lista nie musi mieć stałej długości.
Możesz dodawać elementy na końcu listy w dowolnym momencie!
Aby dodać element do modyfikowalnej listy, używamy funkcji `add` lub skrótu `+=`:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

Jak widzieliśmy w poprzednim przykładzie, możemy dodawać elementy jeden po jednym używając funkcji `add`.
Ale jeśli musimy dodać wszystkie elementy innej listy naraz, możemy po prostu użyć funkcji `addAll` lub skrótu `+=`:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

Czasami chcesz uzyskać dostęp tylko do fragmentu listy.
Rozważ następujący kod:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: najpierw tworzymy listę _tylko do odczytu_ o nazwie `numbers`.
__[2]__: następnie pobieramy fragment listy za pomocą funkcji `slice` i przechowujemy go na liście slice.
Robimy to, definiując indeksy, które chcemy uwzględnić wewnątrz funkcji `slide`.

W Kotlinie możemy uwzględnić ostatni indeks używając `..`, ale możemy też wykluczyć ostatni indeks używając `until`

---

Elementy listy mogą być dowolnego typu, jeśli określimy typ `Any`:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
W powyższym przykładzie mamy kolejno: `String`, `Integer` i `Boolean`.
Możemy również tworzyć listy zawierające listy!

---

Czasami musisz wyszukać element na liście.
W Kotlinie możemy użyć metody `indexOfFirst`:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

Metoda `indexOfFirst` przyjmuje funkcję __predykat__, która będzie ewaluowana dla każdego elementu na liście, dopóki nie będzie prawdziwa, zwracając _indeks_ elementu.
Powyższy kod drukuje pierwszy indeks zawierający ciąg `"Zac"`, w tym przypadku `1`.

Możemy również wstawiać elementy do modyfikowalnej listy na określony indeks za pomocą metody `add(index, element)`:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
Powyższy kod wstawia `"Ali"` na indeksie `1`, co przesuwa wszystko po tym indeksie o 1 w dół

---

W Kotlinie możemy iterować przez listę w bardzo prosty sposób używając słów kluczowych `for..in`:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
Po słowie kluczowym `for` następuje nazwa zmiennej, która będzie kolejno przyjmować wartość każdego elementu listy.
