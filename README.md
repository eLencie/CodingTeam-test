# Тестовое задание

## Endpoints
<a href='http://127.0.0.1:8000/api/categories/'>/api/categories/</a> - эндпоинт, который вернёт все блюда, у которых is_publish=True, сгруппированные по категориям<br>
<a href='http://127.0.0.1:8000/api/food-list/'>/api/food-list/</a> - эндпоинт, который вернёт все блюда, у которых is_publish=True, с возможностью фильтрации по is_vegan, is_special, [topping.name, …]

## Структура проекта
- Django
- Django rest framework
- Django-filter
- Sqlite3

## Пояснительная записка
Модели БД вынес в отдельное приложение restaurant для возможности масштабирования проекта<br>
Запросы к базе данных выполнил с помощью ORM. Сложные и вложенные запросы оптимизировал с помощью встроенных средств оптимизации запросов django - prefetch_related. Оставил в проекте django-debug-toolbar для возможности удостовериться в эффективности запросов.<br>
Покрыл тестами все основные операции с эндпоинтами<br>
Проработал админку исключительно для удобства заполнения БД<br>

```
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
python manage.py test API.tests

# Запуск встроенного веб-сервера
python manage.py runserver
```
