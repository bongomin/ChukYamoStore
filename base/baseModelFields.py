from  django.admin import models

class SharedFields(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstruct = True