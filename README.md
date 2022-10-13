# bank_DB
Проект с базой данных с моделью банка. 
Реализованы:
Таблицы клентов, видов кредитов, самих взятых/погащенных кредитов.
Возможность добавлять пользователей
Выполнена сортировка в соответсвии с заданями


Запускаем проект на своей машине:

Клонируем репозиторий git clone https://github.com/frizzyo/bank_DB
Переходим в папку с проектом cd MyTest (здесь и далее приводятся команды в bash-терминале на машине под win)
Устанавливаем виртуальное окружение python -m venv env
Запускаем виртуальное окружение source env/Scripts/activate
Обновляем pip python -m pip install --upgrade pip
Устанавливаем в виртуальном окружении зависимости для проекта python -m pip install --no-cache-dir -r requirements.txt
Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate
Заполняем данными модели Capital и auth.user — python manage.py loaddata db.json
Запускаем локальный сервер python manage.py runserver
По адресу http://localhost:8000 будет доступен список записей о столицах, a по адресу http://localhost:8000/api/capitals та же информация через API.


Создание суперюзера для доступа к админке:
python manage.py createsuperuser
