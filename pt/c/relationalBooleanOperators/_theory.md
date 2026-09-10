Os **operadores relacionais** comparam dois valores. O resultado não é um tipo especial: é um `int` que vale `1` quando a comparação é verdadeira e `0` quando não é. C tem seis deles:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Como o resultado é um `int`, ele é impresso com `%d` e pode ser armazenado em uma variável `int` como qualquer outro número.

---

Uma função pode retornar uma comparação diretamente: quem chama recebe `1` ou `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Escolher entre `>` e `>=` (ou `<` e `<=`) decide se o valor limite conta: `n >= 100` é `1` para `100`, `n > 100` é `0`.

---

O erro mais comum em C é escrever `=` onde `==` era o pretendido. Um único `=` é uma **atribuição**, e em C uma atribuição é uma expressão cujo valor é o valor que foi atribuído:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
O código com `=` ainda compila, então uma condição escrita como `if (x = 0)` define silenciosamente `x` como `0` em vez de testá-lo. A maioria dos compiladores imprime um aviso para isso: leia-o.

---

Os **operadores lógicos** combinam condições. O operador **e** `&&` dá `1` somente quando os dois lados são verdadeiros, o operador **ou** `||` dá `1` quando pelo menos um lado é verdadeiro:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
Em C, **qualquer valor diferente de zero conta como verdadeiro** e apenas `0` conta como falso, então `5 && 1` é `1` e `0 || -3` é `1`. O resultado de `&&` e `||` é sempre exatamente `1` ou `0`.

---

Uma variável que contém `0` ou um valor diferente de zero pode ser usada como condição por si só: `holiday` sozinho significa "holiday é diferente de zero", não é necessário escrever `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
O operador **não** `!` inverte uma condição: `!0` é `1` e `!` de qualquer valor diferente de zero é `0`.

---

Como `!` transforma qualquer valor diferente de zero em `0` e `0` em `1`, aplicá-lo duas vezes normaliza um valor para exatamente `0` ou `1`: `!!42` é `1`, `!!0` é `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
Isso é útil quando uma função retorna um número arbitrário diferente de zero e você quer um `1` limpo.

---

Desde o C99, o cabeçalho `stdbool.h` fornece o tipo `bool` e as constantes `true` (que é `1`) e `false` (que é `0`):
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Um `bool` ainda é um inteiro por baixo: ele é impresso com `%d`, e funciona com `&&`, `||` e `!` exatamente como o resultado de uma comparação. Ele apenas torna a intenção mais clara do que um `int` simples.

---

Uma função que responde a uma pergunta de sim/não deve retornar `bool`. Um parâmetro `bool` já é uma condição, então use-o diretamente como operando de `&&` ou `||`: escreva `age >= 18 && citizen`, não `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` já está incluído acima do seu código nestes exercícios.

---

`&&` e `||` usam **avaliação de curto-circuito**: eles param assim que o resultado é conhecido.
- com `&&`, se o lado esquerdo é `0` o lado direito nunca é avaliado
- com `||`, se o lado esquerdo é diferente de zero o lado direito nunca é avaliado

Isso permite que uma verificação à esquerda proteja uma operação perigosa à direita:
```c
int ok = count != 0 && total / count > 2;
```
Quando `count` é `0`, a divisão nunca é executada, então o programa não trava.

---

A avaliação de curto-circuito também pula chamadas de função. Em `1 || check()` a função `check` nunca é chamada, então qualquer efeito colateral que ela tenha, como atualizar um contador, não acontece.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Tenha isso em mente quando uma função do lado direito de `&&` ou `||` fizer algo do qual você depende.

---

Os operadores têm uma **precedência** que decide o que é calculado primeiro:
1. `!` é aplicado primeiro
2. depois as comparações relacionais `<`, `>`, `<=`, `>=`
3. depois as comparações de igualdade `==`, `!=`
4. depois `&&`
5. depois `||`

Assim, `a > 0 && a < 10` não precisa de parênteses, e `a && b || c` significa `(a && b) || c` porque `&&` tem ligação mais forte que `||`. Use parênteses para forçar um agrupamento diferente ou simplesmente para tornar a intenção legível.

---

Um `char` é um inteiro pequeno, então caracteres são comparados com os mesmos operadores. Compare com um literal de caractere entre aspas simples: `"a"` com aspas duplas é uma string, que não pode ser comparada dessa forma.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Caracteres consecutivos como `'0'`, `'1'`, ... `'9'` ou `'a'`, `'b'`, ... `'z'` têm códigos consecutivos, então uma verificação de intervalo em caracteres funciona exatamente como uma em números:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Não encadeie comparações como na matemática. `1 <= x <= 10` compila, mas é avaliado como `(1 <= x) <= 10`: a primeira comparação dá `0` ou `1`, e isso é então comparado com `10`, então a expressão inteira é sempre `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Sempre escreva ambas as comparações explicitamente e junte-as com `&&`.

---

Quando uma condição mistura `&&` e `||`, agrupe cada parte com parênteses mesmo quando a precedência já faria a coisa certa: a regra fica legível à primeira vista.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
O operador de resto `%` combina naturalmente com `==`: `n % 4 == 0` é `1` quando `n` é divisível por `4`.
