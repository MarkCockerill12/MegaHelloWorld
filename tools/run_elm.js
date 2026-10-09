// Runs a compiled Elm program in a simulated browser page and prints the text it renders.
// Usage: node run_elm.js <compiled.js>
const fs = require("fs");
const { JSDOM } = require("jsdom");

const page = '<!DOCTYPE html><html><body><div id="app"></div></body></html>';
const dom = new JSDOM(page, { runScripts: "outside-only" });
dom.window.eval(fs.readFileSync(process.argv[2], "utf8"));
dom.window.eval('Elm.Main.init({ node: document.getElementById("app") })');
// Elm renders on the next animation frame
setTimeout(() => console.log(dom.window.document.body.textContent), 50);
