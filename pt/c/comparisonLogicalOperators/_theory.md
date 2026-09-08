Os **operadores de comparação** comparam dois valores e produzem uma resposta: `1` quando a comparação é verdadeira e `0` quando não é.
O operador **igual** `==` verifica se dois valores são iguais, o operador **diferente** `!=` verifica se eles são diferentes:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// imprime "0"
printf("%d\n", a != b);
// imprime "1"
```
Cuidado: `==` (dois sinais) compara, enquanto um único `=` atribui um valor.

---

Os outros operadores de comparação verificam a ordem de dois valores:
- `<` menor que, `>` maior que
- `<=` menor ou igual a, `>=` maior ou igual a
```c
printf("%d\n", 3 < 5);  // imprime "1"
printf("%d\n", 5 >= 6); // imprime "0"
```
Uma função pode retornar uma comparação diretamente, pois o resultado é um `int` comum:
```c
int is_big(int n) {
    return n > 100;
}
```

---

Em C, o resultado de uma comparação não é um tipo especial: é um `int` cujo valor é exatamente `1` (verdadeiro) ou `0` (falso).
Isso significa que você pode armazená-lo em uma variável `int` como qualquer outro número:
```c
int n = 42;
int big = n > 100; // big é 0
```
Não há a palavra `true`/`false` na saída: `printf("%d", 2 == 2)` imprime `1`.

---

Os **operadores lógicos** combinam comparações. O operador **e** `&&` dá `1` somente quando ambos os lados são verdadeiros:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // imprime "1"
```
Não encadeie comparações como na matemática: `1 <= x <= 10` é avaliado como `(1 <= x) <= 10`, que compara um `0` ou `1` com `10` e é sempre verdadeiro.
Sempre escreva as duas comparações explicitamente e junte-as com `&&`.

---

O operador **ou** `||` dá `1` quando pelo menos um dos lados é verdadeiro, e `0` somente quando ambos os lados são falsos:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // imprime "1"
```
Cada lado deve ser uma comparação completa: `day == 6 || 7` não significa "6 ou 7" (você verá o motivo mais adiante).

---

O operador **não** `!` inverte um resultado: `!1` é `0` e `!0` é `1`.
Ele é colocado antes da expressão, então use parênteses para negar uma comparação inteira:
```c
int n = 5;
printf("%d\n", !(n > 3)); // imprime "0"
```
Sem os parênteses, `!n > 3` calcularia primeiro `!n` e depois compararia o resultado com `3`.

---

Os operadores lógicos não funcionam apenas com `0` e `1`: em C, **qualquer valor diferente de zero conta como verdadeiro** e apenas `0` conta como falso.
Assim, `5 && 1` é `1`, `0 || -3` é `1`, e `!` transforma qualquer valor diferente de zero em `0`:
```c
printf("%d\n", !7); // imprime "0"
printf("%d\n", !0); // imprime "1"
```
É por isso que `day == 6 || 7` é sempre verdadeiro: `7` sozinho já é um valor verdadeiro.

---

`&&` e `||` usam **avaliação de curto-circuito**: eles param assim que o resultado já é conhecido.
- com `&&`, se o lado esquerdo for `0`, o lado direito nunca é avaliado
- com `||`, se o lado esquerdo for verdadeiro, o lado direito nunca é avaliado

Isso permite proteger uma operação perigosa com uma verificação colocada à sua esquerda:
```c
int safe = divisor != 0 && value / divisor > 2;
```
Quando `divisor` é `0`, a divisão nunca é executada.

---

A avaliação de curto-circuito também pula chamadas de função: em `0 && check()` a função `check` nunca é chamada, então qualquer efeito colateral que ela tenha (como atualizar um contador) não acontece.

---

Os operadores têm uma **precedência** que decide o que é calculado primeiro:
1. `!` é aplicado primeiro
2. depois as comparações relacionais `<`, `>`, `<=`, `>=`
3. depois as comparações de igualdade `==`, `!=`
4. depois `&&`
5. depois `||`

Assim, `a > 0 && a < 10` não precisa de parênteses: ambas as comparações são calculadas antes do `&&`.
E `x == 1 || y == 2 && z == 3` significa `x == 1 || (y == 2 && z == 3)`, porque `&&` tem precedência maior que `||`.

---

Um `char` é um pequeno número inteiro, então caracteres podem ser comparados com os mesmos operadores.
Compare com um literal de caractere entre aspas simples:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // imprime "1"
```
Aspas duplas criariam uma string, que não pode ser comparada dessa forma.

---

Como caracteres são números, `<` e `>` comparam seus códigos, e caracteres consecutivos como `'a'`, `'b'`, `'c'` ou `'0'`, `'1'`, `'2'` têm códigos consecutivos.
Uma verificação de intervalo em caracteres, portanto, funciona exatamente como uma em números:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Um erro clássico em C é escrever `=` quando o pretendido era `==`. O código ainda compila, porque uma atribuição é uma expressão cujo valor é o valor atribuído:
```c
int x = 5;
if (x = 0) { ... } // atribui 0 a x, a condição é 0 (falso)
if (x = 3) { ... } // atribui 3 a x, a condição é 3 (verdadeiro)
```
A maioria dos compiladores avisa sobre isso, então leia os avisos quando uma condição se comportar de forma estranha.

---

A condição de um `if` é apenas uma expressão que é tratada como verdadeira quando diferente de zero, então comparações e operadores lógicos se encaixam naturalmente:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
Você também pode armazenar o resultado primeiro e testar a variável: `int ok = n > 0; if (ok) { ... }`.

---

Um loop `while` continua executando enquanto sua condição for diferente de zero, então uma comparação decide quando ele para:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// imprime 0, 1, 2
```
Escolher entre `<` e `<=` muda se o último valor é incluído ou não.

---

Desde o C99, o cabeçalho `stdbool.h` fornece o tipo `bool` e as constantes `true` (`1`) e `false` (`0`):
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
Por baixo dos panos, um `bool` ainda é um inteiro: imprimi-lo com `%d` mostra `1` ou `0`, e ele funciona com `&&`, `||` e `!` como qualquer resultado de comparação.
Usar `bool` deixa a intenção de uma função mais clara do que retornar um `int` comum.

---

Um parâmetro `bool` pode ser usado diretamente como operando de `&&` ou `||`, sem compará-lo a `true`: escreva `age >= 18 && citizen`, não `citizen == true`.

---

Quando uma condição mistura `&&` e `||`, adicione parênteses em torno de cada grupo mesmo quando a precedência já faria a coisa certa: isso torna a regra legível à primeira vista.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
