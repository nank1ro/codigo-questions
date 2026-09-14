Every integer is stored in memory as a row of **bits**, each one either `0` or `1`. The number `12` is stored as `00001100` and the number `10` as `00001010`.
**Bitwise operators** work on those single bits instead of on the number as a whole. The **AND** operator `&` compares the two values bit by bit and keeps a `1` only where *both* bits are `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// prints "8"
```
Bit patterns are usually written as hexadecimal literals such as `0x0C`, because each hex digit stands for exactly four bits. Always use `unsigned` types for bit work and print them with `%u`.

---

The **OR** operator `|` compares the two values bit by bit and keeps a `1` where *at least one* of the bits is `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// prints "14"
```
`|` is the usual way to merge two bit patterns into one.

---

The **XOR** operator `^` (exclusive or) keeps a `1` only where the two bits are *different*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// prints "6"
```
A useful property follows from this: applying the same XOR twice gives back the original value.

---

The **NOT** operator `~` takes a single operand and flips every one of its bits: each `0` becomes `1` and each `1` becomes `0`.
An `unsigned int` holds 32 bits, so `~0x0Fu` flips all 32 of them and produces a very large number. To keep only the byte you care about, combine `~` with `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// prints "240"
```
`~` binds tighter than `&`, so it is applied first.
Do not confuse `~` with the logical `!`: `!` looks at the whole value and answers `0` or `1`, while `~` rewrites every bit.

---

The **left shift** operator `<<` moves every bit a number of places to the left and fills the freed places on the right with zeros:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// prints "12"
```
Shifting left by `n` multiplies the value by 2 to the power of `n`.
Two mistakes make a C program undefined: left-shifting a negative value, and shifting by an amount equal to or greater than the width of the type (32 for `unsigned int`). Working with **unsigned** values keeps you clear of the first one.

---

The **right shift** operator `>>` moves every bit to the right; the bits that fall off the right end are discarded. On an unsigned value the freed places on the left are filled with zeros:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// prints "3"
```
Shifting right by `n` divides an unsigned value by 2 to the power of `n`, throwing away the remainder.
Right-shifting a *negative* value is not portable, which is one more reason to keep bit work on `unsigned` types.

---

Each binary bitwise operator has a **compound assignment** form that updates a variable in place: `&=`, `|=`, `^=`, `<<=` and `>>=`.
```c
unsigned int x = 12;
x &= 10;  // same as x = x & 10;
x |= 1;   // same as x = x | 1;
x ^= 3;   // same as x = x ^ 3;
x <<= 1;  // same as x = x << 1;
x >>= 2;  // same as x = x >> 2;
```
They read better than repeating the variable name and are the usual way to change the bits of a flag variable.

---

A **mask** is a value whose bits select the part of another value you care about. Combined with `&`, a mask keeps the bits that are `1` in the mask and zeroes all the others:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// prints "11"
```
`0x0F` keeps the lowest four bits, called the low **nibble**, and `0xFF` keeps the lowest eight bits, one whole byte.

---

Bits are numbered from `0`, starting at the rightmost one, so `1u << n` is a mask with only bit `n` turned on.
To **set** a single bit, that is to turn it on without touching the others, OR the value with that mask:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// prints "6"
```
If the bit was already on the value does not change, which makes setting a bit safe to repeat.

---

To **clear** a single bit, that is to turn it off, AND the value with the *inverse* of the mask:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// prints "5"
```
`~(1u << 1)` is a value with every bit on except bit `1`, so the AND keeps everything else untouched.

---

To **toggle** a single bit, that is to flip it whatever its current state, XOR the value with the mask:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// prints "7"
```
Because XOR undoes itself, toggling the same bit a second time gives the original value back.

---

To **test** a single bit, AND the value with the mask and check whether the result is different from `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // prints "1"
printf("%d\n", (value & (1u << 2)) != 0); // prints "0"
```
The AND does not produce `1`: it produces either `0` or the mask itself, which for bit `3` is `8`. That is why the result is compared with `!= 0` instead of being used as a plain answer.

---

**Flags** are named masks, each one using a different bit, that can all be stored inside a single variable. They are combined with `|` and read back with `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// prints "1"
```
One `unsigned int` can therefore carry 32 independent yes/no answers.

---

Before C23 there was no format specifier that printed a number in binary, and literals like `0b1010` were not standard C either. To show the bits you write the loop yourself: walk from the highest bit down to bit `0` and print `(value >> i) & 1u` each time.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// prints "0101"
```
Shifting the value down by `i` brings bit `i` into the rightmost place, where `& 1u` isolates it.

---

Counting how many bits of a value are `1` is a classic bit loop: test the lowest bit with `& 1u`, add it to a counter, then shift the value one place right with `>>=` and repeat until nothing is left.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count is 2
```
The loop always ends, because an unsigned value shifted right enough times becomes `0`.

---

Several small numbers are often packed inside one larger value. To read one of them back, first shift it down so it starts at bit `0`, then mask off everything above it:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// prints "18", the 0x12 byte
```
Shifting first and masking afterwards is the order to remember: the mask always describes the field once it has reached the bottom.
