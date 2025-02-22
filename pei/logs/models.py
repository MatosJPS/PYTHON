from django.db import models





class Topic (models.Model):
    """UM ASSUNTO DE aPReNDIZAGEM"""
    text = models.CharField(max_length=200)
    """automaticamente vai ter a data de sistema"""
    date_added = models.DateTimeField(auto_now_add=True)

    """Mostrar painel Administrativo"""
    def __str__(self):
        return self.text


class Entry(models.Model):
    """informação espcifica se apagar apaga tudo"""
    Topico = models.ForeignKey (Topic, on_delete=models.CASCADE)
    text = models.TextField ()
    date_added = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """dEvolve uma rpresentação em string"""
        return self.text [:50] + '...'
    

    """Tabela de registo de colaboradoes"""

class colaboradores(models.Model):
    nome = models.CharField (max_length=20)
    apelido = models.CharField(max_length=20)
    matricula = models.CharField (max_length=10)
    dataRegisto = models.DateTimeField (auto_now_add=True)
   
    def __str__(self):
        return self.nome
        


"""Tabela de registo de acessos externos"""

class externos(models.Model):
    nome = models.CharField (max_length=20)
    apelido = models.CharField(max_length=20)
    matricula = models.CharField (max_length=10)
    empresa = models.CharField (max_length=50)
    dataRegisto = models.DateTimeField (auto_now_add=True)
   
    def __str__(self):
        return self.nome
        


"""Crio as entradas em chao de fabrica"""

class entradas(models.Model):
    nome = models.CharField (max_length=20)
    apelido = models.CharField(max_length=20)
    matricula = models.CharField (max_length=10)
    dataRegisto = models.DateTimeField (auto_now_add=True)
   
    def __str__(self):
        return self.nome
        

# Create your models here.

