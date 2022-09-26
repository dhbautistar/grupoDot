# Prueba Tecnica Backend Engineer
## _Diego Bautista_

### Requerimientos del sistema:

- Docker
- Python 3.9 o superior


## Localhost

Para correr en local se deben ejecutar los siguientes comandos:

```sh
docker build -t test1 . && docker run -d --name test1 -p 80:80 test1
```

## Endpoits

- / :: Devuelve string: Endpoint general 
- /api/login :: Devuelve JWT Token
    - Ya que no se hizo uso de una DB, el usuario manejado en memoria es "Diego Bautista", el JSON es el siguiente (Se puede ver en Swagger):
        ```sh
        {
            "username": "Diego Bautista",
            "email": "diego.bautista@gmail.com"
        }
        ```
- /api/palindromo :: Devuelve palindromo mas largo
- /docs :: Swagger

## Pruebas Unitarios

Para ejecutar los test unitarios se puede ejecutar el siguiente comando:

```sh
python -m pytest
```
