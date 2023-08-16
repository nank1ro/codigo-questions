Avrai potuto considerare la situazione in cui vorresti riutilizzare un pezzo di codice, cambiando solo alcuni valori.
Invece di riscrivere l'intero codice, e' molto piu' pulito definire una funzione, che può poi essere utilizzata ripetutamente.
In C usiamo il `tipo di ritorno` seguito dal nome della funzione, per esempio:
```c
void saluta() {
    printf("Ciao!\n");
}

int main() {
    saluta();
    // stampa "Ciao!"
    return 0;
}
```

---

Le parentesi nella definizione di __funzione__ non devono essere vuote se vogliamo specificare i parametri

---

A volte vogliamo che una funzione __restituisca__ un valore.
Bene, possiamo usare la parola chiave `return`

---

Le funzioni possono avere parametri di ingresso multipli, che vengono scritti tra le parentesi della funzione, separati dalle virgole
```c
void saluta(char *nome, bool nuovo_utente) {
  char saluto[40] = "Ciao ";
  strcat(saluto, nome);
  if (nuovo_utente) {
    strcat(saluto, "! Benvenuto a bordo :)");
  }
  printf("%s\n", saluto);
}

int main() {
    // stampa "Ciao Luca"
    saluta("Luca", false);
    return 0;
};
```

---

Nelle funzioni possiamo aggiungere un _commento opzionale_ che spieghi il funzionamento di una funzione:
```c
/*
 * Funzione: ciao_mondo 
 * --------------------
 * stampa "Ciao, Mondo!" nella console.
 */
function ciao_mondo() {
    printf("Ciao, Mondo!\n");
}
```
Possiamo usare `//` per commentare una singola linea, mentre `/* */` per un commento multi-linea
