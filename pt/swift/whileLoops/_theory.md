Frequentemente na programação, precisamos repetir um bloco de código, por exemplo:
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Isso produz a seguinte saída:
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instruções longas gastaríamos muito tempo escrevendo o código, mas felizmente podemos usar loops.
Vamos aprender o loop `while`, obtendo a mesma saída acima.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
Então criamos uma variável `count` atribuindo `2`, o valor inicial.
Depois usamos a instrução `while` que executará o bloco de código até que a condição `count <= 5` seja `true`.
Dentro do bloco de código, não devemos esquecer de adicionar a linha `count += 1`.
Ela incrementa o valor de `count`, caso contrário, nosso loop será infinito

---

Para controlar as vezes que um loop `while` repete, começamos com uma variável definida como um número.
Chamamos essa variável de variável contadora

---

Depois, usamos uma comparação na condição para comparar a variável `counter` com um número

---

Dentro do bloco de código, para parar o loop `while`, incrementamos a variável `counter`

---

A ordem em que você escreve o código afeta a saída

---

Em Swift também temos a variação **repeat-while** do loop `while`.
Ela executa uma única passagem pelo bloco de loop primeiro, _antes_ de considerar a condição do loop.
Depois continua a repetir o loop até que a condição seja `false`.
O loop __repeat-while__ em Swift é análogo a um loop __do-while__ em outras linguagens
