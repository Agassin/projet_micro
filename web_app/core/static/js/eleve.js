// Scripts spécifiques à l'espace élève
document.addEventListener('DOMContentLoaded', function() {
    console.log('eleve.js chargé');

    const logoutBtn = document.getElementById('logoutBtnEleve');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            // simulation déconnexion
            window.location.href = '/';
        });
    }

    // Ajouter écouteurs sur les cartes Moodle pour stocker un accès élève
    document.querySelectorAll('[data-moodle-action]').forEach(function(el){
        el.addEventListener('click', function(e){
            e.preventDefault();
            const action = el.getAttribute('data-moodle-action');
            const moodleUrl = 'https://moodle.org';
            window.open(moodleUrl, '_blank');

            const username = document.getElementById('currentUser') ? document.getElementById('currentUser').textContent : 'eleve';
            const history = JSON.parse(localStorage.getItem('moodle_access_history') || '[]');
            history.push({ username: username, role: 'student', action: action, timestamp: new Date().toISOString(), moodleUsername: username + '_moodle' });
            localStorage.setItem('moodle_access_history', JSON.stringify(history));

            const count = parseInt(localStorage.getItem('moodle_access_count') || '0', 10) + 1;
            localStorage.setItem('moodle_access_count', String(count));
        });
    });
});
