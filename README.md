# Wordpress - XMLRPC Brute Force

Script que nos permite efectuar un ataque de fuerza bruta sobre un fichero xmlrpc.php en Wordpress. Para que se pueda realizar este ataque, es necesario contar con acceso a este fichero primero, el cual se encuentra en el directorio de Wordpress:

	DIRECTORIO WORDPRESS/xmlrpc.php
  
Este ataque lanza una serie de peticiones POST a la función **wp.getUsersBlogs** con la combinación de usuario y contraseña proporcionados:

 	<methodCall>
		<methodName>wp.getUsersBlogs</methodName> 
		<param><value>{username}</value></param>
		<param><value>{password}</value></param>
	</methodCall>
  
En el caso de los usuarios, estos pueden ser introducodos en la línea 60 en forma de lista; es decir, de uno en adelante y probará todas las posibles combinaciones. En el caso del diccionario, por defecto emplea el **rockyou.txt** en un sistema Linux, pero puedes cambiarlo al que necesites simplemente cambiando la ruta en la línea 61.

![image](https://user-images.githubusercontent.com/25083316/178153753-aea37cab-d222-45af-a1a0-3fc0fc2e629c.png)

Por defecto, el xmlrpc devuelve una cadena de texto que dice "*Incorrect username or password*" cuando las credenciales no son válidas, así que simplemente se busca la respuesta que no contenga dicha cadena para proporcionar una credencial válida al usuario.

Básicamente, solo deberás modificar el listado de usuarios, el diccionario, y la URL destino que se encuentra en la línea 22:

![image](https://user-images.githubusercontent.com/25083316/178153841-7e011796-5f31-4f98-9dc8-a3042cf5986e.png)

El script está programado en python 2 y puede ser ejecutado simplemente mandándolo a llamar:

 	python2 xmlrpc-brute-force.py
  
![19](https://user-images.githubusercontent.com/25083316/178153859-c3aa815d-30b1-48d9-9c3b-deea05790d80.png)
