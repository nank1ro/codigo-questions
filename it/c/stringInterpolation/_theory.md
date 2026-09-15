Il C non ha l'interpolazione di stringhe: testo e valori vengono combinati da `printf` attraverso una **stringa di formato**, dove ogni specificatore `%` viene sostituito dall'argomento corrispondente. Gli specificatori più comuni sono:
```c
printf("%d\n", 42);      // stampa "42" (int, %i è lo stesso)
printf("%f\n", 2.5);     // stampa "2.500000" (double, 6 decimali per impostazione predefinita)
printf("%s\n", "hi");    // stampa "hi" (stringa)
printf("%c\n", 'A');     // stampa "A" (carattere singolo)
printf("%x\n", 255);     // stampa "ff" (int come esadecimale minuscolo)
printf("100%%\n");       // stampa "100%" (un segno di percentuale letterale)
```
Lo specificatore deve corrispondere al tipo dell'argomento: stampare un `double` con `%d` o un `int` con `%s` non converte il valore, stampa spazzatura o provoca un crash.

---

`sprintf` funziona esattamente come `printf`, ma invece di scrivere sullo schermo scrive il testo formattato in un array di `char`, chiamato **buffer**, seguito dal `'\0'` terminatore:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // stampa "3-7"
```
Il buffer deve essere dichiarato prima della chiamata e deve essere abbastanza grande per tutto il testo più il terminatore, altrimenti `sprintf` scrive oltre la sua fine.

---

Una funzione che costruisce una stringa di solito riceve il buffer come parametro e lo riempie con `sprintf`. L'array appartiene al chiamante, e dopo la chiamata può leggere il risultato:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // stampa "Hello, Ada!"
```
In questi esercizi `string.h` è già incluso sopra il tuo codice, quindi si può usare `strcmp` per confrontare il risultato.

---

`%x` stampa un intero in esadecimale con lettere minuscole, e `%X` fa lo stesso con lettere maiuscole. `%c` prende un codice di carattere intero e stampa il carattere che rappresenta, quindi `%c` con `65` stampa `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // stampa "1f 1F B"
```

---

Un numero tra `%` e la lettera imposta la **larghezza** minima del campo. Il valore viene riempito con spazi a sinistra, e i **flag** posti subito dopo il `%` cambiano il riempimento:
```c
printf("[%5d]\n", 42);  // stampa "[   42]" allineato a destra in 5 colonne
printf("[%-5d]\n", 42); // stampa "[42   ]" il flag - allinea a sinistra
printf("[%05d]\n", 42); // stampa "[00042]" il flag 0 riempie con zeri
printf("[%+d]\n", 42);  // stampa "[+42]" il flag + mostra sempre il segno
```
Un valore più lungo della larghezza non viene mai tagliato, il campo semplicemente si allarga.

---

Larghezza e flag funzionano con ogni specificatore, quindi `%02x` stampa un intero in esadecimale riempito con zeri fino a due cifre. È così che i colori vengono scritti come `#rrggbb`:
```c
printf("%02x\n", 5);   // stampa "05"
printf("%02x\n", 255); // stampa "ff"
```

---

Un punto seguito da un numero imposta la **precisione**. Per `%f` è il numero di decimali, arrotondato; per `%s` è il numero massimo di caratteri stampati:
```c
printf("%.2f\n", 3.14159);    // stampa "3.14"
printf("%.3s\n", "formatting"); // stampa "for"
```
Larghezza e precisione possono essere combinate: `%8.2f` stampa due decimali allineati a destra in 8 colonne.

---

La precisione è il modo consueto di controllare come appare un `double` in una stringa. Un rapporto come `0.425` diventa una percentuale moltiplicandolo per `100` e stampando un decimale seguito da `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out è "42.5%"
```

---

`sprintf` e `printf` **restituiscono** il numero di caratteri scritti, senza contare il `'\0'` terminatore. Questa è la lunghezza della stringa appena costruita, senza una chiamata separata a `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // stampa "3"
```

---

`sprintf` non sa quanto è grande il buffer. `snprintf` prende la dimensione del buffer come secondo argomento e non scrive mai più di `size - 1` caratteri più il `'\0'`, tagliando il testo se necessario. Il suo valore di ritorno è la lunghezza che il testo **completo** avrebbe avuto, quindi un risultato maggiore o uguale a `size` significa che l'output è stato troncato:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // stampa "formatt 10"
```
`sizeof buffer` dà la dimensione dell'array in byte, che per un array di `char` è il suo numero di elementi.

---

Confrontare il valore di ritorno di `snprintf` con la dimensione del buffer dice se tutto è entrato. Questo è il pattern sicuro per costruire stringhe di lunghezza sconosciuta:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out contiene solo i primi size - 1 caratteri di text
}
```

---

Una stringa può essere costruita in più passi scrivendo ogni pezzo subito dopo il precedente. Il valore di ritorno dice dove finisce il testo, quindi `buffer + n` è l'indirizzo del terminatore e la `sprintf` successiva può continuare da lì:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer è "Hello, world", n è 12
```
Sommare ogni valore di ritorno a `n` lo mantiene uguale alla lunghezza totale del testo costruito finora.

---

Le stringhe possono anche essere combinate senza una stringa di formato. `strcat` di `string.h` aggiunge una copia del suo secondo argomento alla fine del primo, che deve avere abbastanza spazio libero, e `strncat` aggiunge al massimo un dato numero di caratteri:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text è "Hi!!!"
strncat(text, "abcdef", 2); // text è "Hi!!!ab"
```
Entrambe aggiungono sempre il `'\0'` terminatore dopo i caratteri aggiunti.

---

Quando non c'è nulla da formattare, `puts` stampa una stringa seguita da un a capo. A differenza di `printf` non interpreta `%`, quindi il testo viene stampato esattamente come è scritto:
```c
puts("Done");      // stampa "Done" e un a capo
puts("50% off");   // stampa "50% off" e un a capo
printf("50% off"); // non definito: % off non è uno specificatore valido
```
`puts` è la scelta giusta per il testo fisso, e `printf` quando devono essere inseriti dei valori.

---

`strncat` è utile quando va aggiunta solo una parte di una stringa, o quando il pezzo aggiunto deve essere limitato a una lunghezza massima:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name è "file.ba"
```
Quando il limite è più grande della stringa, viene aggiunta l'intera stringa.

---

Mettendo tutto insieme: una riga di report combina un campo di testo allineato a sinistra, un separatore e un numero allineato a destra con un numero fisso di decimali, scritta con `snprintf` in modo da non superare mai il buffer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out è "Ada   |  9.5"
```
Finché ogni valore entra nella sua larghezza, tutte le righe hanno la stessa lunghezza, quindi le colonne risultano allineate quando le righe vengono stampate una sotto l'altra.
