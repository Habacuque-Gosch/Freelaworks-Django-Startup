from django.db import models



class Curriculo(models.Model):
    curriculo = models.FileField(upload_to="curriculo/%Y/%m/%d/", blank=True)