# Generated by Django 4.2.4 on 2023-09-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.PositiveIntegerField()),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('mensalidade_paga', models.BooleanField(default=True)),
            ],
        ),
    ]