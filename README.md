# Experimento Seguridad

# ABC_JOBS_Grupo23

### Integrantes 

Luz Ochoa - ls.ochoa@uniandes.edu.co

Mateo Cáceres - m.caceresa23@uniandes.edu.co

Alejandra Niño - ma.ninog12@uniandes.edu.co

# Experimento Realizado
![image](https://github.com/AlejandraNGomez12/ExperimentoSeguridad/assets/123474214/8c42c55d-017a-428f-a68a-ba58a9a64d61)

# Instrucciones para ejecutar el proyecto

Para la ejecución del proyecto se hizó en ambiente local.

## Requisitos

* Descargar el proyecto y cada microservicio ejecutandose en un puerto diferente.
* Crear el entorno virtual
* Instalar las librerias de JWT, Alchemy, Flask, JWT JSON
* tener instalado postman

## Pasos para la ejecución
1. Abrir el proyecto en el Visual Studio Code.
2. Ejecute en la raiz del proyecto
```shell
python3 -m venv venv
.\venv\Scripts\activate                            
py -m pip install -r requirements.txt
pip install PyJWT
pip  install SQLAlchemy
pip install Flask-SQLAlchemy
```
3. Ejecute el microservicio "Usuario"
   Para el microservicio usuari ejecutarlo en el puerto 5000
```shell
flask run -p 5000
```

4. Ejecute el microservicio "Candidato"
```shell
flask run -p 5001
```

5. Ejecute el microservicio "Permiso"
```shell
flask run -p 5002
```

6. Ejecute el microservicio "Empresa"
```shell
flask run -p 5003
```

7. Crear el usuario con la siguiente estructura:
   endpoint --> http://127.0.0.1:5000/usuario
   metodo: POST
```shell
{
    "usuario": "Usuario1",
    "contrasena": "Usuario1",
    "admin":false, --> si eres administrador marcar como true
    "activo":true
}

```

8. Hacer el login con la siguiente estructura :
   enpoint --> http://127.0.0.1:5000/login
   metodo: POST
   
```shell
{
    "usuario": "XXXXXX",
    "contrasena": "XXXXXX"
}
```


9. Crear las opciones  con la siguiente estructura :
   enpoint --> http://127.0.0.1:5002/opciones
   metodo: POST
```shell
{
    "nombre": "crearEmpresa"
}
```
 Opciones a crear: 
   1. crearCandidato
   2. verCandidato
   3. editarCandidato
   4. verCandidatos
   5. crearEmpresa
   6. verEmpresa
   7. editarEmpresa
   8. verEmpresa


10. Finalmente para que un usuario tenga premisos es necesario crear el permiso con un idUsuario o idCandidato y las opciones: 
 enpoint --> http://127.0.0.1:5002/permisos
   metodo: POST
```shell
{
    "usuarioId":"1",
    "opcionId":"5"
}
```
Si el usuario es un usuario administrador podrá acceder a cualquier opción sin necesidad de tener un permiso creado y el admin será el unico con el privilegio de crear una nueva opción y un nuevo permiso.

NOTA: Es de aclara que todos los microservicios de Empresa, Candidato, Permiso y Opciones se debe hacer uso del Token de seguridad que es generado una vez se haga el login a la aplicación con un usuario y contraseña validos de la siguiente forma:
![image](https://github.com/AlejandraNGomez12/ExperimentoSeguridad/assets/123474214/dfc20b3c-3a60-4713-912e-fe5e19d27954)



