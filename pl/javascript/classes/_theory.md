JavaScript jest obiektowym językiem programowania, co oznacza, że operuje on na konstruktach programistycznych zwanych obiektami.
Możesz myśleć o obiekcie jak o pojedynczej strukturze danych, która zawiera zarówno dane, jak i funkcje; funkcje obiektu nazywane są jego metodami.
Na przykład, gdy wywołujesz:
```javascript
arrayName.push("value");
```
JavaScript sprawdza, czy `arrayName` posiada metodę `push()` (którą mają wszystkie tablice) i wywołuje ją, jeśli ją znajdzie.

---

_Klasy_ to ogólne, elastyczne konstrukty, które stają się budulcem kodu Twojego programu.
Podstawowa klasa składa się tylko ze słowa kluczowego `class` i jej nazwy, na przykład:
```javascript
class ClassName {
    // class definition
}
```

---

Dodajmy coś do naszej klasy `Animal`.
Aby dodać parametry, musimy użyć domyślnego `constructor`a

---

Definiowanie klasy nie tworzy obiektu.
Aby to zrobić, musimy utworzyć __instancję__ klasy.
W JavaScript, aby utworzyć nową instancję klasy, zawsze używamy słowa kluczowego `new` przed nazwą klasy.
Jeśli chcesz przypisać wartość domyślną do parametru, zrób to na liście parametrów konstruktora

---

Gdy klasa posiada własne funkcje, te funkcje nazywane są __metodami__.

---

JavaScript pozwala nam tworzyć klasę jako potomka innej klasy, używając słowa kluczowego `extends`

---

Możesz uzyskać dostęp do właściwości instancji używając _składni z kropką_.
W składni z kropką piszesz nazwę właściwości bezpośrednio po nazwie instancji, oddzieloną kropką `.`, bez żadnych spacji:
```javascript
someInstance.someProperty
```
Używając tej samej składni możemy również aktualizować wartość właściwości
