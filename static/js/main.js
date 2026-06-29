const navToggle = document.querySelector('.nav-toggle');

if (navToggle) {
  navToggle.addEventListener('change', () => {
    document.body.classList.toggle('nav-open', navToggle.checked);
  });
}
