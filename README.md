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


# Collection Postman Proyecto ABC Seguridad
{
	"info": {
		"_postman_id": "b75c8511-3557-47fb-85dc-1ed988a55ebc",
		"name": "ExperimentoSeguridad",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "11344849"
	},
	"item": [
		{
			"name": "CrearEmpresa",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjE0MjYwNywianRpIjoiNGQzNmVlZTItNWM3Ny00OGJiLTkwMzItZDlkOTA4ZjBkZDBlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk2MTQyNjA3LCJleHAiOjE2OTYxNDM1MDd9.lx9eE6ncQM5UOWeZOwWm8ma8al4AAg8mjj4BECyheWo",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"nombre\":\"Empresa\",\r\n    \"nit\":\"1\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5003/empresas",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5003",
					"path": [
						"empresas"
					]
				}
			},
			"response": []
		},
		{
			"name": "Candidato",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjE4MDM1NywianRpIjoiMGUwOWY0NjItN2UxYy00ZDM1LWEyMjUtOTk0YjVmZjc3OTBmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk2MTgwMzU3LCJleHAiOjE2OTYxODEyNTd9.a0xAmm4J7fa5Qv7lV1W3biKEs9zNghbcHBEXEW_Nb-8",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"documento\":\"1\",\r\n    \"nombre\":\"Candidato\",\r\n    \"fechaNacimiento\":\"1999-09-09\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5001/candidatos",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5001",
					"path": [
						"candidatos"
					]
				}
			},
			"response": []
		},
		{
			"name": "ObtenerCandidato",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjE4MDA3NCwianRpIjoiNWEzYTllZTMtMDc5MC00NzRhLTgxMzUtYmI3ODJlYjRkMWM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNjk2MTgwMDc0LCJleHAiOjE2OTYxODA5NzR9.6DGn-DkCY-6jSfK0A47Zrqoz_TNg-qa9puawGTuHhL0",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjEyNzUwOSwianRpIjoiNjAzMDM3MWYtZWY5OC00NDUyLWJiMTctMTc3ODVhMzc3NjA4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk2MTI3NTA5LCJleHAiOjE2OTYxMjg0MDl9.n5QlS9-VrjpDG12d-lKuphHyghvnFKQ0MYttx_gdL38",
						"type": "text",
						"disabled": true
					}
				],
				"url": {
					"raw": "http://127.0.0.1:5001/candidato/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5001",
					"path": [
						"candidato",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "ObtenerCandidatos",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/candidatos",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"candidatos"
					]
				}
			},
			"response": []
		},
		{
			"name": "ObtenerEmpresa",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/empresa/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"empresa",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "CrearOpciones",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjE0MjI2MCwianRpIjoiZTE5MWE2YzgtZmZkMi00NDA3LWI5NjQtZDJhMjFhYWZmMWRlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk2MTQyMjYwLCJleHAiOjE2OTYxNDMxNjB9.NSw-cq8mHKOH_AYpkfwSoxEdpsfYGs5A2VdnmDpCAMk",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"nombre\": \"crearEmpresa\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5002/opciones",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5002",
					"path": [
						"opciones"
					]
				}
			},
			"response": []
		},
		{
			"name": "ObtenerOpcion",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/opcion/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"opcion",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "CrearPermiso",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjE0MjU0OSwianRpIjoiZGNhNDJlYjMtYjYxMC00OGI0LTk1YTItMmMzY2ViYzc1NTg5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk2MTQyNTQ5LCJleHAiOjE2OTYxNDM0NDl9.wH8C8TqSa1p0aLOstFJqTJALChh2mdL2h_NyLgG_B00",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"usuarioId\":\"1\",\r\n    \"opcionId\":\"5\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5002/permisos",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5002",
					"path": [
						"permisos"
					]
				}
			},
			"response": []
		},
		{
			"name": "CrearUsuario",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"usuario\": \"UsuarioAdmin1\",\r\n    \"contrasena\": \"UsuarioAdmin1\",\r\n    \"admin\":true,\r\n    \"activo\":true\r\n    \r\n\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/usuario",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"usuario"
					]
				}
			},
			"response": []
		},
		{
			"name": "login",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"usuario\": \"Aleja\",\r\n    \"contrasena\": \"Aleja\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/login",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"login"
					]
				}
			},
			"response": []
		}
	]
}
