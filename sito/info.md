# Informazioni sul corso

## Orario e modalità delle lezioni

L'insegnamento corrisponde a 6 CFU, corrispondenti a 150 ore di studio
complessive; la parte frontale consta di 56 ore, ripartite *approssimativamente*
in 32 ore di **teoria** (corrispondenti a 4 CFU) e 24 ore di **esercitazioni**
(corrispondenti a 2 CFU); il che comporta circa 100 ore di studio individuale.

Le lezioni si svolgono il *mercoledì* e il *venerdì* dalle *10:30* in aula
*Magna Bertoni* (per informazioni consultate l'[apposito
sito](https://informatica.cdl.unimi.it/it/il-corso/luoghi-e-strutture)).

Il [diario](diario) riporta le date, gli argomenti e il materiale didattico di
ciascuna lezione.svolgono .

## Obiettivi dell'insegnamento

Se informalmente un *algoritmo* è un insieme di regole che consentono di
calcolare in un *numero finito* di passi *ben specificati* la soluzione di un
problema, la **programmazione** è in buona sostanza la disciplina che consente
di tradurre tale oggetto astratto in una sequenza concreta di *istruzioni* e di
*definizioni dei dati* (in un assegnato linguaggio di programmazione) che
rendano il calcolo suscettibile di esecuzione da parte di un dispositivo
automatico (come ad esempio un computer).

L'insegnamento
[Programmazione](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/programmazione-0) 
del primo anno fornisce le prime competenze relative a tale disciplina, esse verranno
accresciute negli anni successivi sia rispetto alla capacità di trattare
*problemi più complessi* (ad esempio negli insegnamenti di 
[Algoritmi e strutture dati](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/algoritmi-e-strutture-dati-0), 
[Ricerca operativa](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/ricerca-operativa), 
[Linguaggi formali e automi](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/linguaggi-formali-e-automi)…) 
o più *specifici*
(in 
[Basi di dati](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/basi-di-dati-0), 
[Sistemi
operativi](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/sistemi-operativi), 
[Reti di calcolatori](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/reti-di-calcolatori-0)…) 
che di considerare *programmi più complessi* per dimensione e ciclo di vita (in
[Ingegneria del software](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/ingegneria-del-software)…).

L'insegnamento [Programmazione
II](https://www.unimi.it/it/corsi/insegnamenti-dei-corsi-di-laurea/2025/programmazione-ii)
ha l'obiettivo di accrescere le competenze acquisite nel corso del primo anno
tramite l'ampliamento della *ricchezza espressiva* del linguaggio (o
*paradigma*) di programmazione; facendo tesoro della conoscenza del paradigma
*imperativo* appresa tramite l'uso del linguaggio *Go*, l'insegnamento introduce
il paradigma *object oriented* (assieme alle relative tecniche di specificazione
e progetto) attraverso il linguaggio *Java* (e non solo).

## Risultati di apprendimento attesi

A seguito del superamento dell'esame, lo studente conosce le principali nozioni
riguardanti l'*object orientation* quali:

* astrazione (tramite procedure e tipi di dati),
* incapsulamento (tramite classi concrete/astratte e interfacce),
* estensibilità (per ereditarietà, o composizione),
* polimorfismo (e tipi generici).

Inoltre lo studente è in grado di:

* definire e comprendere le specifiche (quanto meno informali) di un programma non banale,
* progettare una gerarchia di classi Java in accordo a tali specifiche,
* documentare il codice in modo ragionevole,
* validare (attraverso semplici *test*) il comportamento del codice prodotto.

## Argomenti trattati

L'insegnamento è incentrato attorno alle tematiche del progetto, realizzazione
ed analisi di programmi secondo il paradigma *object oriented*. A tal fine il
corso prevede sia una trattazione più astratta e principiata dell'argomento, che
una presentazione più pratica e concreta, svolta attraverso esempi basati sul
linguaggio di programmazione Java.

Riguardo ai principi, sono introdotti e discussi:

* l'uso di **astrazioni** di vario livello (come i metodi, i tipi di dato astratti, l'iterazione esterna, l'estensione),
* alcuni **strumenti concettuali** per ragionare su tali astrazioni (come l'*invariante di rappresentazione*, la *funzione di astrazione*, le *pre-*/*post-condizioni*, gli *effetti collaterali*, l'*induzione sui tipi di dato*…),
* alcuni **criteri di valutazione della qualità** del progetto di codice *object oriented* (come l'*incapsulamento*, il *data hiding*, la *manutenibilità*, il *riuso* e l'*estendibilità*),
* alcune tecniche di *verifica* e di *debugging*.

Riguardo al linguaggio Java, sono presentati i seguenti aspetti del linguaggio:

* costrutti di controllo del flusso (sequenza, iterazione e selezione),
* tipi di dati elementari,
* funzioni (metodi statici),
* classi (concrete, astratte ed interne),
* interfacce (con metodi di default),
* ereditariertà e polimorfismo,
* tipi generici (uso e cenni alla progettazione e realizzazione, vincoli di tipo e wildcard).

### Programma dettagliato

Rispetto alla bibliografia e al materiale didattico, si precisa che
costituiscono argomenti del corso:

