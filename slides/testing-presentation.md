---
marp: true
theme: default
paginate: true
transition: overlap
math: katex
footer: "BA Dresden | Datenschutz/-sicherheit und die Notwendigkeit von Tests | Kevin Böhme & Rico Ukro"
---

<style>
  /* Adds styling for codeblocks to add line numbers with custom engine */
  /* Based on: https://github.com/orgs/marp-team/discussions/164 */
  pre ol {
      all: unset;
      display: grid;
      grid-template-columns: auto 1fr;
      counter-reset: line-number 0;
    }
    pre ol li {
      display: contents;
    }
    pre ol li span[data-marp-line-number]::before {
      display: block;
      content: counter(line-number) " ";
      counter-increment: line-number;
      text-align: left;
      color: #bbb; /* Lighter color for line numbers */
      font-weight: lighter; /* Lighter font weight for line numbers */
    }
  /* Center all h1 elements */
  h1 {
    text-align: center;
  }
  /* Fix all h2 elements to top */
  h2 {
    position: absolute;
    top: 55px; /* 78.5px is the default theme padding of all slides */
  }
  /* Centered text */
  .centered {
    text-align: center;
  }
  /* For sources of citations */
  .source {
    font-size: 16px;
  }
</style>

<style scoped>
  h1 {
    text-align: left;
  }
</style>

<!-- _footer: "BA Dresden | Datenschutz/-sicherheit und die Notwendigkeit von Tests | \nKevin Böhme & Rico Ukro" -->

![bg left:40% 80%](res/ba_dresden_logo.svg?)

# Datenschutz/-sicherheit

### und die Notwendigkeit von Tests

von Kevin Böhme und Rico Ukro

---

<!--TODO: Delete this slide-->

<style scoped>
p{
  margin: 1px 0;
  font-size: 16px;
}
ul {
  margin: 1px 0;
}
li {
  margin: 1px 0;
  line-height: 1;
  font-size: 16px;
}
</style>
# TODO

Open:
- [ ] H2 so ok, or change it back to default (relative behavior)?
- [x] Reorder slides
  - -> I think it's ok
- [ ] Make this stuff beautiful
- [x] Update Agenda
  - -> Check one more time @Zwirnisw3lt

