from django.db import models

#implementação com o banco

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True) #guarda a data automaticamente
    def __str__(self): # mostra o nome email ao inves de cadastro object
        return f'{self.nome} [{self.email}]'

    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data']
