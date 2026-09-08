**String** to fragment tekstu. W Swift zapisujesz literał ciągu znaków między cudzysłowami, a jego typem jest `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Jak przy każdej innej wartości, `let` tworzy stałą, której nie można zmienić, a `var` tworzy zmienną, którą można.
Swift wnioskuje typ `String` na podstawie literału, więc adnotacja typu jest opcjonalna.

---

**Interpolacja ciągów znaków** wstawia wartość wyrażenia wewnątrz literału ciągu znaków. Otocz wyrażenie w `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Można interpolować dowolny typ: liczby, wartości logiczne i inne ciągi znaków są automatycznie konwertowane na tekst.

---

Dwa ciągi znaków można połączyć operatorem `+`, który tworzy nowy ciąg znaków:
```swift
let full = "Hello" + " " + "world" // Hello world
```
Aby dodać tekst na końcu istniejącej zmiennej typu string, użyj `+=`. Zmienna musi być zadeklarowana za pomocą `var`, ponieważ jej wartość się zmienia:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

Właściwość `count` zwraca liczbę znaków w ciągu, a `isEmpty` ma wartość `true`, gdy ciąg nie zawiera żadnych znaków:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Liczony jest każdy znak, w tym spacje i znaki interpunkcyjne.

---

`String` to kolekcja wartości `Character`. `Character` to pojedyncza litera, cyfra, symbol lub spacja i zapisuje się go w tych samych cudzysłowach co ciąg znaków, więc aby go uzyskać, potrzebujesz adnotacji typu:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Sprawdzanie `isEmpty` jest lepsze niż porównywanie `count` z `0`: czyta się lepiej i nie trzeba liczyć każdego znaku.

---

Wieloliniowy literał ciągu znaków** zaczyna się i kończy trzema cudzysłowami `"""`, każdym w osobnej linii. Każda linia między nimi staje się częścią ciągu znaków, a podziały wierszy są zachowywane:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
To wypisuje obie linie dokładnie tak, jak zostały napisane. Zamykające `"""` ustala też wcięcie: wszelkie białe znaki przed nim są usuwane z początku każdej linii.

---

Ponieważ ciąg znaków jest kolekcją znaków, możesz iterować po nim za pomocą pętli `for`-`in`. Każda iteracja daje ci jeden `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
`Character` można porównać operatorem `==` z literałem znakowym, więc zliczanie, ile razy pojawia się dany znak, to po prostu pętla i licznik.

---

W przeciwieństwie do tablic, ciągów znaków nie można indeksować liczbą całkowitą jak `text[2]`: niektóre znaki zajmują więcej pamięci niż inne, więc Swift używa dedykowanego typu `String.Index`, aby wskazać pozycję.
`startIndex` to pozycja pierwszego znaku, a `endIndex` to pozycja *po* ostatnim. Aby przesunąć się od indeksu, użyj `index(_:offsetBy:)`, a następnie zindeksuj ciąg wynikiem:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Przesunięcie się poza koniec ciągu znaków powoduje awarię w czasie działania programu, więc przesunięcie musi mieścić się w granicach `count`.

---

Praca z indeksami jest rozwlekła, więc Swift oferuje skróty dla najczęstszych przypadków:
- `first` i `last` zwracają pierwszy i ostatni znak jako opcjonalny `Character?` (`nil` dla pustego ciągu)
- `prefix(n)` zwraca pierwsze `n` znaków, a `suffix(n)` ostatnie `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` i `suffix` zwracają `Substring`, widok oryginalnego tekstu. Aby zapisać go jako prawdziwy `String`, otocz go w `String(...)`. Jeśli `n` jest większe niż `count`, po prostu otrzymujesz cały ciąg znaków.

---

Trzy metody odpowiadają na najczęstsze pytania dotyczące zawartości ciągu znaków, a każda z nich zwraca `Bool`:
- `contains(_:)` ma wartość `true`, gdy ciąg zawiera podany tekst (lub znak) w dowolnym miejscu
- `hasPrefix(_:)` ma wartość `true`, gdy ciąg zaczyna się od podanego tekstu
- `hasSuffix(_:)` ma wartość `true`, gdy ciąg kończy się podanym tekstem
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Wszystkie trzy rozróżniają wielkość liter: `"Swift".hasPrefix("s")` ma wartość `false`.

---

Ponieważ `contains`, `hasPrefix` i `hasSuffix` zwracają wartości logiczne, naturalnie łączą się z `||` i `&&`, aby budować bardziej złożone sprawdzenia.

---

`uppercased()` i `lowercased()` zwracają **nowy** ciąg znaków, w którym każda litera jest zamieniona na wielką lub małą. Oryginalny ciąg nie jest modyfikowany:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Obie to metody, więc nie zapomnij o nawiasach.

---

Konwersja na małe litery to zwykły sposób porównywania tekstu z pominięciem wielkości liter: dwa ciągi różniące się tylko wielkością liter stają się równe, gdy oba zostaną zamienione na małe litery.

---

`split(separator:)` dzieli ciąg znaków na tablicę fragmentów wszędzie tam, gdzie pojawia się znak separatora. `joined(separator:)` robi coś przeciwnego: skleja elementy tablicy w jeden ciąg znaków, umieszczając separator między nimi:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Podobnie jak `prefix`, `split` zwraca wartości `Substring`; otocz jedną w `String(...)`, jeśli musisz zapisać ją jako `String`.

---

Dzielenie po spacji to najprostszy sposób na rozbicie zdania na słowa, a łączenie to sposób na odbudowanie tekstu z tablicy.

---

Framework Foundation dodaje wiele dodatkowych metod dla ciągów znaków. Jedną z najbardziej przydatnych jest `replacingOccurrences(of:with:)`, która zwraca nowy ciąg znaków, w którym każde wystąpienie pierwszego tekstu jest zastępowane drugim:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Pamiętaj, aby na początku pliku umieścić `import Foundation`, inaczej metoda nie będzie dostępna. Wywołania metod można łączyć w łańcuch, więc `text.lowercased().replacingOccurrences(of: " ", with: "_")` jest poprawne.

---

Ciągi znaków można porównywać tymi samymi operatorami co liczby. `==` sprawdza, czy dwa ciągi mają dokładnie te same znaki, natomiast `<` i `>` porównują je w porządku alfabetycznym, znak po znaku:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
Porównanie rozróżnia wielkość liter, a każda wielka litera znajduje się **przed** każdą małą literą, więc `"B" < "a"` ma wartość `true`.

---

`Character` nie jest `String`, więc nie można go bezpośrednio połączyć z ciągiem znaków operatorem `+`. Najpierw przekonwertuj go za pomocą `String(...)`:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Połączenie tego z pętlą `for`-`in` pozwala odbudować ciąg znaków znak po znaku, na przykład umieszczając każdy nowy znak przed tymi już zebranymi.
