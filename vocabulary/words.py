"""
Процедуры обращения к БД таблицы слов
"""
from vocabulary.models import Words


def db_get_words(learned=False, all=False):
    if all:
        return Words.objects.all()
    elif learned:
        return Words.objects.filter(is_learned=True)
    else:
        return Words.objects.filter(is_learned=False)


def db_write_word(new_name, new_translation, new_examples):
    word = Words(name=new_name, translation=new_translation, examples=new_examples)
    word.save()


def db_change_learned_word(word_id, to_learned):
    word = Words.objects.get(word_id=word_id)
    if word is None:
        return False
    word.is_learned = True if to_learned else False
    word.save()
    return True


def db_delete_word(word_id):
    word = Words.objects.get(word_id=word_id)
    if not word:
        return False
    word.delete()
    return True


def db_get_num_words_with_period(start=None, end=None, period=False, learn_bitmask=0):
    if period:
        match learn_bitmask:
            case 0:
                return len(Words.objects.filter(created__gte=start, created__lte=end))
            case 1:
                return len(Words.objects.filter(created__gte=start, created__lte=end, is_learned=True))
            case 2:
                return len(Words.objects.filter(created__gte=start, created__lte=end, is_learned=False))
    else:
        match learn_bitmask:
            case 0:
                return len(Words.objects.all())
            case 1:
                return len(Words.objects.filter(is_learned=True))
            case 2:
                return len(Words.objects.filter(is_learned=False))


def db_find_word_by_name(name, russ=True):
    if russ:
        print(Words.objects.filter(name=name))
        return Words.objects.filter(name=name)
    else:
        print(Words.objects.filter(translation=name))
        return Words.objects.filter(translation=name)

