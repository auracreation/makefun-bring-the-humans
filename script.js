const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
const mobile = window.matchMedia('(max-width: 767px)');

function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.hidden = mobile.matches;
}

menuButton.hidden = false;
closeMenu();
mobile.addEventListener('change', closeMenu);
menuButton.addEventListener('click', () => {
  const opening = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(opening));
  navigation.hidden = !opening;
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});

const copyButton = document.querySelector('.copy-button');
const copyStatus = document.querySelector('#copy-status');
let statusTimeout;
copyButton.addEventListener('click', async () => {
  clearTimeout(statusTimeout);
  try {
    await navigator.clipboard.writeText('https://make.fun/r/z1j4n66g');
    copyStatus.textContent = 'Referral link copied.';
  } catch {
    copyStatus.textContent = 'Copy unavailable. Select the visible link to copy it manually.';
  }
  statusTimeout = setTimeout(() => { copyStatus.textContent = ''; }, 5000);
});
