const themeSwitchBtn = document.getElementById('themeSwitch');
const docStyle = document.documentElement.style;

function applyTheme() {
    const currentTheme = localStorage.getItem('theme') || 'dark';

    if (currentTheme == 'dark') {
        docStyle.setProperty('--text', 'var(--text-white)');
        docStyle.setProperty('--bg', 'var(--dark-bg)')
    } else {
        docStyle.setProperty('--text', 'var(--text-black)');
        docStyle.setProperty('--bg', 'var(--light-bg');
    }

    if (themeSwitchBtn) {
        themeSwitchBtn.innerText = currentTheme == 'dark' ? 'Turn on lights' : 'Turn off lights';
    }
}

function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'dark';
    const newTheme = currentTheme == 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', newTheme);
    applyTheme();
}

if (themeSwitchBtn) {
    themeSwitchBtn.addEventListener('click', toggleTheme);
}

applyTheme();