from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Vagas(models.Model):

    OPCOES_CATEGORIAO = [
        ("PJ", "pj"),
        ("FREELANCER", "freelancer" ),
        ("DIARISTAS", "diaristas" ),
    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    numero_telefone = models.CharField(max_length=20, null=False, blank=False)
    tipo_de_vaga = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')
    descricao = models.TextField(null=False, blank=False)
    local = models.CharField(max_length=200, null=False, blank=False)
    salario = models.CharField(max_length=20, null=False, blank=False)
    publicada = models.BooleanField(default=True)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.nome

# # OPCOES_CATEGORIAO = [
#     ("CLT", "clt"),
#     ("PJ", "pj"),
#     ("MENOR APRENDIZ", "menor aprendiz" ),
#     ("ESTAGIO", "estagio" ),
#     ("FREELANCER", "freelancer" ),
#     ("DIARISTAS", "diaristas" ),
# # ]