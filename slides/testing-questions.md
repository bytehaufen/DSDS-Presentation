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

##### Was ist ein Unit Test?

1. Ein Test, der die gesamte Anwendung überprüft.
1. Ein Test, der eine einzelne Funktion oder Methode überprüft.
1. Ein Test, der die Benutzeroberfläche überprüft.
1. Ein Test, der die Datenbank überprüft.

---


##### Welche der folgenden Punkte gehören zu den Zielen eines Software-Tests?

1. Verbesserung der Performance
1. Sicherstellen, dass eine Software korrekt funktioniert
1. Verhindern, dass die Software benutzt wird
1. Senken der Entwicklungszeit

---

##### Welche der folgenden Testmethoden wird üblicherweise zuerst in der Entwicklungsphase durchgeführt?
1. Integrationstest
1. Penetrationstest
1. Unit-Test
1. Systemtest

---

##### Wie unterstützt das _Privacy by Design_ Prinzip die Durchführung von Softwaretests, um Datenschutzrisiken zu minimieren?"

---

##### Erklären Sie das Konzept der testgetriebenen Entwicklung (TDD).
##### Welche Vorteile hat es im Vergleich zu herkömmlichen Ansätzen?

---

##### Welche Art von Test zielt darauf ab, zufällige Eingaben zu verwenden, um Schwachstellen in der Software zu finden?
1. Unit-Test
1. Fuzz-Test
1. Regressionstest
1. Systemtest

---

##### Was ist "Mocking" im Kontext von Softwaretests? 
##### Warum wird es oft in Unit-Tests verwendet?

---

##### Warum ist es wichtig, Testdaten zu anonymisieren oder zu pseudonymisieren?

---

##### Welcher Test wird üblicherweise durchgeführt, um sicherzustellen, dass neue Codeänderungen keine Fehler in bestehender Funktionalität einführen?
1. Smoke-Test
1. Regressionstest
1. Penetrationstest
1. Performance-Test
