# Generated by Django 4.2 on 2023-04-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('word_id', models.AutoField(db_column='wordId', primary_key=True, serialize=False)),
                ('word', models.TextField()),
                ('translation', models.TextField()),
                ('learned', models.BooleanField()),
            ],
            options={
                'db_table': 'words',
            },
        ),
    ]
