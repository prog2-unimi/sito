# Strumenti e materiale di supporto

Questa pagina contiene alcune indicazioni circa il [linguaggio di
programmazione](#java) e gli strumenti di [supporto allo
sviluppo](#strumenti-di-supporto) adottati per il corso.

:::{note}
:class: warnadmonition

Data la *maturità culturale* che ci si attende dagli studenti che frequentano un
insegnamento del secondo anno, il docente **non fornirà alcun supporto**
all'installazione, configurazione e uso pratico degli strumenti qui descritti,
sia nell'ambiente desktop che cloud.
:::

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
librerie incluse nel JDK. Possono risultare molto utili anche i
[vari](https://docs.oracle.com/javase/tutorial/)
[tutorial](https://dev.java/learn/) ufficiali di Oracle.

## Strumenti di supporto

Lo scambio di informazioni tra docente e studenti avverrà principalmente
attraverso il servizio [GitLab](https://gitlab.di.unimi.it/) del Dipartimento di
Informatica a cui gli studenti possono accedere tramite le proprie credenziali
di Ateneo secondo le [istruzioni per utilizzare il servizio](https://gitlab.di.unimi.it/prog2#prog2-gitlab-di).

È possibile usare qualunque editor o IDE, durante il corso verrà utilizzato
l'editor [Visual Studio Code](https://code.visualstudio.com/) con il relativo
[supporto per Java](https://code.visualstudio.com/docs/languages/java); chi
preferisce può installare una [versione open](https://vscodium.com/).

Al fine di consentire l'automazione di alcuni compiti, come la generazione della
documentazione e l'esecuzione dei *black-box* test (necessari al superamento
dell'esame), durante il corso verranno utilizzati il *build automation tool*
denominato [Gradle](https://gradle.org/) unitamente al *testing framework*
[JUnit](https://junit.org/junit5/). Una *conoscenza approfondita del
funzionamento di tali strumenti non è affatto necessaria per il superamento
dell'esame*, perché la loro configurazione ed uso saranno automatizzati da parte
del docente, come ad esempio nel repository degli
[handout](https://github.com/prog2-unimi/handouts). Gli studenti interessati ad
approfondire possono tuttavia consultare un [esempio d'uso più
completo](https://github.com/prog2-unimi/build-automation-example) che può
risultare utile per la realizzazione del progetto.