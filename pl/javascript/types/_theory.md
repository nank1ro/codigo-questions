Każda wartość w JavaScript ma **typ**. Istnieje siedem **prymitywnych** typów:
- `number` dla dowolnej liczby, na przykład `42` czy `3.14`
- `string` dla tekstu, na przykład `"Ana"`
- `boolean` dla `true` i `false`
- `undefined` dla wartości, która nigdy nie została podana
- `null` dla celowo pustej wartości
- `bigint` dla liczb całkowitych dowolnej wielkości, na przykład `9007199254740993n`
- `symbol` dla unikalnych identyfikatorów tworzonych za pomocą `Symbol()`

Wszystko inne (tablice, funkcje, obiekty tworzone za pomocą `{}`, daty...) jest `object`.
Operator `typeof` podaje typ wartości w postaci ciągu znaków:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript jest **dynamicznie typowany**: zmienna nie ma własnego typu, tylko wartość, którą aktualnie przechowuje, go ma. Ta sama zmienna może teraz przechowywać liczbę, a później ciąg znaków, a `typeof` podąża za wartością:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
To wygodne, ale oznacza też, że funkcja może otrzymać wartość nieoczekiwanego typu, więc sprawdzenie za pomocą `typeof` to częsty pierwszy krok. Ponieważ `typeof` zwraca ciąg znaków, porównujesz jego wynik z ciągiem znaków:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` ma kilka odpowiedzi, które potrafią zaskoczyć.
Funkcje otrzymują własną odpowiedź, `"function"`, mimo że są obiektami:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Tablice **nie** otrzymują własnej odpowiedzi: są zwykłym `"object"`, tak samo jak `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
A `typeof null` to `"object"`, historyczny błąd, którego nigdy nie naprawiono. `typeof` dobrze rozróżnia więc typy prymitywne i funkcje, ale nie potrafi odróżnić tablicy, obiektu i `null`.

---

Wartość można przekonwertować na inny typ **jawnie**, wywołując typ jak funkcję:
- `Number(value)` konwertuje na liczbę: `Number("42")` to `42`
- `String(value)` konwertuje na ciąg znaków: `String(42)` to `"42"`
- `Boolean(value)` konwertuje na wartość logiczną: `Boolean("")` to `false`

Wynikiem jest zupełnie nowa wartość; oryginał nie ulega zmianie:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Jawna konwersja uwidacznia twoje intencje: każdy, kto czyta `Number(input)`, wie, że `input` był tekstem.

---

`Number()` jest rygorystyczna: cały ciąg znaków musi być liczbą, w przeciwnym razie wynikiem jest `NaN` ("Not a Number"):
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` i `parseFloat()` są łagodniejsze: czytają cyfry od początku ciągu znaków, pomijają wiodące spacje i zatrzymują się na pierwszym znaku, który nie jest częścią liczby. `parseInt` zachowuje tylko część całkowitą:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
Gdy ciąg znaków nie zaczyna się od czegoś, co może rozpocząć liczbę (opcjonalny znak, a potem cyfra), one również zwracają `NaN`:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` to jedyna wartość, która nie jest równa samej sobie, więc `x === NaN` jest zawsze `false`; aby ją wykryć, użyj `Number.isNaN(x)`.

---

