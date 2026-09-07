Uma **classe** é um modelo para criar objetos. Em Dart, você define uma classe com a palavra-chave `class` seguida do nome da classe e um par de chaves:

```dart
class Animal {
  // fields and methods go here
}
```

Por convenção, os nomes de classes usam **PascalCase** (cada palavra começa com uma letra maiúscula).

---

Uma classe pode ter **variáveis de instância** (também chamadas de campos) que armazenam dados para cada objeto. Você as declara dentro do corpo da classe, dando a cada uma um valor inicial:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Cada objeto criado a partir dessa classe terá seu próprio `name` e `age`.

---

Um **construtor** é um método especial que é executado quando você cria (instancia) um objeto a partir de uma classe. O construtor tem o mesmo nome da classe:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Um parâmetro escrito como `this.name` armazena o valor passado ao construtor diretamente no campo `name` do novo objeto. Um campo definido dessa forma não precisa de um valor inicial.

Você cria um objeto usando a palavra-chave `new` (opcional em Dart) ou apenas o nome da classe:

```dart
var dog = Animal('Rex');
```

---

O parâmetro `this.x` que você viu no exercício anterior é uma abreviação. A forma longa atribui cada parâmetro ao seu campo dentro do corpo do construtor (`this.x` é o campo, `x` é o parâmetro):

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

A mesma classe pode ser escrita como:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Essa forma mais curta é chamada de **parâmetros de inicialização** (initializing formals).

---

Um **método** é uma função definida dentro de uma classe. Métodos descrevem o comportamento de um objeto:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

Você chama um método em um objeto usando a notação de ponto: `dog.speak()`.

---

`this` refere-se à **instância atual** da classe, ou seja, o objeto no qual o método foi chamado. Dentro de um método você pode usá-lo para acessar os próprios campos do objeto:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Aqui, `this.radius` lê o campo `radius` do círculo no qual `diameter()` foi chamado. Quando não há outra variável com o mesmo nome, `this.` pode ser omitido: `radius * 2` funciona da mesma forma.

---

Dart suporta **construtores nomeados**, que permitem definir formas adicionais de criar um objeto. Construtores nomeados são escritos como `ClassName.constructorName`:

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

A parte após os dois-pontos é a **lista de inicialização** (initializer list): ela atribui os campos antes que o corpo do construtor seja executado. Você pode então criar um objeto na origem com: `var p = Point.origin();`

---

Um **getter** é um método especial que lê um valor calculado ou privado e se parece com o acesso a uma propriedade. Você o define com a palavra-chave `get`:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

Você acessa um getter como um campo: `circle.area` (sem parênteses).

A seta `=> expr` é uma abreviação para um corpo que apenas retorna um valor: `{ return expr; }`. Ela funciona para getters e para qualquer função ou método:

```dart
double half(double n) => n / 2;
```

---

Um **setter** é um método especial que permite atribuir um valor enquanto executa uma lógica de validação. Você o define com a palavra-chave `set`:

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

O nome do campo geralmente é prefixado com `_` para marcá-lo como privado.

---

**Herança** permite que uma classe (a **subclasse**) estenda outra classe (a **superclasse**) e reutilize seus campos e métodos. Use a palavra-chave `extends`:

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog` herda `name` e `speak()` de `Animal` e adiciona seu próprio método `fetch()`. Uma classe que não declara nenhum construtor recebe um construtor padrão sem parâmetros, então você pode escrever `var dog = Dog();` e depois chamar tanto `dog.speak()` quanto `dog.fetch()`.

---

Quando o construtor de uma subclasse precisa chamar o construtor da superclasse, use a palavra-chave `super` na **lista de inicialização**:

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)` encaminha o argumento `brand` para o construtor de `Vehicle`.

---

**Sobrescrita de método** permite que uma subclasse forneça sua própria implementação de um método que já existe na superclasse. Use a anotação `@override`:

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

A anotação `@override` informa ao Dart (e a outros desenvolvedores) que você está substituindo intencionalmente o método da superclasse.

---

Uma **classe abstrata** é uma classe que não pode ser instanciada diretamente. Ela é usada como uma base que define um contrato — métodos que devem ser implementados pelas subclasses. Você marca métodos abstratos omitindo o corpo:

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

Tentar instanciar `Shape()` diretamente resulta em um erro.

---

**Membros estáticos** pertencem à própria classe, e não a uma instância específica. Você os declara com a palavra-chave `static` e os acessa diretamente na classe:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

Campos e métodos estáticos são compartilhados por todas as instâncias.

---

Um **construtor factory** usa a palavra-chave `factory` e permite controlar a criação de objetos — por exemplo, retornando uma instância em cache ou um subtipo:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Cada chamada a `Logger()` retorna a mesma instância (padrão singleton).
