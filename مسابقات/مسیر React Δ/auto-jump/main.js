const inputs = document.querySelectorAll('input');

inputs.forEach((input) => {
  input.addEventListener('keyup', (e) => {
    const input = e.target;

    if (input.value.length === 4 && input.nextElementSibling) {
      input.nextElementSibling.focus();
    }
    if (
      e.key === 'Backspace' &&
      input.value.length === 0 &&
      input.previousElementSibling
    ) {
      input.previousElementSibling.focus();
    }
  });
});
