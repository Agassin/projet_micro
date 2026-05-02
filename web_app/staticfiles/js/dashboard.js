// Scripts spécifiques au tableau de bord professeur
document.addEventListener('DOMContentLoaded', function() {
    console.log('dashboard.js chargé');

    // Déconnexion : nettoie le localStorage (simulation) et retourne à l'accueil
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            localStorage.removeItem('moodle_access_history');
            localStorage.removeItem('moodle_access_count');
            window.location.href = '/';
        });
    }

    // Actions Moodle : ouvre une nouvelle fenêtre ou simule la connexion
    document.querySelectorAll('[data-moodle-action]').forEach(function(el){
        el.addEventListener('click', function(e){
            e.preventDefault();
            const action = el.getAttribute('data-moodle-action');
            // Remplacer ci-dessous par l'URL réelle Moodle si disponible
            const moodleUrl = 'https://moodle.org';
            window.open(moodleUrl, '_blank');

            // Enregistrer un log local pour afficher les stats
            const history = JSON.parse(localStorage.getItem('moodle_access_history') || '[]');
            history.push({ username: 'maman', role: 'teacher', action: action, timestamp: new Date().toISOString() });
            localStorage.setItem('moodle_access_history', JSON.stringify(history));

            const count = parseInt(localStorage.getItem('moodle_access_count') || '0', 10) + 1;
            localStorage.setItem('moodle_access_count', String(count));
        });
    });
});
