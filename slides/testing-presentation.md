---
marp: true
theme: default
paginate: true
transition: overlap
math: katex
footer: "BA Dresden | Datenschutz/-sicherheit und die Notwendigkeit von Tests | \nKevin Böhme & Rico Ukro"
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
  /* Centered text */
  .centered {
    text-align: center;
  }
  /* Fixed top */
  .fixed-top {
    position: absolute;
    top: 10%;
  }
  /* For sources of citations */
  .source {
    font-size: 12px;
  }
</style>

![bg left:40% 80%](res/ba_dresden_logo.svg?)

# Datenschutz/-sicherheit

### und die Notwendigkeit von Tests

von Kevin Böhme und Rico Ukro

---

<!--TODO: Delete this slide-->

# TODO

- [ ] Add or remove picture captions
- [ ] Reorder slides
- [ ] Make this stuff beautiful
- [ ] Check Abbreviations
- [ ] Discuss: \
       - Use Mentimeter (or similar) opinion poll?
          Questions: Do you regularly test your software? Will you change your testing habits after this presentation?
- [ ] Collect all inline quotes
- [x] Make example solutions for all exercises as files
- [x] Number the exercises
- [x] Choose online platform to propagate for exercises
  - [onlinegdb.com](https://www.onlinegdb.com/)
  - ...
- [ ] Maybe, Add offset for slide content, because of `fixed-top` heading
- [x] Add example exercise link in the last slide
  - Difficult - match the presentation with markdown or the generated pdf?
- [ ] Vote: Add this topic: [Role of Test Automation in a CI/CD Pipeline(https://dancerscode.com/posts/role-of-test-automation-in-a-ci-cd-pipeline/)]?
- [ ] Vote: Add this topic: [Test Benefit Analysis](https://dancerscode.com/posts/test-benefit-analysis/)?

---

<h1 class="centered">
  Agenda
</h1>

<div style="display: flex; justify-content: space-between;">

  <div style="flex: 1; padding-right: 10px;">
    <ul>
      <li>Was sind Tests?</li>
      <li>Warum Tests?</li>
      <li>Test Driven Development (TDD)</li>
    </ul>
  </div>

  <div style="flex: 1; padding-left: 10px; padding-right: 10px;">
    <ul>
      <li>Grundlagen von Tests und Testverfahren
        <ul>
          <li>Unit Tests</li>
          <li>Integration Tests</li>
          <li>System Tests</li>
          <li>Fuzzing</li>
          <li>Penetration Tests</li>
          <li>Weiterführende Testverfahren</li>
        </ul>
      </li>
      <li>Mocking</li>
    </ul>
  </div>

  <div style="flex: 1; padding-left: 10px;">
    <ul>
      <li>Umsetzung von Tests</li>
      <li>TODO: Add lifedemo <a href="https://www.onlinegdb.com/">onlinegdb.com</a></li>
      <li>Testverfahren für Datensicherheit im Detail</li>
      <li>Datenschutz: Besonderheiten beim Testen
        <!-- TODO: idea: No real data, generated data, eventually from a public database for this purpose -->
        <!-- TODO: add a setion: real implementation (framework) with example -->
      </li>
      <li>Quellen</li>
    </ul>
  </div>

</div>

---

<style scoped>
 ul { list-style-type: none; }
</style>

<h1 class="centered">
  Was sind Tests?
</h1>

* > _&#8222;Software testing is the process of evaluating and verifying that a software product or application does what it’s supposed to do. The benefits of good testing include preventing bugs and improving performance.&#8220;_ <br><span class="source">Quelle: [https://www.ibm.com/topics/software-testing](https://www.ibm.com/topics/software-testing)</span>


<!-- - Evaluierung und Verifizierung von Software -->
<!-- - Verhindern von Fehlern -->
<!-- - Verbesserung der Performance -->

---

<h1 class="centered">
  Warum Tests?
</h1>

---

<h2 class="fixed-top">
  Negativ Beispiele
</h2>

- 1985: Kanadische Strahlentherapie Therac-25
  - Softwarefehler führte zu tödlicher Strahlendosis
  - 3 Verletzte, 3 Tote

- 1994: Airbus A300 der China Airlines
  - Absturz aufgrund eines Softwarefehlers
  - 264 Tote

---

<h2 class="fixed-top">
  Negativ Beispiele
</h2>

- 1996: US-Bank Softwarefehler
  - 823 Kunden fälschlicherweise 920 Millionen US-Dollar gutgeschrieben

- 2015: Bloomberg-Terminal Absturz in Londom
  - Softwarefehler legte 300.000 Händler auf den Finanzmärkten lahm
  - Britische Regierung musste den Verkauf von 3 Mrd. Pfund Staatsanleihen verschieben

---

<h2 class="fixed-top">
  Gesetzliche Anforderungen (DSGVO)
</h2>

- Geeignete technische und organisatorische Maßnahmen
- Schutz personenbezogener Daten durch Tests
- Sicherstellung der System- und Datensicherheit

---

<h2 class="fixed-top">
   Artikel 5 – Grundsätze der Verarbeitung
</h2>

- Angemessene Sicherheit sicherstellen
- Schutz vor unbefugter Verarbeitung und Datenverlust

> _&#8222;in einer Weise verarbeitet werden, die eine angemessene Sicherheit der personenbezogenen Daten gewährleistet [...] durch geeignete technische und organisatorische Maßnahmen („Integrität und Vertraulichkeit“);&#8220;_ <span class="source">Quelle: [Artikel 5 Abs. 1(f) DSGVO](https://dsgvo-gesetz.de/art-5-dsgvo/)</span>

---

<h2 class="fixed-top">
  Artikel 25 – Datenschutz durch Technikgestaltung
</h2>

- **Privacy by Design**: Datenschutz in der Entwicklung berücksichtigen
- Systeme vor Einführung testen

> _&#8222;[...] trifft der Verantwortliche [...] geeignete technische und organisatorische Maßnahmen – wie z. B. Pseudonymisierung –, die dafür ausgelegt sind, die Datenschutzgrundsätze wie etwa Datenminimierung wirksam umzusetzen und die notwendigen Garantien in die Verarbeitung aufzunehmen, um den Anforderungen dieser Verordnung zu genügen und die Rechte der betroffenen Personen zu schützen.&#8220;_ <span class="source">Quelle: [Artikel 25 Abs. 1 DSGVO](https://dsgvo-gesetz.de/art-25-dsgvo/)</span>

---

<h2 class="fixed-top">
  Artikel 32 – Sicherheit der Verarbeitung
</h2>

- Regelmäßige Tests vorgeschrieben
- Vertraulichkeit, Integrität und Verfügbarkeit sicherstellen
- Systeme und Prozesse evaluieren

> _&#8222;Ein Verfahren zur **regelmäßigen** Überprüfung, Bewertung und Evaluierung der Wirksamkeit der technischen und organisatorischen Maßnahmen zur Gewährleistung der Sicherheit der Verarbeitung.&#8220;_ <span class="source">Quelle: [Artikel 32 Abs. 1(f) DSGVO](https://dsgvo-gesetz.de/art-32-dsgvo/)</span>

---

<h2 class="fixed-top">
  Aus technischer Sicht am Beispiel
</h2>

```python
response = requests.get("https://api.example.com/data")

if response.status_code != 200:
    # Handle error
else:
    # Handle response
```

<h3> Warum ist Testing in diesem Kontext wichtig?</h3>

---

- Fehlererkennung: API antwortet korrekt, Fehler werden richtig gehandhabt
- Fehlertoleranz: Anwendung reagiert robust auf verschiedene Antwortcodes und Netzwerkausfälle
- Sicherheit: Sicherstellen, dass keine sensiblen Daten kompremittiert werden
- Zuverlässigkeit: API-Abfrage funktioniert konsistent, auch bei hoher Last oder langsamen Netzwerken
- Validierung der Logik: Richtig implementierte Logik für verschiedene Statuscodes und Inhalte

---

<h2 class="fixed-top">
 Grundlagen von Tests und Testverfahren
</h2>

- Notwendig um Fehler in Software zu finden
- Verschiedene Testarten decken unterschiedliche Aspekte ab:
  - Funktionalität
  - Integration
  - Sicherheit
- Verbindung zum Datenschutz:
  - Sicherstellen, dass keine personenbezogenen Daten kompromittiert werden

---

<h2 class="fixed-top">
  Test Driven Development (TDD)
</h2>

- Wasserfallmodell: Testen erst am Projektende vorgesehen
- V-Modell: Zeitlich klar definierte Abfolge der Testphasen
- Agiles Umfeld:
  - Tests müssen häufig und unter gleichen Bedingungen durchführbar sein
  - Geringer Aufwand für Testausführung erforderlich
  - Tests sollten zeitnah zur Umsetzung der Funktionalität bereitstehen
  - Ziel: Tests müssen mit dem ständigen Wandel Schritt halten

---

<div class="centered">
  <img src="res/test_driven_development.png?" alt="Test driven development" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle:
  [https://blogs.zeiss.com/digital-innovation/de/test-driven-development/](https://blogs.zeiss.com/digital-innovation/de/test-driven-development/)
</div>

---

<h2 class="fixed-top">
 Überblick über Testarten
</h2>

  - Unit Tests
  - Integration Tests
  - Penetration Tests
  - System Tests
  - Fuzzing

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

<h2 class="fixed-top">
  Unit Tests
</h2>

- Testen einzelner Softwarekomponenten
- Ziel: Sicherstellen, dass jede Komponente isoliert korrekt funktioniert
- Wichtig für Datenschutz: Vermeidung unsicherer Funktionen/Klassen in Modulen

> _&#8222;Software unit testing is a process that includes the performance of test planning, the acquisition of a test set, and the measurement of a test unit against its requirements.&#8220;_ <span class="source">Quelle: [IEEE Standard for Software Unit Testing](https://ieeexplore.ieee.org/document/27763)</span>

---

<h2 class="fixed-top">
  Unit Tests
</h2>

<div class="centered">
  <img src="res/unit-test-diagram.png?" alt="Unit Test Diagramm" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle: [https://dancerscode.com/posts/unit-tests/](https://dancerscode.com/posts/unit-tests/)
</div>

---

<h2 class="fixed-top">
  Integration Tests
</h2>

- Testen das Zusammenspiel mehrerer Komponenten
- Ziel: Sicherstellen, dass die Schnittstellen und Datenflüsse korrekt funktionieren
- Im Kontext von Datensicherheit/-schutz: Prüfen, ob sensible Daten korrekt zwischen Modulen übermittelt werden

> _&#8222;Software Integration V&V ensures that software components are validated as they are incrementally integrated&#8220;_ <span class="source">Quelle: [IEEE/ISO/IEC International Standard - Software and systems engineering--Software testing--Part 4: Test techniques,](https://ieeexplore.ieee.org/document/9591574)</span>

<!-- V&V: Verification and Validation -->

---

<h2 class="fixed-top">
  Integration Tests
</h2>

<div class="centered">
  <img src="res/integration-test-diagram.png?" alt="Integration Test Diagramm" style="width: 70%;"/>
</div>

<div class="centered source">

  Quelle: [https://dancerscode.com/posts/integration-tests/](https://dancerscode.com/posts/integration-tests/)
</div>

---

<h2 class="fixed-top">
  System Tests
</h2>


- Testen das gesamte System als Ganzes
- Ziel: Sicherstellen, dass die Software als Gesamtsystem funktioniert und sicher ist
- Relevant für Datenschutz: Überprüfung des gesamten Datenflusses und der Einhaltung von Sicherheitsstandards.

> _&#8222;The objective of the system testing is to find defects in features of the system compared to the way it has been defined in the software system requirements.&#8220;_ <span class="source">Quelle: [ISO/IEC/IEEE International Standard - Software and systems engineering —Software testing —Part 1:Concepts and definitions](https://ieeexplore.ieee.org/document/6588537)</span>

---

<h2 class="fixed-top">
  System Tests
</h2>

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

<h2 class="fixed-top">
  Fuzz Tests - Fuzzing
</h2>

- Testmethode, bei der zufällige Daten an das System gesendet werden
- Ziel: Entdecken von Schwachstellen durch ungewöhnliche oder unerwartete Eingaben.
- Datenschutzrelevant: Aufdecken von Schwachstellen, die zu unbefugtem Zugriff auf personenbezogene Daten führen könnten.

<!-- z.B. Buffer Overflows, Abstürze oder Sicherheitslücken -->

---

<h2 class="fixed-top">
  Fuzz Tests - Fuzzing
</h2>

<div class="centered">
  <img src="res/SAST - InstrumentedFuzzing.webp?" alt="Static Analysis and Code Fuzzing in the V-model" style="width: 60%;"/>
</div>
<div class="centered source">

  Static Analysis and Code Fuzzing in the V-model
  Quelle: [https://dancerscode.com/posts/system-testing/](https://www.code-intelligence.com/what-is-fuzz-testing)
</div>

---

<h2 class="fixed-top">
  Fuzz Tests - Fuzzing
</h2>

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

<h2 class="fixed-top">
  Penetration Tests
</h2>

- Simulierte Angriffe auf ein System, um Sicherheitslücken zu identifizieren
- Auch bekannt als _ethical hacking_
- Besonders wichtig für Datenschutz und Datensicherheit, um Schwachstellen frühzeitig zu erkennen

- Verschiedene Arten von Penetration Tests:
  - White Box
  - Black Box
  - Grey Box

---

<h2 class="fixed-top">
  Penetration Tests
</h2>

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


<h2 class="fixed-top">
  Penetration Tests
</h2>

Phasen eines Penetration Tests:

1. Reconnaissance (Information Gathering)
2. Scanning (z.B. Port-Scanning)
3. Exploitation (Ausnutzung gefundener Schwachstellen)
4. Post-Exploitation (z.B. Aufrechterhaltung des Zugangs)
5. Reporting (Erstellung eines Berichts mit Empfehlungen)

---

<h2 class="fixed-top">
  Überblick: weitere Testverfahren
</h2>

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

<h2 class="fixed-top">
  Mocking
</h2>

- Mocking: Simuliert das Verhalten von Objekten oder Komponenten
- Ziel: Unabhängig von externen Abhängigkeiten testen
- Verwendung:
  - Imitiert APIs, Datenbanken oder andere Dienste
  - Ermöglicht gezieltes Testen von isolierten Funktionen
- Vorteile:
  - Schneller und zuverlässiger als echte externe Ressourcen
  - Erlaubt das Testen von Szenarien, die in der realen Umgebung schwer zu reproduzieren sind

---

# Umsetzung von Tests

---

<h2 class="fixed-top">
  Testdaten und Datenschutz
</h2>

Erforderlich bei Tests von Software, die personenbezogene Daten verarbeitet:

- **Testdaten anonymisieren** oder pseudonymisieren, um DSGVO-Anforderungen zu erfüllen.
- **Automatisierte Tools** nutzen, um sichere und DSGVO-konforme Testdaten zu generieren.
- **Zugriffsbeschränkungen** für Testumgebungen einführen, um Missbrauch von Testdaten zu verhindern.

> _&#8222;Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für die Zwecke der Verarbeitung notwendige Maß beschränkt sein („Datenminimierung“);&#8220;_ <span class="source">Quelle: [Artikel 5 Abs. 1(c) DSGVO](https://dsgvo-gesetz.de/art-5-dsgvo/)</span>
---

<h2 class="fixed-top">
  Und wie erstelle ich Tests?
</h2>

##### Beispiel: Addierer


```python
# adder.py
def add(a, b):
    # Addiert zwei Zahlen
    return a + b
```

---

<h2 class="fixed-top">
  Und wie erstelle ich Tests?
</h2>

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
  Ehmm.. Noch Fragen oder Anmerkungen? 
</h1>

---

<h2 class="fixed-top" style="text-align: center; width: 100%;">
  Link zu den Aufgaben
</h2>
<a href="https://github.com/bytehaufen/DSDS-Presentation/blob/build/pdfs/testing-exercises.pdf" style="text-align: center; display: block;">Gehe zu den Aufgaben</a>

---

## Quellen
- [https://www.geeksforgeeks.org/software-testing-basics/](https://www.geeksforgeeks.org/software-testing-basics/)
- [https://blogs.zeiss.com/digital-innovation/de/test-driven-development/](https://blogs.zeiss.com/digital-innovation/de/test-driven-development/)
- [https://purplesec.us/learn/types-penetration-testing](https://purplesec.us/learn/types-penetration-testing/)
- [https://www.code-intelligence.com/what-is-fuzz-testing](https://www.code-intelligence.com/what-is-fuzz-testing)
- [https://microsoft.github.io/code-with-engineering-playbook/automated-testing/unit-testing/mocking/](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/unit-testing/mocking/)
