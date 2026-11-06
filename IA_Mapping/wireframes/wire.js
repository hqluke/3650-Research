// Disclosure buttons for the wireframes, plus the ?annotate overlay.
// The overlay reads the real markup, so the landmarks, tab order, and live
// regions in the annotated exports are whatever the HTML actually says.

for (const btn of document.querySelectorAll('button[aria-expanded]')) {
  btn.addEventListener('click', () => {
    btn.setAttribute('aria-expanded', String(btn.getAttribute('aria-expanded') !== 'true'));
  });
}

const focus = document.querySelector('[data-focus-on-load]');
if (focus && !location.search.includes('annotate')) focus.focus();

if (location.search.includes('annotate')) addEventListener('load', annotate);

function annotate() {
  document.body.classList.add('annotated');
  const put = (cls, text, x, y) => {
    const el = document.createElement('div');
    el.className = cls;
    el.textContent = text;
    el.style.left = `${x}px`;
    el.style.top = `${y}px`;
    document.body.append(el);
  };
  const rect = el => {
    const r = el.getBoundingClientRect();
    return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height };
  };
  const box = (el, cls, text) => {
    const r = rect(el);
    const b = document.createElement('div');
    b.className = `ann-box ${cls}`;
    Object.assign(b.style, { left: `${r.x}px`, top: `${r.y}px`, width: `${r.w}px`, height: `${Math.max(r.h, 8)}px` });
    document.body.append(b);
    // Live regions are often empty, so their label goes underneath instead of over the controls.
    put(`ann-label ${cls}`, text, r.x, cls === 'live' ? r.y + Math.max(r.h, 8) + 2 : Math.max(r.y - 20, 0));
  };
  const name = el => el.getAttribute('aria-label')
    ?? (el.getAttribute('aria-labelledby') && document.getElementById(el.getAttribute('aria-labelledby'))?.textContent.trim());

  for (const el of document.querySelectorAll('header, nav, main, aside, footer')) {
    const tag = el.tagName.toLowerCase();
    box(el, '', name(el) ? `<${tag}> "${name(el)}"` : `<${tag}>`);
  }
  for (const el of document.querySelectorAll('[aria-live], [role="status"], [role="alert"]')) {
    const kind = el.getAttribute('role') === 'alert' ? 'role="alert"' : `aria-live="${el.getAttribute('aria-live') ?? 'polite'}"`;
    box(el, 'live', `live region: ${kind}`);
  }
  for (const el of document.querySelectorAll('[data-focus-on-load]')) {
    // Measure the heading's text, not its full-width box.
    const range = document.createRange();
    range.selectNodeContents(el);
    const t = range.getBoundingClientRect();
    const r = { x: t.left + scrollX, y: t.top + scrollY, w: t.width };
    put('ann-label focus', 'focus lands here', r.x + r.w + 8, r.y);
  }
  for (const el of document.querySelectorAll('[aria-current], [aria-expanded]')) {
    const r = rect(el);
    if (!r.w) continue;
    const attr = el.hasAttribute('aria-current') ? `aria-current="${el.getAttribute('aria-current')}"` : `aria-expanded="${el.getAttribute('aria-expanded')}"`;
    put('ann-label focus', attr, r.x, r.y + r.h + 2);
  }

  // Tab stops in DOM order. A radio group is one stop (arrow keys move inside it).
  const seen = new Set();
  let n = 0;
  for (const el of document.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])')) {
    if (el.type === 'radio') {
      if (seen.has(el.name)) continue;
      seen.add(el.name);
    }
    const target = el.type === 'radio' || el.type === 'checkbox' ? el.closest('label') ?? el : el;
    const r = rect(target);
    const hidden = !target.getClientRects().length;
    if (hidden && !el.classList.contains('skip-link')) continue;
    n += 1;
    // The skip link sits off screen until it's focused, so its badge goes in the corner.
    if (r.y < 0 || hidden) put('ann-stop', n, 4, 4);
    // Text links get the badge above them so it doesn't cover the words.
    else if (el.matches('a:not(.btn)')) put('ann-stop', n, r.x - 6, r.y - 22);
    else put('ann-stop', n, r.x - 10, r.y - 10);
  }
}
