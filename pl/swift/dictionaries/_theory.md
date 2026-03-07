**Słowniki** są podobne do tablic i krotek, ale dostęp do wartości uzyskuje się poprzez wyszukanie *klucza* zamiast indeksu.
Klucz może być dowolnym ciągiem znaków lub liczbą.
Słowniki są ujęte w nawiasy kwadratowe, na przykład:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
Jest to słownik o nazwie `dictionaryName` z trzema *parami klucz-wartość*.
Klucz `key1` wskazuje na wartość `1`, `key2` na `2` i tak dalej.

---

Dostęp do wartości słownika za pomocą klucza jest podobny do dostępu do wartości tablicy za pomocą indeksu:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Podobnie jak tablice, słowniki są _mutowalne_.
Oznacza to, że można je zmieniać po utworzeniu (jeśli nie zostały zadeklarowane jako stałe).
Jedną z zalet tego jest to, że możemy dodawać nowe _pary klucz/wartość_ do słownika po jego utworzeniu w następujący sposób:
```swift
dictName[newKeyName] = newValue
```

---

Długość `count` słownika to liczba _par klucz-wartość_, które posiada.
Każda para liczy się tylko raz, nawet jeśli wartość jest tablicą. (Tak, możesz też umieszczać tablice wewnątrz słowników!)

---

Ponieważ słowniki są mutowalne, można je zmieniać na wiele sposobów. Elementy można usuwać ze słownika za pomocą metody `removeValue(forKey:)`:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
usunie klucz `keyName` i jego powiązaną wartość ze słownika.

---

Co zrobić, jeśli chcemy wyświetlić listę wszystkich kluczy słownika?
Do tego służy właściwość `keys`.

---

Co zrobić, jeśli chcemy wyświetlić listę wszystkich wartości słownika?
Do tego służy właściwość `values`.

---

Podobnie jak w przypadku tablic, możemy iterować po elementach słownika za pomocą słów kluczowych `for..in`.
Aby uzyskać zarówno klucz, jak i wartość w pętli, nie musimy podawać żadnej właściwości:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

Możemy również użyć właściwości `isEmpty`, której używaliśmy w tablicach, aby sprawdzić, czy słownik jest pusty

---

Aby __dodać__ lub __zmienić__ wartości w słowniku, można również użyć metody `updateValue(_:forKey:)`

---

Wcześniej widzieliśmy, jak usunąć _parę klucz-wartość_ ze słownika za pomocą metody `removeValue()`.
Możemy też usunąć element, przypisując kluczowi wartość `nil`
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
