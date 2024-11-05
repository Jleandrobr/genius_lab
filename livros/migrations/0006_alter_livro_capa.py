# Generated by Django 5.1.2 on 2024-11-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livros", "0005_livro_capa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="capa",
            field=models.ImageField(
                blank=True, null=True, upload_to="capas", verbose_name="Capa do Livro"
            ),
        ),
    ]