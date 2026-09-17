Uma _interpolação_ de String é uma forma programática de gerar uma String.
Em Dart, podemos usar o sinal `+` (concatenação) para exibir duas ou mais strings juntas, como:
```dart
print("Hello " + "Dart!");
// imprime "Hello Dart!"
```

---

Mas usar o sinal `+` para adicionar um número como '10' a uma string como ` "friends"` produz um erro, pois são tipos diferentes de valores

---

A interpolação de string nos permite exibir expressões como adicionar uma string a um número, sem nenhum erro.
Colocar uma expressão dentro de `${}` a avalia.
O valor retornado é convertido em uma String e inserido na String resultante

---

Se você colocar um `$` antes do nome de um identificador, a interpolação de string inserirá o conteúdo desse identificador na `String`

---

Se o que vem após o sinal `$` não for reconhecido como um identificador de programa, o Dart produzirá um erro de compilação: o `$` dentro de uma string deve sempre ser seguido por um identificador ou por uma expressão entre chaves (`${}`).

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

A interpolação de string é melhor usada em instruções de impressão, mas também podemos armazená-las em variáveis como strings normais.
