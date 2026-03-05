A tomada de decisao e necessaria quando queremos executar codigo apenas se uma determinada condicao for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o clima estiver bom.
Na programacao, podemos salvar uma variavel booleana `niceWeather` e executar a acao de brincar ao ar livre `if` (se) essa variavel for `true`, assim:
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Vamos continuar com o exemplo anterior.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
Vimos que a instrucao `if` executa o bloco de codigo apenas se a condicao for `true`.
Outra coisa importante a considerar sao as **chaves** `{}` que indicam um bloco de codigo.

---

Acabamos de ver como executar um bloco de codigo se uma condicao ocorrer, agora vamos ver como executar outro bloco de codigo se a primeira condicao falhar.
Vamos brincar ao ar livre se o clima estiver bom; caso contrario, ficamos em casa.
Em Swift podemos usar a instrucao `else`, assim:
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Vamos supor que temos outra condicao para verificar, como neste exemplo:
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
e a saida deste codigo e `the number is 3`.
Primeiro, vamos verificar se o numero e igual a 2, isso e falso.
Entao vamos para a segunda instrucao e verificamos se `num` e igual a 3, sendo verdadeiro executamos o bloco de codigo seguinte imprimindo `the number is 3`

---

Podemos adicionar quantas instrucoes `else if` quisermos, nao ha limites
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
e a saida deste codigo e `the number is 4`.

---

Tambem podemos aninhar uma instrucao condicional (`if`, `else if` ou `else`) dentro de outra instrucao condicional, para criar uma estrutura mais complexa.
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
e a saida deste codigo e `the number is 4`.

---

O operador condicional ternario e um operador especial com tres partes, que assume a forma `pergunta ? resposta1 : resposta2`.
E um atalho para avaliar uma de duas expressoes com base em se `pergunta` e verdadeira ou falsa.
Se `pergunta` for verdadeira, ele avalia `resposta1` e retorna seu valor; caso contrario, ele avalia `resposta2` e retorna seu valor.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
O codigo abreviado para o codigo acima e:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` recebe o valor de `a`, porque a condicao `a < b` era verdadeira

---

O _operador de coalescencia nula_ `a ?? b` desembrulha um opcional `a` se ele contiver um valor, ou retorna um valor padrao `b` se `a` for `nil`.
A expressao `a` e sempre de um tipo opcional.
A expressao `b` deve corresponder ao tipo armazenado dentro de a.
O operador de coalescencia nula e uma abreviacao para o codigo abaixo:
```swift
a != nil ? a! : b
```
