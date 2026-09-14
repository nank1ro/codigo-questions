Ogni intero è memorizzato in memoria come una riga di **bit**, ognuno dei quali vale `0` oppure `1`. Il numero `12` viene memorizzato come `00001100` e il numero `10` come `00001010`.
Gli **operatori bit a bit** agiscono su quei singoli bit invece che sul numero nel suo complesso. L'operatore **AND** `&` confronta i due valori bit per bit e mantiene un `1` solo dove *entrambi* i bit valgono `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// prints "8"
```
I pattern di bit di solito si scrivono come letterali esadecimali come `0x0C`, perché ogni cifra esadecimale rappresenta esattamente quattro bit. Usa sempre tipi `unsigned` per lavorare con i bit e stampali con `%u`.

---

L'operatore **OR** `|` confronta i due valori bit per bit e mantiene un `1` dove *almeno uno* dei bit vale `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// prints "14"
```
`|` è il modo usuale per unire due pattern di bit in uno solo.

---

L'operatore **XOR** `^` (or esclusivo) mantiene un `1` solo dove i due bit sono *diversi*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// prints "6"
```
Ne deriva una proprietà utile: applicare lo stesso XOR due volte ridà il valore di partenza.

---

L'operatore **NOT** `~` prende un solo operando e inverte ognuno dei suoi bit: ogni `0` diventa `1` e ogni `1` diventa `0`.
Un `unsigned int` contiene 32 bit, quindi `~0x0Fu` li inverte tutti e 32 e produce un numero molto grande. Per tenere solo il byte che ti interessa, combina `~` con `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// prints "240"
```
`~` ha una precedenza più alta di `&`, quindi viene applicato per primo.
Non confondere `~` con il `!` logico: `!` guarda il valore nel suo complesso e risponde `0` oppure `1`, mentre `~` riscrive ogni bit.

---

L'operatore di **scorrimento a sinistra** `<<` sposta ogni bit di un certo numero di posti verso sinistra e riempie di zeri i posti liberati a destra:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// prints "12"
```
Scorrere a sinistra di `n` moltiplica il valore per 2 elevato a `n`.
Due errori rendono indefinito il comportamento di un programma C: scorrere a sinistra un valore negativo, e scorrere di una quantità maggiore o uguale alla larghezza del tipo (32 per `unsigned int`). Lavorare con valori **unsigned** ti mette al riparo dal primo.

---

L'operatore di **scorrimento a destra** `>>` sposta ogni bit verso destra; i bit che cadono dall'estremità destra vengono scartati. Su un valore unsigned i posti liberati a sinistra vengono riempiti con zeri:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// prints "3"
```
Scorrere a destra di `n` divide un valore unsigned per 2 elevato a `n`, scartando il resto.
Scorrere a destra un valore *negativo* non è portabile, ed è un motivo in più per lavorare sui bit con tipi `unsigned`.

---

Ogni operatore bit a bit binario ha una forma di **assegnazione composta** che aggiorna una variabile sul posto: `&=`, `|=`, `^=`, `<<=` e `>>=`.
```c
unsigned int x = 12;
x &= 10;  // same as x = x & 10;
x |= 1;   // same as x = x | 1;
x ^= 3;   // same as x = x ^ 3;
x <<= 1;  // same as x = x << 1;
x >>= 2;  // same as x = x >> 2;
```
Si leggono meglio che ripetere il nome della variabile e sono il modo usuale per cambiare i bit di una variabile flag.

---

Una **maschera** è un valore i cui bit selezionano la parte di un altro valore che ti interessa. Combinata con `&`, una maschera mantiene i bit che valgono `1` nella maschera e azzera tutti gli altri:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// prints "11"
```
`0x0F` mantiene i quattro bit più bassi, chiamati **nibble** basso, e `0xFF` mantiene gli otto bit più bassi, un intero byte.

---

I bit sono numerati a partire da `0`, iniziando dal più a destra, quindi `1u << n` è una maschera con solo il bit `n` acceso.
Per **impostare** un singolo bit, cioè accenderlo senza toccare gli altri, esegui l'OR del valore con quella maschera:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// prints "6"
```
Se il bit era già acceso il valore non cambia, il che rende l'impostazione di un bit sicura da ripetere.

---

Per **cancellare** un singolo bit, cioè spegnerlo, esegui l'AND del valore con l'*inverso* della maschera:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// prints "5"
```
`~(1u << 1)` è un valore con ogni bit acceso tranne il bit `1`, quindi l'AND lascia intatto tutto il resto.

---

Per **commutare** un singolo bit, cioè invertirlo qualunque sia il suo stato attuale, esegui lo XOR del valore con la maschera:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// prints "7"
```
Poiché lo XOR annulla se stesso, commutare lo stesso bit una seconda volta ridà il valore originale.

---

Per **verificare** un singolo bit, esegui l'AND del valore con la maschera e controlla se il risultato è diverso da `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // prints "1"
printf("%d\n", (value & (1u << 2)) != 0); // prints "0"
```
L'AND non produce `1`: produce `0` oppure la maschera stessa, che per il bit `3` è `8`. Ecco perché il risultato viene confrontato con `!= 0` invece di essere usato così com'è come risposta.

---

I **flag** sono maschere con nome, ognuna delle quali usa un bit diverso, e possono essere tutte memorizzate in una singola variabile. Si combinano con `|` e si leggono con `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// prints "1"
```
Un solo `unsigned int` può quindi portare 32 risposte sì/no indipendenti.

---

Prima del C23 non esisteva uno specificatore di formato che stampasse un numero in binario, e nemmeno letterali come `0b1010` erano C standard. Per mostrare i bit scrivi tu il ciclo: parti dal bit più alto e scendi fino al bit `0`, stampando ogni volta `(value >> i) & 1u`.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// prints "0101"
```
Scorrere il valore a destra di `i` porta il bit `i` nella posizione più a destra, dove `& 1u` lo isola.

---

Contare quanti bit di un valore valgono `1` è un classico ciclo sui bit: verifica il bit più basso con `& 1u`, aggiungilo a un contatore, poi scorri il valore di un posto a destra con `>>=` e ripeti finché non resta più niente.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count is 2
```
Il ciclo termina sempre, perché un valore unsigned diventa `0` dopo abbastanza scorrimenti a destra.

---

Diversi numeri piccoli vengono spesso impacchettati dentro un valore più grande. Per rileggerne uno, prima scorrilo a destra in modo che parta dal bit `0`, poi maschera tutto ciò che sta sopra:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// prints "18", the 0x12 byte
```
Prima scorrere e mascherare dopo è l'ordine da ricordare: la maschera descrive sempre il campo una volta che questo è arrivato in fondo.
