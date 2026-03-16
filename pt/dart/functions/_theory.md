Uma **função** é um bloco de código reutilizável que realiza uma tarefa específica. Em Dart, você define uma função com um tipo de retorno, um nome e um par de parênteses `()`.

Quando uma função não retorna nenhum valor, seu tipo de retorno é `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

Você chama a função escrevendo seu nome seguido de `()`:

```dart
sayHello(); // prints Hello!
```

---

Funções podem **retornar um valor** para quem as chamou. Você declara o tipo de retorno antes do nome da função e usa a palavra-chave `return` para enviar o valor de volta:

```dart
int getAge() {
  return 25;
}
```

O tipo antes do nome da função (`int`) informa ao Dart que tipo de valor a função retornará. Você pode usar `String`, `int`, `double`, `bool` e outros.

---

Funções podem aceitar **parâmetros** — valores passados ao chamar a função. Os parâmetros são declarados dentro dos parênteses com seu tipo e nome:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Cada parâmetro tem um tipo (`int`) e um nome (`n`). Múltiplos parâmetros são separados por vírgulas.

---

Dart suporta **funções de seta** usando a sintaxe `=>`. Quando o corpo de uma função é uma única expressão, você pode encurtá-la com `=>` em vez de `{ return ...; }`:

```dart
// Função regular
int double(int n) {
  return n * 2;
}

// Função de seta — mesmo resultado
int double(int n) => n * 2;
```

Funções de seta tornam o código mais conciso. O `=>` substitui tanto as chaves quanto a palavra-chave `return`.

---

Dart suporta **parâmetros nomeados** — parâmetros envolvidos em chaves `{}`. Parâmetros nomeados devem ser chamados pelo nome e podem ter valores padrão ou ser marcados como `required`:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Parâmetros nomeados melhoram a legibilidade, especialmente quando uma função tem muitos parâmetros.
