Być może zastanawiałeś się nad sytuacją, w której chciałbyś ponownie wykorzystać fragment kodu, ale z nieco innymi wartościami.
Zamiast przepisywać cały kod, znacznie lepiej jest zdefiniować funkcję, którą można następnie wielokrotnie używać.
W C używamy `return_type` poprzedzonego nazwą `function`, na przykład:
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

Nawiasy w __definicji funkcji__ nie muszą być puste, jeśli chcemy określić parametry

---

Czasami chcemy, aby funkcja __zwracała__ wartość.
Do tego służy słowo kluczowe `return`.

---

Funkcje mogą mieć wiele parametrów wejściowych, które zapisuje się wewnątrz nawiasów funkcji, oddzielone przecinkami.
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

W funkcjach możemy dodać _opcjonalny komentarz_ wyjaśniający, co dana funkcja robi:
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
Możemy użyć `//` dla komentarza jednoliniowego i `/* */` dla komentarza wieloliniowego
