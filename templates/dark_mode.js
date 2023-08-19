function toggleTheme() {
    const htmlTag = document.querySelector('html');
    const currentTheme = htmlTag.getAttribute('data-bs-theme');
    const button = document.getElementById('themeToggle');

    if (currentTheme === 'dark') {
        htmlTag.setAttribute('data-bs-theme', 'light');
        button.innerText = 'Dark Mode';
        button.classList.remove('btn-outline-light');
        button.classList.add('btn-outline-dark');
    } else {
        htmlTag.setAttribute('data-bs-theme', 'dark');
        button.innerText = 'Light Mode';
        button.classList.remove('btn-outline-dark');
        button.classList.add('btn-outline-light');
    }
}