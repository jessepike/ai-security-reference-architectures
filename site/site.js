const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');
if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
}

document.querySelectorAll('.nav-menu > button').forEach((button) => {
  button.addEventListener('click', () => button.setAttribute('aria-expanded', String(button.getAttribute('aria-expanded') !== 'true')));
});

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
