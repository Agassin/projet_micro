// script.js - Gestion de la connexion et des sessions

document.addEventListener('DOMContentLoaded', function() {
    // Variables globales
    const currentUser = localStorage.getItem('username');
    const isProfessor = localStorage.getItem('user_role') === 'professor';

    // 1. Gestion de la page de connexion (login.html)
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;

            if (username && password) {
                // Stocker les informations de connexion
                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('username', username);
                localStorage.setItem('last_login', new Date().toISOString());

                // Déterminer le rôle
                const role = username.toLowerCase() === 'maman' ? 'professor' : 'student';
                localStorage.setItem('user_role', role);

                // Animation de chargement
                const submitBtn = loginForm.querySelector('.login-btn');
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Connexion en cours...';
                submitBtn.disabled = true;

                // Redirection après 1 seconde
                setTimeout(() => {
                    if (role === 'professor') {
                        window.location.href = 'dashboard.html';
                    } else {
                        window.location.href = 'eleve.html';
                    }
                }, 1000);
            } else {
                alert('Veuillez remplir tous les champs');
            }
        });

        // Pré-remplissage pour les tests
        document.getElementById('username').value = 'maman';
        document.getElementById('password').value = 'test123';
    }

    // 2. Vérification de connexion pour les pages protégées
    const protectedPages = ['dashboard.html', 'eleve.html'];
    const currentPage = window.location.pathname.split('/').pop();

    if (protectedPages.includes(currentPage)) {
        const isLoggedIn = localStorage.getItem('isLoggedIn');
        if (!isLoggedIn) {
            window.location.href = 'login.html';
            return;
        }

        // Mettre à jour l'affichage de l'utilisateur
        updateUserDisplay();

        // Gestion de la déconnexion
        setupLogoutButtons();
    }

    // 3. Gestion des déconnexions
    function setupLogoutButtons() {
        const logoutBtns = document.querySelectorAll('#logoutBtn, #logoutBtnEleve');

        logoutBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                // Confirmation de déconnexion
                if (confirm('Êtes-vous sûr de vouloir vous déconnecter ?')) {
                    // Effacer les données de session
                    localStorage.removeItem('isLoggedIn');
                    localStorage.removeItem('username');
                    localStorage.removeItem('user_role');
                    localStorage.removeItem('moodle_username');
                    localStorage.removeItem('moodle_password');

                    // Redirection vers la page d'accueil
                    window.location.href = 'index.html';
                }
            });
        });
    }

    // 4. Mettre à jour l'affichage utilisateur
    function updateUserDisplay() {
        const userElements = document.querySelectorAll('#currentUser, .user-info span');
        const userAvatar = document.querySelector('.user-avatar');

        if (currentUser && userElements.length > 0) {
            userElements.forEach(element => {
                if (element.id === 'currentUser' || element.classList.contains('user-info')) {
                    element.textContent = currentUser;
                }
            });
        }

        // Initiales pour l'avatar
        if (userAvatar && currentUser) {
            const initials = currentUser.charAt(0).toUpperCase();
            userAvatar.textContent = initials;
            userAvatar.style.backgroundColor = isProfessor ? '#3a86ff' : '#38b000';
        }
    }

    // 5. Animation des cartes au survol
    const cards = document.querySelectorAll('.activity-card, .info-card, .tool-card, .eleve-card, .cours-card, .feature-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // 6. Mettre à jour la date actuelle dans les headers
    updateCurrentDate();

    // 7. Gestion des cartes Moodle
    setupMoodleCards();

    // Fonctions utilitaires
    function updateCurrentDate() {
        const today = new Date();
        const dateString = today.toLocaleDateString('fr-FR', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        // Mettre à jour la date dans les tableaux de bord
        const headers = document.querySelectorAll('.dashboard-header h2, .eleve-header h2');

        headers.forEach(header => {
            const dateElement = document.createElement('div');
            dateElement.className = 'current-date';
            dateElement.innerHTML = `<i class="far fa-calendar"></i> ${dateString}`;
            dateElement.style.cssText = 'color: rgba(255,255,255,0.8); font-size: 0.9rem; margin-top: 5px;';
            header.insertAdjacentElement('afterend', dateElement);
        });
    }

    function setupMoodleCards() {
        // Sélectionner toutes les cartes qui doivent ouvrir Moodle
        const moodleCards = document.querySelectorAll('[data-moodle-action]');

        moodleCards.forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();

                const action = this.getAttribute('data-moodle-action');
                const username = localStorage.getItem('username') || 'guest';
                const isProfessor = localStorage.getItem('user_role') === 'professor';

                // Animation de chargement
                const originalContent = this.innerHTML;
                this.innerHTML = '<div style="text-align: center;"><i class="fas fa-spinner fa-spin"></i><br>Connexion à Moodle...</div>';
                this.style.cursor = 'wait';
                this.style.opacity = '0.7';

                // Générer les identifiants Moodle
                const moodleCredentials = generateMoodleCredentials(username, isProfessor);

                // Stocker temporairement
                localStorage.setItem('temp_moodle_user', moodleCredentials.username);
                localStorage.setItem('temp_moodle_pass', moodleCredentials.password);

                // Ouvrir Moodle après un délai
                setTimeout(() => {
                    openMoodleWithAutoLogin(moodleCredentials, action);

                    // Restaurer la carte
                    setTimeout(() => {
                        this.innerHTML = originalContent;
                        this.style.cursor = 'pointer';
                        this.style.opacity = '1';
                    }, 1500);
                }, 800);
            });
        });
    }

    function generateMoodleCredentials(username, isProfessor) {
        // Générer des identifiants uniques mais reproductibles
        const baseUsername = username.toLowerCase().replace(/[^a-z0-9]/g, '');
        const roleSuffix = isProfessor ? '_prof' : '_eleve';
        const randomSuffix = Math.random().toString(36).substring(2, 6);

        const moodleUsername = `mathman_${baseUsername}${roleSuffix}_${randomSuffix}`;
        const moodlePassword = `Moodle${username.slice(0, 1).toUpperCase()}${Date.now().toString(36).slice(-6)}!`;

        return {
            username: moodleUsername,
            password: moodlePassword,
            role: isProfessor ? 'professor' : 'student'
        };
    }

    function openMoodleWithAutoLogin(credentials, action = 'courses') {
        const moodleBaseUrl = 'https://camalexylan.moodlecloud.com';
        let targetUrl = moodleBaseUrl;

        // Déterminer l'URL cible selon l'action
        switch(action) {
            case 'virtual-class':
                targetUrl += '/mod/bigbluebuttonbn/view.php';
                break;
            case 'resources':
                targetUrl += '/course/resources.php';
                break;
            case 'courses':
            default:
                targetUrl += '/my/courses.php';
        }

        // Créer un formulaire pour l'auto-connexion
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = targetUrl;
        form.target = '_blank';
        form.style.display = 'none';

        // Champs d'authentification
        const fields = [
            { name: 'username', value: credentials.username },
            { name: 'password', value: credentials.password },
            { name: 'rememberusername', value: '1' }
        ];

        fields.forEach(field => {
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = field.name;
            input.value = field.value;
            form.appendChild(input);
        });

        // Ajouter au DOM et soumettre
        document.body.appendChild(form);
        form.submit();

        // Nettoyer après 2 secondes
        setTimeout(() => {
            if (document.body.contains(form)) {
                document.body.removeChild(form);
            }
        }, 2000);

        // Log de l'accès Moodle
        logMoodleAccess(credentials.username, action);
    }

    function logMoodleAccess(username, action) {
        const accessLog = {
            username: currentUser,
            moodleUsername: username,
            action: action,
            timestamp: new Date().toISOString(),
            role: isProfessor ? 'professor' : 'student'
        };

        // Récupérer l'historique existant
        let accessHistory = JSON.parse(localStorage.getItem('moodle_access_history') || '[]');
        accessHistory.push(accessLog);

        // Garder seulement les 50 derniers accès
        if (accessHistory.length > 50) {
            accessHistory = accessHistory.slice(-50);
        }

        // Sauvegarder
        localStorage.setItem('moodle_access_history', JSON.stringify(accessHistory));

        // Mettre à jour le compteur
        updateAccessCounter();
    }

    function updateAccessCounter() {
        let count = parseInt(localStorage.getItem('moodle_access_count') || '0');
        count++;
        localStorage.setItem('moodle_access_count', count.toString());
    }

    // 8. Initialisation des badges Moodle
    initializeMoodleBadges();

    function initializeMoodleBadges() {
        const accessCount = localStorage.getItem('moodle_access_count');
        if (accessCount && parseInt(accessCount) > 0) {
            // Ajouter un badge sur les cartes Moodle
            const moodleCards = document.querySelectorAll('[data-moodle-action]');
            moodleCards.forEach(card => {
                const badge = document.createElement('div');
                badge.className = 'moodle-access-badge';
                badge.textContent = `${accessCount}`;
                badge.title = `${accessCount} accès à Moodle`;
                badge.style.cssText = `
                    position: absolute;
                    top: -8px;
                    right: -8px;
                    background: #ff006e;
                    color: white;
                    border-radius: 50%;
                    width: 20px;
                    height: 20px;
                    font-size: 0.7rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                `;

                card.style.position = 'relative';
                if (!card.querySelector('.moodle-access-badge')) {
                    card.appendChild(badge);
                }
            });
        }
    }

    // 9. Afficher les statistiques Moodle si disponibles
    displayMoodleStats();

    function displayMoodleStats() {
        if (isProfessor) {
            const accessHistory = JSON.parse(localStorage.getItem('moodle_access_history') || '[]');
            const studentAccess = accessHistory.filter(log => log.role === 'student').length;
            const professorAccess = accessHistory.filter(log => log.role === 'professor').length;

            if (accessHistory.length > 0) {
                console.log(`📊 Statistiques Moodle:`);
                console.log(`   Total des accès: ${accessHistory.length}`);
                console.log(`   Accès élèves: ${studentAccess}`);
                console.log(`   Accès professeur: ${professorAccess}`);

                // Optionnel: afficher dans l'interface
                const statsElement = document.getElementById('moodleStats');
                if (statsElement) {
                    statsElement.innerHTML = `
                        <small>Moodle: ${accessHistory.length} accès (${studentAccess} élèves)</small>
                    `;
                }
            }
        }
    }

    // 10. Gestion du retour à l'accueil depuis les pages de connexion
    const homeButtons = document.querySelectorAll('[data-go-home]');
    homeButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            window.location.href = 'index.html';
        });
    });
});