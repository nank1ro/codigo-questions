Vous avez peut-être considéré la situation où vous aimeriez réutiliser un morceau de code, juste avec quelques valeurs différentes.
Au lieu de réécrire tout le code, il est beaucoup plus propre de définir une fonction, qui peut alors être utilisée à plusieurs reprises.
En C, nous utilisons le `return_type` suivi du nom de la `function`, par exemple :
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

Les parenthèses dans la __définition de fonction__ ne doivent pas être vides si nous voulons spécifier des paramètres

---

Parfois, nous voulons qu'une fonction __retourne__ une valeur.
Eh bien, il y a le mot-clé `return`.

---

Les fonctions peuvent avoir plusieurs paramètres d'entrée, qui sont écrits entre les parenthèses de la fonction, séparés par des virgules.
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

Dans les fonctions, nous pouvons ajouter un _commentaire optionnel_ qui explique ce que la fonction fait :
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
Nous pouvons utiliser `//` pour un commentaire d'une seule ligne et `/* */` pour un commentaire multiligne
