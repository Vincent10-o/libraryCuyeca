# Generated by Django 4.2.7 on 2023-12-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_summary_author_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_pages',
            field=models.IntegerField(default=0),
        ),
    ]