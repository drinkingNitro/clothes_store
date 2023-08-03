# clothes_store
Тестовое задание веб приложение "магазин одежды" на Django/DRF.
Использованы модели product, user, favorite. Весь функционал реализован на DRF. Аутентификация выполняется по токену DRF.
Файл env_config содержит переменные, которые нужно заполнить для запуска приложения.

1. Просмотр товаров, отображаются поля (имя, цена, адрес картинки): GET /api/products/.
2. Просмотр деталей товара, отображаются все поля: GET /api/products/<int:pk>/. pk = id продукта.

3. Регистрация пользователя: POST /api/users/create/. Обязательные поля: username, password. Необязательные поля: first_name, last_name, email.
4. Получение токена для пользователя: POST /api/obtain_auth_token/. Обязательные поля: username, password.

5. Просмотр списка избранного пользователя: GET /api/users/favorite/.
6. Добавление продукта в избранное пользователя: POST /api/users/add_favorite/<int:pk>/. pk = id продукта.
7. Удаление продукта из избранного: DELETE /api/users/favorite/<int:pk>/. pk = id избранного.
