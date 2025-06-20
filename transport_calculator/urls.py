from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from transport import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='home'),  # Page d'accueil redirigeant vers la page de connexion
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transport', include('transport.urls')),  # Vos URLs d'application
    path('accounts/register/', views.register, name='register'),
    # URLs d'authentification
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='home'  # Assurez-vous que 'home' est défini dans vos URLs
    ), name='logout'),
]