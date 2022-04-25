# Добавить зону доставки

### запрос
* Url: **/api/manage-couriers/create-zone/**
* Allow: **POST**
* Content-Type: **application/json**
* Headers: отсутствуют, при необходимости могут быть добавлены(например, для ограничения доступа)
* Body: 
```json 
{
  "polygon": [
    {
      "lng": 0,
      "ltd": 0
    }
  ],
  "name_zone": "string"
}
```


**Пример запроса:**

   /api/manage-couriers/create-zone/
   
**Ответ**

* HTTP_200: При удачном добавлении  
* HTTP_422: При некорректных входных данных

