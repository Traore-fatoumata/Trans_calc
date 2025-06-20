from django.test import TestCase
from django.urls import reverse
from .models import Marchandise, Cargaison

class TransportTests(TestCase):
    def setUp(self):
        # Créez des données de test
        self.marchandise_aerienne = Marchandise.objects.create(
            numero="M001", poids=10, volume=50000, type_cargaison="A"
        )
        self.marchandise_routiere = Marchandise.objects.create(
            numero="M002", poids=20, volume=400000, type_cargaison="R"
        )

    def test_creation_marchandise(self):
        """Teste la création d'une marchandise."""
        self.assertEqual(Marchandise.objects.count(), 2)

    def test_calcul_cout_aerien(self):
        """Teste le calcul pour une cargaison aérienne."""
        cargaison = Cargaison.objects.create(type_cargaison="A", distance=300)
        cargaison.marchandises.add(self.marchandise_aerienne)
        cout = cargaison.calculer_cout()
        self.assertEqual(cout, 10 * 300 * 10)  # 10 × distance × poids

    def test_calcul_cout_routier_volume_eleve(self):
        """Teste le calcul pour une cargaison routière avec volume élevé."""
        cargaison = Cargaison.objects.create(type_cargaison="R", distance=200)
        cargaison.marchandises.add(self.marchandise_routiere)
        cout = cargaison.calculer_cout()
        self.assertEqual(cout, 6 * 200 * 20)  # 6 × distance × poids (car volume > 380000)

    def test_vues(self):
        """Teste l'accès aux pages."""
        urls = [
            reverse("home"),
            reverse("marchandise_list"),
            reverse("cargaison_list"),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)