# Generated by Django 5.1.2 on 2024-10-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emprestimo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emprestimo",
            name="data_devolucao",
            field=models.DateField(
                blank=True, null=True, verbose_name="Data de Devolução"
            ),
        ),
    ]