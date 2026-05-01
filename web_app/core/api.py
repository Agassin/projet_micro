from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthLoginAPIView(APIView):
    """API d'authentification pour la connexion utilisateur.

    Les identifiants sont actuellement codés en dur pour la phase de test.
    """

    authentication_classes = []
    permission_classes = []

    HARD_CODED_CREDENTIALS = {
        'maman': {
            'password': 'test123',
            'redirect_url': '/dashboard/'
        },
        'eleve': {
            'password': 'test123',
            'redirect_url': '/eleve/'
        }
    }

    def post(self, request, *args, **kwargs):
        username = str(request.data.get('username', '')).strip()
        password = str(request.data.get('password', ''))

        if not username or not password:
            return Response(
                {'success': False, 'detail': 'Veuillez fournir un identifiant et un mot de passe.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = self.HARD_CODED_CREDENTIALS.get(username)
        if user is None or user['password'] != password:
            return Response(
                {'success': False, 'detail': 'Identifiants invalides.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {'success': True, 'redirect_url': user['redirect_url']},
            status=status.HTTP_200_OK
        )
