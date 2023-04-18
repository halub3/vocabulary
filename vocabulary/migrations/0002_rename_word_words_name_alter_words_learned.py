# Generated by Django 4.2 on 2023-04-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='words',
            old_name='word',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='words',
            name='learned',
            field=models.BooleanField(default=False),
        ),
    ]