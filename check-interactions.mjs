import { readFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';
import assert from 'node:assert/strict';

for (const denied of [false, true]) {
  const elements = new Map();
  for (const selector of ['.menu-toggle', '#main-nav', '.copy-button', '#copy-status']) {
    elements.set(selector, { handlers: {}, hidden: false, textContent: '', attributes: {},
      addEventListener(event, handler) { this.handlers[event] = handler; },
      setAttribute(key, value) { this.attributes[key] = value; },
      getAttribute(key) { return this.attributes[key]; }, focus() {} });
  }
  let copied;
  runInNewContext(readFileSync(new URL('./script.js', import.meta.url), 'utf8'), {
    document: { querySelector: selector => elements.get(selector), addEventListener() {} },
    window: { matchMedia: () => ({ matches: true, addEventListener() {} }) },
    navigator: { clipboard: { async writeText(value) { if (denied) throw new Error('Permission denied'); copied = value; } } },
    setTimeout() {}, clearTimeout() {}
  });
  const menu = elements.get('.menu-toggle');
  assert.equal(elements.get('#main-nav').hidden, true);
  menu.handlers.click();
  assert.equal(menu.getAttribute('aria-expanded'), 'true');
  assert.equal(elements.get('#main-nav').hidden, false);
  await elements.get('.copy-button').handlers.click();
  assert.equal(copied, denied ? undefined : 'https://make.fun/r/z1j4n66g');
  assert.match(elements.get('#copy-status').textContent, denied ? /Copy unavailable.*visible link/ : /Referral link copied/);
}
console.log('PASS: mobile menu state, exact clipboard value and readable permission-denied fallback');
