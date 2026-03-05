Les **objets** sont similaires aux tableaux, mais vous accédez aux valeurs en cherchant une *clé* au lieu d'un index.
Une clé peut être n'importe quelle chaîne ou nombre.
Les objets sont enclos entre accolades, comme ceci :
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
C'est un dictionnaire appelé `objectName` avec trois *paires clé-valeur*.
La clé `key1` pointe vers la valeur `1`, `key2` vers `2`, et ainsi de suite.

---

Accéder aux valeurs du dictionnaire par clé est tout comme accéder aux valeurs du tableau par index :
```javascript
// gets the age value from the user dictionary
user['age'];
```

---

Comme les tableaux, les dictionnaires sont _mutables_.
Cela signifie qu'ils peuvent être modifiés après leur création (s'ils ne sont pas déclarés constant).
L'un des avantages de ceci est que nous pouvons ajouter de nouvelles _paires clé/valeur_ au dictionnaire après sa création comme ceci :
```javascript
dictName[newKeyName] = newValue;
```

---

Parce que les variables dictionnaires sont mutables, elles peuvent être modifiées de plusieurs façons.
Les éléments peuvent être supprimés d'un dictionnaire avec le mot-clé 'delete' :
```javascript
delete dictName[keyName];
```
supprimera la clé `keyName` et sa valeur associée du dictionnaire.

---

Et si nous voulions lister toutes les clés du dictionnaire ?
Eh bien, il y a la méthode `Object.keys()`.

---

Et si nous voulions lister toutes les valeurs du dictionnaire ?
Eh bien, il y a la méthode `Object.values()`.

---

Comme pour les tableaux, nous pouvons boucler entre les éléments du dictionnaire en utilisant la méthode `Object.entries()`.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
