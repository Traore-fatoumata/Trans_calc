from django.db import models
from django.core.validators import MinValueValidator

class Marchandise(models.Model):
    CARGAISON_TYPES = (
        ('R', 'Routière'),
        ('A', 'Aérienne'),
    )
    
    numero = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100, verbose_name="Nom de la marchandise")
    poids = models.FloatField(validators=[MinValueValidator(0.01)])
    volume = models.FloatField(validators=[MinValueValidator(0.01)])
    type_cargaison = models.CharField(max_length=1, choices=CARGAISON_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} ({self.numero}) - {self.get_type_cargaison_display()}"

class Cargaison(models.Model):
    CARGAISON_TYPES = (
        ('R', 'Routière'),
        ('A', 'Aérienne'),
    )
    
    type_cargaison = models.CharField(max_length=1, choices=CARGAISON_TYPES)
    distance = models.FloatField(validators=[MinValueValidator(1)])
    marchandises = models.ManyToManyField(Marchandise)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cargaison {self.id} ({self.get_type_cargaison_display()})"

    def poids_total(self):
        return sum(m.poids for m in self.marchandises.all())

    def volume_total(self):
        return sum(m.volume for m in self.marchandises.all())

    def calculer_cout(self):
        poids = self.poids_total()
        volume = self.volume_total()
        
        if self.type_cargaison == 'A':
            if volume < 80000:
                return 10 * self.distance * poids
            else:
                return 12 * self.distance * poids
        else:  # Routière
            if volume < 380000:
                return 4 * self.distance * poids
            else:
                return 6 * self.distance * poids