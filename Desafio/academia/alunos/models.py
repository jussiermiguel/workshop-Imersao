from django.db import models

# Definindo um modelo chamado Aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=255)# Campo para o nome do aluno (máximo de 255 caracteres)
    idade = models.PositiveIntegerField()# Campo para a idade do aluno (somente números inteiros positivos)
    data_de_nascimento = models.DateField(null=True, blank=True)# Campo para a data de nascimento do aluno (pode ser nulo e em branco)
    cpf = models.CharField(max_length=14, unique=True) # Campo para o CPF do aluno (único)
    SEXO_CHOICES = (      
         # Opções para o campo de sexo do aluno (escolhas pré-definidas)          
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    mensalidade_paga = models.BooleanField(default=True, help_text="Indica se a mensalidade do aluno está paga ou não.")
   
    # Método que retorna uma representação em string do objeto Aluno
    def __str__(self):
        return self.nome