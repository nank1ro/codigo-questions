Em Swift podemos usar o sinal `+` para exibir duas ou mais strings juntas, como:
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

Mas usar o sinal `+` para adicionar um numero como '10' a uma string como `"friends"` produz um erro, pois sao tipos diferentes de valores

---

A interpolacao de string nos permite exibir expressoes como adicionar uma string a um numero, sem qualquer erro.

---

Cada declaracao de interpolacao de string consiste em duas partes, a `\()` onde inserimos o numero ou variavel, e a string normal

---

Em seguida, adicionamos o diferente tipo de valor entre chaves para que seja exibido como uma unica declaracao de impressao. Como aqui, com `\(5)`

---

Inserir variaveis como `friends` entre parenteses exibe seu valor tambem

---

Podemos usar parenteses para inserir valores quantas vezes quisermos dentro da interpolacao de string

---

As interpolecoes de string sao melhor usadas em declaracoes de impressao, mas tambem podemos armazena-las em variaveis como strings normais.
