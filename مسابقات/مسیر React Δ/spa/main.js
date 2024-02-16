document.querySelectorAll('.navlink').forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const path = e.target.getAttribute('href');
    window.history.pushState({}, '', path);
    change(path);
  });
});

function change(path) {
  let text = '';
  switch (path) {
    case '/':
      text = 'به کوئرا خوش آمدید';
      break;
    case '/bootcamp':
      text = 'به بوت کمپ خوش آمدید';
      break;
    case '/college':
      text = 'به کالج خوش آمدید';
      break;
    case '/juniora':
      text = 'به جونیورا خوش آمدید';
      break;
  }
  document.querySelector('main').innerHTML = `<h1>${text}</h1>`;
}

window.addEventListener('popstate', () => {
  change(window.location.pathname);
});
