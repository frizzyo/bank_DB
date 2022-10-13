# bank_DB
Проект с базой данных с моделью банка. 
Реализованы:
Таблицы клентов, видов кредитов, самих взятых/погащенных кредитов.
Возможность добавлять пользователей
Выполнена сортировка в соответсвии с заданями


Запускаем проект на своей машине:

1. Клонируем репозиторий git clone https://github.com/frizzyo/bank_DB
2. Переходим в папку с проектом cd MyTest (здесь и далее приводятся команды в bash-терминале на машине под win)
3. Устанавливаем виртуальное окружение python -m venv env
4. Запускаем виртуальное окружение source env/Scripts/activate
5. Обновляем pip python -m pip install --upgrade pip
6. Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate
7. Заполняем данными модели Capital и auth.user — python manage.py loaddata db.json
8. Запускаем локальный сервер python manage.py runserver
9. По адресу http://localhost:8000/bank будут предоставлена вся доступная информация


Создание суперюзера для доступа к админке:
python manage.py createsuperuser
