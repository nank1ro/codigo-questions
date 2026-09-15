Una `List` non contiene solo valori: contiene valori **di un solo tipo**. Il tipo viene scritto tra parentesi angolari subito dopo il nome della collezione:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` e `int` qui sono **argomenti di tipo**, e un tipo che ne accetta uno viene chiamato **generico**. La classe lista viene scritta una sola volta, e `List<String>` e `List<int>` sono due tipi diversi prodotti da essa.

Il vantaggio è che il compilatore sa cosa c'è dentro:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // ok: first è una String
```

---

`List` non è l'unica collezione generica. Una `Set` accetta un argomento di tipo, e una `Map` ne accetta **due**: uno per le chiavi e uno per i valori, in quest'ordine.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Un letterale di collezione vuoto non può essere dedotto dal suo contenuto, quindi scrivi gli argomenti di tipo sul letterale stesso:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Una volta che i tipi sono noti, tutto ciò che estrai dalla collezione ha già il tipo giusto: `ages['Ada']` è un `int?`, mai un valore misterioso.

---

Dart ha anche il tipo `dynamic`, che significa «qualsiasi cosa va bene». Una `List<dynamic>` accetta ogni valore, quindi sembra più comoda di una `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accettato
print(things.first.toUpperCase()); // accettato
```

Il rovescio della medaglia è che nulla viene controllato mentre scrivi il codice. Ogni chiamata su un valore `dynamic` viene risolta mentre il programma è in esecuzione, quindi un refuso come `things.first.toUpperCse()` compila felicemente ed esplode davanti a un utente.

I generics sono l'alternativa: un solo pezzo di codice che funziona con **qualsiasi** tipo, mentre ogni suo utilizzo viene comunque controllato per **un solo** tipo. Questo è il senso di tutto l'argomento.

---

Non sei limitato alle classi generiche fornite da Dart: puoi dichiararne di tue. Un **parametro di tipo** va tra parentesi angolari dopo il nome della classe, e da lì in poi è un tipo normale all'interno del corpo:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` è solo un segnaposto. Viene riempito quando una `Box` viene creata, in modo esplicito o per inferenza:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, dedotto dall’argomento
print(a.value + 1);      // 8, il compilatore sa che value è un int
```

La lettera non conta: `T` è una convenzione per «tipo», niente di più.

---

Una funzione può essere generica da sola, senza trovarsi in una classe generica. Il parametro di tipo va tra il nome e la lista dei parametri:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, qui T è String
print(firstOf([10, 20]));        // 10, qui T è int
```

Un solo corpo di funzione, controllato una volta, riutilizzato per ogni tipo. L'argomento di tipo di solito viene dedotto dagli argomenti, ma può essere scritto esplicitamente quando l'inferenza non ha nulla su cui lavorare:

```dart
final empty = firstOf<String>(<String>[]); // lancia, ma il tipo è chiaro
```

I metodi dentro una classe seguono esattamente la stessa regola.

---

Dentro una classe generica il parametro di tipo è visibile ovunque: nei campi, nei parametri del costruttore, nelle firme dei metodi e nei corpi dei metodi. Viene dichiarato una sola volta, accanto al nome della classe, e ogni membro può usarlo.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

È la creazione dell'oggetto a decidere il tipo: `Holder<String>('fig')` rende `item` una `String`, `Holder<int>(3)` lo rende un `int`.

---

Una classe può dichiarare più di un parametro di tipo, separati da virgole. `Map<K, V>` è l'esempio integrato: un tipo per le chiavi, uno per i valori.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

L'**ordine** fa parte del tipo: `Entry<String, int>` e `Entry<int, String>` sono tipi non correlati, e un valore di uno non può essere assegnato all'altro. I parametri di tipo possono anche essere riordinati in un tipo di ritorno, ed è così che un metodo può restituire una versione invertita dell'oggetto:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Con la null safety solida il punto interrogativo può trovarsi in due posti diversi, e significano due cose diverse:

```dart
Box<int?> a = Box(null); // una scatola che esiste e contiene un int nullable
Box<int>? b = null;      // nessuna scatola, ma se esiste contiene un int
```

In `Box<int?>` l'**argomento di tipo** è nullable, quindi `a.value` ha tipo `int?` e può essere `null`, mentre `a` in sé è sempre presente. In `Box<int>?` è la **variabile** a essere nullable, quindi `b` può essere `null` e ti serve `b?.value` o `b!.value` per raggiungere il suo interno.

