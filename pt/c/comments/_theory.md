Um **comentário** é um texto dentro do seu código-fonte destinado a pessoas, não ao compilador. O compilador descarta os comentários antes de construir o programa, então você pode usá-los para explicar para que serve o código, deixar lembretes ou registrar uma decisão.

O tipo mais comum é o **comentário de linha única**: tudo, de `//` até o fim dessa linha, é ignorado.
```c
// Greet the user
printf("Hello\n");
```
A primeira linha não faz nada quando o programa roda; apenas o `printf` produz saída.

---

Como o compilador remove os comentários completamente, adicionar ou excluir um comentário nunca muda o que um programa faz. Apenas o código que **não** está comentado roda.

Isso torna o `//` uma forma rápida de desativar uma linha de código sem excluí-la. Isso se chama **comentar o código** (commenting out):
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
A segunda linha agora é um comentário, então `total` continua `10`. Remover o `//` traz a linha de volta à vida.

Comentar o código é útil enquanto você experimenta, mas lembre-se de limpar depois: código que fica comentado por muito tempo apenas confunde quem for ler em seguida.

---

Quando um comentário precisa de mais de uma linha, o C oferece o **comentário de múltiplas linhas** (também chamado de comentário de bloco): ele começa com `/*` e termina com `*/`, e tudo entre eles é ignorado, incluindo as quebras de linha.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Um comentário de bloco também pode ser curto e ficar em uma única linha: `/* like this */`.

Ao contrário do `//`, que termina no fim da linha, um comentário `/*` só termina no `*/`. Se você esquecer de fechá-lo, o compilador tratará todo o código seguinte como parte do comentário.

---

Comentários de bloco **não aninham**. O compilador encerra um comentário `/*` no primeiro `*/` que encontrar, não importa quantos `/*` tenham vindo antes dele:
```c
/* outer /* inner */ still code */
```
Aqui o comentário termina logo depois de `inner`, então `still code */` é compilado como código e produz um erro.

Isso importa quando você quer comentar um bloco que já contém um comentário `/* */`: o `*/` interno fecharia seu comentário externo cedo demais. Nesse caso, coloque `//` no início de cada linha em vez disso.

---

Um comentário não precisa de uma linha própria: ele pode vir depois do código, na mesma linha. Esse é um **comentário de fim de linha** (trailing comment), e é um bom lugar para uma nota curta sobre aquela instrução específica:
```c
int retries = 3; // give up after three attempts
```
Tanto `//` quanto `/* */` funcionam como comentários de fim de linha, mas cuidado com o `/*`: como ele só termina no `*/`, um `/*` não fechado no fim de uma linha engole as linhas seguintes, e o programa deixa de compilar.

---

Um uso comum dos comentários de bloco é o **comentário de cabeçalho**: um bloco curto colocado diretamente acima de uma função que diz o que ela faz, o que seus parâmetros significam e o que ela retorna.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Quem chama `to_seconds` agora pode ler o cabeçalho em vez do corpo. Mantenha o cabeçalho junto da função para que sejam atualizados juntos.

---

O compilador substitui cada comentário por um único espaço. Isso significa que um comentário `/* */` pode aparecer em qualquer lugar onde um espaço pode, até mesmo no meio de uma instrução ou de uma expressão:
```c
int area = width /* cm */ * height /* cm */;
```
Isso é ocasionalmente útil para rotular os operandos ou os argumentos de uma chamada. Um comentário `//` não consegue fazer isso, porque comentaria o resto da linha, incluindo o código depois dele.

---

Programadores usam algumas palavras-chave convencionais no início de um comentário para sinalizar trabalho que não está terminado:

- `TODO` marca algo que ainda precisa ser escrito
- `FIXME` marca código que se sabe estar errado e deve ser corrigido

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Editores e ferramentas podem listar esses marcadores, então o trabalho pendente é fácil de encontrar. Quando o trabalho estiver pronto, exclua o marcador: um `TODO` desatualizado é enganoso.

---

Um bom comentário explica **por que** o código faz algo, não **o que** ele faz. O código já mostra o que acontece; repeti-lo em palavras adiciona ruído e fica desatualizado assim que o código muda:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
O motivo por trás dos números é o que o leitor não consegue adivinhar:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Se um comentário apenas repete a linha abaixo dele, exclua-o ou substitua-o pelo motivo.

---

Juntando tudo: use `//` para notas curtas e comentários de fim de linha, `/* */` para blocos mais longos e comentários de cabeçalho, marque trabalho não terminado com `TODO` ou `FIXME` e remova código comentado e marcadores desatualizados quando não forem mais necessários.
