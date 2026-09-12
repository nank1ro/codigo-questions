Niektóre operacje nie kończą się od razu: pobieranie pliku, odczyt z bazy danych, oczekiwanie na timer. JavaScript nie zamraża się, gdy one trwają. Zamiast tego daje ci **`Promise`**: obiekt, który reprezentuje wartość dostępną **później**.

Funkcja oznaczona **`async`** zawsze zwraca obietnicę. Cokolwiek funkcja zwróci, staje się wartością wewnątrz tej obietnicy:
```javascript
async function fetchNumber() {
  return 42;
}
```
Aby wydobyć wartość z obietnicy, używasz **`await`**. Wstrzymuje on funkcję, dopóki obietnica nie będzie miała swojej wartości, a potem daje ci zwykłą wartość. `await` jest dozwolony tylko wewnątrz funkcji `async`:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Bez `await` `n` byłoby samą obietnicą, a `console.log(n)` wypisałoby `Promise { 42 }` zamiast liczby.

---

Dodanie `async` przed funkcją zmienia to, co ona oddaje: ciało nadal liczy zwykłą wartość, ale wywołujący otrzymuje obietnicę opakowującą tę wartość.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
Obie funkcje zawierają ten sam kod; różni się tylko sposób odczytania wyniku. `shoutLater("hi")` musi być wywołane z `await` wewnątrz innej funkcji `async`, aby oddać `"HI"`.

Oznaczenie funkcji jako `async` nic nie kosztuje, gdy nie ma czego czekać, a to właśnie ono pozwala później używać w niej `await`.

---

