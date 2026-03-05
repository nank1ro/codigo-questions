Nous savons comment répéter du code en utilisant une boucle `while`.
Comme ce programme répétant des instructions pour afficher `hello`
```c
int counter = 0;

while (counter < 5) {
    printf("Hello\n");
    counter++;
}
```
Mais nous pouvons faire la même chose avec des boucles `for` :
```c
for (int i = 0; i < 5; i++) {
    printf("Hello\n");
}
```

---

Dans une boucle `for` nous pouvons spécifier combien de fois nous voulons que notre boucle s'exécute

---

Nous pouvons utiliser `<` pour boucler jusqu'au nombre suivant exclus, ou `<=` pour boucler jusqu'au nombre suivant inclus

---

La variable appelée `i` est la variable compteur.
Nous pouvons lui donner le nom que nous voulons.
Elle compte à quelle répétition de la boucle nous sommes actuellement
