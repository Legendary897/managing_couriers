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
    },
    {
      "lng": 1,
      "ltd": 1
    },
    {
      "lng": 2,
      "ltd": 1
    }
  ],
  "name_zone": "TEST_ZONE"
}
```


**Пример запроса:**

   /api/manage-couriers/create-zone/
   
**Ответ**

* HTTP_200: При удачном добавлении  
* HTTP_422: При некорректных входных данных

