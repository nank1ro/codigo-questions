Często w programowaniu musimy powtarzać blok kodu, na przykład:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
Daje to następujący wynik:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Oczywiście, przy długich instrukcjach spędzilibyśmy dużo czasu na pisaniu kodu, ale na szczęście możemy używać pętli.
Poznajmy pętlę `while`, uzyskując ten sam wynik co powyżej.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Stworzyliśmy zmienną `count` przypisując jej `2`, wartość początkową.
Następnie użyliśmy instrukcji `while`, która będzie uruchamiać blok kodu, dopóki warunek `count <= 5` jest `true`.
Wewnątrz bloku kodu **NIE** możemy zapomnieć o dodaniu linii `count += 1`.
Zwiększa ona wartość `count`, w przeciwnym razie nasza pętla będzie nieskończona

---

Aby kontrolować, ile razy pętla `while` się powtarza, zaczynamy od zmiennej ustawionej na liczbę.
Tę zmienną nazywamy zmienną licznikową

---

Następnie używamy porównania w warunku, aby porównać zmienną `counter` z liczbą.

---

Wewnątrz bloku kodu, aby zatrzymać pętlę `while`, zwiększamy zmienną `counter`.

---

Kolejność pisania kodu wpływa na wynik.

---

W JavaScript mamy również wariant **do-while** pętli `while`.
Wykonuje on najpierw pojedyncze przejście przez blok pętli, _przed_ sprawdzeniem warunku pętli.
Następnie kontynuuje powtarzanie pętli, dopóki warunek jest `false`.
