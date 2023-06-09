# Generated by Django 4.2 on 2023-04-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0004_words_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('lesson_id', models.AutoField(db_column='lessonId', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('level', models.TextField()),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
    ]
