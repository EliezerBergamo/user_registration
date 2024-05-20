from django.db import models


class User (models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=70,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    email_funcional = models.EmailField(
        max_length=50,
        null=False,
        blank=False
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )
