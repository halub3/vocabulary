function showTranslation(obj) {
        let translation = document.getElementById(obj.name);
        if(obj.dataset.translate == 1){
            obj.textContent = 'Скрыть перевод';
            obj.dataset.translate = 0;
            translation.style.display = 'block';
        } else {
            obj.textContent = 'Показать перевод';
            obj.dataset.translate = 1;
            translation.style.display = 'none';
        }
    }

async function wordStudyingLearned(obj) {
    obj.disabled = true;
    obj.style.backgroundColor = 'green';
    obj.style.color = 'white';

    let response = await fetch('/change-learned', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({word_id: obj.id, to_learned: 1})
      });
    if (response.ok) {
        let answer = await response.text();
        alert(answer);
    } else {
        alert("Произошла ошибка");
    }
}

async function deleteLesson(obj) {
    let response = await fetch('/delete-lesson', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({lesson_id: obj.name})
      });
    if (response.ok) {
        alert("Урок удален");
        location. reload()
    } else {
        alert("Произошла ошибка удаления");
    }
}

async function deleteWord(obj) {
    let response = await fetch('/delete-word', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({word_id: obj.name})
      });
    if (response.ok) {
        alert("Слово удалено");
        location. reload()
    } else {
        alert("Произошла ошибка удаления");
    }
}

async function changedWordLearned(obj, make_learned) {
    let to_learned = 0;
    if (make_learned) {
        to_learned = 1;
    }
    let response = await fetch('/change-learned', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({word_id: obj.name, to_learned: to_learned})
      });
    if (response.ok) {
        alert("Успешно");
        location.reload();
    } else {
        alert("Произошла ошибка удаления");
    }
}

function checkAnswer(form) {
    let answer = form.translation.value;
    let correct = document.getElementById("answer-" + form.name).textContent.toLowerCase();
    if (answer.toLowerCase() == correct) {
        alert("Верно - " + answer);
    } else {
        alert("Ошибка, " + answer + " неверно, попробуйте еще!");
    }
    form.reset();
}