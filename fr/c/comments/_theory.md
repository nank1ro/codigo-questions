Un **commentaire** est du texte à l'intérieur de votre code source qui est destiné aux personnes, pas au compilateur. Le compilateur jette les commentaires avant de construire le programme, vous pouvez donc les utiliser pour expliquer à quoi sert le code, laisser des rappels ou noter une décision.

Le type le plus courant est le **commentaire sur une seule ligne** : tout ce qui se trouve de `//` jusqu'à la fin de cette ligne est ignoré.
```c
// Greet the user
printf("Hello\n");
```
La première ligne ne fait rien lorsque le programme s'exécute ; seul le `printf` produit une sortie.

---

Comme le compilateur supprime complètement les commentaires, ajouter ou supprimer un commentaire ne change jamais ce que fait un programme. Seul le code qui n'est **pas** commenté s'exécute.

Cela fait de `//` un moyen rapide de désactiver une ligne de code sans la supprimer. Cela s'appelle **mettre en commentaire** :
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
La deuxième ligne est maintenant un commentaire, donc `total` reste `10`. En retirant le `//`, la ligne revient à la vie.

Mettre en commentaire est pratique pendant que vous expérimentez, mais pensez à nettoyer : du code qui reste commenté pendant longtemps ne fait que troubler la personne qui le lira ensuite.

---

Quand un commentaire a besoin de plus d'une ligne, le C propose le **commentaire multi-ligne** (aussi appelé commentaire de bloc) : il commence par `/*` et se termine par `*/`, et tout ce qui se trouve entre les deux est ignoré, y compris les sauts de ligne.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Un commentaire de bloc peut aussi être court et tenir sur une seule ligne : `/* like this */`.

Contrairement à `//`, qui s'arrête à la fin de la ligne, un commentaire `/*` s'arrête seulement au `*/`. Si vous oubliez de le fermer, le compilateur traitera tout le code suivant comme faisant partie du commentaire.

---

Les commentaires de bloc **ne s'imbriguent pas**. Le compilateur termine un commentaire `/*` au tout premier `*/` qu'il trouve, peu importe le nombre de `/*` qui le précèdent :
```c
/* outer /* inner */ still code */
```
Ici, le commentaire se termine juste après `inner`, donc `still code */` est compilé comme du code et produit une erreur.

Cela compte lorsque vous voulez mettre en commentaire un bloc qui contient déjà un commentaire `/* */` : le `*/` intérieur fermerait aussi votre commentaire extérieur trop tôt. Dans ce cas, placez plutôt `//` devant chaque ligne.

---

Un commentaire n'a pas besoin de sa propre ligne : il peut suivre le code sur la même ligne. C'est un **commentaire en fin de ligne**, et c'est un bon endroit pour une courte note sur cette instruction spécifique :
```c
int retries = 3; // give up after three attempts
```
`//` et `/* */` fonctionnent tous les deux comme commentaires en fin de ligne, mais attention avec `/*` : puisqu'il s'arrête seulement au `*/`, un `/*` non fermé à la fin d'une ligne avale les lignes qui suivent, et le programme ne compile plus.

---

Une utilisation courante des commentaires de bloc est le **commentaire d'en-tête** : un court bloc placé directement au-dessus d'une fonction qui dit ce qu'elle fait, ce que signifient ses paramètres et ce qu'elle retourne.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
La personne qui appelle `to_seconds` peut maintenant lire l'en-tête au lieu du corps. Gardez l'en-tête à côté de la fonction pour qu'ils soient mis à jour ensemble.

---

Le compilateur remplace chaque commentaire par un seul espace. Cela signifie qu'un commentaire `/* */` peut apparaître partout où un espace peut, même au milieu d'une instruction ou d'une expression :
```c
int area = width /* cm */ * height /* cm */;
```
C'est parfois utile pour étiqueter les opérandes ou les arguments d'un appel. Un commentaire `//` ne peut pas faire cela, parce qu'il mettrait en commentaire le reste de la ligne, y compris le code qui le suit.

---

Les programmeurs utilisent quelques mots-clés conventionnels au début d'un commentaire pour signaler du travail qui n'est pas terminé :

- `TODO` marque quelque chose qui doit encore être écrit
- `FIXME` marque du code qui est connu pour être faux et qui doit être corrigé

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Les éditeurs et les outils peuvent lister ces marqueurs, donc le travail en attente est facile à trouver. Une fois le travail fait, supprimez le marqueur : un `TODO` périmé est trompeur.

---

Un bon commentaire explique **pourquoi** le code fait quelque chose, pas **ce qu'**il fait. Le code montre déjà ce qui se passe ; le répéter avec des mots ajoute du bruit et devient obsolète dès que le code change :
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
La raison derrière les nombres est ce qu'un lecteur ne peut pas deviner :
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Si un commentaire ne fait que répéter la ligne en dessous, supprimez-le ou remplacez-le par la raison.

---

Mise en commun : utilisez `//` pour les notes courtes et les commentaires en fin de ligne, `/* */` pour les blocs plus longs et les commentaires d'en-tête, marquez le travail non terminé avec `TODO` ou `FIXME`, et supprimez le code mis en commentaire et les marqueurs périmés une fois qu'ils ne sont plus nécessaires.
