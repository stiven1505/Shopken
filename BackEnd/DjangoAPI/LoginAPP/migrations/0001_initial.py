# Generated by Django 4.1.11 on 2023-09-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('UsuariosId', models.AutoField(primary_key=True, serialize=False)),
                ('UsuarioName', models.CharField(max_length=500)),
                ('Password', models.CharField(max_length=500)),
            ],
        ),
    ]