Done:
- [x] Customize source links font-size
- [x] Slide [go to exercises](#Praktische-Übungen-zur-Implementierung-von-Tests) heading looks miss-shifted
- [x] Slide `Picture of TDD` really without heading?
- [x] Check Abbreviations
- [x] Add or remove picture captions
  - -> No, not necessary
- [x] Flatten `Agenda`; make Details as comments -> @rico
- [x] Make headings academic
- [x] Discuss:
  - Use Mentimeter (or similar) opinion poll? -> **NO, thats totally bullshit**
- [x] Collect all inline quotes
  - -> no, "Es bleibt alles da wo es ist!!!!111!!!"
- [x] Make example solutions for all exercises as files
- [x] Number the exercises
- [x] Choose online platform to propagate for exercises
  - [onlinegdb.com](https://www.onlinegdb.com/)
  - ...
- [x] Maybe, Add offset for slide content, because of `h2` heading
  - -> Reject, to much effort
- [x] Add example exercise link in the last slide
- [x] Vote: Add this topic: [Role of Test Automation in a CI/CD Pipeline(https://dancerscode.com/posts/role-of-test-automation-in-a-ci-cd-pipeline/)]?
  - -> No, we have enough content
- [x] Vote: Add this topic: [Test Benefit Analysis](https://dancerscode.com/posts/test-benefit-analysis/)?
  - -> No, we have enough content
- [x] Discuss: For the test example, first show the test, then the implementation -> Better match with TDD
  - -> Added as comment for explanation
- [ ] Check that the `pdf`s look like the slides 
---

#  Agenda

- Begriffsklärung und Bedeutung von Softwaretests
- Zweck und Notwendigkeit von Softwaretests
- Grundlagen der Testmethoden und -verfahren
- Durchführung von Softwaretests
- Offene Fragen und Diskussion
- Praktische Übungen zur Implementierung von Tests

<!--
Zu Grundlagen der Testmethoden und -verfahren:
- Testgetriebene Entwicklung (TDD - Test Driven Development)
- Übersicht über Testverfahren
+ Unit-Tests
+ Integrationstests
+ Systemtests
+ Fuzz-Tests - Fuzzing
+ Penetrationstests
+ Weitere Testverfahren im Überblick
- Mocking

Zu Durchführung von Softwaretests:
- Testdatenmanagement und Datenschutzkonformität
- Beispiel Implementierung
-->

---

<style scoped>
 ul { list-style-type: none; }
</style>

#  Begriffsklärung und Bedeutung von Softwaretests

* > _&#8222;Software testing is the process of evaluating and verifying that a software product or application does what it’s supposed to do. The benefits of good testing include preventing bugs and improving performance.&#8220;_ <br><span class="source">Quelle: [https://www.ibm.com/topics/software-testing](https://www.ibm.com/topics/software-testing)</span>


<!--
- Evaluierung und Verifizierung von Software
- Verhindern von Fehlern
- Verbesserung der Performance

- Frage: Nutzen Sie regelmäßig Softwaretests?
-->

---

# Zweck und Notwendigkeit von Softwaretests

---

##  Fallstudien: Historische Beispiele

- 1985: Kanadische Strahlentherapie Therac-25
  - Softwarefehler führte zu tödlicher Strahlendosis
  - 3 Verletzte, 3 Tote

- 1994: Airbus A300 der China Airlines
  - Absturz aufgrund eines Softwarefehlers
  - 264 Tote

---

## Fallstudien: Historische Beispiele

- 1996: US-Bank Softwarefehler
  - 823 Kunden fälschlicherweise 920 Millionen US-Dollar gutgeschrieben

- 2015: Bloomberg-Terminal Absturz in Londom
  - Softwarefehler legte 300.000 Händler auf den Finanzmärkten lahm
  - Britische Regierung musste den Verkauf von 3 Mrd. Pfund Staatsanleihen verschieben

---

## Gesetzliche Anforderungen an Softwaretests (DSGVO)

- Geeignete technische und organisatorische Maßnahmen
- Schutz personenbezogener Daten durch Tests
- Sicherstellung der System- und Datensicherheit

---

### Artikel 5 – Grundsätze der Verarbeitung

- Angemessene Sicherheit sicherstellen
- Schutz vor unbefugter Verarbeitung und Datenverlust

> _&#8222;in einer Weise verarbeitet werden, die eine angemessene Sicherheit der personenbezogenen Daten gewährleistet [...] durch geeignete technische und organisatorische Maßnahmen („Integrität und Vertraulichkeit“);&#8220;_ <span class="source">Quelle: [Artikel 5 Abs. 1(f) DSGVO](https://dsgvo-gesetz.de/art-5-dsgvo/)</span>

---

### Artikel 25 – Datenschutz durch Technikgestaltung

- **Privacy by Design**: Datenschutz in der Entwicklung berücksichtigen
- Systeme vor Einführung testen

> _&#8222;[...] trifft der Verantwortliche [...] geeignete technische und organisatorische Maßnahmen – wie z. B. Pseudonymisierung –, die dafür ausgelegt sind, die Datenschutzgrundsätze wie etwa Datenminimierung wirksam umzusetzen und die notwendigen Garantien in die Verarbeitung aufzunehmen, um den Anforderungen dieser Verordnung zu genügen und die Rechte der betroffenen Personen zu schützen.&#8220;_ <span class="source">Quelle: [Artikel 25 Abs. 1 DSGVO](https://dsgvo-gesetz.de/art-25-dsgvo/)</span>

---

### Artikel 32 – Sicherheit der Verarbeitung

- Regelmäßige Tests vorgeschrieben
- Vertraulichkeit, Integrität und Verfügbarkeit sicherstellen
- Systeme und Prozesse evaluieren

> _&#8222;Ein Verfahren zur **regelmäßigen** Überprüfung, Bewertung und Evaluierung der Wirksamkeit der technischen und organisatorischen Maßnahmen zur Gewährleistung der Sicherheit der Verarbeitung.&#8220;_ <span class="source">Quelle: [Artikel 32 Abs. 1(f) DSGVO](https://dsgvo-gesetz.de/art-32-dsgvo/)</span>

---

### Aus technischer Sicht am Beispiel

```python
response = requests.get("https://api.example.com/data")

if response.status_code != 200:
    # Handle error
else:
    # Handle response
```

---

### Warum ist Testing in diesem Kontext wichtig?
<ul data-marpit-fragment="1">
  <li>Fehlererkennung: API antwortet korrekt, Fehler werden richtig gehandhabt</li>
  <li>Fehlertoleranz: Anwendung reagiert robust auf verschiedene Antwortcodes und Netzwerkausfälle</li>
  <li>Sicherheit: Sicherstellen, dass keine sensiblen Daten kompromittiert werden</li>
  <li>Zuverlässigkeit: API-Abfrage funktioniert konsistent, auch bei hoher Last oder langsamen Netzwerken</li>
  <li>Validierung der Logik: Richtig implementierte Logik für verschiedene Statuscodes und Inhalte</li>
</ul>

---

# Grundlagen der Testmethoden und -verfahren

---

## Testgetriebene Entwicklung (TDD - Test Driven Development)

- Wasserfallmodell: Testen erst am Projektende vorgesehen
- V-Modell: Zeitlich klar definierte Abfolge der Testphasen
- Agiles Umfeld:
  - Tests müssen häufig und unter gleichen Bedingungen durchführbar sein
  - Geringer Aufwand für Testausführung erforderlich
  - Tests sollten zeitnah zur Umsetzung der Funktionalität bereitstehen
  - Ziel: Tests müssen mit dem ständigen Wandel Schritt halten

---

## Testgetriebene Entwicklung (TDD - Test Driven Development)

<div class="centered">
  <img src="res/test_driven_development.png?" alt="Test driven development" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle: [https://blogs.zeiss.com/digital-innovation/de/test-driven-development/](https://blogs.zeiss.com/digital-innovation/de/test-driven-development/)
</div>

---

## Übersicht über Testverfahren

- Unit-Tests
- Integrationstests
- Penetrationstests
- Systemtests
- Fuzz-Tests - Fuzzing

<!-- Unit Tests:
     - Testen einzelne, isolierte Komponenten
     - Sicherstellen der korrekten Funktion von Funktionen/Methoden -->

<!-- Integration Tests:
     - Prüfen das Zusammenspiel mehrerer Module
     - Sicherstellen der korrekten Interaktion zwischen Komponenten -->

<!-- Penetration Tests:
     - Simulieren gezielte Angriffe
     - Finden von Sicherheitslücken und Schwachstellen -->

<!-- System Tests:
     - Überprüfen das gesamte System in realistischer Umgebung
     - Sicherstellen, dass das System den Anforderungen entspricht -->

<!-- Fuzzing:
     - Automatisierte Eingaben zufällig generieren
     - Finden von Schwachstellen wie Abstürzen oder Sicherheitslücken -->

---

## Unit-Tests

- Testen einzelner Softwarekomponenten
- Ziel: Sicherstellen, dass jede Komponente isoliert korrekt funktioniert
- Wichtig für Datenschutz: Vermeidung unsicherer Funktionen/Klassen in Modulen

> _&#8222;Software unit testing is a process that includes the performance of test planning, the acquisition of a test set, and the measurement of a test unit against its requirements.&#8220;_ <span class="source">Quelle: [IEEE Standard for Software Unit Testing](https://ieeexplore.ieee.org/document/27763)</span>

---

## Unit-Tests

<div class="centered">
  <img src="res/unit-test-diagram.png?" alt="Unit Test Diagramm" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle: [https://dancerscode.com/posts/unit-tests/](https://dancerscode.com/posts/unit-tests/)
</div>

---

## Integrationstests

- Testen das Zusammenspiel mehrerer Komponenten
- Ziel: Sicherstellen, dass die Schnittstellen und Datenflüsse korrekt funktionieren
- Im Kontext von Datensicherheit/-schutz: Prüfen, ob sensible Daten korrekt zwischen Modulen übermittelt werden

> _&#8222;Software Integration V&V ensures that software components are validated as they are incrementally integrated&#8220;_ <span class="source">Quelle: [IEEE/ISO/IEC International Standard - Software and systems engineering--Software testing--Part 4: Test techniques,](https://ieeexplore.ieee.org/document/9591574)</span>

<!-- V&V: Verification and Validation -->

---

## Integrationstests

<div class="centered">
  <img src="res/integration-test-diagram.png?" alt="Integration Test Diagramm" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle: [https://dancerscode.com/posts/integration-tests/](https://dancerscode.com/posts/integration-tests/)
</div>

---

## Systemtests


- Testen das gesamte System als Ganzes
- Ziel: Sicherstellen, dass die Software als Gesamtsystem funktioniert und sicher ist
- Relevant für Datenschutz: Überprüfung des gesamten Datenflusses und der Einhaltung von Sicherheitsstandards.

> _&#8222;The objective of the system testing is to find defects in features of the system compared to the way it has been defined in the software system requirements.&#8220;_ <span class="source">Quelle: [ISO/IEC/IEEE International Standard - Software and systems engineering —Software testing —Part 1:Concepts and definitions](https://ieeexplore.ieee.org/document/6588537)</span>

---

## Systemtests

<div class="centered">
  <img src="res/system-test-diagram.png?" alt="System Test Diagramm" style="width: 60%;"/>
</div>
<div class="centered source">

  Quelle: [https://dancerscode.com/posts/system-testing/](https://dancerscode.com/posts/system-testing/)
</div>

<!-- System Test deckt sowohl die Anwendung als auch alle Abhängigkeiten ab -->
<!-- Umfasst alle externen Systeme und Schnittstellen, die die Anwendung nutzt -->

<!-- Ziel: -->
<!-- - Überprüfung der vollständigen Funktionsfähigkeit der gesamten Anwendung unter realen Bedingungen -->
<!-- - Sicherstellen, dass alle Komponenten (inklusive externe Abhängigkeiten) korrekt integriert und funktional sind -->

---

## Fuzz-Tests - Fuzzing

- Testmethode, bei der zufällige Daten an das System gesendet werden
- Ziel: Entdecken von Schwachstellen durch ungewöhnliche oder unerwartete Eingaben.
- Datenschutzrelevant: Aufdecken von Schwachstellen, die zu unbefugtem Zugriff auf personenbezogene Daten führen könnten.

<!-- z.B. Buffer Overflows, Abstürze oder Sicherheitslücken -->

---

## Fuzz-Tests - Fuzzing

<div class="centered">
  <img src="res/SAST - InstrumentedFuzzing.webp?" alt="Static Analysis and Code Fuzzing in the V-model" style="width: 70%;"/>
</div>
<div class="centered source">

  Quelle: [https://dancerscode.com/posts/system-testing/](https://www.code-intelligence.com/what-is-fuzz-testing)
</div>

<!--
Static Analysis and Code Fuzzing in the V-model
-->
---

## Fuzz-Tests - Fuzzing

Arten von Fuzz-Tests:

- **Dumb Fuzzers**: Generieren zufällige Eingaben
- **Smart Fuzzers**: Erzeugen gezielte Eingaben
- **Mutationsbasiert**: Verändern bestehende Eingaben in semivalide Varianten
- **Generationsbasiert**: Erzeugt eingaben aus bekannten Strukturen
- **Black-Box**: Kein Wissen über die Programminterne Struktur
- **White-Box**: Kennt die Programmstruktur
- **Gray-Box**: Teilweise Kenntnis der Struktur
- **Abdeckungsgesteuert**: Optimiert Mutationen für maximale Codeabdeckung

<!-- Codeabdeckung: Misst, wie viel Prozent des Programmcodes durch Tests ausgeführt wird -->
<!-- White Box: Tester hat Zugriff auf den Quellcode und die Systemarchitektur -->
<!-- Black Box: Tester hat keine Informationen über das System -->
<!-- Grey Box: Mischung aus White Box und Black Box -->

---

## Penetrationstests

- Simulierte Angriffe auf ein System, um Sicherheitslücken zu identifizieren
- Auch bekannt als _ethical hacking_
- Besonders wichtig für Datenschutz und Datensicherheit, um Schwachstellen frühzeitig zu erkennen

- Verschiedene Arten von Penetration Tests:
  - White Box
  - Black Box
  - Grey Box

---

## Penetrationstests

Unterschiedliche Angriffsvektoren:
- Network
- Web Application
- Client Side
- Wireless
- Social Engineering
- Physical Penetration Testing

<!-- Network: z.B. Angriffe auf Netzwerkprotokolle und -dienste -->
<!-- Web Application: z.B. Datenbankinjektionen, Source Code -->
<!-- Client Side: z.B. Angriffe auf Browser -> Cross Site Scripting -->
<!-- Wireless: z.B. Angriffe auf WLAN -->
<!-- Social Engineering: z.B. Phishing -->
<!-- Physical Penetration Testing: z.B. Einbruch -->

---

## Penetrationstests

Phasen eines Penetration Tests:

1. Reconnaissance (Information Gathering)
2. Scanning (z.B. Port-Scanning)
3. Exploitation (Ausnutzung gefundener Schwachstellen)
4. Post-Exploitation (z.B. Aufrechterhaltung des Zugangs)
5. Reporting (Erstellung eines Berichts mit Empfehlungen)

---

## Weitere Testverfahren im Überblick

- **Regressionstests**: Prüfen auf neue Fehler nach Code-Änderungen
- **Load Tests**: Testen, ob das System unter Last stabil bleibt
- **End-to-End Tests**: Prüfen des gesamten System-Workflows
- **Smoke Tests**: Schnelltests nach einem Build zur Grundfunktionsprüfung
- **Sanity Tests**: Prüfen neuer Änderungen auf Korrektheit
- **Acceptance Tests (UAT)**: Überprüft Nutzeranforderungen
- **Performance Tests**: Misst Reaktionszeit und Stabilität
- **Usability Tests**: Überprüfung der Benutzerfreundlichkeit der Software
- **Alpha/Beta Tests**: Frühe/späte Testphasen mit internen/externen Nutzern

<!-- Regressionstests: Letztendlich CI/CD Automatisierte unit/integration/system test -->

---

## Mocking - Simulation externer Abhängigkeiten

- Mocking: Simuliert das Verhalten von Objekten oder Komponenten
- Ziel: Unabhängig von externen Abhängigkeiten testen
- Verwendung:
  - Imitiert APIs, Datenbanken oder andere Dienste
  - Ermöglicht gezieltes Testen von isolierten Funktionen
- Vorteile:
  - Schneller und zuverlässiger als echte externe Ressourcen
  - Erlaubt das Testen von Szenarien, die in der realen Umgebung schwer zu reproduzieren sind

---

# Durchführung von Softwaretests

---

## Testdatenmanagement und Datenschutzkonformität

Erforderlich bei Tests von Software, die personenbezogene Daten verarbeitet:

- **Testdaten anonymisieren** oder pseudonymisieren, um DSGVO-Anforderungen zu erfüllen.
- **Automatisierte Tools** nutzen, um sichere und DSGVO-konforme Testdaten zu generieren.
- **Zugriffsbeschränkungen** für Testumgebungen einführen, um Missbrauch von Testdaten zu verhindern.

> _&#8222;Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für die Zwecke der Verarbeitung notwendige Maß beschränkt sein („Datenminimierung“);&#8220;_ <span class="source">Quelle: [Artikel 5 Abs. 1(c) DSGVO](https://dsgvo-gesetz.de/art-5-dsgvo/)</span>
---

## Entwicklung und Implementierung von Tests

##### Beispiel: Addierer


```python
# adder.py
def add(a, b):
    # Addiert zwei Zahlen
    return a + b
```

<!--
Richtige Reihenfolge:
- Schnittstelle definieren -> Hier: Funkt. Signatur
- Tests schreiben
- Funktion implementieren
-->

---

## Entwicklung und Implementierung von Tests

##### Dazugehöriger Test

```python
# test_adder.py    # Bei online IDEs: main.py
import unittest # Importiere das Testframework
from adder import add # Importiere die Funktion add aus adder.py

class TestAdder(unittest.TestCase):
    def test_add_small_positiv_numbers(self): # Testfall 1
        self.assertEqual(add(1, 2), 3) # Erwartetes Ergebnis: 3

    def test_add_small_negativ_numbers(self): # Testfall 2
      self.assertEqual(add(-1, -2), -3) # Erwartetes Ergebnis: -3

if __name__ == '__main__':
  unittest.main() # Starte die Testausführung
```

Zum ausprobieren z.B. auf: [onlinegdb.com](https://www.onlinegdb.com/)

---

<h1 style="text-align: center; position: absolute; top: 40%; width: 100%; right: 0%">
  Offene Fragen und Diskussion
</h1>

<!--
Nutzen Sie regelmäßig Softwaretests?
-->

---

## Praktische Übungen zur Implementierung von Tests

<style scoped>
  a {
    display: block;
    text-align: center;
  }
</style>

[Zu den Übungsaufgaben](https://github.com/bytehaufen/DSDS-Presentation/blob/build/pdfs/testing-exercises.pdf)

---

## Quellen

<style scoped>
li {
  margin: 1px 0;
  line-height: 1.6;
  font-size: 20px;
}
</style>

1. Myers, Glenford J., Corey Sandler, and Tom Badgett. _The Art of Software Testing_. John Wiley & Sons, 2011.
2. Pajankar, Ashwin. _Python Unit Test Automation: Automate, Organize, and Execute Unit Tests in Python_. Apress, 2022.
3. GeeksforGeeks. &#8222;Software Testing Basics.&#8220; _GeeksforGeeks_, [https://www.geeksforgeeks.org/software-testing-basics/](https://www.geeksforgeeks.org/software-2esting-basics/). Abgerufen am 15. Sep. 2024.
4. Zeiss. &#8222;Test Driven Development (TDD).&#8220; _Digital Innovation Blog_. Zeiss, [https://blogs.zeiss.com/digital-innovation/de/test-driven-development/](https://blogs.zeiss.com/digital-innovation/de/test-driven-development/). Abgerufen am 18. Sep. 2024.
5. Purplesec. &#8222;Types of Penetration Testing.&#8220; _PurpleSec_, [https://purplesec.us/learn/types-penetration-testing/](https://purplesec.us/learn/types-penetration-testing/). Abgerufen am 19. Sep. 2024.
6. Microsoft. _Unit Testing: Mocking in Automated Testing_. Code With Engineering Playbook, [https://microsoft.github.io/code-with-engineering-playbook/automated-testing/unit-testing/mocking/](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/unit-testing/mocking/). Abgerufen am 17. Sep. 2024.
7. Code Intelligence. &#8222;What is Fuzz Testing?&#8220; _Code Intelligence_, [https://www.code-intelligence.com/what-is-fuzz-testing](https://www.code-intelligence.com/what-is-fuzz-testing). Abgerufen am 20. Sep. 2024.
