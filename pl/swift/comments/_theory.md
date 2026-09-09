**Komentarz** to notatka zapisana w kodzie źródłowym dla osób, które go czytają. Kompilator całkowicie ignoruje komentarze, więc nigdy nie zmieniają one działania programu.

Najprostszym komentarzem jest **komentarz jednoliniowy**: zaczyna się od `//` i trwa do końca linii.
```swift
// Greets the user
print("Hello")
```
Używaj komentarzy, aby wyjaśnić, do czego służy dany fragment kodu albo dlaczego został napisany w ten sposób.

---

Komentarz nie musi zajmować własnej linii: może następować po kodzie w tej samej linii. Jest to **komentarz końcowy** i dobre miejsce na krótką notatkę o tej konkretnej instrukcji:
```swift
let retries = 3 // give up after three attempts
```
Wszystko od `//` do końca linii jest ignorowane, a kod przed nim działa jak zwykle.

---

Ponieważ kompilator całkowicie usuwa komentarze, dodanie lub usunięcie komentarza nigdy nie zmienia działania programu. Wykonywany jest tylko kod, który **nie** jest zakomentowany.

Dzięki temu `//` jest szybkim sposobem na wyłączenie linii kodu bez jej usuwania. Nazywa się to **zakomentowaniem**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
Druga linia jest teraz komentarzem, więc `total` pozostaje `10`. Usunięcie `//` przywraca linii życie.

Zakomentowywanie przydaje się podczas eksperymentowania, ale pamiętaj o sprzątaniu: kod, który pozostaje zakomentowany przez długi czas, tylko dezorientuje tego, kto będzie go następnie czytał.

---

Gdy komentarz musi zająć więcej niż jedną linię, Swift oferuje **komentarz wieloliniowy** (nazywany także komentarzem blokowym): zaczyna się od `/*` i kończy na `*/`, a wszystko pomiędzy jest ignorowane, łącznie ze zmianami linii.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Komentarz blokowy może być też krótki i zmieścić się w jednej linii: `/* like this */`.

---

W przeciwieństwie do `//`, które kończy się na końcu linii, komentarz `/*` kończy się dopiero na `*/`. Jeśli zapomnisz go zamknąć, kompilator traktuje cały kolejny kod jako część komentarza i zgłasza błąd:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Zarówno `//`, jak i `/* */` działają jako komentarze końcowe, ale w przypadku `/*` zawsze upewnij się, że `*/` jest na miejscu.

---

W wielu językach komentarze blokowe nie mogą zawierać innych komentarzy blokowych, ale w Swift **mogą być zagnieżdżane**: każde `/*` musi mieć swoje własne `*/`, a komentarz kończy się dopiero wtedy, gdy zamknięty zostanie najbardziej zewnętrzny.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Tutaj `still a comment */` jest częścią zewnętrznego komentarza, więc wypisywane jest tylko `done`. To właśnie pozwala zakomentować cały blok kodu, nawet gdy ten blok zawiera już komentarz `/* */`.

---

Aby zakomentować kilka linii naraz, otocz je jednym komentarzem blokowym zamiast dodawać `//` do każdej linii:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Dzięki zagnieżdżaniu działa to nawet wtedy, gdy jedna z tych linii zawiera już komentarz `/* */`.

---

Częstym zastosowaniem komentarzy blokowych jest **komentarz nagłówkowy**: krótki blok umieszczony bezpośrednio nad funkcją, który mówi, co ona robi i co oznaczają jej parametry.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Każdy, kto wywołuje `toSeconds`, może teraz przeczytać nagłówek zamiast ciała funkcji. Trzymaj nagłówek obok funkcji, aby aktualizować je razem.

---

Swift ma trzeci rodzaj komentarza, **komentarz dokumentacyjny**: jednoliniowy komentarz zaczynający się od `///` (trzech ukośników), umieszczany bezpośrednio nad funkcją, typem lub właściwością.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Dla kompilatora to zwykły komentarz, ale narzędzia takie jak Xcode czytają go i pokazują jako tekst pomocy dla `greet`. Komentarze dokumentacyjne obsługują **Markdown**, więc można używać backticków dla kodu, `**pogrubienia**` oraz list.

---

Pierwsza linia komentarza dokumentacyjnego to **streszczenie**: krótkie zdanie mówiące, co robi funkcja. Napisz je w trzeciej osobie, jakbyś opisywał funkcję: "Zwraca...", "Dodaje...", "Sprawdza...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
Komentarz musi znajdować się bezpośrednio nad deklaracją, bez pustej linii pomiędzy, w przeciwnym razie Xcode nie przypisze go do funkcji.

---

Komentarze dokumentacyjne występują także w formie blokowej: `/**` otwiera komentarz, a `*/` zamyka go — dokładnie jak komentarz wieloliniowy, ale z drugą gwiazdką na początku.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` i `/** text */` oznaczają dla narzędzi to samo; `///` to najczęstszy wybór w kodzie Swift, podczas gdy `/** */` sprawdza się przy długich opisach. Zwykły komentarz `/* */` lub `//` **nie** jest dokumentacją, nawet gdy znajduje się nad funkcją.

---

Po streszczeniu komentarz dokumentacyjny może opisać parametry i wartość zwracaną za pomocą specjalnych elementów listy Markdown, które rozpoznaje Xcode:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Kolejność jest zawsze taka sama: najpierw streszczenie, potem `- Parameter name:` dla każdego parametru, a na końcu `- Returns:`.

---

Niektóre komentarze stosują konwencję, którą rozumieją edytory. W Swift najczęstsze **znaczniki** to:
- `// MARK: - Title` oznacza sekcję pliku, dzięki czemu pojawia się w menu nawigacji Xcode
- `// TODO: ...` wskazuje coś, co jeszcze trzeba napisać
- `// FIXME: ...` wskazuje kod, o którym wiadomo, że jest błędny i musi zostać poprawiony

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Dla kompilatora są to zwykłe komentarze; Xcode wypisuje je na liście, dzięki czemu łatwo znaleźć zaległą pracę. Gdy praca jest gotowa, usuń znacznik: nieaktualny `TODO` wprowadza w błąd.

---

`TODO` zwykle znajduje się obok elementu zastępczego, który pozwala kodowi się kompilować, dopóki nie zostanie napisana właściwa implementacja. Gdy ukończysz pracę, zastąp element zastępczy i usuń znacznik w tej samej zmianie, aby komentarz nigdy nie kłamał o stanie kodu.

---

`FIXME` różni się od `TODO`: kod już istnieje, ale wiadomo, że jest błędny. Dobry `FIXME` mówi, na czym polega błąd i, gdy to możliwe, podaje przykład, który go pokazuje, aby kolejna osoba mogła szybko go naprawić. Podobnie jak w przypadku `TODO`, usuń znacznik po naprawieniu błędu, ale zachowaj komentarz dokumentacyjny, który nadal jest prawdziwy.

---

Dobry komentarz wyjaśnia **dlaczego** kod coś robi, a nie **co** robi. Kod już pokazuje, co się dzieje; powtarzanie tego słowami dodaje szumu i starzeje się, gdy tylko kod się zmieni:
```swift
// set timeout to 30
let timeout = 30
```
Tego, czego czytelnik nie może odgadnąć, jest uzasadnienie tej liczby:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Jeśli komentarz tylko powtarza linię znajdującą się pod nim, usuń go albo zastąp wyjaśnieniem przyczyny.
