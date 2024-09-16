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
  Aufgabe x - Unit tests - Schaltjahr
</h2>

1. Entwickeln Sie Unit-Tests für eine Funktion `is_leap_year(year: int) -> bool`, die überprüft, ob ein gegebenes Jahr ein Schaltjahr ist.
2. Erstellen Sie mindestens 5 Testfälle, die verschiedene Szenarien abdecken (z.B. reguläre Jahre, Schaltjahre, Grenzfälle).
_Hinweise: Nutzen Sie die Bibliothek `unittest`_
3. Implementieren Sie die Funktion `is_leap_year(year: int) -> bool` so, dass die Tests erfolgreich sind.

---

<h2 class="fixed-top">
  Aufgabe x - Unit tests - Schaltjahr - Beispiel für Testfall
</h2>

Datei `test_leapyear.py`:

```python
import unittest
import leapyear


class TestLeapYear(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(leapyear.is_leap_year(2024))


if __name__ == "__main__":
    unittest.main()

```

---

<h2 class="fixed-top">
  Aufgabe x - Unit tests - Schaltjahr - Beispiel für Implementierung
</h2>

Datei `leapyear.py`:

```python
def is_leap_year(year: int) -> bool:
    return False

```

---
