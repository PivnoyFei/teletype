<h1 align="center"><a target="_blank" href="https://github.com/PivnoyFei/yatube_project/">Проект yatube</a></h1>

## Описание
Мини социальная сеть на Django, где каждый зарегистрированный пользователь может кастомизировать свой профиль, оставлять посты и комментировать чужие, создавать группы, ставить лайки, дизлайки и подписываться на пользователей, группы, чтобы следить за их обновлениями в ленте.

Вы можете оценить сайт перейдя по <a target="_blank" href="http://pivnoyfei.pythonanywhere.com/">ссылке</a>

### Стек:

```bash
Python 3.7, Django 2.2.19
```

### Запуск проекта в dev-режиме
Клонируем репозиторий и переходим в него:
```bash
git clone git@github.com:PivnoyFei/yatube_project.git
cd yatube_project
```

Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```

Ставим зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```
Переходим в папку проекта:
```bash
cd yatube
```
Выполняем миграции:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Создаем суперпользователя:
```bash
python manage.py createsuperuser
```

В папке с файлом manage.py выполните команду:
```bash
python manage.py runserver
```

### Автор
[Смелов Илья](https://github.com/PivnoyFei)
<p><a>
<img src="https://cdn.icon-icons.com/icons2/2134/PNG/512/heart_cute_emoji_emo_icon_131637.png" 
  height="40" width="40" />
</a></p>
