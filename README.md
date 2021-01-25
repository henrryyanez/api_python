# API DJANGO

## Requerimientos
- Python 3.8
- Django (2.1)
- Django REST Framework
- Django Rest Auth

## Instalación
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`history/:id/` | GET | READ | devuelve las ultimas consultas realizadas limitando la cantidad de salidas
`process_email/`| POST | CREATE | Crea una nueva consulta de procesamiento predictivo

## Uso
Podemos usar [curl](https://curl.haxx.se/) o Postman para realizar las pruebas necesarias.


Primero, iniciamos el servidor con el siguiente comando.
```
	python manage.py runserver
```
Solo los usuarios autenticados pueden hacer uso de la API:
```
	http  http://127.0.0.1:8000/history/30/
```
Va a responder:
```
 {  "detail": "Cabecera token inválida. Las credenciales no fueron suministradas."  }
```
Iniciamos, Si intentamos ingresar con credenciales válidas:
```
	http http://127.0.0.1:8000/history/1/ "Authorization: Token <TOKEN>"
```
Se va a obtener el resultado de las consultas almacenadas, en este caso vemos:
```
[
    {
        "text": "www.google.com href Freee free pack href",
        "result": "HAM",
        "created_at": "2021-01-24T22:29:00.992888Z"
    }
]
```

## Login y Tokens

Para obtener un token primero tienes que loguearte
```
	http http://127.0.0.1:8000/rest-auth/login/ username="USERNAME" password="PASSWORD"
```
Luego vas a poder ver tu token
```
{
    "key": "<TOKEN>"
}
```
**Todos los request necesitan un token válido, de lo contrario no podrá ser procesado**

Nosotros podemos crear usuarios. (password1 y password2 deben ser iguales)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
Nosotros podemos hacer logout de la API , el token debe ser el actual:
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```


### Comandos
```
http POST http://127.0.0.1:8000/process_email/ "Authorization: Token <YOUR_TOKEN>" "texto": "www.google.com href Freee free pack href"

```

### Consulta de peticiones realizadas con un limit de resultados:
La api soporte un numero entero para mostrar ese cantidad indicada: int=50:
```
http http://127.0.0.1:8000/history/50/ "Authorization: Token <YOUR_TOKEN>"
```

Listo ya puedes comenzar a probar.

