Em Swift, podemos usar o sinal `+` para exibir duas ou mais strings juntas, assim:
```swift
print("Hello " + "Swift!") // imprime "Hello Swift!"
```

---

Mas usar o sinal `+` para adicionar um numero como '10' a uma string como `"friends"` produz um erro, pois sao tipos diferentes de valores

---

A interpolacao de strings nos permite exibir expressoes como adicionar uma string a um numero, sem nenhum erro.

---

Toda instrucao de interpolacao de string consiste em duas partes: o `\()` onde inserimos o numero ou variavel, e a string normal

---

Em seguida, adicionamos o tipo diferente de valor entre chaves para que ele seja exibido como uma unica instrucao de impressao. Como aqui, com `\(5)`

---

Inserir variaveis como `friends` entre os parenteses tambem exibe seus valores

---

Podemos usar parenteses para inserir valores quantas vezes quisermos dentro da interpolacao de string

---

Interpolacoes de string sao mais usadas em instrucoes de impressao, mas tambem podemos armazena-las em variaveis como strings normais.
