Eine **verkettete Liste** speichert Werte in einzelnen, im Speicher verstreuten **Knoten**: Jeder Knoten enthält einen Wert und einen Zeiger auf den nächsten Knoten, und der letzte zeigt auf `NULL`. Der Zeiger innerhalb verweist auf den gerade deklarierten Typ, daher braucht das struct ein **Tag**, um sich selbst zu benennen; der `typedef`-Name existiert innerhalb der geschweiften Klammern noch nicht:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Knoten werden verknüpft, indem die Adresse des einen im `next` des anderen gespeichert wird, und auf die Member des Knotens, auf den gezeigt wird, greift man mit dem Pfeil zu:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Knoten, die als lokale Variablen deklariert werden, verschwinden, wenn ihre Funktion zurückkehrt, daher werden Listen auf dem **Heap** mit `malloc` aus `stdlib.h` aufgebaut. Er reserviert die angeforderte Anzahl von Bytes und gibt deren Adresse zurück, oder `NULL`, wenn der Speicher erschöpft ist; `sizeof(Node)` ist die richtige Menge für einen Knoten:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
Heap-Speicher wird nie von selbst freigegeben: Jeder Knoten, der von `malloc` kommt, muss mit `free(node)` zurückgegeben werden, sobald er nicht mehr benötigt wird. In diesen Übungen ist `stdlib.h` inkludiert und `Node` über deinem Code deklariert.

---

Eine Liste wird von einem einzelnen Zeiger auf ihren ersten Knoten gehalten, dem **Kopf**. Jeder andere Knoten wird vom Kopf aus erreicht, indem man `next` folgt, und der Pfeil lässt sich verketten: `head->next` ist der zweite Knoten und `head->next->next` der dritte. Eine leere Liste ist ein Kopf gleich `NULL`, und das `next` des letzten Knotens ist ebenfalls `NULL`, daher dereferenziert ein Pfeil zu viel `NULL` und lässt das Programm abstürzen.

---

Das Durchlaufen einer Liste, genannt **Traversierung**, ist eine Schleife, die beim Kopf startet und `next` folgt, bis sie `NULL` erreicht. Eine `for`-Schleife drückt das in einer einzigen Zeile aus, mit einem Zeiger als Schleifenvariable:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
Es gibt keinen Index: Der einzige Weg, einen Knoten zu erreichen, führt über den Zeiger, der im vorherigen Knoten gespeichert ist.

---

Das Einfügen eines Knotens am **Anfang** erzeugt ihn, lässt ihn auf den aktuellen Kopf zeigen und gibt ihn als neuen Kopf zurück. Der Aufrufer speichert das Ergebnis zurück in seine Kopf-Variable:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Das Anhängen an eine leere Liste funktioniert genauso: Der neue Knoten zeigt auf `NULL` und wird zur ganzen Liste.

---

