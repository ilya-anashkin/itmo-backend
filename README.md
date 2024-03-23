# itmo-backend

Author: Anashkin Ilya


## Для запуска

Подготовить файл .env на примере example.env

Установить необходимые библиотеки (при необходимости создайте новый venv)

```sh
pip install -r requirements.txt
```

Запустить БД

```sh
./db.sh
```

Запустить Бэкенд

```sh
./run.sh
```

## Итоговое реализованное API

В данном API поддерживаются коды ответа: 200, 202, 400, 404, 500


### Movies

GET /api/movies - вернуть все фильмы

Пример ответа
```json
{

    "list": [

        {

            "id": 1,

            "title": "Example movie",

            "year": 2018,

            "director": director,

            "length": "02:30:00",

            "rating": 8

        },

    ...

    ]

}
```

GET /api/movies/:id - вернуть фильм с определенным id

Пример ответа
```json
{
    "movie": {

        "id": 1,

        "title": "Example movie",

        "year": 2018,

        "director": director,

        "length": "02:30:00",

        "rating": 8

    }
}
```

POST /api/movies - добавить фильм в БД

Пример запроса
```json
{
    "movie": {

        "id": 1,

        "title": "Example movie",

        "year": 2018,

        "director": director,

        "length": "02:30:00",

        "rating": 8

    }

}
```

Пример ответа
```json
{
    "movie": {

        "id": 1,

        "title": "Example movie",

        "year": 2018,

        "director": director,

        "length": "02:30:00",

        "rating": 8

    }

}
```

PATCH /api/movies/:id - изменить фильм в БД

Пример запроса
```json
{
    "movie": {

        "id": 1,

        "title": "Example movie",

        "year": 2018,

        "director": director,

        "length": "02:30:00",

        "rating": 8

    }

}
```

Пример ответа
```json
{
    "movie": {

        "id": 1,

        "title": "Example movie",

        "year": 2018,

        "director": director,

        "length": "02:30:00",

        "rating": 8

    }

}
```

DELETE /api/movies/:id - удалить фильм из БД с определенным id

В случае иных ошибок возвращается ответ:
```json
{

    "status": 500,

    "reason": "<Причина неудачи>"

}
```

### Directors

GET /api/directors - вернуть всех режиссеров

Пример ответа
```json
{

    "list": [

        {

            "id": 1,

            "fio": "Example fio",

        },

    ...

    ]

}
```

GET /api/directors/:id - вернуть режиссера с определенным id

Пример ответа
```json
{
    "director": {

        "id": 1,

        "fio": "Example fio",

    }
}
```

POST /api/directors - добавить режиссера в БД

Пример запроса
```json
{
    "director": {

        "id": 1,

        "fio": "Example fio",

    }
}
```

Пример ответа
```json
{
    "director": {

        "id": 1,

        "fio": "Example fio",

    }
}
```

PATCH /api/directors/:id - изменить режиссера в БД

Пример запроса
```json
{
    "director": {

        "id": 1,

        "fio": "Example fio",

    }
}
```

Пример ответа
```json
{
    "director": {

        "id": 1,

        "fio": "Example fio",

    }
}
```

DELETE /api/directors/:id - удалить режиссера из БД с определенным id

В случае иных ошибок возвращается ответ:
```json
{

    "status": 500,

    "reason": "<Причина неудачи>"

}
```