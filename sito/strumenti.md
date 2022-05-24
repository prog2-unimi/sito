# Strumenti e materiale di supporto

Questa pagina contiene alcune indicazioni circa il [linguaggio di
programmazione](#java) e gli strumenti di [supporto allo sviluppo](#strumenti-di-supporto)
adottati per il corso.

Si osserva che, data la *maturità culturale* che ci si attende dagli studenti
che frequentano un insegnamento del secondo anno, il docente **non intende
fornire alcun supporto** all'installazione, configurazione e uso pratico degli
strumenti qui descritti.

## Java

Sebbene a partire dalle versioni più recenti le differenze nel linguaggio siano
minime e il corso non coprirà le *feature* più moderne, è comunque consigliabile
usare l'ultima versione coperta da [long term
support](https://en.wikipedia.org/wiki/Long-term_support) (LTS) del Java
Development Kit (JDK), ossia il **Java SE Development Kit 17**.  Si consiglia
pertanto di installare la **versione ufficiale Oracle**, disponibile
gratuitamente sia con licenza
[proprietaria](https://www.oracle.com/technetwork/java/javase/downloads/) che
[open source](https://openjdk.java.net/).

Oltre ai libri di testo, è di fondamentale importanza consultare la
[documentazione](https://docs.oracle.com/en/java/javase/17/), in particolare
quella delle [API](https://docs.oracle.com/en/java/javase/17/docs/api/) delle
librerie incluse nel JDK. Possono risultare molto utili anche i [vari](https://docs.oracle.com/javase/tutorial/) [tutorial](https://dev.java/learn/) ufficiali di Oracle.

## Strumenti di supporto

Sebbene sia possibile usare un IDE, durante il corso (e durante l'esame) verrà
utilizzato l'editor [Visual Studio Code](https://code.visualstudio.com/) con il
relativo [supporto per Java](https://code.visualstudio.com/docs/languages/java);
chi preferisce può installare una [versione open](https://vscodium.com/).
Evidentemente ciascuno può adoperare (sul proprio computer) l'editor che trova
più comodo.

Per gli studenti interessati, ma sottolineando che *non è assolutamente materia
dell'insegnamento* e *non è assolutamente richiesto per il superamento dell'esame*,
è possibile usare uno strumento di [build automation](https://en.wikipedia.org/wiki/Build_automation),
come quello mostrato nel [repository d'esempio](https://github.com/prog2-unimi/build-automation-example).

### GitHub e Gitpod

<div style="background-color: lightyellow;">

```{warning}

Gli strumenti descritti in questa sezione, il cui uso è del tutto facoltativo, sono
indicati e offerti senza alcuna garanzia di funzionamento, o di supporto, da parte
del docente.

Nel caso in cui venga riscontrata una qualunque difficoltà, o malfunzionamento,
si consiglia di procedere in modo autonomo con l'installazione e configurazione
dell'ambiente di sviluppo sul proprio computer.
```
</div>

Per svolgere le esercitazioni e gli *homework* è possibile utilizzare il *cloud
IDE* [Gitpod](https://www.gitpod.io/) che consiste di una di istanza [Visual
Studio Code](https://code.visualstudio.com/) e
dell'[OpenJDK](https://openjdk.java.net/), offerti come servizio cloud (ossia
accessibili gratuitamente in rete, senza necessità di installare, o configurare,
alcun software).

Si consiglia che gli studenti interessati creino quanto prima un account su
[GitHub](https://github.com/), necessario per l'uso di GitPod; si osservi che
creando l'account con l'indirizzo ufficiale `@studenti.unimi.it` è possibile
beneficiare di [agevolazioni
interessanti](https://education.github.com/students) come il [GitHub Student
Developer Pack](https://education.github.com/pack).

Una volta creato l'account è possibile verificare che tutto funzioni a dovere
usando il bottone "Open in Gitpod" nel [repository delle
esercitazioni](https://github.com/prog2-unimi/esercitazioni).