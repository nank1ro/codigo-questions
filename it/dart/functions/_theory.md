Una **funzione** è un blocco di codice riutilizzabile che esegue un'attività specifica. In Dart, si definisce una funzione con un tipo di ritorno, un nome e una coppia di parentesi `()`.

Quando una funzione non restituisce alcun valore, il suo tipo di ritorno è `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

Si chiama la funzione scrivendo il suo nome seguito da `()`:

```dart
sayHello(); // prints Hello!
```

---

Le funzioni possono **restituire un valore** al chiamante. Si dichiara il tipo di ritorno prima del nome della funzione e si usa la parola chiave `return` per inviare il valore indietro:

```dart
int getAge() {
  return 25;
}
```

Il tipo prima del nome della funzione (`int`) indica a Dart che tipo di valore restituirà la funzione. Si possono usare `String`, `int`, `double`, `bool` e altri.

---

Le funzioni possono accettare **parametri** — valori passati quando si chiama la funzione. I parametri sono dichiarati tra le parentesi con il loro tipo e nome:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Ogni parametro ha un tipo (`int`) e un nome (`n`). I parametri multipli sono separati da virgole.

---

Dart supporta le **funzioni freccia** usando la sintassi `=>`. Quando il corpo di una funzione è una singola espressione, è possibile abbreviarla con `=>` invece di `{ return ...; }`:

```dart
// Funzione normale
int double(int n) {
  return n * 2;
}

// Funzione freccia — stesso risultato
int double(int n) => n * 2;
```

Le funzioni freccia rendono il codice più conciso. Il `=>` sostituisce sia le parentesi graffe che la parola chiave `return`.

---

Dart supporta i **parametri con nome** — parametri racchiusi tra parentesi graffe `{}`. I parametri con nome devono essere chiamati per nome e possono avere valori predefiniti o essere contrassegnati come `required`:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

I parametri con nome migliorano la leggibilità, specialmente quando una funzione ha molti parametri.
