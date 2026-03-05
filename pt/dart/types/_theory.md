Os tipos permitem categorizar todos os diferentes tipos de dados que você usa no seu código.
Em Dart, um __tipo__ é uma forma de dizer ao compilador como você vai usar um determinado dado.
Aqui estão exemplos de tipos que o Dart suporta:
- int
- String
- double
- dynamic
- num

O Dart suporta muitos outros tipos. Estes listados são os principais que você vai usar.

---

Não há problema em definir explicitamente o tipo de uma variável, por exemplo:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Variáveis com tipo explícito também podem ser constantes, basta adicionar a palavra-chave `const` ou `final` antes do tipo:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Nota: Dados mutáveis permitem que você os altere quando quiser de forma fácil. No entanto, muitos programadores experientes apreciam os benefícios dos dados imutáveis. Quando um valor é imutável, você pode confiar que ninguém poderá alterar o valor depois que você o criar. Limitar seus dados dessa forma evita muitos bugs difíceis de encontrar e torna o programa mais fácil de entender e testar.

---

Embora seja possível anotar o tipo de uma variável, isso é redundante. Você sabe que `10` é do tipo `int` e `3.14` é do tipo `double`. O compilador Dart é capaz de inferir isso graças à __inferência de tipos__. Nem todas as linguagens de programação possuem _inferência de tipos_, e isso torna o Dart uma linguagem de programação muito poderosa.

Você pode simplesmente remover o tipo das variáveis, por exemplo:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

Quando o tipo de uma variável não é explicitamente anotado, o Dart tentará inferir seu tipo.

---

Existe uma forma programática de verificar o tipo de uma variável, usando a palavra-chave `is`:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

Como você pode ver, o Dart atribuiu o tipo `double` à variável `number`.

---

A palavra-chave `is` permite verificar se uma variável é do tipo que você define. Mas você também
 pode verificar se uma variável não é do tipo definido com a palavra-chave `is!`
```dart
final number = 3.14;
print(number is! int); // true
```

---

Outra opção que você tem para ver o tipo de uma variável em _tempo de execução_ é usar a propriedade `runtimeType`, que está disponível para todos os tipos.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

Às vezes você se encontrará na situação de ter um tipo, mas precisar convertê-lo para outro. Você pode ficar tentado a fazer:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

Mas o Dart vai reclamar e dar o erro:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Algumas linguagens de programação não são tão restritivas e farão a conversão silenciosamente. A experiência mostra que esse tipo de conversão implícita silenciosa é uma fonte frequente de bugs e problemas de desempenho. O Dart desativou essa funcionalidade para evitar esses problemas.

Lembre-se, os computadores dependem dos programadores para descobrir o que fazer. Em Dart, isso inclui ser explícito sobre o tipo de conversão.

Em vez de esperar uma conversão implícita do Dart, você precisa dizer explicitamente que deseja que o Dart converta o tipo para você. Veja como converter um número `double` para `int`:
```dart
var integer = decimal.toInt();
```

A atribuição diz ao Dart, de forma inequívoca, que você deseja converter do tipo original `double` para o novo tipo `double`.

> NOTAS: Neste caso, atribuir um valor decimal a um inteiro perde precisão. A variável `integer` tem o valor __3__ em vez de __3.14__. É por isso que é importante ser explícito. O Dart quer ter certeza do que você está fazendo e avisa que você perderá informação ao converter.

---

Até agora vimos os operadores usados independentemente em inteiros ou decimais. E se você tiver
um inteiro e precisar multiplicá-lo por um número decimal? Vejamos um exemplo:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` é do tipo `int` enquanto `pi` é do tipo `double`. Qual será o tipo de `circumference`? O Dart atribuirá o tipo `double` à variável `circumference`. Esta é a escolha mais segura, pois se tivesse feito do tipo `int` poderia ter causado perda de precisão.

Se você quiser um `int` como resultado, precisa fazer a conversão explicitamente:
```dart
const circumference = (2 * pi * radius).toInt();
```

Os parênteses dizem ao Dart para multiplicar primeiro, e depois pegar o resultado e convertê-lo para um valor inteiro. Infelizmente o analisador não vai gostar deste código:
 > Const variables must be initialized with a constant value.

O problema é que o método `toInt` é um método apenas de tempo de execução. Isso significa que a variável `circumference` não pode ser determinada em tempo de compilação, então não é possível que a variável seja constante. Para corrigir, substitua `const` por `final`:

```dart
final circumference = (2 * pi * radius).toInt();
```

Agora `circumference` é uma variável __constante em tempo de execução__ do tipo `int`.

---

Às vezes você pode ter uma variável com um tipo genérico, mas precisa de uma funcionalidade que existe apenas em um subtipo. Se você tem certeza de que o tipo da variável é o subtipo que precisa, então pode usar a palavra-chave `as` para mudar seu tipo. Esse procedimento também é conhecido como __type casting__, aqui está um exemplo:

```dart
num number = 3;
```

Digamos que queremos verificar se o número é par, e a funcionalidade em questão está presente apenas no subtipo `int`.
```dart
print(number.isEven);
```

O código acima deve retornar um erro de tipo:
> The getter `isEven` isn't defined for the type 'num'.

O tipo `num` é um tipo muito genérico para saber se um número é par ou ímpar. Apenas inteiros podem ser pares ou ímpares.
O problema ocorre se `num` contém um valor `double`, já que `num` inclui tanto os tipos `double` quanto `int`. Neste caso, temos certeza de que __3__ é um inteiro, então podemos fazer o cast para `int`

```dart
final integer = number as int;
print(integer.isEven); // false
```

A palavra-chave `as` faz o compilador reconhecer a variável `integer` como tendo o tipo `int`. Isso permite que você use a propriedade `isEven` que está presente nos inteiros. Como o número __3__ não é par, o resultado é false.

Você precisa ter cuidado ao fazer cast. Se você fizer o cast incorretamente, terá um erro em tempo de execução:
```dart
num numero = 3;
final decimale = numero as double;
```

Isso vai travar o programa com o seguinte erro:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

O tipo em tempo de execução de `number` é `int` e não `double`. Em Dart, você não pode fazer cast com tipos do mesmo nível, como `int` e `double`. Você só pode fazer cast de subtipos.
