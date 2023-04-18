from django.db import models


class Words(models.Model):
    word_id = models.AutoField(db_column='wordId', primary_key=True)
    name = models.TextField()
    translation = models.TextField()
    examples = models.TextField()
    is_learned = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    class Meta:
        db_table = 'words'


class Lessons(models.Model):
    lesson_id = models.AutoField(db_column='lessonId', primary_key=True)
    name = models.TextField()
    description = models.TextField()
    date = models.DateField()
    level = models.TextField()
    created = models.DateField(auto_now=True)

    class Meta:
        db_table = 'lessons'
