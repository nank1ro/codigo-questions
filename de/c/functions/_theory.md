Sie könnten schon erwogen haben, eine Codestelle wiederzuverwenden, nur mit einigen unterschiedlichen Werten.
Anstatt den ganzen Code neu zu schreiben, ist es viel sauberer, eine Funktion zu definieren, die dann wiederholt verwendet werden kann.
In C verwenden wir den `return_type` gefolgt vom `function`-Namen, zum Beispiel:
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

Die Klammern in der __Funktionsdefinition__ müssen nicht leer sein, wenn wir Parameter angeben wollen

---

Manchmal möchten wir, dass eine Funktion einen Wert __zurückgibt__.
Nun, dafür gibt es das `return`-Schlüsselwort.

---

Funktionen können mehrere Eingabeparameter haben, die in den Klammern der Funktion geschrieben werden, getrennt durch Kommas.
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

In Funktionen können wir einen _optionalen Kommentar_ hinzufügen, der erklärt, was die Funktion macht:
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
Wir können `//` für einen einzeiligen Kommentar und `/* */` für einen mehrzeiligen Kommentar verwenden
