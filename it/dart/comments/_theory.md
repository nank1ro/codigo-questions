> Prima di iniziare, volevo dirti che sono molto felice di insegnare Dart.
Con questo messaggio colgo l'occasione per farti sapere che l'applicazione che stai usando è stata scritta proprio in Dart, utilizzando il framework Flutter. È quindi un onore per me poter condividere la mia esperienza in questo linguaggio.

Dart, come molti altri linguaggi di programmazione, ti permette di commentare il codice.
Questo ti permette di scrivere del testo accanto al codice.
I commenti vengono ignorati dal compilatore.

Dart supporta i commenti a linea singola, i commenti multi-linea ed i commenti sulla documentazione.

Ecco come scrivere un commento a linea singola:
```dart
// Questo è un commento. Non viene eseguito.
```

---

Puoi impilare i commenti a linea singola in modo da scrivere commenti _multi-linea_.
```dart
// Questo è un commento
// su molteplici linee
```

---

Puoi anche creare blocchi di commento, o commenti _multi-linea_.
I commenti _multi-linea_ iniziano con `/*` e finiscono con `*/`.
```dart
/*
Questo è un commento
su molteplici linee
*/
```

---

In aggiunta a questi due modi di scrivere i commenti, Dart include i _commenti alla documentazione_.

I _commenti alla documentazione_ sono commenti su più righe o su una sola riga che iniziano con `///` o `/**.` L'uso di `///` su righe consecutive ha lo stesso effetto di un commento di documentazione su più righe.

I _commenti alla documentazione_ sono molto utili perché permettono di generare la documentazione. 
Vorrai aggiungere i _commenti alla documentazione_ al tuo codice per rendere chiaro che cosa fa un particolare blocco di codice.

All'interno di un _commento alla documentazione_, l'analyzer (analizzatore del codice) risolve i nomi racchiusi in parentesi quadre come riferimenti ad altri elementi dell'API.
Utilizzando le parentesi quadre ci si può riferire a _classi_, _metodi_, _campi_, _variabili_, _funzioni_ e _parametri_.

Ecco un esempio:
```dart
/// Un camelide sudamericano addomesticato (Lama glama).
///
/// Come ogni altro animale, i lama devono mangiare,
/// quindi non dimenticare di dargli da mangiare con [feed] un po’ di [Food].
class Llama {
  String? name;

  /// Dà da mangiare al tuo lama [food].
  ///
  /// Il tipico lama mangia una balla di fieno a settimana.
  void feed(Food food) {
    // ...
  }

  /// Fa fare esercizio al tuo lama con un’[activity] per
  /// [timeLimit] minuti.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

Nella documentazione generata, `[feed]` diventa un link alla documentazione del metodo `feed` e `[Food]` diventa un link alla documentazione per la classe `Food`.
Mentre `[activity]` e `[timeLimit]` diventano un link alla documentazione dei parametri `activity` e `timeLimit` rispettivamente.
