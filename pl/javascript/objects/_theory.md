**Obiekty** są podobne do tablic, ale dostęp do wartości uzyskuje się poprzez wyszukiwanie *klucza* zamiast indeksu.
Klucz może być dowolnym ciągiem znaków lub liczbą.
Obiekty są otoczone nawiasami klamrowymi, jak poniżej:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
Jest to słownik o nazwie `objectName` z trzema *parami klucz-wartość*.
Klucz `key1` wskazuje na wartość `1`, `key2` na `2` i tak dalej.

---

Dostęp do wartości słownika za pomocą klucza jest podobny do dostępu do wartości tablicy za pomocą indeksu:
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Podobnie jak tablice, słowniki są _mutowalne_.
Oznacza to, że można je zmieniać po ich utworzeniu (o ile nie są zadeklarowane jako stałe).
Jedną z zalet jest to, że możemy dodawać nowe _pary klucz/wartość_ do słownika po jego utworzeniu w następujący sposób:
```javascript
dictName[newKeyName] = newValue;
```

---

Ponieważ zmienne słownikowe są mutowalne, można je zmieniać na wiele sposobów.
Elementy można usuwać ze słownika za pomocą słowa kluczowego 'delete':
```javascript
delete dictName[keyName];
```
usunie klucz `keyName` i powiązaną z nim wartość ze słownika.

---

Co zrobić, jeśli chcemy wylistować wszystkie klucze słownika?
Do tego służy metoda `Object.keys()`.

---

Co zrobić, jeśli chcemy wylistować wszystkie wartości słownika?
Do tego służy metoda `Object.values()`.

---

Podobnie jak w przypadku tablic, możemy iterować po elementach słownika za pomocą metody `Object.entries()`.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
