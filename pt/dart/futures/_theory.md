Algumas operações levam tempo: ler um arquivo, chamar um servidor, esperar um temporizador. O Dart não bloqueia o programa enquanto elas rodam. Em vez disso, uma função assim retorna um **`Future<T>`**: a promessa de que um valor do tipo `T` estará disponível **mais tarde**.

O future mais simples é aquele que já tem o seu valor, construído com `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Para tirar o valor de um future você usa **`await`**. `await` pausa a função atual até o future ser concluído e então entrega o valor puro. Só é permitido dentro de uma função marcada com **`async`**, então `main` passa a ser `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Sem `await`, `n` seria o próprio `Future`, e `print(n)` mostraria `Instance of 'Future<int>'` em vez do número.

---

Marcar uma função como `async` faz duas coisas: permite `await` no corpo e faz a função **retornar um `Future`**. O que você devolve com `return` vira o valor com que o future é concluído, então o tipo de retorno declarado é `Future<T>` mesmo que o corpo devolva um `T` puro:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

Aqui você não precisa de `Future.value`: a palavra-chave `async` embrulha o valor retornado para você.

---

`Future.value` conclui na hora. Para simular um trabalho que leva tempo, use **`Future.delayed`**: ele recebe uma `Duration` e uma função, espera a duração e então conclui com o que a função retorna:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` é construída com parâmetros nomeados como `seconds`, `milliseconds` ou `minutes`. Dentro de uma função `async` você também pode aguardar um atraso sozinho, sem valor, apenas para pausar:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Os dois estilos são comuns; o segundo se lê como código sequencial comum.

---

Mantenha claros os dois lados de um future:

- uma função `async` **declara** `Future<T>` e **retorna** um `T` puro: o embrulho é automático
- quem faz `await` em um `Future<T>` **recebe** um `T` puro: o desembrulho é automático

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Escrever `int count() async` é um erro: uma função `async` precisa declarar um tipo de retorno `Future` (ou `void`).

---

`await` não é o único jeito de usar um future. Você também pode registrar um **callback** com **`then`**: a função que você passa é chamada com o valor assim que o future é concluído. Diferente de `await`, `then` **não** pausa a função atual, então o código depois dele roda primeiro:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Mesmo um future construído com `Future.value` entrega seu valor só depois que o código atual termina, e é por isso que `waiting` é impresso primeiro. `then` funciona em qualquer função, `async` ou não.

---

Dentro de uma função `async`, `await` deixa você escrever passos assíncronos como se fossem código sequencial comum. Cada `await` espera pelo seu future, e a linha seguinte só roda quando o valor está disponível:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` também pode ser usado diretamente dentro de uma expressão: `return await width() * await height();` dá o mesmo resultado.

---

Quando uma função chega a um `await`, ela **pausa** naquela linha e o resto do programa continua. As linhas depois do `await` só rodam quando o future é concluído. Ler uma função `async` de cima para baixo, portanto, mostra a ordem exata dos seus efeitos:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

Um future também pode concluir com um **erro**. Quando uma função `async` lança, a exceção não escapa na hora: ela vira o erro do future retornado. Quem faz `await` nesse future vê o erro lançado no `await`, então ele pode ser tratado com um `try`/`catch` comum:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

O `await` dentro do `try` é essencial: `return parseLater(s);` entregaria o future ao chamador **sem esperar**, então o erro chegaria depois que o bloco `try` já tivesse terminado e o `catch` nunca rodaria.

---

Os erros viajam com o future, não pela pilha de chamadas. Chamar uma função `async` que lança nunca derruba o chamador por si só: o erro fica guardado no future retornado e aparece mais tarde, no ponto em que o future é aguardado. Um `try`/`catch` precisa então envolver o **`await`**, não a chamada que criou o future.

Se ninguém aguardar nem tratar o future que falhou, o Dart relata uma *unhandled exception* e, em um programa de linha de comando, encerra com erro.

---

Com callbacks, os erros são tratados por **`catchError`**, a contraparte de `then`. Os dois retornam um novo future, então costumam ser encadeados: `then` recebe o valor se o future der certo, `catchError` recebe o erro se ele falhar, e só um dos dois callbacks roda:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

Um `catchError` colocado depois de `then` também captura erros lançados dentro do callback de `then`. Como com `then`, o código depois da cadeia roda primeiro, porque os callbacks só são invocados quando o código atual termina.

---

Quando vários futures não dependem uns dos outros, entregue todos a **`Future.wait`**: ele recebe uma `List<Future<T>>`, deixa que rodem ao mesmo tempo e retorna um único `Future<List<T>>` que conclui quando **todos** terminam. Os resultados mantêm a ordem da lista de entrada, independentemente de qual future terminou primeiro:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` leva `25` milissegundos, porque `fast()` só é chamada depois que `slow()` concluiu; `await Future.wait([slow(), fast()])` leva cerca de `20`, a duração do mais longo.

---

`Future.wait` é a ferramenta para "carregar várias coisas e então continuar". O formato típico é: montar a lista de futures, fazer `await Future.wait` nela e então usar a lista resultante:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` conclui primeiro, mas a lista ainda segue a ordem das chamadas: `stock()` primeiro, `orders()` em segundo.

---

Você não precisa de `Future.wait` para rodar dois futures ao mesmo tempo. Uma função `async` começa a rodar assim que é **chamada**, até o seu primeiro `await`; o future que você recebe de volta é o trabalho já em andamento. O truque, então, é: **chamar primeiro, aguardar depois**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Compare com `return await words() / await pages();`, onde `pages()` só é chamada depois que `words()` concluiu: mesmo resultado, o dobro do tempo. Prefira a forma concorrente sempre que a segunda chamada não precisar do resultado da primeira.

---

Um erro se **propaga** por todo `await` que não o captura. Se `load()` falha, `await load()` dentro de `loadTwice()` lança; como `loadTwice` não tem `try`/`catch`, o próprio future dela falha com o mesmo erro; e assim por diante cadeia acima, até que algum `await` esteja envolvido em um `try`/`catch`:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

Isso espelha como as exceções se propagam pelas chamadas síncronas: você as trata uma vez, no nível que sabe o que fazer.

---

`Future.wait` segue a mesma regra: se **qualquer um** dos futures falhar, o future combinado conclui com esse erro e `await Future.wait(...)` lança. Você nunca recebe uma lista parcial com os valores que deram certo. Para manter os outros, trate o erro dentro de cada future individual, por exemplo com `catchError`, antes de passá-lo para `Future.wait`.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

Como `await` transforma erros de future em exceções comuns, todos os padrões usuais de `try`/`catch` valem para código assíncrono, inclusive laços que tentam de novo. Dentro de um bloco `catch`, **`rethrow`** lança o mesmo erro outra vez, e é assim que você desiste depois da última tentativa:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

Um parâmetro do tipo função como `Future<String> Function() task` recebe a **função** em si, não um future: cada chamada de `task()` inicia uma nova tentativa.
