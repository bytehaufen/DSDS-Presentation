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
    font-size: 20px;
  }
  /* Make ordered lists use lower-alpha */
  ol { list-style-type: lower-alpha; }
</style>

<style scoped>
  h1 {
    text-align: left;
  }
</style>

<!-- _footer: "" -->

![bg left:40% 80%](res/ba_dresden_logo.svg?)

# Datenschutz/-sicherheit

### und die Notwendigkeit von Tests

von Kevin Böhme und Rico Ukro

##### - _Übungsfragen_ -

---

##### Was ist ein Unit-Test?

1. Ein Test, der die gesamte Anwendung überprüft.
1. Ein Test, der einzelne Funktionen, Methoden oder Klassen überprüft.
1. Ein Test, der die Benutzeroberfläche überprüft.
1. Ein Test, der die Datenbank überprüft.

<span data-marpit-fragment="1">Die richtige Antwort ist: **Ein Test, der einzelne Funktionen, Methoden oder Klassen überprüft.** Unit-Tests prüfen kleine, isolierte Teile der Software, um sicherzustellen, dass diese korrekt funktionieren.</span>

---

##### Welche der folgenden Punkte gehören zu den Zielen eines Software-Tests?

1. Verbesserung der Performance
1. Sicherstellen, dass eine Software korrekt funktioniert
1. Verhindern, dass die Software benutzt wird
1. Senken der Entwicklungszeit

<span data-marpit-fragment="1">Die richtigen Antworten sind: **Sicherstellen, dass eine Software korrekt funktioniert** und **Verbesserung der Performance.**</span>

---

##### Welche der folgenden Testmethoden wird üblicherweise zuerst in der Entwicklungsphase durchgeführt?
1. Integrationstest
1. Penetrationstest
1. Unit-Test
1. Systemtest

<span data-marpit-fragment="1">Die richtige Antwort ist: **Unit-Test**. Diese Tests werden früh durchgeführt, um die kleinsten Bausteine der Software zu testen.</span>

---

##### Wie unterstützt das **Privacy by Design** Prinzip die Durchführung von Softwaretests, um Datenschutzrisiken zu minimieren?

<span data-marpit-fragment="1">_Privacy by Design_ bedeutet, dass Datenschutz schon während der Entwicklung berücksichtigt wird. Softwaretests helfen dabei, Schwachstellen zu identifizieren, bevor die Software in Produktion geht, was das Risiko von Datenschutzverletzungen reduziert.</span>

---

##### Erklären Sie das Konzept der testgetriebenen Entwicklung (TDD).
<span data-marpit-fragment="1">TDD ist eine Methodik, bei der Tests vor dem Schreiben der eigentlichen Funktionalität erstellt werden.</span>
##### Welche Vorteile hat es im Vergleich zu herkömmlichen Ansätzen?

<span data-marpit-fragment="1">Der Vorteil ist, dass die Software kontinuierlich gegen die Tests validiert wird, was zu weniger Fehlern und besserer Codequalität führt.</span>

---

##### Welche Art von Test zielt darauf ab, zufällige Eingaben zu verwenden, um Schwachstellen in der Software zu finden?

1. Unit-Test
1. Fuzz-Test
1. Regressionstest
1. Systemtest

<span data-marpit-fragment="1">Die richtige Antwort ist: **Fuzz-Test**. Er verwendet zufällige Eingaben, um Schwachstellen oder unerwartetes Verhalten in der Software zu entdecken.</span>

---

##### Was ist "Mocking" im Kontext von Softwaretests? 
<span data-marpit-fragment="1">Mocking ist das Simulieren von Abhängigkeiten wie Datenbanken oder APIs, um zu testen, wie die zu testende Funktion damit interagiert. </span>
##### Warum wird es oft in Unit-Tests verwendet?

<span data-marpit-fragment="1">Es wird in Unit-Tests verwendet, um unabhängige und isolierte Tests durchzuführen.</span>

---

##### Warum ist es wichtig, Testdaten zu anonymisieren oder zu pseudonymisieren?

<span data-marpit-fragment="1">Testdaten sollten anonymisiert oder pseudonymisiert werden, um sicherzustellen, dass keine echten personenbezogenen Daten ungeschützt in Testumgebungen verwendet werden. Dies minimiert das Risiko von Datenschutzverletzungen und entspricht den Anforderungen der DSGVO.</span>

---

##### Welcher Test wird üblicherweise durchgeführt, um sicherzustellen, dass neue Codeänderungen keine Fehler in bestehender Funktionalität einführen?

1. Smoke-Test
1. Regressionstest
1. Penetrationstest
1. Performance-Test

<span data-marpit-fragment="1">Die richtige Antwort ist: **Regressionstest**. Diese Tests prüfen, ob bestehende Funktionen nach Codeänderungen weiterhin korrekt funktionieren.</span>

