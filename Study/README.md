# Тестовое задание 
## Что нужно сделать
Документация к API
127.0.0.1/redoc/
Клонировать репозиторий.
    git@github.com:zhukov1414/TestTaskHardQode.git

Cоздать и активировать виртуальное окружение, установить зависимости:
    $ cd /Study/
    $ python -m venv venv

Для Windows:
    $ source venv/Scripts/activate

Для MacOs/Linux:
    $ source venv/bin/activate
Установить зависимости:
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt

Выполнить миграции:
    (venv) $ python manage.py migrate

Создать суперюзера:
    (venv) $ python manage.py cratesuperuser

Запустить сервер:
    (venv) $ python manage.py runserver

- Python 
- Django 
- DRF
- Автор Евгений
