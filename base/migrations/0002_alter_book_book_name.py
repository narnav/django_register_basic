# Generated by Django 5.0.1 on 2024-01-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
