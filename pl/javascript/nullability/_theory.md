JavaScript ma dwa różne sposoby na powiedzenie "nie ma tu żadnej wartości".
`undefined` oznacza, że wartość **nigdy nie została dostarczona**. Zmienna zadeklarowana bez wartości przyjmuje `undefined`, i tak samo właściwość, która nie istnieje w obiekcie:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` to wartość, którą **Ty** przypisujesz celowo, aby powiedzieć "pusto, i wiem o tym":
```javascript
let owner = null;
console.log(owner);
// prints null
```
Zatem `undefined` to zwykle język informujący Cię, że czegoś brakuje, podczas gdy `null` to programista stwierdzający, że coś jest celowo puste.

---

Funkcje dają `undefined` jeszcze w dwóch sytuacjach.
Gdy wywołasz funkcję z **mniejszą liczbą argumentów**, niż deklaruje, brakujące parametry przyjmują `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Gdy funkcja kończy działanie **bez `return`** (lub z samym `return;`), jej wywołanie daje `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Zauważ, że jawne przekazanie `null` to nie to samo, co pominięcie argumentu: `greet(null)` wypisuje `null`, ponieważ `null` to prawdziwa wartość przekazana do funkcji.

---

Operator `typeof` zwraca typ wartości w postaci ciągu znaków. Dla `undefined` odpowiada `"undefined"`, zgodnie z oczekiwaniami:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Dla `null` odpowiada jednak `"object"`. To błąd z samej pierwszej wersji JavaScriptu, którego nigdy nie naprawiono, ponieważ zbyt dużo kodu od niego zależy:
```javascript
console.log(typeof null);
// prints object
```
Zatem `typeof` to niezawodny sposób wykrycia `undefined`, ale już nie `null`. Aby sprawdzić `null`, porównaj z nią bezpośrednio: `value === null`.

---

Jak `null` i `undefined` porównują się ze sobą? To zależy od operatora.
**Luźne** porównanie `==` traktuje je jako to samo i uznaje je za różne od każdej innej wartości, w tym `0`, `""` i `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
**Ścisłe** porównanie `===` porównuje także typ, a `null` i `undefined` mają różne typy:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

W większości przypadków nie obchodzi Cię, *który* z dwóch znaczników "braku wartości" otrzymałeś: chcesz po prostu wiedzieć, czy wartość w ogóle jest.
Ponieważ `null == undefined` daje `true` i nic innego nie jest luźno równe `null`, porównanie `value == null` to standardowy idiom łapiący **oba** przypadki naraz:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
To jedyny przypadek, w którym `==` jest preferowane nad `===`: zapis `value === null || value === undefined` robi dokładnie to samo, tylko dłużej.
Wartości takie jak `0`, `""` i `false` to *nie* `null`: to prawdziwe wartości, które po prostu są falsy.

---

Odczytanie właściwości z `null` lub `undefined` to błąd, który zatrzymuje program:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` to `undefined`, a `undefined` nie ma żadnych właściwości. Operator **opcjonalnego łańcuchowania** `?.` rozwiązuje ten problem: jeśli wartość po jego lewej stronie to `null` lub `undefined`, całe wyrażenie się zatrzymuje i przyjmuje wartość `undefined` zamiast zgłaszać błąd:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Gdy lewa strona jednak ma wartość, `?.` zachowuje się dokładnie jak zwykła kropka `.`. Można łączyć ich kilka: `user.address?.street?.name` zwraca `undefined`, gdy tylko jakiekolwiek ogniwo jest brakujące.

---

Opcjonalne łańcuchowanie nie ogranicza się do właściwości po kropce. Istnieją jeszcze dwie formy.
`?.[]` odczytuje element lub obliczony klucz tylko wtedy, gdy lewa strona ma wartość:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` wywołuje funkcję tylko wtedy, gdy ona istnieje, co jest wygodne dla opcjonalnych callbacków:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
W każdej formie sprawdzenie dotyczy wartości **tuż przed** `?.`: `post?.tags?.[0]` jest bezpieczne nawet wtedy, gdy samo `post` to `null` lub `undefined`.

