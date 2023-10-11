# Docker-Sample

## Documentación del ejercicio

Aquí encontrarán la documentación sobre el uso del ejercicio, además del compendio de comandos a utilizar para levantar el proyecto.

Cuando se descargue el proyecto lanzamos el comando para compilar y levantar el proyecto:

```shell
   docker build -t nombre_de_la_imagen .
```

En el comando anterior buscamos compilar la imagen, además con el comando -t después le podemos asignar un nombre a nuestra imagen, seguido de la ubicación, si ya nos encontramos en la ubicación entonces solo colocamos un punto.

```shell
   docker run -d -p 8000:8000 nombre_de_la_imagen
```

Ahora para levantar la imagen corremos el comando run, seguido de dos banderas que representan
   -d: para que lo haga en segundo plano
   -p: para definir el puerto

Una vez corriendo el contenedor podemos revisar que esté arriba con el comando:

```shell
   docker ps
```
Si queremos revisar todos los servicios en nuestro sistema colocamos:

```shell
   docker ps -a
```

Ahora bien para detener nuestra aplicacion, despues de ubicarla con el comando "ps", seleccionamos el ID del servicio y lo colocamos con:

```shell
   docker stop id_container
```

Otros comandos importantes para conocer las imágenes y volúmenes que tenemos en el sistema:

```shell
   docker image ls

   docker volume ls
```

Por último, para eliminar alguna imagen, volumen o contenedor solo debemos utilizar el comando rm antes del ID de lo que querran borrar, por ejemplo:

```shell
   docker volume rm id_volume

   docker image rm id_image

   docker rm id_container
```

## Docker compose comandos

Para el caso de Docker Compose, los comandos tienen cierta similitud, comenzando por el de compilado

Cuando queremos compilar el proyecto con docker compose y el archivo no tiene algun nombre especifico utilizamos:

```shell
   docker-compose build
```

Una vez compilado el proyecto, para levantarlo utilizamos:

```shell
   docker-compose up
```

Si queremos levantarlo sin estar dentro de los logs utilizamos el comando -d:

```shell
   docker-compose up -d
```

Para terminar algún servicio utilizamos:

```shell
   docker-compose down
```

Para saber el estado y listado de contenedores utilizamos:

```shell
   docker-compose ps
```

Por último, si utilizamos un composé con nombre distinto, para utilizar los comandos anteriores debemos colocar la bander -f seguido del nombre del compose, algo así:

```shell
   docker-compose -f nombre_compose build


   docker-compose -f nombre_compose up


   docker-compose -f nombre_compose down
```