Gdy wartość naprawdę przychodzi później, obietnicę budujesz sam za pomocą **`new Promise`**. Przyjmuje on jedną funkcję, która otrzymuje callback **`resolve`**: wywołaj `resolve(value)`, gdy wartość jest gotowa, a obietnica zostanie spełniona z tą wartością.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` planuje wykonanie `callback` po `ms` milisekundach i zwraca od razu, więc nic nie jest blokowane w międzyczasie.

Funkcja przekazana do `new Promise` uruchamia się od razu, ale obietnica pozostaje **oczekująca**, dopóki nie zostanie wywołane `resolve`. Zrobienie `await` na niej daje wartość:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Obietnica zawsze znajduje się w jednym z trzech stanów:

- **oczekująca**: praca wciąż trwa;
- **spełniona**: praca się powiodła i obietnica przechowuje wartość;
- **odrzucona**: praca zawiodła i obietnica przechowuje błąd.

Obietnica zaczyna jako oczekująca i zmienia stan co najwyżej raz. Gdy jest spełniona lub odrzucona, jest **rozstrzygnięta** i nigdy już się nie zmienia.

Wywołanie funkcji `async` nigdy nie czeka: zaczyna pracę i natychmiast wręcza ci oczekującą obietnicę, więc linia po wywołaniu wykonuje się, zanim praca się skończy. Ta obietnica to zwykły obiekt, a nie wartość w niej ukryta, dlatego zapominanie o `await` jest tak częstym błędem.

---

`await` to nie jedyny sposób odczytania obietnicy. Każda obietnica ma metodę **`.then(callback)`**: callback otrzymuje wartość, gdy tylko obietnica zostanie spełniona.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** buduje obietnicę już spełnioną z `value`, co jest wygodne, gdy masz wartość pod ręką, ale musisz zwrócić obietnicę.

`.then` zwraca **nową** obietnicę spełnioną z tym, co zwróci callback, więc wywołania można **łączyć w łańcuch**, gdzie każdy krok pracuje na wyniku poprzedniego:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Funkcja `async` czyta się z góry na dół jak każda inna funkcja: `await` po prostu wstrzymuje ją, dopóki oczekiwana obietnica nie zostanie spełniona, a potem wykonanie biegnie dalej w następnej linii.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
Zwróć uwagę na ostatnią linię: funkcję `async` nadal trzeba **wywołać**. Napisanie `main` bez nawiasów definiuje pracę, ale nigdy jej nie rozpoczyna i nic nie zostaje wypisane.

---

Praca asynchroniczna też może się nie udać. Funkcja przekazana do `new Promise` otrzymuje drugi callback, **`reject`**: wywołaj `reject(error)`, a obietnica stanie się odrzucona zamiast spełnionej.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
Zawsze odrzucaj obiektem `Error`: niesie on `message` i ślad stosu, czego nie robi sam ciąg znaków.

Odrzucenie odczytuje się za pomocą **`.catch(callback)`**, lustrzanego odbicia `.then`. **`Promise.reject(error)`** buduje obietnicę już odrzuconą, tak jak `Promise.resolve` buduje spełnioną:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Wywołanie zarówno `resolve`, jak i `reject`, albo dwukrotne wywołanie, nic nie zmienia: liczy się tylko pierwsze wywołanie.

---

`.then`, `.catch` i `.finally` to ogniwa tego samego łańcucha. Odrzucenie pomija każde `.then`, aż trafi na `.catch`; gdy callback `.catch` zwróci wartość, łańcuch znów jest spełniony i biegnie normalnie.

**`.finally(callback)`** wykonuje się, gdy łańcuch się rozstrzygnie, niezależnie od tego, czy został spełniony, czy odrzucony. Jego callback nie przyjmuje argumentu, a jego wartość zwracana jest ignorowana, więc wartość dalej płynie do następnego `.then`. To miejsce na porządki, takie jak ukrycie spinnera:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

Wewnątrz funkcji `async` nie potrzebujesz `.catch`. Oczekiwanie na odrzuconą obietnicę za pomocą `await` **rzuca** błąd, więc zajmie się nim zwykła instrukcja `try` / `catch` / `finally`:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
Działa też w drugą stronę: `throw` wewnątrz funkcji `async` nie wywala wywołującego, tylko odrzuca obietnicę zwróconą przez funkcję.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
Jak w każdym bloku `try`, linie po nieudanym `await` są pomijane, blok `catch` się wykonuje, a blok `finally` wykonuje się w obu przypadkach.

---

Częstym użyciem `try` / `catch` wokół `await` jest zastąpienie niepowodzenia rozsądną wartością domyślną, tak aby wywołujący nigdy nie musiał zajmować się błędem:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Zachowaj `await` przed `measure(path)`, nawet jeśli wartość jest zwracana od razu. Bez niego obietnica opuszcza funkcję, nigdy nie przechodząc przez blok `try`, a odrzucenie wymknęłoby się `catch`.

---

Gdy potrzebnych jest kilka wyników, oczekiwanie na nie jedno po drugim marnuje czas: każde zaczyna się dopiero, gdy poprzednie się skończyło. **`Promise.all(promises)`** przyjmuje tablicę już działających obietnic i zwraca jedną obietnicę spełnioną z tablicą wszystkich ich wartości:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Warto zapamiętać dwie reguły:

- wartości wracają **w kolejności z tablicy**, a nie w kolejności, w jakiej się zakończyły;
- jeśli którakolwiek obietnica zostanie odrzucona, obietnica zwrócona przez `Promise.all` zostaje natychmiast odrzucona z tym pierwszym błędem, a pozostałe wartości przepadają.

---

`Promise.all` działa z tablicą dowolnej długości, także pustą: oczekiwanie na `Promise.all([])` za pomocą `await` od razu oddaje pustą tablicę. Dzięki temu można bezpiecznie przekazać listę budowaną w czasie działania, bez specjalnego przypadku dla „nie ma na co czekać”.
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
Zwracana tablica zawsze ma dokładnie tyle elementów, ile tablica otrzymana, na tych samych pozycjach, więc można po niej iterować jak po każdej innej tablicy.

---

Różnica między czekaniem **sekwencyjnym** a **równoległym** zależy od tego, *gdzie* postawisz `await`:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
W pierwszej wersji drugie pobieranie zaczyna się dopiero, gdy pierwsze się skończy, ponieważ `await` wstrzymuje funkcję w tej linii. W drugiej oba wywołania są wykonane, zanim cokolwiek będziemy oczekiwać, więc oba pobierania już działają, podczas gdy `Promise.all` czeka.

Używaj sekwencyjnych `await` tylko wtedy, gdy drugie zadanie naprawdę potrzebuje wyniku pierwszego. W przeciwnym razie uruchom najpierw wszystko, a oczekuj razem.

---

`Promise.all` poddaje się, gdy tylko jedna obietnica zostanie odrzucona. Gdy mimo wszystko chcesz dostać każdy wynik, użyj **`Promise.allSettled(promises)`**: nigdy nie jest odrzucana i jest spełniana jednym małym obiektem na obietnicę, w tej samej kolejności:

- `{ status: "fulfilled", value: ... }` dla tych, które się powiodły;
- `{ status: "rejected", reason: ... }` dla tych, które zawiodły.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
Czytaj `value` tylko wtedy, gdy `status` to `"fulfilled"`, a `reason` tylko wtedy, gdy to `"rejected"`: druga właściwość po prostu nie istnieje.

---

**`Promise.race(promises)`** rozstrzyga się, gdy tylko rozstrzygnie się **pierwsza** z obietnic, i kopiuje jej wynik: jest spełniona z pierwszą wartością albo odrzucona z pierwszym błędem. Pozostałe nie są anulowane, wciąż działają, ale cokolwiek wyprodukują, jest ignorowane.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
Typowym zastosowaniem jest limit czasu: uruchom wyścig prawdziwej pracy z obietnicą, która po chwili zawodzi, a dostaniesz albo wynik, albo błąd timeoutu.

Uważaj na pustą tablicę: `Promise.race([])` pozostaje oczekująca na zawsze, bo nie ma nic, co mogłoby ją rozstrzygnąć.

---

Połączenie ostatnich elementów daje małe narzędzie używane w prawie każdej prawdziwej aplikacji: limit czasu. Zbuduj obietnicę odrzucaną po `ms` milisekundach, uruchom z nią wyścig prawdziwej pracy, a to, co rozstrzygnie się pierwsze, decyduje o wyniku:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Zwracanie obietnicy z funkcji `async` jest w porządku: obietnica oddawana przez funkcję podąża za nią, więc wywołujący oczekuje finalnej wartości, a nie obietnicy obietnicy.
