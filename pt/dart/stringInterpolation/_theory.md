Uma _interpolacao_ de String e uma forma programatica de gerar uma String.
Em Dart, podemos usar o sinal `+` (concatenacao) para exibir duas ou mais strings juntas, como:
```dart
print("Hello " + "Dart!");
// imprime "Hello Dart!"
```

---

Mas usar o sinal `+` para adicionar um numero como '10' a uma string como ` "friends"` produz um erro, pois sao tipos diferentes de valores

---

A interpolacao de string nos permite exibir expressoes como adicionar uma string a um numero, sem nenhum erro.
Colocar uma expressao dentro de `${}` a avalia.
O valor retornado e convertido em uma String e inserido na String resultante

---

Se voce colocar um `$` antes do nome de um identificador, a interpolacao de string inserira o conteudo desse identificador na `String`

---

Se o que vem apos o sinal `$` nao for reconhecido como um identificador de programa, voce encontrara um erro

---

Tambem podemos inserir variaveis apos os sinais de dolar para mostrar seus valores

---

Podemos usar chaves para inserir valores quantas vezes quisermos usando a interpolacao de string

---

Dentro de `${}` tambem podemos colocar condicoes, por exemplo:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// imprime The answer is correct
```

---

A interpolacao de string e melhor usada em instrucoes de impressao, mas tambem podemos armazena-las em variaveis como strings normais.
