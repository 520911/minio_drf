## Тестовый проект по созданию API интерфейса S3 Minio на основе Django Rest Framework'a

### Для запуска проекта нужно:
- Скопировать репозиторий
- Запустить docker-compose up --build -d
- Провести миграции python manage.py migrate
- Запустить сервер Django python manage.py runserver

## Для проверки работоспособности используется Postman (необходима авторизация Base Auth):
- Посмотреть файлы в хранилище метод GET: http://127.0.0.1:8000/api/v1/files/
- Загрузить файл в хранилище метод POST: http://127.0.0.1:8000/api/v1/files/
В Body form-data необходимо указать:
key: file_path тип File и выбрать файл в локального диска
- Получить ссылку на скачивание файла: http://127.0.0.1:8000/api/v1/download/
В Body form-data необходимо указать:
key: nema - название документа
