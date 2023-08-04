from django.db import models
from django.urls import reverse

# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

   
class Livre(models.Model):
    """Model definition for Livre."""
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="image")
    auteur = models.CharField(max_length=50)
    document = models.FileField(upload_to='documents/')
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Livre."""

        verbose_name = 'Livre'
        verbose_name_plural = 'Livres'

    def __str__(self):
        return self.nom
    
    #def def get_absolute_url(self):
       # return reverse('Biblio', args=[self.pk])