Są dwa sposoby, aby zapytać „czy to `NaN`?", i odpowiadają na różne pytania.
Stara globalna funkcja `isNaN(value)` najpierw **konwertuje** `value` na liczbę, a potem sprawdza. Mówi więc `true` dla wszystkiego, co nie może stać się liczbą, nawet jeśli wcale nie jest `NaN`:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` **nie** konwertuje: jest `true` tylko wtedy, gdy `value` naprawdę jest liczbą `NaN`:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Preferuj `Number.isNaN`, a jeśli chcesz wiedzieć, czy konwersja się nie powiodła, najpierw konwertuj.

---

JavaScript konwertuje też **niejawnie**, a operator `+` to miejsce, gdzie daje o sobie znać najczęściej. Jeśli któraś strona jest ciągiem znaków, `+` **skleja** wartości, a druga strona jest konwertowana na ciąg znaków:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Każdy inny operator arytmetyczny konwertuje obie strony na **liczby**:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
Dodawanie więc wartości pochodzących z tekstu (wejście użytkownika, pliki, adresy URL) może po cichu zbudować ciąg znaków zamiast sumy. Dla bezpieczeństwa konwertuj za pomocą `Number()` przed dodawaniem.

---

Krótkim sposobem na przekonwertowanie ciągu znaków na liczbę jest **plus jednoargumentowy**: `+` postawiony przed pojedynczą wartością konwertuje ją dokładnie tak, jak robi to `Number()`:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
Jest zwięzły, ale łatwo go pomylić z dodawaniem, więc wiele zespołów woli jawne `Number("5")`.

---

**Luźne** porównanie `==` konwertuje obie strony do wspólnego typu przed porównaniem, według trudnych do zapamiętania reguł:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
**Ścisłe** porównanie `===` nigdy nie konwertuje: wartości różnych typów po prostu nie są równe:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Domyślnie używaj `===` (i `!==`). Jedynym częstym wyjątkiem jest `value == null`, które sprawdza jednocześnie `null` i `undefined`.

---

Gdy JavaScript potrzebuje wartości logicznej, na przykład w warunku `if` albo w `Boolean(value)`, konwertuje wartość. Tylko osiem wartości staje się `false`; nazywa się je **falsy**:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` oraz `NaN`.
**Wszystko inne jest truthy**, w tym niektóre wartości, które wyglądają na puste:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` to niepusty ciąg znaków, więc jest truthy; pusta tablica jest obiektem, więc też jest truthy.

---

Popularnym skrótem do przekonwertowania dowolnej wartości na wartość logiczną jest **podwójna negacja** `!!`: pierwszy `!` konwertuje na wartość logiczną i ją odwraca, a drugi odwraca z powrotem:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` i `Boolean(value)` dają dokładnie ten sam wynik; jawna postać jest łatwiejsza do odczytania.

---

JavaScript ma jeden typ `number` dla liczb całkowitych i dziesiętnych: każda liczba jest 64-bitową wartością zmiennoprzecinkową (*double*). Dlatego `5` i `5.0` to ta sama wartość, a osobnego typu całkowitoliczbowego nie ma:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
Aby zapytać, czy liczba nie ma części ułamkowej, użyj `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Literały szablonowe konwertują interpolowaną wartość na ciąg znaków według tych samych reguł co `String()`, więc `${5.0}` staje się `"5"`, a nie `"5.0"`.

---

Ponieważ liczby to typy double, niektóre ułamki dziesiętne nie mogą być przechowywane dokładnie i pojawiają się drobne błędy:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
Metoda `toFixed(digits)` zaokrągla liczbę do `digits` miejsc po przecinku, ale zwraca **ciąg znaków**, co jest w porządku do wyświetlania i złe do dalszych obliczeń:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
Aby otrzymać zaokrągloną **liczbę**, przekonwertuj wynik z powrotem za pomocą `Number()`:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

Typ `number` może reprezentować liczby całkowite dokładnie tylko do `Number.MAX_SAFE_INTEGER`, czyli `9007199254740991`. Powyżej tej granicy cyfry się gubią:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
Dla większych liczb całkowitych użyj `bigint`: zapisz literał z przyrostkiem `n` albo przekonwertuj za pomocą `BigInt()`:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` pokazuje przyrostek `n`; `String(big)` daje same cyfry.
Typów `bigint` i `number` nie można mieszać w obliczeniach arytmetycznych: `big + 1` zgłasza `TypeError`. Przekonwertuj jedną stronę jawnie, za pomocą `BigInt(count)` albo `Number(big)`.

---

Ponieważ `typeof` odpowiada `"object"` dla tablic, obiektów i `null`, rozróżnienie ich wymaga dwóch dodatkowych sprawdzeń.
`Array.isArray(value)` jest `true` tylko dla tablic:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
Dla `null` porównaj bezpośrednio, `value === null`. Połączenie tego daje pełny obraz dowolnej wartości:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Najpierw sprawdź `null` i tablice, ponieważ zwykły `typeof` nie potrafi ich rozróżnić.

---

Tekst pochodzący z formularzy, plików czy adresów URL jest zawsze ciągiem znaków, nawet gdy reprezentuje liczbę lub wartość logiczną. Przekształcenie go z powrotem w odpowiedni typ łączy to, co już widziałeś: porównaj z `"true"` i `"false"` dla wartości logicznych, a dla liczb wypróbuj `Number()`, pamiętając, że `Number("")` to `0` i że `Number.isNaN` mówi ci, kiedy konwersja się nie powiodła:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
Gdy nic nie pasuje, zostaw ciąg znaków taki, jaki jest.
