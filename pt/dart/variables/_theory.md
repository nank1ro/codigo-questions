Variáveis são contêineres para armazenar valores.
Toda variável em Dart é um objeto (`Object`).
Para criar uma variável, precisamos dar a ela um __nome__, levando em consideração o fato de que não deve conter espaços.
Observe o seguinte:

```dart
int number = 1;
```

Esta instrução declara uma variável chamada `number` do tipo `int`.
Em seguida, define o valor da variável como o número `1`.
A parte `int` da declaração é conhecida como __anotação de tipo__, e informa ao Dart explicitamente o tipo da variável.

---

No exemplo anterior, vimos a criação de uma variável:

```dart
int number = 1;
```

Não se deixe enganar pelo símbolo `=`.
Ele não é o símbolo de igualdade como na matemática, mas é conhecido como o __operador de atribuição__ porque atribui um valor à variável.
O sinal de igualdade, por outro lado, é `==`.

---

Se você quiser alterar o valor de uma variável, simplesmente atribua a ela um valor diferente do mesmo tipo:

```dart
int number = 1;
number = 2;
```

---

O tipo `int` permite armazenar números inteiros.
Para salvar números decimais, podemos usar o tipo `double`:

```dart
double pi = 3.14159;
```

Este exemplo é semelhante ao anterior. Desta vez, porém, a variável é do tipo `double`, um tipo que permite armazenar números decimais com alta precisão.

---

Dart é uma linguagem __type-safe__.
Isso significa que quando você atribui um tipo a uma variável, não pode alterá-lo depois. Veja um exemplo:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

`3.14159` é do tipo `double`, mas você já definiu `integerNumber` com o tipo `int`.

Claro, ocasionalmente pode ser útil atribuir tipos relacionados à mesma variável. Por exemplo, você pode querer uma variável `integerNumber` que aceite tanto números `int` quanto `double`, assim:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Tanto `int` quanto `double` estendem `num`, então ambos os tipos são aceitos.
No entanto, se tentarmos atribuir uma `String`, o compilador retorna um erro.

---

Se você gosta de viver com risco, podemos ignorar completamente a __segurança de tipos__ da linguagem usando o tipo `dynamic`.
Isso permite que você atribua qualquer tipo de valor à variável.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

Essa abordagem é fortemente desencorajada, pois os erros não são mais interceptados pelo _analisador_ do código, mas apenas em _tempo de execução_ (quando o programa está rodando).

---

Dart suporta __inferência de tipos__.
Não é necessário indicar o tipo de uma variável, pois o Dart pode inferir seu tipo.
A palavra-chave `var` diz ao Dart para usar o tipo mais apropriado.

```dart
var number = 5;
```

Não é necessário dizer ao Dart que o número `5` é do tipo `int`.
O Dart infere o tipo e torna `number` do tipo `int`.

---

Dart suporta dois tipos diferentes de "_variáveis_" cujo valor nunca muda. Elas são declaradas com as palavras-chave `const` e `final`.
Vamos começar vendo o que significa `const`.

## const (constantes)

Variáveis cujo valor pode ser alterado são conhecidas como __dados mutáveis__. Dados mutáveis são frequentemente usados em excesso e podem apresentar problemas. É fácil perder o controle de todos os pontos no código que podem alterar o valor de uma variável.

Por essa razão, você deve usar `const`antes em vez de `var`iáveis sempre que possível. Essas variáveis que não podem ter o valor alterado também são chamadas de __dados imutáveis__.

Para criar uma constante em Dart, usamos a palavra-chave `const`:

```dart
const number = 5;
```

Assim como `var`, o Dart com a __inferência de tipos__ determina que `number` é do tipo `int`.

---

Quando você declarou uma variável constante, não pode mais alterar seu valor. Por exemplo:

```dart
const number = 2;
number = 3; // Error
```

Este código produz o erro:
> Constant variables can't be assigned a value.

Ou seja, não é possível alterar o valor de uma variável constante.

---

Frequentemente você se encontrará na situação de querer usar uma constante, mas sem saber o valor em tempo de compilação. Você só saberá o valor depois que o programa tiver iniciado a execução.
Este tipo de constante é conhecido como uma __constante de tempo de execução__.

Em Dart, `const` é usado apenas para __constantes de tempo de compilação__, para valores que podem ser determinados pelo compilador antes que o programa seja executado.

Se você não pode criar uma variável constante porque não sabe seu valor em tempo de compilação, então deve usar a palavra-chave `final` para tornar a variável uma __constante de tempo de execução__.

Existem muitas razões pelas quais você não pode saber o valor de uma variável antes de executar o programa. Por exemplo, você pode ter que obter o valor do servidor, ou pedir ao usuário.

---

Aqui está um exemplo de um valor que só pode ser obtido em tempo de execução:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` é uma função para obter a data e hora atuais de quando o código é executado.
Com o campo `hour` acessamos o número de horas que se passaram desde o início do dia.

Como o valor de `hour` é diferente dependendo de quando o código é executado, isso pode ser definido como o valor de _tempo de execução_.

Se você tentar alterar o valor de uma variável `final`, obterá um erro.
