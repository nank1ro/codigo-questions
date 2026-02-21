Variaveis sao containers para armazenar valores.
Toda variavel em Dart e um objeto (`Object`).
Para criar uma variavel, temos que dar a ela um __nome__ levando em conta o fato de que ela nao deve conter espacos.
Dê uma olhada no seguinte:

```dart
int number = 1;
```

Esta instrucao declara uma variavel chamada `number` do tipo `int`.
Em seguida, define o valor da variavel como numero `1`.
A parte `int` da declaracao e conhecida como __anotacao de tipo__, e diz ao Dart explicitamente o tipo da variavel.

---

No exemplo anterior, vimos a criacao de uma variavel:

```dart
int number = 1;
```

Nao se deixe enganar pelo simbolo `=`.
Nao e o simbolo de igualdade como em matematica, mas e conhecido como o __operador de atribuicao__ porque atribui um valor a variavel.
O sinal de igualdade, por outro lado, e `==`.

---

Se voce quiser mudar o valor de uma variavel, simplesmente atribua a ela um valor diferente do mesmo tipo:

```dart
int number = 1;
number = 2;
```

---

O tipo `int` permite armazenar numeros inteiros.
Para salvar numeros decimais, podemos usar o tipo `double`:

```dart
double pi = 3.14159;
```

Este exemplo e semelhante ao anterior. Desta vez, no entanto, a variavel e do tipo `double`, um tipo que permite armazenar numeros decimais com alta precisao.

---

Dart e uma linguagem __tipada estaticamente__.
Isso significa que quando voce atribui um tipo a uma variavel, voce nao pode altera-lo depois. Aqui esta um exemplo:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

3.14159` e do tipo `double`, mas voce ja definiu `integerNumber` com o tipo `int`.

Claro que ocasionalmente pode ser util atribuir tipos relacionados a mesma variavel. Por exemplo, voce pode querer uma variavel `integerNumber` que aceite tanto numeros `int` quanto `double`, como aqui:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Tanto `int` quanto `double` estendem `num`, entao ambos os tipos sao aceitos.
No entanto, se tentarmos atribuir uma `String`, o compilador retorna um erro.

---

Se voce gosta de viver perigosamente, podemos ignorar completamente a __segurança de tipo__ da linguagem usando o tipo `dynamic`.
Isso permite que voce atribua qualquer tipo de valor a variavel.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

Esta abordagem e fortemente desencorajada, pois os erros nao sao mais interceptados pelo _analisador_ do codigo, mas apenas em _tempo de execucao_ (quando o programa esta rodando).

---

Dart suporta __inferencia de tipo__.
Nao e necessario indicar o tipo de uma variavel pois Dart pode inferir seu tipo.
A palavra-chave `var` diz ao Dart para usar o tipo mais apropriado.

```dart
var number = 5;
```

Nao e necessario dizer ao Dart que o numero `5` e do tipo `int`.
Dart infere o tipo e torna `number` do tipo `int`.

---

Dart suporta dois tipos diferentes de "_variaveis_" cujo valor nunca muda. Elas sao declaradas com as palavras-chave `const` e `final`.
Vamos comecar vendo o que e meant por `const`.

## const (constantes)

Variaveis cujo valor voce pode mudar sao conhecidas como __dados mutaveis__. Dados mutaveis sao frequentemente superutilizados e podem apresentar problemas. E facil perder o controle de todos os pontos no codigo que podem mudar o valor de uma variavel.

Por este motivo, voce deve usar `const`antes em vez de `var`iaveis sempre que possivel. Essas variaveis que nao podem mudar de valor tambem sao chamadas de __dados imutaveis__.

Para criar uma constante em Dart usamos a palavra-chave `const`:

```dart
const number = 5;
```

Assim como `var`, Dart com a __inferencia de tipo__ determina que `number` e do tipo `int`.

---

Quando voce declarou uma variavel constante, voce nao pode mais mudar seu valor. Por exemplo:

```dart
const number = 2;
number = 3; // Error
```

Este codigo produz o erro:
> Constant variables can't be assigned a value.

Ou seja, nao e possivel mudar o valor de uma variavel constante.

---

Voce frequentemente se encontrara na situacao de querer usar uma constante mas nao conhecer o valor em tempo de compilacao. Voce so conhecera o valor depois que o programa tiver iniciado a execucao.
Este tipo de constante e conhecida como uma __constante de tempo de execucao__.

Em Dart, `const` e usado apenas para __constantes de tempo de compilacao__ para valores que podem ser determinados pelo compilador antes que o programa seja executado.

Se voce nao pode criar uma variavel constante porque nao conhece seu valor de tempo de compilacao, entao voce deve usar a palavra-chave `final` para tornar a variavel uma __constante de tempo de execucao__.

Existem muitas razoes pelas quais voce nao pode conhecer o valor de uma variavel antes de executar o programa. Por exemplo, voce teria que obter o valor do servidor, ou pedir ao usuario por ele.

---

Aqui esta um exemplo de um valor que so pode ser obtido em tempo de execucao:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` e uma funcao para obter a data e hora atual de quando o codigo e executado.
Com o campo `hour`, acessamos o numero de horas que passaram desde o inicio do dia.

Como o valor de `hour` e diferente dependendo de quando o codigo e executado, isso pode ser definido como o valor _de tempo de execucao_.

Se voce tentar mudar o valor de uma variavel `final`, voce recebe um erro.
