Du könntest dich schon in einer Situation befunden haben, in der du ein Stück Code wiederverwenden möchtest, nur mit einigen anderen Werten.
Anstatt den ganzen Code neu zu schreiben, ist es viel sauberer, eine Funktion zu definieren, die dann wiederholt verwendet werden kann.
In JavaScript verwenden wir das Schlüsselwort `function` gefolgt vom Namen der Funktion:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

Die Klammern in der __Funktionsdefinition__ müssen nicht leer sein, wenn wir Parameter angeben wollen

---

Manchmal möchten wir, dass eine Funktion einen Wert __zurückgibt__.
Nun ja, es gibt das Schlüsselwort `return`.

---

Funktionen können mehrere Eingabeparameter haben, die in den Klammern der Funktion geschrieben werden und durch Kommas getrennt sind.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

Du kannst einen _Standardwert_ für jeden Parameter in einer Funktion definieren, indem du dem Parameter nach dem Typ des Parameters einen Wert zuweist.
Wenn ein Standardwert definiert ist, kannst du diesen Parameter beim Aufruf der Funktion auslassen
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

Die __Rest-Parameter__-Syntax ermöglicht es uns, eine unbegrenzte Anzahl von Argumenten als Array darzustellen.
Schreibe Rest-Parameter, indem du drei Punkt-Zeichen `...` vor dem Namen des Parameters einfügst.
Die an einen Rest-Parameter übergebenen Werte werden im Funktionskörper als Array verfügbar gemacht.
Zum Beispiel wird ein Rest-Parameter namens `numbers` im Funktionskörper als konstantes Array namens numbers verfügbar gemacht

---

In Funktionen können wir einen _optionalen Kommentar_ hinzufügen, der erklärt, was die Funktion tut:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Wir können `//` für einen einzeiligen Kommentar und `/** */` für einen mehrzeiligen Kommentar verwenden