---

Gdy już wiesz, że wartość może być brakująca, zwykle chcesz w jej miejscu mieć wartość **domyślną**. Robią to dwa operatory, a różnią się tym, co uznają za "brakujące".
`a || b` zwraca `b` zawsze, gdy `a` jest **falsy**: nie tylko `null` i `undefined`, ale też `0`, `""`, `false` i `NaN`.
Operator **nullish coalescing** `a ?? b` zwraca `b` tylko wtedy, gdy `a` to `null` lub `undefined`, a każdą inną wartość zachowuje:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Używaj `??`, gdy `0`, `""` lub `false` to pełnoprawne wartości, które trzeba zachować, a `||`, gdy naprawdę chcesz zamienić każdą wartość falsy.

---

Bardzo częsty wzorzec to "wypełnij tę właściwość tylko wtedy, gdy nie jest jeszcze ustawiona". Zapisany z `??` powtarza nazwę:
```javascript
options.timeout = options.timeout ?? 1000;
```
Operator **przypisania nullish** `??=` robi to samo w jednym kroku: przypisuje prawą stronę tylko wtedy, gdy lewa strona ma obecnie wartość `null` lub `undefined`, a każdą inną wartość zostawia nietkniętą:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` pozostaje `0`, ponieważ `0` nie jest nullish; `timeout` nie istniał, więc otrzymuje `1000`. Ta sama idea istnieje dla `||` jako `||=`, które nadpisuje każdą wartość falsy.

---

**Parametr domyślny** nadaje parametrowi wartość, gdy wywołujący jej nie podaje. Zasada jest precyzyjna: wartość domyślna jest używana tylko wtedy, gdy argument to `undefined`, co obejmuje jego pominięcie. Przekazanie `null` **nie** uruchamia wartości domyślnej, ponieważ `null` to wartość:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Parametry domyślne stosują regułę `undefined`, podczas gdy `??` obejmuje i `null`, i `undefined`: wybierz to, które pasuje do sposobu wywoływania Twojej funkcji.

---

Opcjonalne łańcuchowanie i zabezpieczenie `== null` dobrze ze sobą współpracują: łańcuch odczytuje zagnieżdżoną wartość bez zgłaszania błędu, a zabezpieczenie decyduje, co zrobić, gdy wynik jest brakujący:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
W ostatnim `return` zwykła kropka `.` jest bezpieczna, ponieważ zabezpieczenie już udowodniło, że każde ogniwo istnieje.

---

Wiele wbudowanych metod zgłasza "niczego nie znaleziono", zwracając `undefined`. Metoda tablic `find(callback)` to typowy przykład: zwraca pierwszy element, dla którego callback daje `true`, albo `undefined`, gdy żaden element nie pasuje:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Odczytanie tutaj `found.price` zgłosiłoby błąd, więc `?.` i `??` to naturalni towarzysze `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` i `undefined` zachowują się różnie, gdy obiekt jest konwertowany do JSON za pomocą `JSON.stringify()`.
JSON ma wartość `null`, ale nie ma `undefined`, więc właściwość o wartości `undefined` jest po prostu **pomijana**, a właściwość `null` jest zachowywana:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Wewnątrz tablic pozycje nie mogą zniknąć, więc tam `undefined` staje się `null`:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Sprawdzenie `obj.key === undefined` nie potrafi odróżnić dwóch sytuacji: właściwość nie istnieje albo istnieje i przechowuje wartość `undefined`.
`Object.hasOwn(obj, key)` odpowiada tylko na pierwsze pytanie: zwraca `true`, gdy obiekt ma **własną** właściwość o nazwie `key`, niezależnie od jej wartości:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"Własna" oznacza zadeklarowaną na samym obiekcie: dziedziczone składowe, takie jak `toString`, są dostępne na każdym obiekcie, ale `Object.hasOwn(config, "toString")` daje `false`.
