from django.db import models


class Pessoa(models.Model):
    documento = models.CharField(db_index=True, max_length=14, primary_key=True)
    nome = models.CharField(max_length=60)

    cnh = models.CharField(max_length=11, null=True)
    # CPF, RG ?

    def __eq__(self, other):
        if other:
            return (self.documento == other.documento and self.nome == other.nome)
        return False

    class Meta:
        abstract = True
