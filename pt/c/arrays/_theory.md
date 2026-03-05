Arrays são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
Um array armazena múltiplos valores de um único tipo e usa **índices** para distinguir esses valores.
Você pode atribuir itens a um array com uma expressão da forma:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` é o tipo de dado que você usará para o array, por exemplo `int`, `double`, etc.
`array_name` é o nome da variável que armazena os itens.
`array_size` é o tamanho máximo que o array pode ter.
Finalmente, `item1` e `item2` são os valores que queremos salvar no array

---

Você pode acessar um item individual do array pelo seu índice.
Um índice é como um endereço que identifica a posição do item no array.
O índice aparece diretamente após o nome do array, entre colchetes, assim:
```
list_name[index];
```

Os índices do array começam com `0`, **não** `1`! Você acessa o primeiro item de um array assim: `list_name[0]`.
O segundo item de um array está no índice 1: `list_name[1]`.

---

Um índice de lista se comporta como qualquer outro nome de variável! Ele pode ser usado tanto para acessar quanto para atribuir valores.
Você viu como acessar um índice de lista assim:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Gets the value 5
```
É assim que uma atribuição funciona:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // prints the new value 1
```

---

Você pode calcular o tamanho em bytes de um array obtendo o `sizeof` do array, depois precisa dividir pelo tamanho de um elemento.
Isso funciona porque cada item no array tem o mesmo tipo e, portanto, o mesmo tamanho.
O *comprimento* resultante é o número de itens que ele contém

---

Um array em C deve ter um tamanho fixo.
Você não pode adicionar itens ao final de um array após declarar seu tamanho.

---

Na programação em C, você pode criar um array de arrays.
Esses arrays são conhecidos como arrays multidimensionais, por exemplo:
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
