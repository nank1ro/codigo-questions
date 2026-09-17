> Antes de começar, gostaria de dizer que estou muito feliz em ensinar Dart a você.
Com esta mensagem, aproveito para informar que o aplicativo que você está usando foi escrito justamente em Dart, utilizando o framework Flutter. Portanto, é uma honra para mim poder compartilhar minha experiência na linguagem.

Dart, assim como muitas outras linguagens de programação, permite que você documente seu código.
Isso permite que você escreva qualquer texto junto ao código.
Comentários são ignorados pelo compilador.

Dart suporta comentários de _linha única_, comentários de _múltiplas linhas_ e comentários de _documentação_.

Veja como escrever um comentário de _linha única_:
```dart
// Isto é um comentário. Ele não é executado.
```

---

Você pode empilhar comentários de _linha única_ para escrever comentários de _múltiplas linhas_.
```dart
// Isto é um
// multi-line comment
```

---

Você também pode criar blocos de comentários, ou comentários de _múltiplas linhas_.
Comentários de _múltiplas linhas_ começam com `/*` e terminam com `*/`.
```dart
/*
This is a multi-line
comment
*/
```

---

Além dessas duas formas de escrever comentários, Dart inclui _comentários de documentação_.

_Comentários de documentação_ são comentários de múltiplas linhas ou de linha única que começam com `///` ou `/**.` O uso de `///` em linhas consecutivas tem o mesmo efeito de um comentário de documentação de múltiplas linhas.

_Comentários de documentação_ são muito úteis porque permitem que a documentação seja gerada.
Você vai querer adicionar _comentários de documentação_ ao seu código para deixar claro o que um determinado bloco de código faz.

Dentro de um _comentário de documentação_, o analisador resolve os nomes colocados entre colchetes como referências a outros elementos da API.
Usando colchetes, pode-se fazer referência a _classes_, _métodos_, _campos_, _variáveis_, _funções_ e _parâmetros_.

Aqui está um exemplo:
```dart
/// Um camelídeo sul-americano domesticado (Lama glama).
///
/// Assim como qualquer outro animal, lhamas precisam comer,
/// então não se esqueça de [feed] com um pouco de [Food].
class Llama {
  String? name;

  /// Alimenta sua lhama com [food].
  ///
  /// A lhama típica come um fardo de feno por semana.
  void feed(Food food) {
    // ...
  }

  /// Exercita sua lhama com uma [activity] por
  /// [timeLimit] minutos.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

Na documentação gerada, `[feed]` se torna um link para a documentação do método `feed`, e `[Food]` se torna um link para a documentação da classe `Food`.
Enquanto `[activity]` e `[timeLimit]` se tornam links para a documentação de `activity` e `timeLimit` respectivamente.
