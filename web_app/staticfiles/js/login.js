document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;

            if (username && password) {
                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('username', username);

                const submitBtn = loginForm.querySelector('.login-btn');
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Connexion en cours...';
                submitBtn.disabled = true;

                setTimeout(() => {
                    if (username.toLowerCase() === 'maman') {
                        window.location.href = 'dashboard.html'; // Version professeur
                    } else {
                        window.location.href = 'eleve.html'; // Version élève
                    }
                }, 1000);
            } else {
                alert('Veuillez remplir tous les champs');
            }
        });
    }

    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');

    if (usernameField && passwordField) {
        usernameField.value = localStorage.getItem('lastUsername') || '';

        if (!usernameField.value) {
            usernameField.focus();
        }

        usernameField.addEventListener('blur', function() {
            if (this.value.trim()) {
                localStorage.setItem('lastUsername', this.value.trim());
            }
        });
    }
});