Wir wissen, wie man Code mit einer `while`-Schleife wiederholt.
Wie dieses Programm Anweisungen wiederholt, um `hello` anzuzeigen
```c
int counter = 0;

while (counter < 5) {
    printf("Hello\n");
    counter++;
}
```
Aber wir können dasselbe mit `for`-Schleifen tun:
```c
for (int i = 0; i < 5; i++) {
    printf("Hello\n");
}
```

---

In einer `for`-Schleife können wir angeben, wie oft wir unsere Schleife ausführen möchten

---

Wir können `<` verwenden, um bis zur nächsten Zahl ausgeschlossen zu schleifen, oder `<=` um bis zur nächsten Zahl eingeschlossen zu schleifen

---

Die Variable `i` ist die Zählervariable.
Wir können ihr den Namen geben, den wir möchten.
Sie zählt, in welcher Wiederholung der Schleife wir uns gerade befinden
