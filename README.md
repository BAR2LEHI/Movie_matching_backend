## Как запустить проект
1.  Клонировать репозиторий:
```
git clone git@github.com:BAR2LEHI/Movie_matching_backend.git
```
2. Перейти в папку с  проектом:
```
cd movie_matching_backend
```
3. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

-   Если у вас Linux/MacOS
    
    ```
    source venv/bin/activate
    ```
    
-   Если у вас Windows
    ```
    source venv/Scripts/activate
    ```
4. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
5. Создайте в корневой папке проекта файл .env и наполните его:
```
SECRET_KEY='Your_Secret_Key_Django_Project'
NAME='Your_DB_Name'
USER='Your_DB_Username'
PASSWORD='Your_DB_Password'
HOST='localhost'
PORT='5432'
```

#### Подключение PostgeSQL
1. Установите СУБД PostgeSQL c официального сайта: 
- https://www.postgresql.org/download/
2. Следуйте инструкциям при установке и создайте пользователя.
- Создайте Базу Данных и укажите её название.
- Подставьте свои данные в файле .env по примеру из п.5 предыдущего раздела


     
6. Перейдите в директорию, где находится файл *manage.py*:
```
cd backend/
```
7. Выполните миграции:
```
python manage.py migrate
```
8. Создайте суперпользователя:
```
python manage.py createsuperuser
```
- Введите данные нового суперпользователя, они необходимы для входа в Админ-панель Django

Документация проекта доступна по адресу:
http://127.0.0.1:8000/docs/

Вход в Админ-панель доступен по адресу:
http://127.0.0.1:8000/admin/     *Указывайте username и password своего superuser'a*
