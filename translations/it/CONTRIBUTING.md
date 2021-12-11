# Benvenuto

#### _Leggi questo in altre lingue:

<kbd>[<img title="English" alt="English" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/gb.svg" width="22"> English](../../CONTRIBUTING.md)</kbd>

Grazie per investire il tuo tempo nel contribuire al nostro progetto!
Qualsiasi contributo da voi dato si rifletterà sull'[App Codigo](https://codigo.bestofcode.dev)

## Guida per i nuovi contributori

Ecco alcune risorse per aiutarti a iniziare a contribure nell'open source (disponibili in lingua inglese):

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

## Iniziamo

Puoi contribuire in molti modi alle domande di codigo:
- aggiungendone di nuove
- creando una issue per un bug
- correggendo bug e refusi

## Crea una issue

Quando crei una issue, per favore fornisci quanti più dettagli possibili sul problema che stai riscontrando.
Se puoi fornisci anche uno screenshot dell'app che mostra il problema.

> Se riscontri un problema in un esercizio specifico all'interno dell'app, clicca sull'icona di segnalazione in alto a destra, in questo modo verrai automaticamente reindirizzato a GitHub e il titolo con il percorso dell'esercizio verrà già fornito per te.

## Creare una pull request (comunemente chiamata PR)

Quando crei un PR, devi completare il template.
Questo ti chiederà di fornire i dettagli delle modifiche con una descrizione, un link ad una issue ed il tipo di cambiamento:
- [ ] ✨ Nuova feature (cambiamento non radicale che aggiunge funzionalità)
- [ ] 🛠️ Bug fix (modifica non radicale che risolve un problema)
- [ ] ❌ Breaking change (correzione o caratteristica che causerebbe un cambiamento della funzionalità esistente)
- [ ] 🧹 Rifattorizzazione del codice
- [ ] 📝 Documentazione
- [ ] 🗑️ Chore 

Per poter revisionare la tua PR ci sono alcuni requisiti:
1. Tutti i controlli (checks) di GitHub devono passare
2. Assegna a te stesso la PR e chiunque ti abbia aiutato.
3. Aggiungi l'etichetta appropriata (bug, chore, question, feature)
4. Segna la tua PR come pronta (ready)
5. Aggiungi @nank1ro come revisore

__Riesaminerò la tua PR solo dopo che tutti questi passaggi sono stati completati__

> 1. Maggiori informazioni sui controlli (checks) su Github

<img src="/local_assets/github-checks.png"/>

Questi sono i controlli di GitHub, ognuno di questi "semafori" deve essere verde.
Se il controllo `validate_exercises` fallisce, clicca sul pulsante destro __Details__

Scorri verso il basso fino a trovare gli errori, come in questa immagine:

<img src="/local_assets/failed-assert.png"/>

Leggi l'errore e correggilo seguendo le istruzioni fornite.

Il _percorso relativo all'esercizio_ ti dice in quale esercizio si è verificato l'errore.

## Exercise Composition

Per comporre un esercizio per farlo funzionare nell'app, usiamo il seguente ordine:

<img src="/local_assets/exercise-composition.svg" width="180"/>

Non tutte queste sezioni sono richieste, questo varia in base al tipo di esercizio.

## Add new questions

Per aggiungere nuove domande suggeriamo di iniziare usando i nostri template predefiniti, che puoi trovare nella sezione
/translations/{langCode}/templates

Attualmente Codigo supporta quattro tipi di esercizi:
- esegui il codice (codice: 1)
- riempi gli spazi vuoti (codice: 2)
- scegli la/e risposte (codice: 3)
- ordina il codice (codice: 4)

Nei modelli si può trovare il linguaggio di programmazione, seguito dal codice del linguaggio, per esempio:

c_2 => Un esercizio di _riempimento di spazi vuoti_ nel linguaggio di programmazione C

Puoi copiare un modello e sostituire tutto il testo con il tuo nuovo esercizio, così non dovrai riscrivere la struttura dell'esercizio da zero ogni volta.

Se stai scrivendo un esercizio di tipo __esegui il codice__ (codice: 1), puoi anche usare la CLI.
Per maggiori informazioni leggi il [CLI Readme.md](/cli/README.md)

## Q&A

<details>
  <summary>Posso aggiungere un nuovo linguaggio di programmazione?</summary>
Sì, è possibile aggiungere un nuovo linguaggio di programmazione, ma questo richiede un sacco di lavoro perché comporta anche una nuova release dell'app.

Inoltre, non tutti i linguaggi di programmazione sono supportati dal nostro backend.
	Per ora ho intenzione di aggiungere `Kotlin` e `Go`.
	
Tutti i linguaggi di programmazione che il nostro backend supporta sono:

- Assembly (NASM 2.14.02)
- Bash (5.0.0)
- Basic (FBC 1.07.1)
- C (Clang 7.0.1)
- C++ (Clang 7.0.1)
- C (GCC 7.4.0)
- C++ (GCC 7.4.0)
- C (GCC 8.3.0)
- C++ (GCC 8.3.0)
- C (GCC 9.2.0)
- C++ (GCC 9.2.0)
- Clojure (1.10.1)
- C# (Mono 6.6.0.161)
- COBOL (GnuCOBOL 2.2)
- Common Lisp (SBCL 2.0.0)
- D (DMD 2.089.1)
- Elixir (1.9.4)
- Erlang (OTP 22.2)
- Executable
- F# (.NET Core SDK 3.1.202)
- Fortran (GFortran 9.2.0)
- Go (1.13.5)
- Groovy (3.0.3)
- Haskell (GHC 8.8.1)
- Java (OpenJDK 13.0.1)
- JavaScript (Node.js 12.14.0)
- Kotlin (1.3.70)
- Lua (5.3.5)
- Multi-file program
- Objective-C (Clang 7.0.1)
- OCaml (4.09.0)
- Octave (5.1.0)
- Pascal (FPC 3.0.4)
- Perl (5.28.1)
- PHP (7.4.1)
- Plain Text
- Prolog (GNU Prolog 1.4.5)
- Python (2.7.17)
- Python (3.8.1)
- R (4.0.0)
- Ruby (2.7.0)
- Rust (1.40.0)
- Scala (2.13.2)
- SQL (SQLite 3.27.2)
- Swift (5.2.3)
- TypeScript (3.7.4)
- Visual Basic Net (vbnc 0.0.0.5943)
</details>

<details>
  <summary>Non trovo informazioni su qualcosa</summary>
	Apri una issue, e se questo può essere utile ad altri, lo aggiungerò al file CONTRIBUTING o al README
	</details>
