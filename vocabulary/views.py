import random
import json
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from . import words
from . import lessons


def index(request):
    return render(request, "index.html")


def add_word(request):
    return render(request, "word_add.html")


def send_word(request):
    if request.method == "POST":
        cache.clear()
        name = request.POST.get("new_name")
        translation = request.POST.get("new_translation")
        examples = request.POST.get("new_examples", "").replace(";", ",")
        context = {"name": name}
        if len(name) == 0:
            context["success"] = False
            context["comment"] = "Имя должно быть не пустым"
        elif len(translation) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(examples) == 0:
            context["success"] = False
            context["comment"] = "Примеры должны быть не пустыми"
        else:
            context["success"] = True
            context["comment"] = "Скорее выучите его"
            words.db_write_word(name, translation, examples)
        return render(request, "word_request.html", context)
    else:
        add_word(request)


def add_lesson(request):
    return render(request, "lesson_add.html")


def send_lesson(request):
    if request.method == "POST":
        cache.clear()
        name = request.POST.get("new_name")
        description = request.POST.get("new_description")
        date = request.POST.get("new_date")
        level = request.POST.get("new_level")
        context = {"name": name}
        if len(name) == 0:
            context["success"] = False
            context["comment"] = "Имя должно быть не пустым"
        elif len(description) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(date) == 0:
            context["success"] = False
            context["comment"] = "Дата должна быть не пустой"
        elif len(level) == 0:
            context["success"] = False
            context["comment"] = "Уровень должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Желаем успехов"
            lessons.db_write_lesson(name, description, date, level)
        return render(request, "lesson_request.html", context)
    else:
        add_word(request)


def word_list(request):
    words_all = words.db_get_words(all=True)
    words_all = sorted(words_all, key=lambda x: (x.is_learned, x.created))
    return render(request, "word_list.html", context={"words": words_all})


def start_studying(request):
    words_learned = words.db_get_words(learned=False)
    if len(words_learned) > 3:
        words_learned = random.sample(list(words_learned), 3)
    return render(request, "studying.html", context={"words": words_learned})


def change_learned_word(request):
    if request.method == "POST":
        cache.clear()
        data = json.loads(request.body)
        to_learned = True if data['to_learned'] == 1 else False
        word_id = int(data['word_id'])
        if words.db_change_learned_word(word_id=word_id, to_learned=to_learned):
            return HttpResponse("Успех!")
        else:
            return HttpResponse("Ошибка!")


def delete_word(request):
    if request.method == "POST":
        cache.clear()
        data = json.loads(request.body)
        if not data:
            return HttpResponse(status=404)
        word_id = int(data['word_id'])
        if words.db_delete_word(word_id):
            return HttpResponse("Успех")
        else:
            return HttpResponse(status=404)


def lesson_list(request):
    lessons_list = lessons.db_get_lessons()
    lessons_list = sorted(lessons_list, key=lambda x: x.date)
    return render(request, "lesson_list.html", context={"lessons": lessons_list})


def lesson_delete(request):
    if request.method == "POST":
        cache.clear()
        data = json.loads(request.body)
        if not data:
            return HttpResponse(status=404)
        lesson_id = int(data['lesson_id'])
        if lessons.db_delete_lesson(lesson_id):
            return HttpResponse("Успех")
        else:
            return HttpResponse(status=404)


def get_stats(request):
    stats = {}
    if request.method == "POST":
        cache.clear()
        start = request.POST.get("date_start")
        end = request.POST.get("date_end")
        if not start and not end:
            stats['total'] = words.db_get_num_words_with_period(period=False, learn_bitmask=0)
            stats['learned'] = words.db_get_num_words_with_period(period=False, learn_bitmask=1)
            stats['studying'] = words.db_get_num_words_with_period(period=False, learn_bitmask=2)
            stats['lessons'] = lessons.db_get_num_lessons_with_period(period=False)
        else:
            duration = {
                'start': start,
                'end': end
            }
            stats['duration'] = duration
            stats['total'] = words.db_get_num_words_with_period(start=start, end=end, period=True, learn_bitmask=0)
            stats['learned'] = words.db_get_num_words_with_period(start=start, end=end, period=True, learn_bitmask=1)
            stats['studying'] = words.db_get_num_words_with_period(start=start, end=end, period=True, learn_bitmask=2)
            stats['lessons'] = lessons.db_get_num_lessons_with_period(start=start, end=end, period=True)
    else:
        stats['total'] = words.db_get_num_words_with_period(period=False, learn_bitmask=0)
        stats['learned'] = words.db_get_num_words_with_period(period=False, learn_bitmask=1)
        stats['studying'] = words.db_get_num_words_with_period(period=False, learn_bitmask=2)
        stats['lessons'] = lessons.db_get_num_lessons_with_period(period=False)

    return render(request, "stats.html", context=stats)