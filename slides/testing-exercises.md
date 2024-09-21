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

![bg left:40% 80%](res/ba_dresden_logo.svg)

# Datenschutz/-sicherheit

### und die Notwendigkeit von Tests

##### - _Aufgaben_ -

---

<h2 class="fixed-top">
  Aufgabe 1 - Unit tests - Schaltjahr
</h2>

Ihr Kunde &#8222;Karl&#8220; hat für sein Produkt &#8222;Karl's Karlender&#8220;, bei Ihnen angefragt, die fehlende Implementierung für die Berechnung der Schaltjahre zu übernehmen:

1. Entwickeln Sie Unit-Tests für eine Funktion `is_leap_year(year: int) -> bool`, die überprüft, ob ein gegebenes Jahr ein Schaltjahr ist
2. Erstellen Sie mindestens 5 Testfälle, die verschiedene Szenarien abdecken (z.B. reguläre Jahre, Schaltjahre, Grenzfälle).
   _Hinweise: Nutzen Sie die Bibliothek `unittest`_
3. Implementieren Sie die Funktion `is_leap_year(year: int) -> bool`

_Negative Kalenderjahre sind nicht vorgesehen._

---

<h2 class="fixed-top">
  Aufgabe 1 - Unit tests - Schaltjahr
</h2>

Als kleine Starthilfe:

- _Template_: [`test_leapyear.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/leapyear/template/test_leapyear.py)
- _Template_: [`leapyear.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/leapyear/template/leapyear.py)

---

<h2 class="fixed-top">
  Aufgabe 2 - Unit/Integration tests - Sockenversand
</h2>

Für einen renommierten Online-Sockenversand soll die bisherige stark veraltete und fehleranfällige MS-SQL-Server Implementierung durch ein modernes Python Backend ersetzt werden.

Ihre Aufgabe ist es:

1. Unit-Tests für die Funktionalität des Sockenversands zu entwickeln
2. Implementierung der Funktionalität des Sockenversands zu erstellen
3. Integrationstests für die Funktionalität des Sockenversands zu entwickeln

---

<h2 class="fixed-top">
  Aufgabe 2 - Unit/Integration tests - Sockenversand
</h2>

Anforderungen:

- Klasse `SockStore`: Verwaltet den Bestand an Socken und stellt die folgenden Schnittstellen bereit
- Methode `search(self, color: str) -> int`: Gibt die Anzahl der Socken einer bestimmten Farbe zurück
- Methode `buy_sock(self, color)`: Kauft ein Paar Socken einer bestimmten Farbe und gibt die gekaufte Farbe zurück
- Methode `add_sock(self, color: str, quantity: int)`: Fügt Socken einer bestimmten Farbe und Menge hinzu

---

<h2 class="fixed-top">
  Aufgabe 2 - Unit/Integration tests - Sockenversand
</h2>

Als kleine Starthilfe:

- _Template_: [`test_sockstore_unit.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/sockstore/template/test_sockstore_unit.py)

- _Template_: [`sockstore.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/sockstore/template/sockstore.py)
- _Template_: [`test_sockstore_integration.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/sockstore/template/test_sockstore_integration.py)

---
  
<h2 class="fixed-top">
  Aufgabe 3 - System tests - Blog
</h2>

Einer Ihrer Kunden, die Firma &#8222;Bloggify&#8220;, hat Sie beauftragt, die System tests für ihre Blogging-Plattform zu entwickeln. Das Plattform-Backend ist mittels REST-API über [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts) erreichbar.

Ihre Aufgabe ist es:

1. System tests für die Blogging-Plattform zu entwickeln
2. Schwachstellen durch System tests in der Blogging-Plattform zu finden, um diese dem Kunden zu melden

---

<h2 class="fixed-top">
  Aufgabe 3 - System tests - Blog
</h2>

Guide für die API:
- [https://jsonplaceholder.typicode.com/guide](https://jsonplaceholder.typicode.com/guide)

Als kleine Starthilfe:

- _Template_: [`test_blog_system.py`](https://raw.githubusercontent.com/bytehaufen/DSDS-Presentation/main/exercises/blog/template/test_blog_system.py)
