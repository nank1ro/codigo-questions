**Lista wiązana** przechowuje wartości w osobnych **węzłach** rozproszonych po pamięci: każdy węzeł zawiera wartość i wskaźnik do następnego węzła, a ostatni z nich wskazuje na `NULL`. Wskaźnik wewnątrz odwołuje się do właśnie deklarowanego typu, więc struktura potrzebuje **tagu**, żeby nazywać samą siebie; nazwa z `typedef` nie istnieje jeszcze wewnątrz nawiasów klamrowych:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Węzły łączy się, zapisując adres jednego w polu `next` drugiego, a do pól wskazywanego węzła dochodzi się strzałką:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Węzły zadeklarowane jako zmienne lokalne znikają, gdy ich funkcja się kończy, więc listy buduje się na **stercie** za pomocą `malloc` z `stdlib.h`. Rezerwuje on żądaną liczbę bajtów i zwraca ich adres, albo `NULL`, gdy pamięć się wyczerpie; `sizeof(Node)` to odpowiednia ilość dla jednego węzła:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
Pamięć sterty nigdy nie jest zwalniana sama z siebie: każdy węzeł uzyskany z `malloc` trzeba oddać za pomocą `free(node)`, gdy tylko przestaje być potrzebny. W tych ćwiczeniach `stdlib.h` jest dołączony, a `Node` zadeklarowany nad twoim kodem.

---

Listę przechowuje pojedynczy wskaźnik do jej pierwszego węzła, **głowy**. Każdy kolejny węzeł osiąga się od głowy, podążając za `next`, a strzałkę można łączyć w łańcuch: `head->next` to drugi węzeł, a `head->next->next` trzeci. Pusta lista to głowa równa `NULL`, a `next` ostatniego węzła również jest `NULL`, więc podążenie o jedną strzałkę za daleko wyłuskuje `NULL` i powoduje awarię programu.

---

Przechodzenie po liście (**traversal**) to pętla, która zaczyna od głowy i podąża za `next`, aż dotrze do `NULL`. Pętla `for` wyraża to w pojedynczym wierszu, ze wskaźnikiem jako zmienną pętli:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
Nie ma tu indeksu: jedynym sposobem, by dotrzeć do węzła, jest wskaźnik przechowywany w węźle poprzedzającym.

---

Dodanie węzła na **początku** tworzy go, sprawia, że wskazuje on na obecną głowę, i zwraca go jako nową głowę. Wywołujący zapisuje wynik z powrotem do swojej zmiennej głowy:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Wstawianie do pustej listy działa tak samo: nowy węzeł wskazuje na `NULL` i staje się całą listą.

---

