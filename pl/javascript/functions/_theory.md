Być może zastanawiałeś się nad sytuacją, w której chciałbyś ponownie użyć fragmentu kodu, tylko z kilkoma różnymi wartościami.
Zamiast przepisywać cały kod, o wiele porządniej jest zdefiniować funkcję, którą można następnie używać wielokrotnie.
W JavaScript używamy słowa kluczowego `function`, po którym następuje nazwa funkcji:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

Nawiasy w __definicji funkcji__ nie muszą być puste, jeśli chcemy określić parametry

---

Czasami chcemy, aby funkcja __zwracała__ wartość.
Do tego służy słowo kluczowe `return`.

---

Funkcje mogą mieć wiele parametrów wejściowych, które są zapisywane w nawiasach funkcji, oddzielone przecinkami.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

Możesz zdefiniować _domyślną_ wartość dla dowolnego parametru w funkcji, przypisując wartość do parametru po typie tego parametru.
Jeśli zdefiniowana jest wartość domyślna, możesz pominąć ten parametr podczas wywoływania funkcji
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

Składnia __parametru rest__ pozwala nam reprezentować nieokreśloną liczbę argumentów jako tablicę.
Parametry rest zapisuje się przez wstawienie trzech znaków kropki `...` przed nazwą parametru.
Wartości przekazane do parametru rest są dostępne w ciele funkcji jako tablica.
Na przykład parametr rest o nazwie `numbers` jest dostępny w ciele funkcji jako stała tablica o nazwie numbers

---

W funkcjach możemy dodać _opcjonalny komentarz_ wyjaśniający, co robi funkcja:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Możemy użyć `//` dla komentarza jednoliniowego i `/** */` dla komentarza wieloliniowego
