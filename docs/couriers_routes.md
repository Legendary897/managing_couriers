# Добавить курьера

### запрос
* Url: **/api/manage-couriers/create-couriers/**
* Allow: **POST**
* Content-Type: **application/json**
* Headers: отсутствуют, при необходимости могут быть добавлены(например, для ограничения доступа)
* Body: 
```json
{
  "couriers_info": {
    "name": "string",
    "surname": "string",
    "age": 0
  },
  "id_zone": 0
}
```

**Пример запроса:**

   /api/manage-couriers/create-couriers/
   
**Ответ**

* HTTP_200: При удачном добавлении  
* HTTP_422: При некорректных входных данных


# Получить курьера по точке доставки

### запрос
* Url: **/api/manage-couriers/get-courier/**
* Allow: **GET**
* Content-Type: **application/json**
* Headers: отсутствуют, при необходимости могут быть добавлены(например, для ограничения доступа)

**Пример запроса:**

   /api/manage-couriers/get-courier/?lng=55.992757&ltd=92.919069
   
**Ответ**
```json
{
  "id": 2,
  "id_zone": 1,
  "couriers_info": {
    "name": "string",
    "surname": "string",
    "age": 0
  }
}
```

* HTTP_200: При удачном добавлении  
* HTTP_422: При некорректных входных данных
