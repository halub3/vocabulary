# Generated by Django 4.2 on 2023-04-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0006_rename_learned_words_is_learned'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
