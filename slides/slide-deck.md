---
marp: true
theme: default
paginate: true
transition: overlap
math: katex
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

---

# Agenda

- Was sind Tests?
- Warum Tests?
- Auflistung der Testverfahren
  - Unit Tests
  - Integration Tests
  - System Tests
  - Fuzzing
- Quellen

---

# Quellen

- [Placeholder](www.example.com)
