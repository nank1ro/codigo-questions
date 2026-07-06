Una **función** es un bloque de código reutilizable que realiza una tarea específica. En Dart, se define una función con un tipo de retorno, un nombre y un par de paréntesis `()`.

Cuando una función no devuelve ningún valor, su tipo de retorno es `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

Se llama a la función escribiendo su nombre seguido de `()`:

```dart
sayHello(); // prints Hello!
```

---

Las funciones pueden **devolver un valor** al llamador. Se declara el tipo de retorno antes del nombre de la función y se usa la palabra clave `return` para enviar el valor de vuelta:

```dart
int getAge() {
  return 25;
}
```

El tipo antes del nombre de la función (`int`) le indica a Dart qué tipo de valor devolverá la función. Se puede usar `String`, `int`, `double`, `bool` y más.

---

Las funciones pueden aceptar **parámetros** — valores que se pasan al llamar a la función. Los parámetros se declaran dentro de los paréntesis con su tipo y nombre:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Cada parámetro tiene un tipo (`int`) y un nombre (`n`). Los parámetros múltiples se separan por comas.

---

Dart admite **funciones flecha** usando la sintaxis `=>`. Cuando el cuerpo de una función es una sola expresión, se puede acortar con `=>` en lugar de `{ return ...; }`:

```dart
// Función normal
int double(int n) {
  return n * 2;
}

// Función flecha — mismo resultado
int double(int n) => n * 2;
```

Las funciones flecha hacen el código más conciso. El `=>` reemplaza tanto las llaves como la palabra clave `return`.

---

Dart admite **parámetros con nombre** — parámetros encerrados entre llaves `{}`. Los parámetros con nombre deben llamarse por su nombre y pueden tener valores por defecto o marcarse como `required`:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Los parámetros con nombre mejoran la legibilidad, especialmente cuando una función tiene muchos parámetros.
