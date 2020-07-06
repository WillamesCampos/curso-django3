from django.db import models


class Post(models.Model):

    class Categorias(models.TextChoices):
        TECH = 'TC', 'Technology'
        CR = 'CR', 'Curiosity'
        GR = 'GR', 'Geral'

    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR
    )
    deleted = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    def full_name(self): #não tem funcionalidade, só para fins didáticos
        return self.title + self.subtitle

    full_name.admin_order_field = 'title' # admin_order_field torna o campo ordenável no django admin

