Arrays são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
Um array armazena múltiplos valores de um ou vários tipos e usa **índices** para distinguir esses valores.
Você pode atribuir itens a um array com uma expressão da forma:
```javascript
var arrayName = [item1, item2];
```

---

Você pode acessar um item individual do array pelo seu índice.
Um índice é como um endereço que identifica a posição do item no array.
O índice aparece diretamente após o nome do array, entre colchetes, assim:
```javascript
arrayName[index];
```
Os índices de arrays começam com `0`, **não** `1`! Você acessa o primeiro item de um array assim: `arrayName[0]`.
O segundo item em um array está no índice 1: `arrayName[1]`.

---

Um índice de array se comporta como qualquer outro nome de variável.
Ele pode ser usado para acessar e também para atribuir valores.
Você viu como acessar um índice de array assim:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
É assim que uma atribuição funciona:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Assim como strings, arrays possuem um **comprimento**.
O comprimento de um array é o número de itens que ele contém

---

Um array não precisa ter um comprimento fixo.
Você pode adicionar itens ao final de um array quando quiser!
Para adicionar um item a um array usamos a função `push`:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

Às vezes, você só quer acessar uma parte de um array.
Considere o seguinte código:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
Primeiro, criamos um array chamado `numbers`.
Depois, pegamos uma subseção do array e a armazenamos no array slice.
Fazemos isso definindo os índices que queremos incluir após o nome do array: `numbers.slice(1, 3)`.
Tenha em mente que o índice da direita é excluído

---

Em JavaScript podemos fatiar um array como quisermos!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
Se o seu fatiamento de array incluir o primeiro ou o último item de um array, o índice desse item não precisa ser incluído

---

Os elementos de um array podem ser de qualquer tipo.
```javascript
var arrayName = ["one", 2, true];
```
De fato, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas também podemos ter arrays com arrays!

---

Às vezes você precisa procurar um item em um array.
Em JavaScript podemos usar o método `indexOf()`:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
O código acima imprime o primeiro índice que contém a string `"Zac"`, `1` neste caso.
Também podemos inserir itens em um array em um índice específico, usando o método `splice()`:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
O código acima insere `"Ali"` no índice `1`, o que move tudo, após esse índice, uma posição para baixo.
O segundo valor `0` significa _deleteCount_ (contagem de exclusões); neste caso, não excluímos nenhum item do array; mas se tivéssemos especificado `1`, o valor `Zac` teria sido removido do array

---

Em JavaScript podemos percorrer um array de uma forma muito simples usando as palavras-chave `for..of`:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
Um nome de variável segue a palavra-chave `for`, ele receberá o valor de cada item do array por vez.
