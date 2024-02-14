from django.db import models
from django.contrib.auth.models import User



class Resumo(models.Model):
    nome_completo = models.CharField(max_length=150, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    titulo_profissional = models.CharField(max_length=150, null=False, blank=False)
    descricao_pessoal = models.TextField(null=False, blank=False)
    resumo_experiencia_profissional = models.TextField(null=False, blank=False)
    # pago = models.BooleanField(default=True)
    usuario_edit = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_edit",
    )

    def __str__(self):
        return self.nome_completo
    
    def pago(self):
        return self.pago

# class Curriculo(models.Model):
#     curriculo = models.FileField(upload_to="curriculo/%Y/%m/%d/", blank=True)

# OPCOES_CATEGORIAO = [
#     ("Programador", "Desenvolvedor"),
#     ("Front-end", "front-end"),
#     ("Back-end", "back-end"),
#     ("Web Design", "web design" ),
#     ("Serviços gerais", "serviços gerais" ),
#     ("FREELANCER", "freelancer" ),
#     ("DIARISTAS", "diaristas" ),
# ]

# cargo = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')

