from django.db import models

class QuickContact(models.Model):
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_info