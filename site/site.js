document.documentElement.classList.add('js');

const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');
if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
}

const navMenus = [...document.querySelectorAll('[data-nav-menu]')];
navMenus.forEach((menu) => {
  menu.addEventListener('toggle', () => {
    if (!menu.open) return;
    navMenus.forEach((other) => { if (other !== menu) other.open = false; });
  });
});

document.addEventListener('click', (event) => {
  if (event.target.closest('.site-header')) return;
  navMenus.forEach((menu) => { menu.open = false; });
  nav?.classList.remove('is-open');
  navToggle?.setAttribute('aria-expanded', 'false');
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  if (document.querySelector('.image-dialog[open]')) return;
  const openMenu = navMenus.find((menu) => menu.open);
  if (openMenu) {
    openMenu.open = false;
    openMenu.querySelector('summary')?.focus();
    return;
  }
  if (nav?.classList.contains('is-open')) {
    nav.classList.remove('is-open');
    navToggle?.setAttribute('aria-expanded', 'false');
    navToggle?.focus();
  }
});

nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
  nav.classList.remove('is-open');
  navToggle?.setAttribute('aria-expanded', 'false');
}));

const dialog = document.querySelector('.image-dialog');
const dialogImage = dialog?.querySelector('img');
const close = () => dialog?.close();
document.querySelectorAll('[data-full-image]').forEach((trigger) => {
  trigger.addEventListener('click', () => {
    if (!dialog || !dialogImage) return;
    dialogImage.src = trigger.dataset.fullImage;
    dialogImage.alt = trigger.dataset.fullAlt || '';
    dialog.showModal();
  });
});
dialog?.querySelector('.image-dialog-close')?.addEventListener('click', close);
dialog?.addEventListener('click', (event) => { if (event.target === dialog) close(); });

const walkthroughArticle = document.querySelector('[data-walkthrough]');
if (walkthroughArticle) {
  const stops = [...walkthroughArticle.querySelectorAll('[data-walkthrough-stop]')];
  const links = [...document.querySelectorAll('[data-walkthrough-link]')];
  const progress = document.querySelector('.walkthrough-progress');
  const previous = document.querySelector('[data-walkthrough-previous]');
  const next = document.querySelector('[data-walkthrough-next]');

  document.body.classList.add('walkthrough-enhanced');

  const targetFromHash = () => {
    if (!location.hash) return null;
    try { return document.getElementById(decodeURIComponent(location.hash.slice(1))); }
    catch { return null; }
  };

  const stopFromHash = () => targetFromHash()?.closest('[data-walkthrough-stop]') || stops[0];

  const showStop = (stop, moveFocus = false, requestedTarget = null) => {
    const index = Math.max(0, stops.indexOf(stop));
    stops.forEach((item, itemIndex) => { item.hidden = itemIndex !== index; });
    links.forEach((link, itemIndex) => {
      if (itemIndex === index) link.setAttribute('aria-current', 'step');
      else link.removeAttribute('aria-current');
    });
    if (progress) progress.textContent = `Conversation stop ${index + 1} of ${stops.length}`;
    if (previous) previous.disabled = index === 0;
    if (next) {
      next.disabled = index === stops.length - 1;
      next.textContent = index === stops.length - 1 ? 'Walkthrough complete' : 'Next';
    }
    if (moveFocus) {
      const focusTarget = requestedTarget || stop.querySelector('h2');
      focusTarget?.closest('details')?.setAttribute('open', '');
      focusTarget?.setAttribute('tabindex', '-1');
      focusTarget?.focus({ preventScroll: true });
      focusTarget?.scrollIntoView({ block: 'start', behavior: 'auto' });
    }
  };

  const move = (offset) => {
    const current = stops.indexOf(stopFromHash());
    const target = stops[Math.min(stops.length - 1, Math.max(0, current + offset))];
    const heading = target?.querySelector('h2');
    if (heading) {
      history.pushState(null, '', `#${heading.id}`);
      showStop(target, true, heading);
    }
  };

  links.forEach((link) => {
    link.addEventListener('click', (event) => {
      const target = document.getElementById(link.hash.slice(1));
      const stop = target?.closest('[data-walkthrough-stop]');
      if (!stop) return;
      event.preventDefault();
      history.pushState(null, '', link.hash);
      showStop(stop, true, target);
    });
  });
  previous?.addEventListener('click', () => move(-1));
  next?.addEventListener('click', () => move(1));
  window.addEventListener('popstate', () => showStop(stopFromHash(), true, targetFromHash()));
  showStop(stopFromHash(), Boolean(location.hash), targetFromHash());

  walkthroughArticle.querySelectorAll('[data-copy-template]').forEach((button) => {
    button.addEventListener('click', async () => {
      const actions = button.closest('.template-actions');
      const heading = actions?.previousElementSibling;
      const parts = heading ? [heading.textContent.trim()] : [];
      let node = actions?.nextElementSibling;
      while (node && !node.matches('h2, h3, details')) {
        parts.push(node.innerText.trim());
        node = node.nextElementSibling;
      }
      const status = actions?.querySelector('[role="status"]');
      try {
        await navigator.clipboard.writeText(parts.filter(Boolean).join('\n\n'));
        if (status) status.textContent = 'Copied.';
      } catch {
        if (status) status.textContent = 'Copy failed. Use the Markdown download.';
      }
    });
  });

  let printDetails = [];
  window.addEventListener('beforeprint', () => {
    printDetails = [...walkthroughArticle.querySelectorAll('details')].map((detail) => detail.open);
    walkthroughArticle.querySelectorAll('details').forEach((detail) => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => {
    walkthroughArticle.querySelectorAll('details').forEach((detail, index) => { detail.open = printDetails[index] ?? false; });
  });
}