Zwolnienie listy oznacza zwolnienie każdego węzła, krok po kroku podczas przejścia. Wskaźnik `next` trzeba zapisać **przed** zwolnieniem węzła, bo zwolnionego węzła nie wolno już czytać, nawet jego `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Zapisanie `free(head)`, a potem `head = head->next` czyta pamięć, która została właśnie zwolniona, co jest zachowaniem niezdefiniowanym. `free(NULL)` jest dozwolone i nic nie robi, więc pusta lista nie wymaga szczególnego przypadku.

---

Lista nie przechowuje swojej długości: trzeba ją policzyć podczas przejścia. Wariant pętli z `while` trzyma wskaźnik na zewnątrz, co jest wygodne, gdy ciało pętli aktualizuje inne zmienne:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Dla pustej listy ciało pętli nigdy się nie wykona i licznik pozostaje `0`.

---

Dodanie węzła na **końcu** wymaga ostatniego węzła, tego, którego `next` to `NULL`. Funkcja przechodzi, aż go znajdzie, potem przypina tam nowy węzeł i zwraca niezmienioną głowę:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Gdy lista jest pusta, nie ma ostatniego węzła, do którego można przejść: nowy węzeł jest po prostu zwracany jako głowa.

---

Wyszukiwanie na liście to przejście, które porównuje każdą wartość i zatrzymuje się na pierwszym dopasowaniu. Funkcja zwraca wskaźnik do znalezionego węzła albo `NULL`, gdy dociera do końca listy bez dopasowania:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Zwracanie węzła zamiast wartości pozwala wywołującemu zmodyfikować go albo użyć go jako punktu wyjścia do innej operacji.

---

Po `free(p)` zmienna `p` nadal przechowuje stary adres, ale pamięć, na którą wskazuje, nie jest już twoja: `p` to teraz **wiszący wskaźnik** (dangling pointer). Czytanie lub pisanie przez niego albo zwolnienie go drugi raz to zachowanie niezdefiniowane: program może wypisać starą wartość, wypisać śmieci albo ulec awarii, a kompilator nie będzie narzekał. Gdy wskaźnik ma przetrwać `free`, ustaw go zaraz po nim na `NULL`, żeby każde późniejsze użycie zostało wyłapane przez sprawdzenie `NULL`.

---

Wstawienie **po** danym węźle nie wymaga przejścia: nowy węzeł przejmuje następnik `node`, a potem `node` jest kierowany na nowy:
```c
new_node->next = node->next;
node->next = new_node;
```
Kolejność tych dwóch przypisań ma znaczenie: ustawienie najpierw `node->next` nadpisałoby jedyny wskaźnik do reszty listy, a te węzły zostałyby utracone. Wstawienie po ostatnim węźle też działa, ponieważ jego `next` to `NULL`.

---

Usunięcie pierwszego węzła jest lustrzanym odbiciem `push_front`: zapisz adres drugiego węzła, zwolnij pierwszy i zwróć zapisany adres jako nową głowę. Wywołujący zapisuje wynik z powrotem do swojej zmiennej głowy:
```c
Node *next = head->next;
free(head);
return next;
```
Zdejmowanie aż głowa stanie się `NULL` zwalnia całą listę, po jednym węźle na wywołanie.

---

Usunięcie węzła w środku wymaga węzła **przed** nim, więc przejście trzyma dwa wskaźniki: `prev`, już odwiedzony węzeł, oraz `cur`, ten właśnie badany. Gdy `cur` pasuje, `prev->next` zostaje tak przekierowany, aby go pominąć, a `cur` jest zwalniany. Jeśli dopasowaniem jest sama głowa, `prev` to wciąż `NULL`, a nową głową jest `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Gdy żaden węzeł nie pasuje, lista jest zwracana bez zmian.

---

Odwracanie listy obraca każdy wskaźnik `next`, w miejscu, za pomocą trzech wskaźników: `prev` to już odwrócona część, `head` przetwarzany węzeł, a `next` kopia reszty listy, zapisana przed zmianą powiązania. W każdym kroku bieżący węzeł jest kierowany z powrotem na `prev`, a potem zarówno `prev`, jak i `head` przesuwają się do przodu:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Gdy `head` dotrze do `NULL`, każde powiązanie zostało odwrócone, a `prev` to nowa głowa.

---

Lista wiązana jest tania tam, gdzie tablica jest droga, i odwrotnie. Dodanie lub usunięcie na **początku** to kilka przypisań wskaźników niezależnie od długości, podczas gdy tablica musiałaby przesunąć każdy element. Z drugiej strony węzły nie leżą obok siebie, więc nie ma `list[i]`: dotarcie do n-tego węzła, ostatniego czy poznanie całkowitej długości oznacza przejście od głowy przez każdy węzeł po drodze. Programy, które często doklejają elementy, trzymają drugi wskaźnik do ostatniego węzła, **ogona**, aby uniknąć tego przejścia.

---

Zebranie tego w całość: lista często jest budowana z tablicy. Wstawianie na początku odwraca kolejność, więc tablicę przechodzi się **od tyłu**, od ostatniego elementu do pierwszego, i pierwszy element trafia na głowę. Program wypisuje potem listę podczas przejścia i zwalnia ją węzeł po węźle, tak że każdy `malloc` ma swoją parę w `free`.
