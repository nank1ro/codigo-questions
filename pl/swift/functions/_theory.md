Być może rozważałeś sytuację, w której chciałbyś ponownie użyć fragmentu kodu, tylko z kilkoma różnymi wartościami.
Zamiast przepisywać cały kod, o wiele schludniej jest zdefiniować funkcję, która następnie może być wielokrotnie używana.
W Swift używamy słowa kluczowego `func` po którym następuje nazwa funkcji:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Nawiasy w __definicji funkcji__ nie muszą być puste, jeśli chcemy określić parametry

---

Czasami chcemy, aby funkcja __zwróciła__ wartość.
Do tego służy słowo kluczowe `return`.

---

Funkcje mogą mieć wiele parametrów wejściowych, które są zapisane w nawiasach funkcji, oddzielone przecinkami.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

Możesz użyć typu krotki jako typu zwracanego przez funkcję, aby zwrócić wiele wartości jako część jednej złożonej wartości zwracanej.

---

Jeśli nie chcesz etykiety argumentu dla parametru, wpisz podkreślenie `_` zamiast jawnej etykiety argumentu dla tego parametru

---

Możesz zdefiniować _domyślną_ wartość dla dowolnego parametru w funkcji, przypisując wartość do parametru po jego typie.
Jeśli wartość domyślna jest zdefiniowana, możesz pominąć ten parametr przy wywoływaniu funkcji
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

_Parametr wariadyczny_ przyjmuje zero lub więcej wartości określonego typu.
Używasz parametru wariadycznego, aby określić, że parametr może otrzymać zmienną liczbę wartości wejściowych podczas wywoływania funkcji.
Parametry wariadyczne zapisuje się przez wstawienie trzech kropek `...` po nazwie typu parametru.
Wartości przekazane do parametru wariadycznego są dostępne w ciele funkcji jako tablica odpowiedniego typu.
Na przykład, parametr wariadyczny o nazwie `numbers` i typie `Double...` jest dostępny w ciele funkcji jako stała tablica o nazwie numbers i typie `[Double]`

---

W funkcjach możemy dodać _opcjonalny komentarz_ wyjaśniający, co robi funkcja:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
Możemy używać `///` dla komentarza jednoliniowego i `/** */` dla komentarza wieloliniowego
