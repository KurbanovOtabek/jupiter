# CRM сервисной службы медицинского оборудования

# JUPITER project

python manage.py startapp jupiter_api

# миграции
python manage.py makemigrations
python manage.py migrate

чтобы создать новую БД в консоли пишем:

**createdb jupiter_db**

удалить БД в консоли пишем:

**dropdb jupiter_db**

# админка

создание суперпользователя:

**python manage.py createsuperuser**