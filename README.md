# A01284529_ExamenRedes Proyecto de Encriptación y Desencriptación de Imágenes

Este proyecto es una aplicación web que permite encriptar y desencriptar imágenes utilizando el algoritmo AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining).

## Requisitos

Para ejecutar esta aplicación, necesitarás tener instalado lo siguiente:

- Python 3
    - pillow
    - pycryptodome 
- Node.js
- npm (Node Package Manager / Express)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias de Node.js ejecutando `npm install` en la terminal con el directorio raíz del proyecto.

3. Instala igualmente lo requerimiento para python3 ejecutando `pip install pillow` y `pip install pycryptodome` en la terminal con el directorio raiz del proyecto

## Uso

1. Ejecuta el servidor Node.js ejecutando `node app.js`.
2.  Es necesario asegurarse que para que el proyecto funcione las carpetas **`decrypted_images`** y **`encrypted_images`** esten vacias, ya que si se encuentran archivos con el mismo nombre puede llegar a fallar. 
3. Accede a la aplicación en tu navegador web en `http://localhost:3000/encrypt`.
4. En cualquier caso que no llegara a funcionar utilizar el siguiente comando
 `curl -X POST -H "Content-Type: application/json" -d '{"data": "tus_datos_a_encriptar"}' http://localhost:3000/encrypt` 
en la terminal con el directorio raiz del proyecto 
5. Si se quiere volver a usar la aplicacion, borrar las imagenes ya anteriormente mencionadas en el paso 2. 


### Endpoints API

- `POST /encrypt`: Encripta datos. Debes enviar un objeto JSON en el cuerpo de la solicitud con el siguiente formato: `{"data": "datos_a_encriptar"}`.
 *En esta version no se necesitan poner datos, ya vienen configuradas las imagenes a encryptas, con solo poner el endpoint se activa la funcion para encriptar.* 

## Tecnologías Utilizadas

- **Express**: Un framework web para Node.js que facilita la creación de aplicaciones web y API.
- **Crypto**: Un módulo en Node.js que proporciona funciones de criptografía, utilizado para encriptar y desencriptar los datos.
- **PIL (Python Imaging Library)**: Una biblioteca en Python para el procesamiento de imágenes, utilizada para manipular las imágenes encriptadas y desencriptadas.
- **axios**: Una biblioteca en Node.js para realizar solicitudes HTTP, aunque no la hemos utilizado en este README, podría ser útil para interactuar con la API desde el código.
- **curl**: Una herramienta de línea de comandos para realizar solicitudes HTTP.

## Retroalimentacion

Este proyecto tiene aun muchas areas de mejoras, en especial en la parte de la arquitectura, a pesar de tener las imagenes organizadas al crear, tener solo dos archivos para todo el proyecto. Una para la creacion del servidor, o el API. y otro para la encriptacion y desencriptacion. Lo mejor seria el dividir el archivo de Encriptacion.py para que sean dos archivos cada uno con su funcion. 

* Encriptacion
* Desencriptacion 

esto facilitaria el llamado de los enpoints para que se puedan llamar las funciones individualmente en vez de que las dos funciones se ejecuten por estar en el mismo archivo, dejandonos solo un endpoint para la encriptacion y desencriptacion. 

al igual que hay areas de mejoras en el codigo de encriptacion, para poder hacer aun mas validaciones y que sean mas detalladas las peticiones. 

