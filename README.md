# DSDS-Presentation

Slides for the presentation of the DSDS module in the BA-Dresden with the
topic (_not final_) **Testing**.

The slides have been created with [marp](https://marp.app/).

## Interaction with the _marp-cli_ (stolen from the [marp documentation](https://github.com/marp-team/marp-cli))

[npx (`npm exec`)](https://docs.npmjs.com/cli/v7/commands/npx) is the best way to
use the latest Marp CLI if you wanted one-shot Markdown conversion
_without install_. Just run below if you have
installed [Node.js](https://nodejs.org/) v16 and later.

```bash
# Convert slide deck into HTML
npx @marp-team/marp-cli@latest ./slides/slide-deck.md --engine ./engine/engine.js
npx @marp-team/marp-cli@latest ./slides/slide-deck.md -o output.html --engine ./engine/engine.js

# Convert slide deck into PDF
npx @marp-team/marp-cli@latest ./slides/slide-deck.md --pdf --engine ./engine/engine.js
npx @marp-team/marp-cli@latest ./slides/slide-deck.md -o output.pdf --engine ./engine/engine.js

# Convert slide deck into PowerPoint document (PPTX)
npx @marp-team/marp-cli@latest ./slides/slide-deck.md --pptx --engine ./engine/engine.js
npx @marp-team/marp-cli@latest ./slides/slide-deck.md -o output.pptx --engine ./engine/engine.js

# Watch mode
npx @marp-team/marp-cli@latest -w ./slides/slide-deck.md --engine ./engine/engine.js

# Server mode (Pass directory to serve)
npx @marp-team/marp-cli@latest -s ./slides --engine ./engine/engine.js
```

## Marp ressources

- [Marp markdown documentation](https://marpit.marp.app/markdown)
- [Marp transition documentation](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#built-in-transition)


