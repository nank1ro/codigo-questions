**Komentarz** to notatka zapisana w kodzie źródłowym dla osób, które go czytają. Kompilator całkowicie ignoruje komentarze, więc nigdy nie zmieniają one tego, co robi program.

Najprostszy komentarz to **komentarz jednoliniowy**: zaczyna się od `//` i trwa do końca linii.
```kotlin
// Greets the user
println("Hello")
```
Używaj komentarzy, aby wyjaśnić, do czego służy fragment kodu albo dlaczego został napisany w taki sposób.

---

Komentarz nie musi mieć własnej linii: może następować po kodzie w tej samej linii. To **komentarz końcowy**, dobre miejsce na krótką notatkę o tej konkretnej instrukcji:
```kotlin
val retries = 3 // give up after three attempts
```
Wszystko od `//` do końca linii jest ignorowane, a kod przed nim wykonuje się normalnie.

---

Ponieważ kompilator całkowicie usuwa komentarze, dodanie lub usunięcie komentarza nigdy nie zmienia działania programu. Wykonuje się tylko kod, który **nie** jest zakomentowany.

Dzięki temu `//` to szybki sposób na wyłączenie linii kodu bez jej usuwania. Nazywa się to **zakomentowaniem** kodu:
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
Druga linia jest teraz komentarzem, więc `total` pozostaje `10`. Usunięcie `//` przywraca ją do życia.

Zakomentowywanie kodu jest wygodne podczas eksperymentów, ale pamiętaj o sprzątaniu: kod, który długo pozostaje zakomentowany, tylko dezorientuje następną osobę, która go przeczyta.

---

Gdy komentarz potrzebuje więcej niż jednej linii, Kotlin oferuje **komentarz wieloliniowy** (nazywany też komentarzem blokowym): zaczyna się od `/*` i kończy na `*/`, a wszystko pomiędzy jest ignorowane, łącznie ze znakami nowej linii.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Komentarz blokowy może też być krótki i zmieścić się w jednej linii: `/* like this */`.

---

W przeciwieństwie do `//`, który kończy się na końcu linii, komentarz `/*` kończy się dopiero przy `*/`. Jeśli zapomnisz go zamknąć, kompilator potraktuje cały dalszy kod jako część komentarza i zgłosi błąd:
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
Zarówno `//`, jak i `/* */` działają jako komentarze końcowe, ale przy `/*` zawsze upewnij się, że `*/` jest na miejscu.

---

W Javie komentarz blokowy nie może zawierać innego komentarza blokowego, ale w Kotlinie **można je zagnieżdżać**: każdy `/*` musi mieć własny `*/`, a komentarz kończy się dopiero wtedy, gdy zamknięty zostanie ten najbardziej zewnętrzny.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Tutaj `still a comment */` jest częścią zewnętrznego komentarza, więc wypisane zostaje tylko `done`. To właśnie pozwala zakomentować cały blok kodu, nawet jeśli ten blok zawiera już komentarz `/* */`.

---

Aby zakomentować kilka linii naraz, otocz je jednym komentarzem blokowym zamiast dodawać `//` do każdej linii:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
Dzięki zagnieżdżaniu działa to nawet wtedy, gdy jedna z tych linii zawiera już komentarz `/* */`.

---

Częstym zastosowaniem komentarzy blokowych jest **komentarz nagłówkowy**: krótki blok umieszczony bezpośrednio nad funkcją, który mówi, co ona robi i co oznaczają jej parametry.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Kto wywołuje `toSeconds`, może teraz przeczytać nagłówek zamiast ciała funkcji. Trzymaj nagłówek obok funkcji, aby były aktualizowane razem.

---

