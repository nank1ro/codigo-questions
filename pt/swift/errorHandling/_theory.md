Em Swift um erro é um **valor**, não um crash. Qualquer tipo pode agir como um ao se conformar ao protocolo `Error`, e um enum é a escolha usual porque os casos nomeiam exatamente o que pode dar errado:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Uma função que pode falhar é marcada com `throws`, e ela reporta a falha com `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Chamar essa função exige `try`, e a chamada precisa ficar dentro de um bloco `do` seguido por um bloco `catch` que diz o que fazer quando ela falha:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
Quando o `throw` executa, o restante do bloco `do` é pulado e o `catch` assume. Nada quebra: o programa continua depois do `catch`.

---

Uma função que lança erros ainda pode retornar um valor. A palavra-chave `throws` fica entre a lista de parâmetros e a seta de retorno:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Lendo em voz alta: *square recebe um `Int`, pode lançar um erro e retorna um `Int`*.

No local da chamada o valor só existe quando nada foi lançado, então a atribuição fica dentro do bloco `do`:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
O `try` não é um enfeite opcional: o compilador rejeita a chamada sem ele, então um leitor sempre vê quais linhas podem falhar.

---

Um `catch` sem padrão trata todos os erros da mesma forma. Na maioria das vezes você quer reagir a uma falha específica, então um `catch` pode carregar um **padrão**: o caso que ele está disposto a tratar.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift testa as cláusulas `catch` de cima para baixo e executa a primeira cujo padrão corresponde.

O último `catch` não tem padrão de propósito. Um `catch` com padrão cobre apenas o caso que ele nomeia, e Swift insiste que todo erro seja tratado em algum lugar, então um bloco `do` que lista padrões precisa de um `catch` final sem padrão para recolher o resto.

---

A ordem importa. Swift compara o valor lançado com cada padrão de `catch` na ordem em que são escritos e para na primeira correspondência, então um `catch` sem padrão colocado primeiro engoliria tudo abaixo dele. Mantenha os casos específicos no topo e o catch-all no final.

Um erro que não corresponde a nenhum dos padrões não é ignorado: ele cai no `catch` final sem padrão.

---

Um caso de erro pode carregar dados. Dê ao caso **valores associados** e o `throw` os preenche, então quem trata aprende não apenas *o que* falhou mas *o quanto*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
O `catch` correspondente vincula esses valores com `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
O nome depois do `let` é você quem escolhe; é uma nova constante disponível apenas dentro daquele bloco `catch`. É assim que um erro carrega uma mensagem útil sem que você precise colar números em strings no ponto onde a falha acontece.

---

Um enum geralmente guarda todas as maneiras pelas quais uma única tarefa pode falhar, um caso por motivo:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Escrever um `catch` por caso fica repetitivo. Em vez disso, capture o tipo inteiro de uma vez e faça um `switch` sobre o valor:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` significa *capturar qualquer coisa que seja um `FormError` e chamá-la de `error`*. Dentro do bloco `error` tem o tipo do enum, então o `switch` enxerga os casos e verifica que você cobriu todos. O `catch` final sem padrão ainda é necessário, porque algum outro tipo de erro pode chegar a esse bloco `do`.

---

Um validador fica mais legível quando as rejeições vêm primeiro e o trabalho real fica sem indentação no final. O `guard` é feito para isso: ele declara a condição que deve valer, e seu bloco `else` executa quando ela não vale.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
O bloco `else` de um `guard` precisa sair do escopo atual, e `throw` é uma das maneiras de fazer isso, ao lado de `return`, `break` e `continue`. Vários `guard`s empilhados no topo de uma função parecem uma lista das regras que a entrada precisa satisfazer.

---

Às vezes você não se importa com o *porquê* de algo ter falhado, apenas que falhou. O `try?` transforma uma chamada que lança erros em um **opcional**: o valor quando ela tem sucesso, `nil` quando ela lança.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
Sem `do`, sem `catch`: a falha é dobrada no opcional que você já sabe desempacotar. O preço é que o valor do erro é descartado, então use `try?` apenas quando genuinamente não há nada a reportar.

---

Como o `try?` produz um opcional, o operador de coalescência nula `??` termina o trabalho fornecendo um fallback:
```swift
let port = (try? readPort(text)) ?? 8080
```
Os parênteses importam. Sem eles, o `try?` tentaria cobrir a expressão inteira incluindo o `??`, e o compilador pede que você seja explícito sobre onde a chamada que falha termina.

Leia a linha como uma frase: *use a porta que conseguimos ler, caso contrário 8080*. Duas linhas de `do`/`catch` viram uma quando a recuperação realmente é apenas um valor padrão.

---

Existe uma terceira forma: o `try!`. Ele diz ao compilador *esta chamada não pode falhar*, então sem `do`, sem `catch` e sem opcional. Se ela falhar mesmo assim, o programa para imediatamente.
```swift
let pattern = try! Regex("[0-9]+")
```
Esse é o formato em que o `try!` é defensável: o argumento é um literal escrito por você, no seu próprio código, e se estiver errado o programa está quebrado e deve parar durante a sua primeira execução de teste.

Qualquer coisa que chega em tempo de execução — uma linha digitada por um usuário, um arquivo, uma resposta de rede — pode estar errada de maneiras que você não consegue ver enquanto escreve o código, e `try!` sobre ela transforma uma falha recuperável em um crash na frente do usuário. Use `do`/`catch` ou `try?` nesses casos.

---

Quando uma função lança um erro, tudo depois do `throw` é pulado — incluindo a linha que deveria fechar o arquivo ou liberar o lock. O `defer` resolve isso: ele registra um bloco agora e o executa quando o escopo atual termina, de qualquer maneira que termine.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
A chamada imprime `open`, depois `close`, e só então o erro segue para quem chamou. Se a função tivesse retornado normalmente, `close` ainda seria impresso — esse é o ponto. Coloque a limpeza bem ao lado da configuração e pare de se preocupar com qual saída o código toma.

---

Um escopo pode registrar mais de um `defer`. Eles executam em ordem **reversa**: o último registrado é o primeiro a executar.

Essa não é uma regra arbitrária. Limpezas geralmente desfazem uma configuração que aconteceu em ordem — abrir o arquivo, depois travá-lo — e desfazer tem que ir no sentido contrário: destravar, depois fechar. A ordem reversa faz de cada `defer` a imagem espelhada da linha acima dele.

---

Uma função que recebe uma closure tem um problema: ela não pode saber se a closure que lhe é entregue vai lançar um erro. Marcar a função com `throws` forçaria todo chamador a escrever `try`, mesmo os que passam uma closure inofensiva. O `rethrows` diz *eu lanço apenas se a closure que você me deu lançar*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Dentro do corpo você ainda escreve `try`, porque a chamada realmente pode falhar. No local da chamada o compilador olha para a closure que você passou:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // não precisa de try
```
A biblioteca padrão usa isso em todo lugar — `map`, `filter` e `sorted(by:)` são todos `rethrows` — que é o motivo de você nunca escrever `try` na frente de um `map` comum.

---

Um bloco `do` não se limita a um tipo de erro. Cada passo pode falhar à sua maneira, e cada falha ganha seu próprio `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
O primeiro `try` que lança encerra o bloco, então os passos seguintes nunca executam — o valor simplesmente nunca existiu. É isso que torna esse formato legível: o caminho feliz fica em uma linha reta no topo, e cada maneira de dar errado é listada embaixo.
