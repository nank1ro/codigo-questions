`Set` to typ danych, który można używać do przechowywania kolekcji różnych informacji jako sekwencji pod jedną nazwą zmiennej.
Główna różnica w stosunku do `List` polega na tym, że `Set` pozwala na przechowywanie tylko jednego elementu każdej wartości.

Podobnie jak `List`, `Set` przechowuje wiele wartości jednego lub wielu typów i używa **indeksów** do ich rozróżniania.
Możesz przypisać elementy do zbioru za pomocą wyrażenia:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` oznacza typ elementów wewnątrz zbioru, na przykład może to być `Int`, `String`, `Any`...

---

`Set` to kolekcja __unikalnych__ elementów bez określonej kolejności.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

W __[1]__ próbujemy utworzyć zbiór z liczbą __1__ pojawiającą się dwukrotnie, ale jak widać każdy element musi być unikalny i drugi __1__ jest automatycznie odrzucany.

---

W Kotlinie istnieją dwa typy `Set`:

- `Set` nie może być modyfikowany po utworzeniu.
- `MutableSet` może być modyfikowany po utworzeniu, co oznacza, że można dodawać, usuwać lub aktualizować jego elementy.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ generuje błąd, ponieważ `Set` jest _tylko do odczytu_.

Aby utworzyć modyfikowalny zbiór, użyj słowa kluczowego `mutableSetOf`
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

Najczęstszą operacją na `Set` jest sprawdzanie przynależności za pomocą `in` lub `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

Jak widać powyżej, `in` i `contains` zwracają wartość `Bool` informującą, czy przekazany element jest obecny w zbiorze

---

Kolejność elementów w `Set` nie ma znaczenia.
W rzeczywistości, jeśli porównasz dwa `Set` z tymi samymi elementami w różnej kolejności, okaże się, że są równe.

---

Na `Set` można wykonywać różne operacje, takie jak suma, część wspólna, różnica i podzbiór.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

Aby przekonwertować `Set` na `List`, możemy użyć funkcji `toList()`
