# Generated by Django 5.1.2 on 2024-11-05 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "verbose_name": "Perfil do usuário",
                "verbose_name_plural": "Perfis dos usuários",
            },
        ),
    ]