Kotlin ma trzeci rodzaj komentarza, **komentarz dokumentacyjny**, zapisywany w formacie o nazwie **KDoc**: zaczyna się od `/**` (ukośnik i dwie gwiazdki), kończy na `*/` i jest umieszczany bezpośrednio nad funkcją, klasą lub właściwością.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Dla kompilatora to tylko komentarz, ale narzędzia takie jak IntelliJ IDEA czytają go i pokazują jako tekst pomocy dla `greet`. `*` na początku wewnętrznych linii to jedynie konwencja utrzymująca wyrównanie bloku. W KDoc możesz używać Markdown, a nawiasy kwadratowe takie jak `[name]` zamieniają się w odnośniki do tego parametru.

---

Pierwsza linia komentarza dokumentacyjnego to **podsumowanie**: krótkie zdanie mówiące, co robi funkcja. Pisz je w trzeciej osobie, jakbyś opisywał funkcję: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
Komentarz musi znajdować się bezpośrednio nad deklaracją, bez żadnej innej instrukcji pomiędzy, w przeciwnym razie narzędzia nie powiążą go z funkcją.

---

Po podsumowaniu komentarz dokumentacyjny może opisać parametry i zwracaną wartość za pomocą **znaczników KDoc**, które zawsze zaczynają się od `@`:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Po `@param` podaje się nazwę parametru, a następnie jego opis; jest jeden `@param` na każdy parametr. `@return` opisuje wartość zwracaną przez funkcję. Kolejność jest zawsze taka sama: najpierw podsumowanie, potem znaczniki `@param`, potem `@return`.

---

Funkcja z więcej niż jednym parametrem dostaje jeden znacznik `@param` dla każdego z nich, zapisany w tej samej kolejności co parametry:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Znacznik wciąż jest tylko komentarzem: jeśli zmienisz nazwę parametru i zapomnisz o znaczniku, nic się nie zepsuje, ale dokumentacja zacznie kłamać. Aktualizuj KDoc razem z sygnaturą.

---

Kompilator szuka komentarzy tylko w kodzie, nigdy wewnątrz **literału tekstowego**. Między podwójnymi cudzysłowami `//` i `/* */` to zwykłe znaki:
```kotlin
println("50 // 2") // prints 50 // 2
```
Pierwszy `//` jest częścią tekstu, drugi rozpoczyna prawdziwy komentarz. Najczęściej zaskakuje to przy adresach internetowych, które zawierają `//` zaraz po protokole.

---

Niektóre komentarze podlegają konwencji, którą rozumieją edytory. Najczęstsze **znaczniki** to:
- `// TODO: ...` oznacza coś, co dopiero trzeba napisać
- `// FIXME: ...` oznacza kod, o którym wiadomo, że jest błędny i musi zostać poprawiony

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
Dla kompilatora to zwykłe komentarze; IntelliJ IDEA zbiera je w dedykowanym oknie narzędziowym, dzięki czemu łatwo znaleźć zaległą pracę. `TODO` zwykle znajduje się obok zaślepki, która utrzymuje kod kompilowalnym do czasu napisania prawdziwej implementacji. Gdy kończysz pracę, zamień zaślepkę i usuń znacznik w tej samej zmianie, aby komentarz nigdy nie kłamał o stanie kodu.

---

`FIXME` różni się od `TODO`: kod już istnieje, ale wiadomo, że jest błędny. Dobry `FIXME` mówi, na czym polega błąd i, jeśli to możliwe, podaje przykład, który go pokazuje, aby następna osoba mogła go szybko naprawić. Podobnie jak przy `TODO`, usuń znacznik po naprawieniu błędu, ale zostaw komentarz dokumentacyjny, który nadal jest prawdziwy.

---

Dobry komentarz wyjaśnia, **dlaczego** kod coś robi, a nie **co** robi. Kod już pokazuje, co się dzieje; powtarzanie tego słowami dodaje szumu i dezaktualizuje się, gdy tylko kod się zmieni:
```kotlin
// set timeout to 30
val timeout = 30
```
Powodu stojącego za tą liczbą czytelnik nie jest w stanie odgadnąć:
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
Jeśli komentarz jedynie powtarza linię poniżej, usuń go albo zastąp powodem. Najlepsze komentarze to te, które mówią coś, czego kod powiedzieć nie może.
