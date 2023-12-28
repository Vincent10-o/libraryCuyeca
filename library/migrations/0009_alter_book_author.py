# Generated by Django 4.2.7 on 2023-12-27 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_number_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, default='No hay un autor asociado', null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author'),
        ),
    ]
