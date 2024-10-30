# Generated by Django 5.1.2 on 2024-10-30 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("livros", "0002_alter_livro_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Emprestimo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_emprestimo",
                    models.DateField(
                        auto_now_add=True, verbose_name="Data de Empréstimo"
                    ),
                ),
                ("data_devolucao", models.DateField(verbose_name="Data de Devolução")),
                (
                    "data_prevista_devolucao",
                    models.DateTimeField(verbose_name="Data Prevista de Devolução"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Aberto", "Aberto"), ("Fechado", "Fechado")],
                        max_length=50,
                        verbose_name="Status",
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="livros.livro",
                        verbose_name="Livro",
                    ),
                ),
            ],
            options={
                "verbose_name": "Empréstimo",
                "verbose_name_plural": "Empréstimos",
                "ordering": ["data_emprestimo"],
            },
        ),
    ]
