Em Swift, podemos usar o sinal `+` para exibir duas ou mais strings juntas, assim:
```swift
print("Hello " + "Swift!") // imprime "Hello Swift!"
```

---

Mas usar o sinal `+` para adicionar um número como '10' a uma string como `"friends"` produz um erro, pois são tipos diferentes de valores

---

A interpolação de strings nos permite exibir expressões como adicionar uma string a um número, sem nenhum erro.

---

Toda instrução de interpolação de string consiste em duas partes: o `\()` onde inserimos o número ou variável, e a string normal

---

Em seguida, adicionamos o tipo diferente de valor entre chaves para que ele seja exibido como uma única instrução de impressão. Como aqui, com `\(5)`

---

Inserir variáveis como `friends` entre os parênteses também exibe seus valores

---

Podemos usar parenteses para inserir valores quantas vezes quisermos dentro da interpolacao de string

---

Interpolações de string são mais usadas em instruções de impressão, mas também podemos armazená-las em variáveis como strings normais.
