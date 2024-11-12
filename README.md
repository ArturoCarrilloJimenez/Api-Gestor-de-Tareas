# FastApi

## Instalar las librerías
Esta es una api de un gestor de tareas con autenticación entre otras cosas

``` bash
pip install -r requirements.txt
```

## Estructura de carpetas

La estructura de carpetas se compone de la siguiente forma:

```
|- config
|- crud
|- middleware
|- model
|- routes
|- schemas
|- utils
```
__Config__ contiene la conexión con la base de datos y la generación de la clave secreta, este contendrá todas las configuraciones

__CRUD__ contienen las rutas de lectura, escritura, modificación y eliminado de los modelos, las funciones de un crud

__Middleware__ contiene la verificación del token en una ruta de FastApi77

__Model__ contiene los modelos de SQL

__Routes__ contiene las rutas que no sean del crud

__Schemas__ contiene los esquemas de pydantic

__Utils__ contiene las utilidades de la api como la autenticación o el hash de texto entre otras cosas


