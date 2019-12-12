from django.db import models

# Create your models here.
class Comments(models.Model):
    user    = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True) # initially created saved only
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'
