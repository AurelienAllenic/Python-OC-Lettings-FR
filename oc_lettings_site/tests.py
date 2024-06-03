from django.test import TestCase, Client
from django.test.utils import override_settings
from django.urls import reverse


class ErrorPagesTests(TestCase):
    def setUp(self):
        # Client est une instance de classe pour faire des requêtes de test
        self.client = Client()

    @override_settings(DEBUG=False)
    def test_404_error_page(self):
        # Fait une requête à une URL qui n'existe pas
        response = self.client.get('/nonsense')
        # Vérifie que la réponse est bien une erreur 404
        self.assertEqual(response.status_code, 404)
        # Vérifie que le bon template est utilisé pour la page 404
        self.assertTemplateUsed(response, 'oc_lettings_site/404.html')
    
    @override_settings(DEBUG=False)
    def test_500_error_page(self):
            # Après l'exception, nous devons récupérer la réponse du gestionnaire d'erreur 500
            response = self.client.get(reverse('get_500'))
            # Vérifier que la réponse est bien une erreur 500
            self.assertEqual(response.status_code, 500)


class IndexPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
