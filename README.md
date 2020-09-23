# Решение тестового задания
Основное приложение находится в папке promo

Для записи json файла promotion.json используется код в файле write.py, который можно запустить, например, так. 

```sh
$  python manage.py write amount=1, group='avtostop'
```
Проверка наличия промокода YH0PVRQO в файле promotion.json
```sh
$  python manage.py check YH0PVRQO
```