* per quanto concerne il libro di testo [Program Development in Java:
  Abstraction, Specification, and Object-Oriented Design](http://www.informit.com/store/program-development-in-java-abstraction-specification-9780768684698) i capitoli dall'1 al 9;

* per quanto concerne il libro di testo [Effective Java](http://www.informit.com/store/effective-java-9780134685991)
  i capitoli 2, 3, 4, 5 (eccetto gli *item* 32 e 33), 8 (eccetto gli *item* 53 e 55), 9 (eccetto l'*item* 66), 10;

* per quanto concerne  [The Java™
  Tutorials](https://dev.java/learn/), le sezioni
    * "Running Your First Java Application" limitatamente a [Getting Started
      with Java](https://dev.java/learn/getting-started/);
    * "Getting to Know the Language", limitatamente a [Java Language Basics](https://dev.java/learn/language-basics/), [Objects,
      Classes, Interfaces, Packages, and inheritance](https://dev.java/learn/oop/),
      [Classes and Objects](https://dev.java/learn/classes-objects/),
      [Numbers and strings](https://dev.java/learn/numbers-strings/),
      [Inheritance](https://dev.java/learn/inheritance/),
      [Interfaces](https://dev.java/learn/interfaces/),
      [Generics](https://dev.java/learn/generics/) e
      [Packages](https://dev.java/learn/packages/);
    * "Mastering the API", limitatamente a [The Collections
      Framework](https://dev.java/learn/api/collections-framework/).


:::{note}
:class: warnadmonition

Si veda anche la sezione "Materiale di supporto" in fondo a questa pagina:
alcuni dei contenuti citati in tale sezione potranno costituire il *punto di
partenza per alcune domande durante l'esame orale*, per cui *si raccomanda di
prenderne visione*! 
:::

## Prerequisiti

Di seguito sono elencate alcune conoscenze preliminari che è bene aver acquisito
*in modo solido* prima di apprestarsi a seguire le lezioni:

* programmazione [il corso di "Programmazione" è formalmente **propedeutico**],
* tecniche di dimostrazione di base [dagli insegnamenti di "Matematica del
  discreto" e/o "Logica matematica"];
* aspetti elementari dei linguaggi formali [dal corso "Linguaggi formali e
  automi"].

## Modalità di valutazione

L'insegnamento non prevede prove in itinere.

La prova finale è costituita da una **progetto individuale** (da svolgere a
casa) che verte sulla progettazione e sviluppo di un software secondo delle
*specifiche* assegnate, seguito da una **discussione orale**.

Attraverso tali prove il candidato deve dimostrare:

* la conoscenza delle definizioni e delle nozioni fondamentali riguardo agli
  aspetti di orientazione agli oggetti e programmazione,
* la capacità di applicare tale conoscenza a un semplice caso concreto tramite
  lo sviluppo di frammenti di codice.

### Dettagli pratici

Per ciascun appello, **alla chiusura delle iscrizioni** su SIFA/UNIMIA (che di
norma avviene una settimana prima della data dell'appello), gli studenti
*regolarmente iscritti* riceveranno per email le informazioni su come *reperire
la descrizione del progetto* (costituita da una cartella compressa contenente le
specifiche, i file di test e le configurazioni necessarie a compilare, eseguire
e testare il codice e la documentazione).

Entro il **mezzogiorno della data dell'appello** gli studenti dovranno
*consegnare* la propria *soluzione* (esclusivamente nel *formato descritto nel
progetto*) tramite il [servizio di upload](https://upload.di.unimi.it/) del
Dipartimento di Informatica.

Nei giorni seguenti (generalmente entro una settimana), gli studenti che
potranno accedere all'orale riceveranno per email le informazioni su come
*prenotare tempestivamente* la data ed ora del colloquio (che si terranno in
base alle disponibilità del docente, generalmente entro due settimane). 

La mancata consegna del progetto nei termini stabiliti, la mancata prenotazione
della data del colloquio entro la data indicata, o l'assenza dal colloquio,
comporteranno il **mancato superamento** dell'esame.

### Criteri di valutazione

Per maggior chiarezza, i criteri di valutazione della *prova pratica* sono
ispirati al contenuto di tutte le lezioni ed il materiali didattici elencati nel
diario, con particolare riferimento alle sezioni

* 5.7 Reasoning about Data Abstractions
* 5.8 Design Issues
* 5.9 Locality and Modifiability
* 9.2 Some Criteria for Specifications

del libro di testo "Program Development in Java: Abstraction, Specification, and
Object-Oriented Design".

Per quanto concerne l'*orale*, un'ottima **traccia** ai concetti su cui verterà
la discussione è costituita dal contenuto delle *Sidebar* presenti nelle parti
comprese nel programma del libro di testo medesimo.

## Bibliografia

I libri di testo (ossia il cui uso *non è facoltativo*) del corso sono:

* Barbara H. Liskov, John Vogel Guttag (2000)
  [Program Development in Java: Abstraction, Specification, and Object-Oriented Design](http://www.informit.com/store/program-development-in-java-abstraction-specification-9780768684698) *Addison-Wesley Professional*,

* Joshua Bloch (2017),
  [Effective Java](http://www.informit.com/store/effective-java-9780134685991), *Addison-Wesley Professional*.

Si consulti anche la sezione sul [linguaggio Java](strumenti.md#il-linguaggio-java) della pagina sugli
[strumenti](strumenti) per avere informazioni sulla documentazione specifica del
linguaggio.

Le letture consigliate, utili ad approfondire e migliorare la propria competenza
generale riguardo alla programmazione, sono:

* Brian W. Kernighan, Rob Pike (1999)
  [The Practice of Programming](http://www.informit.com/store/practice-of-programming-9780201615869) *Addison-Wesley Professional Computing Series*

* Steve McConnel (2004)
  [Code Complete](http://www.informit.com/store/code-complete-9780735619678) *Microsoft Press*

### Materiale di supporto

Materiale di supporto molto utile può essere reperito a partire da:

* gli [handout](https://github.com/prog2-unimi/handouts), 
* le [note](https://github.com/prog2-unimi/notes) e da
* i [temi d'esame svolti](https://prog2unimi-temi-svolti.netlify.app/).

I contenuti di questo materiale potranno costituire il *punto di partenza per
alcune domande durante l'esame orale*, per cui **si raccomanda di prenderne
visione** per tempo.
