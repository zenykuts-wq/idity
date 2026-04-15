from django.db import models

class QuickContact(models.Model):
    # Одне поле для телефону або пошти
    contact_info = models.CharField(max_length=255, verbose_name="Контактні дані")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_info