# IP_Camera_pkg
Pasos para conectar el video captado en una camara ip en una red local con ROS.

## En el Movil.
1. Descargar la app IP Webcam
2. AL ingresar a la app > preferencias de video > Resolución de video a (640x480) esto para obtener tasas más elevadas de fps.
3. al final de la pantalla de inicio > iniciar servidor
4. La url asociada al servidor creado se muestra en la parte inverior de la pantalla como iPv4:http://192.168.20.23:8080 (Este es mi caso)
### otro dispositivo
5. Para inspeccionar el funcionamiento, ingresar a la url descrita
6. Para acceder unicamente al video transmitido, concatenar /video a la url. Eg: http://192.168.20.23:8080/video



