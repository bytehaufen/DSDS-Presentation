// engine.js
// Custom Marpit engine for Marp CLI for code block numbering
// Based on: https://github.com/orgs/marp-team/discussions/164
module.exports = ({ marp }) =>
    marp.use(({ marpit }) => {
      const { highlighter } = marpit
  
      marpit.highlighter = function (...args) {
        const original = highlighter.apply(this, args)
        const listItems = original
          .split(/\n(?!$)/) // Don't split at the trailing newline
          .map(
            (line) =>
              `<li><span data-marp-line-number></span><span>${line}</span></li>`
          )
  
        return `<ol>${listItems.join('')}</ol>`
      }
    }) 
    
//TODO: Add mermaid support
//Ideas: https://github.com/orgs/marp-team/discussions/207