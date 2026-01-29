// Fonctionnalités pour la page de connexion
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const username = form.querySelector('input[type="text"]').value;
            const password = form.querySelector('input[type="password"]').value;
            
            if (username.trim() === '' || password.trim() === '') {
                e.preventDefault();
                alert('Veuillez remplir tous les champs');
            }
        });
    }
});