Una `T` semplice significa `T extends Object?`, quindi un argomento di tipo nullable come `Box<int?>` è perfettamente legale.

---

La differenza conta appena usi il valore. Su una `Box<int?>` raggiungi il campo normalmente e poi gestisci il `null` al suo interno, mentre su una `Box<int>?` devi prima superare la scatola mancante:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, la scatola c’è, il suo contenuto è null

Box<int>? b = null;
print(b?.value ?? 0); // 0, manca proprio la scatola
```

Scrivere `b.value` su una `Box<int>?` non compila affatto: Dart si rifiuta di leggere un campo di qualcosa che potrebbe non esistere.

---

Una `T` senza vincolo potrebbe essere qualsiasi cosa, quindi dentro il corpo puoi usare solo ciò che ogni oggetto ha. Questo non compila:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Un **vincolo** risolve il problema. Scrivere `T extends num` dice che «`T` può essere solo un numero», e in cambio il corpo può usare tutto ciò che un `num` offre:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

Il vincolo viene controllato nel punto di chiamata: `half(4)` e `half(2.5)` vanno bene, `half('fig')` è un errore di compilazione. Un vincolo è una promessa in entrambe le direzioni: argomenti più ristretti in cambio di più potenza dentro.

---

La parola chiave per un vincolo è sempre `extends`, anche quando il vincolo è un'interfaccia anziché una superclasse. Non esiste `implements` in una lista di parametri di tipo.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Senza il vincolo, `a > b` non compilarrebbe: l'operatore di confronto appartiene a `num`, non a ogni oggetto.

---

Un vincolo può menzionare il parametro di tipo stesso. `Comparable<T>` è l'interfaccia di tutto ciò che sa confrontarsi con i propri simili, tramite `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // negativo: fig viene prima
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

Quindi `T extends Comparable<T>` si legge come «qualsiasi tipo che può essere confrontato con se stesso», che è esattamente ciò di cui ha bisogno una funzione di ordinamento o di massimo:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` e `DateTime` la soddisfano entrambe direttamente. `int` e `double` implementano `Comparable<num>`, quindi una lista di numeri viene semplicemente confrontata come `num`.

---

Lo stesso vincolo funziona altrettanto bene per l'elemento più piccolo: cambia solo il segno del confronto. `compareTo` restituisce un numero negativo quando il ricevente viene prima, quindi `item.compareTo(best) < 0` significa «questo è più piccolo».

---

Una classe generica può avere costruttori denominati e **factory** come qualsiasi altra classe, e il parametro di tipo è disponibile al loro interno. Un costruttore factory non crea l'oggetto in prima persona: esegue un corpo e ne restituisce uno, il che gli permette di scegliere, riutilizzare o costruire l'istanza nel modo che preferisce.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

L'argomento di tipo va sulla classe, non sul nome del costruttore: `Box<int>.first(...)`. Dentro la factory, `<T>[]` è una vera `List<T>` vuota, quindi una factory è il posto naturale per costruire un valore predefinito per un tipo che non conosci ancora.

---

Un parametro di tipo scritto senza vincolo non è affatto privo di vincoli: `class Box<T>` è la forma breve di `class Box<T extends Object?>`. È per questo che `Box<int?>` viene accettata, e per questo dentro la classe non puoi mai dare per scontato che `value` sia non-null.

Per vietare gli argomenti di tipo nullable, vincola il parametro con `Object`:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` è il tipo di tutto tranne `null`, quindi `T extends Object` si legge come «qualsiasi cosa, purché sia davvero presente».

---

Un `typedef` dà un nome a un tipo, e può avere parametri di tipo propri. Il motivo usuale è nominare una volta sola una famiglia di tipi funzione invece di scriverla per esteso a ogni uso:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` è solo un altro modo di scrivere `int Function(String)`, quindi i due sono intercambiabili. Il guadagno è la leggibilità: un parametro dichiarato come `Transform<I, O> transform` dice a cosa serve la funzione, mentre `O Function(I)` dice solo come è fatta.

Un typedef generico e una funzione generica si combinano naturalmente, con i parametri di tipo della funzione che riempiono quelli del typedef.
