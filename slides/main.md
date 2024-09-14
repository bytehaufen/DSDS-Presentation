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
</style>

![bg left:40% 80%](https://www.ba-dresden.de/tmpl/daten/berufsakademie_sachsen/img/logo/ba_dresden_logo.svg)

# Datenschutz/-sicherheit

### und die Notwendigkeit von Tests

von Kevin Böhme und Rico Ukro

---

<!--TODO: Delete this slide-->

# TODO

- [ ] Reorder slides
- [ ] Make this stuff beautiful
- [ ] Check Abbreviations
- [ ] Discuss: \
       - Use Mentimeter (or similar) opinion poll?
          Questions: Do you regularly test your software? Will you change your testing habits after this presentation?
      - Create interactive quiz? (e.g. Kahoot)
- [ ] Collect all inline quotes

---

# Agenda

- Was sind Tests?
- Warum Tests?
- Grundlagen von Tests und Testverfahren
  - Unit Tests
  - Integration Tests
  - Penetration Tests
  - System Tests
  - Fuzzing
- Testverfahren für Datensicherheit im Detail
- Datenschutz: Besonderheiten beim Testen
   <!-- TODO: idea: No real data, generated data, eventually from a public database for this purpose -->
- Quellen

---

<style scoped>
 ul { list-style-type: none; }
</style>

## Was sind Tests?

* > _Software testing is the process of evaluating and verifying that a software product or application does what it’s supposed to do. The benefits of good testing include preventing bugs and improving performance._ \[[ibm.com](https://www.ibm.com/topics/software-testing)\]

<!-- - Evaluierung und Verifizierung von Software -->
<!-- - Verhindern von Fehlern -->
<!-- - Verbesserung der Performance -->

---

## Warum Tests?

TODO: Python or js ? &rArr; Consistence

```javascript
let response = fetch("https://api.example.com/data");

if (typeof response === "undefined") {
  // Handle error
} else {
  // Handle response
}
```

```python
response = requests.get("https://api.example.com/data")

if response.status_code != 200:
    # Handle error
else:
    # Handle response
```

- Warum ist Testing in diesem Kontext wichtig?

---

<style scoped>
  a { color: inherit; }
</style>

# Quellen

- _[Placeholder](www.example.com)_
