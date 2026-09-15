Chaque entier est stocké en mémoire comme une rangée de **bits**, chacun valant `0` ou `1`. Le nombre `12` est stocké sous la forme `00001100` et le nombre `10` sous la forme `00001010`.
Les **opérateurs bit à bit** agissent sur ces bits individuels plutôt que sur le nombre dans son ensemble. L'opérateur **AND** `&` compare les deux valeurs bit par bit et garde un `1` uniquement là où *les deux* bits valent `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// affiche "8"
```
Les motifs de bits s'écrivent généralement sous forme de littéraux hexadécimaux tels que `0x0C`, car chaque chiffre hexadécimal correspond exactement à quatre bits. Utilisez toujours des types `unsigned` pour travailler sur les bits et affichez-les avec `%u`.

---

L'opérateur **OR** `|` compare les deux valeurs bit par bit et garde un `1` là où *au moins un* des bits vaut `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// affiche "14"
```
`|` est la façon habituelle de fusionner deux motifs de bits en un seul.

---

L'opérateur **XOR** `^` (ou exclusif) garde un `1` uniquement là où les deux bits sont *différents*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// affiche "6"
```
Une propriété utile en découle: appliquer le même XOR deux fois redonne la valeur d'origine.

---

L'opérateur **NOT** `~` prend un seul opérande et inverse chacun de ses bits: chaque `0` devient `1` et chaque `1` devient `0`.
Un `unsigned int` contient 32 bits, donc `~0x0Fu` inverse les 32 et produit un très grand nombre. Pour ne garder que l'octet qui vous intéresse, combinez `~` avec `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// affiche "240"
```
`~` a une priorité plus élevée que `&`, il est donc appliqué en premier.
Ne confondez pas `~` avec le `!` logique: `!` considère la valeur entière et répond `0` ou `1`, tandis que `~` réécrit chaque bit.

---

L'opérateur de **décalage à gauche** `<<` déplace chaque bit d'un certain nombre de rangs vers la gauche et remplit les rangs libérés à droite avec des zéros:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// affiche "12"
```
Décaler à gauche de `n` multiplie la valeur par 2 puissance `n`.
Deux erreurs rendent le comportement d'un programme C indéfini: décaler à gauche une valeur négative, et décaler d'un montant supérieur ou égal à la largeur du type (32 pour un `unsigned int`). Travailler avec des valeurs **unsigned** vous met à l'abri de la première.

---

L'opérateur de **décalage à droite** `>>` déplace chaque bit vers la droite; les bits qui tombent du bord droit sont perdus. Sur une valeur non signée, les rangs libérés à gauche sont remplis de zéros:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// affiche "3"
```
Décaler à droite de `n` divise une valeur non signée par 2 puissance `n`, en jetant le reste.
Décaler à droite une valeur *négative* n'est pas portable, ce qui est une raison de plus pour réserver le travail sur les bits aux types `unsigned`.

---

Chaque opérateur bit à bit binaire possède une forme d'**affectation composée** qui met à jour une variable sur place: `&=`, `|=`, `^=`, `<<=` et `>>=`.
```c
unsigned int x = 12;
x &= 10;  // équivaut à x = x & 10;
x |= 1;   // équivaut à x = x | 1;
x ^= 3;   // équivaut à x = x ^ 3;
x <<= 1;  // équivaut à x = x << 1;
x >>= 2;  // équivaut à x = x >> 2;
```
Elles se lisent mieux que de répéter le nom de la variable et constituent la façon habituelle de modifier les bits d'une variable de flags.

---

Un **masque** est une valeur dont les bits sélectionnent la partie d'une autre valeur qui vous intéresse. Combiné avec `&`, un masque garde les bits qui valent `1` dans le masque et met tous les autres à zéro:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// affiche "11"
```
`0x0F` garde les quatre bits les plus bas, appelé le **nibble** bas, et `0xFF` garde les huit bits les plus bas, un octet entier.

---

Les bits sont numérotés à partir de `0`, en commençant par le plus à droite, donc `1u << n` est un masque avec seulement le bit `n` activé.
Pour **activer** un seul bit, c'est-à-dire le mettre à `1` sans toucher aux autres, faites un OR de la valeur avec ce masque:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// affiche "6"
```
Si le bit était déjà activé, la valeur ne change pas, ce qui rend l'activation d'un bit sans risque à répéter.

---

Pour **effacer** un seul bit, c'est-à-dire le mettre à `0`, faites un AND de la valeur avec l'*inverse* du masque:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// affiche "5"
```
`~(1u << 1)` est une valeur avec tous les bits activés sauf le bit `1`, donc le AND laisse tout le reste intact.

---

Pour **basculer** un seul bit, c'est-à-dire l'inverser quel que soit son état actuel, faites un XOR de la valeur avec le masque:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// affiche "7"
```
Comme le XOR s'annule lui-même, basculer le même bit une seconde fois redonne la valeur d'origine.

---

Pour **tester** un seul bit, faites un AND de la valeur avec le masque et vérifiez si le résultat est différent de `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // affiche "1"
printf("%d\n", (value & (1u << 2)) != 0); // affiche "0"
```
Le AND ne produit pas `1`: il produit soit `0`, soit le masque lui-même, qui pour le bit `3` vaut `8`. C'est pourquoi le résultat est comparé avec `!= 0` au lieu d'être utilisé comme réponse directe.

---

Les **flags** sont des masques nommés, chacun utilisant un bit différent, qui peuvent tous être stockés dans une seule variable. Ils sont combinés avec `|` et relus avec `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// affiche "1"
```
Un `unsigned int` peut donc transporter 32 réponses oui/non indépendantes.

---

Avant C23, il n'existait aucun spécificateur de format qui affichait un nombre en binaire, et les littéraux comme `0b1010` n'étaient pas non plus du C standard. Pour montrer les bits, vous écrivez la boucle vous-même: parcourez du bit le plus haut jusqu'au bit `0` et affichez `(value >> i) & 1u` à chaque fois.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// affiche "0101"
```
Décaler la valeur vers la droite de `i` rangs amène le bit `i` à la position la plus à droite, où `& 1u` l'isole.

---

Compter combien de bits d'une valeur valent `1` est une boucle de bits classique: testez le bit le plus bas avec `& 1u`, ajoutez-le à un compteur, puis décalez la valeur d'un rang vers la droite avec `>>=` et répétez jusqu'à ce qu'il ne reste plus rien.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count vaut 2
```
La boucle se termine toujours, car une valeur non signée décalée vers la droite assez de fois devient `0`.

---

Plusieurs petits nombres sont souvent regroupés dans une valeur plus grande. Pour relire l'un d'eux, décalez-le d'abord vers la droite pour qu'il commence au bit `0`, puis masquez tout ce qui est au-dessus:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// affiche "18", l'octet 0x12
```
Décaler d'abord et masquer ensuite est l'ordre à retenir: le masque décrit toujours le champ une fois qu'il est arrivé en bas.