Das Freigeben einer Liste bedeutet, jeden Knoten freizugeben, Schritt für Schritt wie bei einer Traversierung. Der `next`-Zeiger muss gesichert werden, **bevor** der Knoten freigegeben wird, weil man einen freigegebenen Knoten nicht mehr lesen darf, auch nicht sein `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Schreibt man `free(head)` und danach `head = head->next`, liest man Speicher, der gerade freigegeben wurde, was undefiniertes Verhalten ist. `free(NULL)` ist erlaubt und tut nichts, daher braucht eine leere Liste keinen Sonderfall.

---

Eine Liste speichert ihre Länge nicht: Sie muss mit einer Traversierung gezählt werden. Die `while`-Form der Schleife behält den Zeiger außerhalb, was praktisch ist, wenn der Schleifenkörper andere Variablen aktualisiert:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Bei einer leeren Liste läuft der Schleifenkörper nie, und der Zähler bleibt `0`.

---

Das Einfügen eines Knotens am **Ende** braucht den letzten Knoten, also denjenigen, dessen `next` `NULL` ist. Die Funktion läuft, bis sie ihn findet, hängt dort den neuen Knoten an und gibt den unveränderten Kopf zurück:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Ist die Liste leer, gibt es keinen letzten Knoten, zu dem man laufen könnte: Der neue Knoten wird einfach als Kopf zurückgegeben.

---

Das Durchsuchen einer Liste ist eine Traversierung, die jeden Wert vergleicht und beim ersten Treffer stoppt. Die Funktion gibt einen Zeiger auf den gefundenen Knoten zurück, oder `NULL`, wenn sie das Ende der Liste ohne Treffer erreicht:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Den Knoten statt dem Wert zurückzugeben erlaubt dem Aufrufer, ihn zu ändern oder ihn als Startpunkt für eine andere Operation zu verwenden.

---

Nach `free(p)` enthält die Variable `p` immer noch die alte Adresse, aber der Speicher, auf den sie zeigt, gehört nicht mehr dir: `p` ist jetzt ein **hängender Zeiger**. Durch ihn zu lesen oder zu schreiben, oder ihn ein zweites Mal freizugeben, ist undefiniertes Verhalten: Das Programm gibt vielleicht den alten Wert aus, gibt Datenmüll aus oder stürzt ab, und der Compiler beschwert sich nicht. Muss ein Zeiger das `free` überleben, setze ihn direkt danach auf `NULL`, damit jede spätere Verwendung stattdessen von einer `NULL`-Prüfung abgefangen wird.

---

Das Einfügen **nach** einem gegebenen Knoten braucht keine Traversierung: Der neue Knoten übernimmt den Nachfolger von `node`, dann zeigt `node` auf den neuen:
```c
new_node->next = node->next;
node->next = new_node;
```
Die Reihenfolge der beiden Zuweisungen ist wichtig: Würde man zuerst `node->next` setzen, überschriebe man den einzigen Zeiger auf den Rest der Liste, und diese Knoten wären verloren. Das Einfügen nach dem letzten Knoten funktioniert ebenfalls, da sein `next` `NULL` ist.

---

Das Entfernen des ersten Knotens ist das Spiegelbild von `push_front`: Sichere die Adresse des zweiten Knotens, gib den ersten frei und gib die gesicherte Adresse als neuen Kopf zurück. Der Aufrufer speichert das Ergebnis zurück in seine Kopf-Variable:
```c
Node *next = head->next;
free(head);
return next;
```
Entfernt man, bis der Kopf `NULL` ist, wird die ganze Liste freigegeben, ein Knoten pro Aufruf.

---

Das Entfernen eines Knotens in der Mitte braucht den Knoten **davor**, daher hält die Traversierung zwei Zeiger: `prev`, den bereits besuchten Knoten, und `cur`, den gerade untersuchten. Passt `cur`, wird `prev->next` dazu gebracht, ihn zu überspringen, und `cur` wird freigegeben. Ist der Treffer der Kopf selbst, ist `prev` noch `NULL`, und der neue Kopf ist `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Passt kein Knoten, wird die Liste unverändert zurückgegeben.

---

Das Umkehren einer Liste dreht jeden `next`-Zeiger um, direkt in der Liste, mit drei Zeigern: `prev` ist der bereits umgedrehte Teil, `head` der gerade verarbeitete Knoten und `next` eine Kopie des Rests der Liste, gesichert bevor die Verknüpfung geändert wird. In jedem Schritt zeigt der aktuelle Knoten zurück auf `prev`, dann rücken `prev` und `head` beide vor:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Wenn `head` `NULL` erreicht, wurde jede Verknüpfung umgedreht, und `prev` ist der neue Kopf.

---

Eine verkettete Liste ist dort günstig, wo ein Array teuer ist, und umgekehrt. Am **Anfang** einzufügen oder zu entfernen sind ein paar Zeigerzuweisungen, egal wie lang die Liste ist, während ein Array jedes Element verschieben müsste. Andererseits liegen Knoten nicht zusammenhängend, daher gibt es kein `list[i]`: Den n-ten Knoten, den letzten oder die Gesamtlänge zu erreichen bedeutet, vom Kopf über jeden dazwischenliegenden Knoten zu laufen. Programme, die häufig anhängen, halten oft einen zweiten Zeiger auf den letzten Knoten, das **Tail**, um diesen Weg zu vermeiden.

---

Zum Zusammensetzen: Eine Liste wird oft aus einem Array aufgebaut. Am Anfang anzuhängen kehrt die Reihenfolge um, daher wird das Array **rückwärts** durchlaufen, vom letzten Element zum ersten, und das erste Element landet am Kopf. Das Programm gibt die Liste dann mit einer Traversierung aus und gibt sie Knoten für Knoten frei, sodass jede `malloc` von einem `free` begleitet wird.
