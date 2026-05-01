document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    if (!loginForm) {
        return;
    }

    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');
    const submitBtn = loginForm.querySelector('.login-btn');

    if (usernameField) {
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

    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const username = usernameField.value.trim();
        const password = passwordField.value;

        if (!username || !password) {
            alert('Veuillez remplir tous les champs');
            return;
        }

        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Connexion en cours...';
        submitBtn.disabled = true;

        try {
            const response = await fetch('/api/auth/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                window.location.href = data.redirect_url;
                return;
            }

            alert(data.detail || 'Identifiants invalides');
        } catch (error) {
            alert('Erreur de connexion. Veuillez réessayer.');
        } finally {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }
    });
});
