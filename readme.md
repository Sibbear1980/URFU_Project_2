# Программная инженерия. Группа 1

## Домашнее задание №1
**Цель задания**: научиться использовать линтер flake8 для автоматической проверки качества кода в процессе Continuous Integration.

Для задания выбрана [модель определения эмоционального окраса текста](https://huggingface.co/blanchefort/rubert-base-cased-sentiment)
### Запуск приложения
1. Создать виртуальное окружение:

    `python3 -m venv env`

2. Активировать виртуальное окружение:

    `source env/bin/activate`

3. Перейти в URFU_Project_2
   
    `cd URFU_Project_2`
   
4. Установить зависимости:

    `pip install -r requirements.txt`
   
5. Запустить приложение:

    `uvicorn Api:app`

6. Cформировать POST запрос

    ```python
    curl -X 'POST' 'http://127.0.0.1:8000/predict/'
         -H 'Content-Type: application/json'
         -d '{ "text": 
         """It was a wonderful journey.
            We have visited many beautiful places and
            seen many sightings! I am happy!"""}'
    ```

_Пример ответа_: \
{"Исходный текст":"It was a wonderful journey. We have visited many beautiful places and seen many sightings! I am happy!","Результат:":"позитивный :)"}

### Используемые зависимости
Приведены в файле [requirements.txt](https://github.com/Sibbear1980/URFU_Project_2/blob/main/requirements.txt)

**Скрипт для создания приложения с моделью:**
 - Api.py
 
**Скрипт для тестирования:**
 - Api_test.py

### Тестирование API приложения
Тестирование запускается из терминала командой `pytest Api_test.py` \
либо автоматически при загрузке изменений проекта на Github

>Тестируется наличие ответа от приложения и правильность определения эмоционального окраса текста (позитивный/нейтральный/негативный)

### Участники команды:
 - Коньшина Ольга
 - Ильиных Виктория
 - Шабанов Дмитрий
 - Воробьев Василий 
 - Прохорова Екатерина
 - Егоренкова Татьяна
