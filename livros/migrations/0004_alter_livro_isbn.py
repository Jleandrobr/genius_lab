# Generated by Django 5.1.2 on 2024-10-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livros", "0003_alter_livro_isbn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="isbn",
            field=models.CharField(
                editable=False, max_length=13, unique=True, verbose_name="ISBN"
            ),
        ),
    ]
