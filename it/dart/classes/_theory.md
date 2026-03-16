Una **classe** è un modello per creare oggetti. Raggruppa dati correlati (campi) e comportamenti (metodi) insieme.

In Dart, dichiari una classe con la parola chiave `class` seguita dal nome della classe (per convenzione, in PascalCase):

```dart
class Car {
  String brand = 'Toyota';
}
```

Crei un'**istanza** (oggetto) della classe in questo modo:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

Un **costruttore** è un metodo speciale che viene eseguito quando crei un'istanza di una classe. Viene utilizzato per inizializzare i campi dell'oggetto.

In Dart, il costruttore più semplice usa la **sintassi abbreviata** `this.nomeCampo` per assegnare i parametri direttamente ai campi:

```dart
class Car {
  String brand;
  Car(this.brand);
}

void main() {
  final car = Car('Toyota');
  print(car.brand); // Toyota
}
```

---

Un **metodo** è una funzione definita all'interno di una classe. I metodi descrivono il comportamento di un oggetto.

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double area() {
    return 3.14 * radius * radius;
  }
}

void main() {
  final c = Circle(5);
  print(c.area()); // 78.5
}
```

I metodi possono accedere direttamente ai campi dell'oggetto per nome (o tramite `this.nomeCampo`).

---

Un **getter** è un metodo speciale che sembra una proprietà quando vi si accede. Usa la parola chiave `get` per definirne uno:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // acceduto come un campo, non come una chiamata a metodo
}
```

I getter sono utili per valori calcolati derivati dai campi.

---

L'**ereditarietà** permette a una classe di riutilizzare i campi e i metodi di un'altra classe. Usa la parola chiave `extends` per creare una sottoclasse (classe figlia):

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('Meow');
  }
}
```

La classe figlia chiama il costruttore genitore con `super(...)`. L'annotazione `@override` indica che il metodo sostituisce la versione del genitore.
