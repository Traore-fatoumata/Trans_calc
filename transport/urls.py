from django.urls import path
from .views import (
    home,
    MarchandiseListView, MarchandiseCreateView, MarchandiseUpdateView, MarchandiseDeleteView,
    CargaisonListView, CargaisonCreateView, CargaisonDeleteView,
    calculer_cout
)

urlpatterns = [
    path('', home, name='home'),
    path('marchandises/', MarchandiseListView.as_view(), name='marchandise_list'),
    path('marchandises/ajouter/', MarchandiseCreateView.as_view(), name='marchandise_create'),
    path('marchandises/<int:pk>/modifier/', MarchandiseUpdateView.as_view(), name='marchandise_update'),
    path('marchandises/<int:pk>/supprimer/', MarchandiseDeleteView.as_view(), name='marchandise_delete'),
    path('cargaisons/', CargaisonListView.as_view(), name='cargaison_list'),
    path('cargaisons/ajouter/', CargaisonCreateView.as_view(), name='cargaison_create'),
    path('cargaisons/<int:pk>/supprimer/', CargaisonDeleteView.as_view(), name='cargaison_delete'),
    path('cargaisons/<int:pk>/calcul/', calculer_cout, name='calculer_cout'),
    
]