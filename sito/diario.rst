Diario delle lezioni
====================

Il seguente diario riporta gli *argomenti* e il *materiale didattico* relativi
sia alle **lezioni già svolte** (riguardo alle quali costituisce il programma
d'esame *de facto*), che alle lezioni **ancora da svolgere**, per le quali è *da
intendersi del tutto indicativo* (sia riguardo alle date che al contenuto).

Le *lezioni* di **teoria** sono indicate col prefisso *T*, mentre le
**esercitazioni** sono indicate col prefisso *E*; in ogni caso, la pagina sulla
:doc:`prossima lezione <lezione>` contiene di volta in volta il link aggiornato
per l'accesso sincrono. Le registrazioni delle lezioni sono raccolte nel `canale
YouTube del corso <https://bit.ly/3cmDTyM>`__ nelle *playlist* denominate
`teoria <https://bit.ly/2ZW2k0K>`__ e `esercitazioni
<https://bit.ly/3hSCNM3>`__.

Il *materiale didattico* indicato come *PDJ* si riferisce al libro di testo
`Program Development in Java
<http://www.informit.com/store/program-development-in-java-abstraction-specification-9780768684698>`__,
quello indicato con *EJ* si riferisce al libro di testo `Effective Java
<http://www.informit.com/store/effective-java-9780134685991>`__, quello indicato
con *JT* a `The Java™ Tutorials <https://docs.oracle.com/javase/tutorial/>`__,
quello con *H* si riferisce agli handout (siano essi *notebook* o *sorgenti*
disponibili nel `repository degli handout
<https://github.com/prog2-unimi/handouts>`__ del corso), in fine il materiale
indicato con *E* si riferisce alle esercitazioni (disponibili nel `repository
delle esercitazioni <https://github.com/prog2-unimi/esercitazioni>`__ del
corso); si veda la nota sui :ref:`numeri di sezione <numeridisezione>` che reca
indicazioni su quali parti del materiale sono *parte del programma* e quali
*letture consigliate, ma facoltative*.

|

.. table::
  :widths: 10 10 30 50

  +---------+---------+----------------------------------+-----------------------------------------------------------------+
  | Lezione | Data    | Argomento                        | Materiale didattico                                             |
  +=========+=========+==================================+=================================================================+
  | T1      | M 29/9  | Introduzione                     | PDJ 1                                                           |
  +---------+---------+----------------------------------+-----------------------------------------------------------------+
  | T2      | V 2/10  | Il linguaggio Java               | PDJ 2 *1 - 3*; JT `Language Basics`_, `Packages`_               |
  +---------+---------+                                  +-----------------------------------------------------------------+
  | T3      | M 6/10  |                                  | PDJ 2 *4, 5*; JT `Classes and Objects`_                         |
  +---------+---------+                                  +-----------------------------------------------------------------+
  | T4      | V 9/10  |                                  | PDJ 2 *6 - 8*; JT `Lists`_, `IO Streams`_                       |
  +---------+---------+----------------------------------+-----------------------------------------------------------------+
  | T5      | M 13/10 | Astrazione procedurale           | PDJ 3; [`How to Write Javadoc`_. `Javadoc Guide`_]              |
  +---------+---------+                                  +                                                                 +
  | E1      | V 16/10 |                                  |                                                                 |
  +---------+---------+----------------------------------+-----------------------------------------------------------------+
  | T6      | M 20/10 | Eccezioni                        | PDJ 4; EJ 10                                                    |
  +---------+---------+                                  +                                                                 +
  | E2      | V 23/10 |                                  |                                                                 |
  +---------+---------+----------------------------------+-----------------------------------------------------------------+
  | T7      | M 27/10 | Astrazione dei dati              | PDJ 5                                                           |
  +---------+---------+                                  +                                                                 +
  | E3      | V  3/11 |                                  |                                                                 |
  +---------+---------+                                  +                                                                 +
  | T8      | M  6/11 |                                  |                                                                 |
  +---------+---------+                                  +                                                                 +
  | E4      | V 16/10 |                                  |                                                                 |
  +---------+---------+----------------------------------+-----------------------------------------------------------------+

|

.. _Getting Started: https://docs.oracle.com/javase/tutorial/getStarted/
.. _Language Basics: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/
.. _Classes and Objects: https://docs.oracle.com/javase/tutorial/java/javaOO/
.. _Packages: https://docs.oracle.com/javase/tutorial/java/package/
.. _Lists: https://docs.oracle.com/javase/tutorial/collections/interfaces/list.html
.. _IO Streams: https://docs.oracle.com/javase/tutorial/essential/io/streams.html
.. _Default Methods: https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html
.. _Nested Classes: https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html
.. _Anonymous Classes: https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html
.. _Collections: https://docs.oracle.com/javase/tutorial/collections/
.. _Collections (documentation): https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/doc-files/coll-index.html
.. _Generics: https://docs.oracle.com/javase/tutorial/java/generics/
.. _Generics (Bracha): https://docs.oracle.com/javase/tutorial/extra/generics/

.. _Collections (Bloch): https://www.cs.cmu.edu/~charlie/courses/15-214/2016-fall/slides/15-collections%20design.pdf

.. _For-each: https://docs.oracle.com/javase/8/docs/technotes/guides/language/foreach.html
.. _Programming With Assertions: https://docs.oracle.com/javase/8/docs/technotes/guides/language/assert.html

.. _How to Write Javadoc: https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html
.. _Javadoc Guide: https://docs.oracle.com/en/java/javase/11/javadoc/

.. _JUnit: https://junit.org/
.. _Rice Theorem: https://www.dcc.fc.up.pt/~acm/ricep.pdf

.. admonition:: Nota bene
  :class: alert alert-secondary

  Accanto a ciascun riferimento che reca un numero di *capitolo* possono trovarsi
  dei *numeri o titoli di sezione o item* essi sono da intendersi nel seguente modo:

  .. _numeridisezione:

  * se assenti: l'*intero capitolo è parte del programma* (ad esempio, con "PDJ 5" si intende
    l'intero capitolo 5 di "Program Development in Java"),

  * se presenti (fuori parentesi): solo *le sezioni/item indicate sono parte del programma* (ad esempio,
    con "EJ 1 3-6, 9" si intende che del capitolo 1 di "Effective Java"
    sono strettamente parte del programma solo gli item 3, 4, 5, 6 e 9),

  * se presenti tra parentesi quadre: le  *sezioni indicate sono letture caldamente raccomandate,
    ma facoltative* (ad esempio con "PDJ 15 [2-4, 7]" si intende che del capitolo 15 di
    "Program Development in Java" è consigliata la lettura delle sezioni 2, 3, 4 e 7).

