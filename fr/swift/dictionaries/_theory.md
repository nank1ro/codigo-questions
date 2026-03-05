**Les dictionnaires** sont similaires aux tableaux et aux tuples, mais vous accédez aux valeurs en recherchant une *clé* au lieu d'un index
Une clé peut être n'importe quelle chaîne ou nombre.
Les dictionnaires sont entre crochets, comme ceci :
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
Ceci est un dictionnaire appelé `dictionaryName` avec trois *paires clé-valeur*.
La clé `key1` pointe vers la valeur `1`, `key2` vers `2`, et ainsi de suite.

---

L'accès aux valeurs du dictionnaire par clé est tout comme l'accès aux valeurs du tableau par index :
```swift
// gets the age value from the user dictionary
user['age']
```

---

Comme les tableaux, les dictionnaires sont _mutables_.
Cela signifie qu'ils peuvent être modifiés après leur création (s'ils ne sont pas déclarés constants).
Un avantage de ceci est que nous pouvons ajouter de nouvelles _paires clé/valeur_ au dictionnaire après sa création comme ceci :
```swift
dictName[newKeyName] = newValue
```

---

La longueur `count` d'un dictionnaire est le nombre de _paires clé-valeur_ qu'il contient.
Chaque paire compte une seule fois, même si la valeur est un tableau. (C'est vrai : vous pouvez aussi mettre des tableaux à l'intérieur des dictionnaires !)

---

Parce que les dictionnaires sont mutables, ils peuvent être modifiés de plusieurs façons. Les éléments peuvent être supprimés d'un dictionnaire avec la méthode `removeValue(forKey:)` :
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
will remove the key `keyName` and its associated value from the dictionary.

---

What if we want to list all the keys of the dictionary?
Well, these's the `keys` property.

---

What if we want to list all the values of the dictionary?
Well, these's the `values` property.

---

Comme pour les tableaux, nous pouvons boucler entre les éléments du dictionnaire en utilisant les mots-clés `for..in`.
To get both the key and the value in the loop we don't have to specify any property:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

Nous pouvons également utiliser la propriété `isEmpty` que nous avons utilisée avec les tableaux pour déterminer si un dictionnaire est vide

---

Afin d'__ajouter__ ou de __modifier__ des valeurs dans un dictionnaire, nous pouvons également utiliser la méthode `updateValue(_:forKey:)`

---

Previously we saw how to remove a _key-value pair_ from the dictionary with the `removeValue()` method.
Nous pouvons également supprimer un élément en assignant à la clé la valeur `nil`
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
