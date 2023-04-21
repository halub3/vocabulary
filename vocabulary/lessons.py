"""
Процедуры обращения к БД таблицы уроков
"""
from vocabulary.models import Lessons


def db_write_lesson(new_name, new_description, new_date, new_level):
    lesson = Lessons(name=new_name, description=new_description, date=new_date, level=new_level)
    lesson.save()


def db_get_lessons():
    return Lessons.objects.all()


def db_delete_lesson(lesson_id):
    lesson = Lessons.objects.get(lesson_id=lesson_id)
    if not lesson:
        return False
    lesson.delete()
    return True


def db_get_num_lessons_with_period(start=None, end=None, period=False):
    if period:
        return len(Lessons.objects.filter(date__gte=start, date__lte=end))
    else:
        return len(Lessons.objects.all())