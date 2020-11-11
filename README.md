# IP_Camera_pkg
Pasos para conectar el video captado en una camara ip en una red local con ROS.

## En el Movil.
1. Descargar la app IP Webcam
2. AL ingresar a la app > preferencias de video > Resolución de video a (640x480) esto para obtener tasas más elevadas de fps.
3. al final de la pantalla de inicio > iniciar servidor
4. La url asociada al servidor creado se muestra en la parte inverior de la pantalla como iPv4:http://192.168.20.23:8080 (Este es mi caso)
La dirección IP es:  192.168.20.23
El puerto: 8080

### otro dispositivo
5. Para inspeccionar el funcionamiento, ingresar a la url descrita
6. Para acceder unicamente al video transmitido, concatenar /video a la url. Eg: http://192.168.20.23:8080/video

## En PC
1. dirigirse al directorio o workspace deseado.
```sh
$ cd workspace
```
2. clonar este repositorio (Paquete de ROS).
```sh
$ git clone 
```
3. Modificar en el archivo pubisher.py la direccion IP a la de ustedes.

4.Compilar
```sh
$ catkin_make
```
5.Establecer las variables de entorno
```sh
$ source devel/setup.bash 
```
6.Ejecutar pubisher.py (crea un nodo "IPCamera" que publica al tópico "camera_image" la imagen)
```sh
$ rosrun IP_Camera_pkg pubisher.py
```
7.Ejecutar en otra terminal (estableciendo variables de entorno) subscriber.py (crea un nodo que se subscribe al tópico "camera_image" y visualiza la información)

```sh
$ rosrun IP_Camera_pkg subscriber.py
```
