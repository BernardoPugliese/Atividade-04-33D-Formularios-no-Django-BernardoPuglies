# Generated by Django 3.2.13 on 2023-09-15 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaiorPublico23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('date', models.DateField(null=True)),
                ('publico', models.IntegerField(null=True)),
                ('presence', models.CharField(choices=[('N', 'Não estive presente'), ('S', 'Estive presente')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game', models.IntegerField(null=True)),
                ('position', models.CharField(max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Títulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('importancia', models.CharField(choices=[('M', 'Muito Importante'), ('I', 'Importante'), ('P', 'Pouco Importante')], max_length=1, null=True)),
                ('quantidade', models.IntegerField(null=True)),
                ('watched', models.CharField(choices=[('A', 'Assisti'), ('N', 'Não assisti'), ('P', 'Não assisti todos')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ídolos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=70, null=True)),
                ('born_date', models.DateField(null=True)),
                ('birth_place', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
