## Instalación
Puedes clonar el repositorio cómo desees, utilizando ssh o html.

Clona el repositorio utilizando ```git clone https://github.com/Javiramos276/Ip-filter-attack.git```

Una vez clonado el repositorio puedes abrir una consola cmd y ubicarte en la direccion donde clonaste el repositorio para ejecutar ```python main.py```.

### Formatos aceptados de lectura

Este script acepta **formatos de lectura como archivos de texto y tambien archivos comprimidos de tipo .gz**, simplemente suelta los archivos de tu interes en la carpeta donde se encuentra el main.py y ejecuta ```python main.py``` para comenzar la busqueda.


### ¿Qué debo pasarle al programa?
Supongamos un ejemplo de un txt:


66.249.64.0 - - [01/Apr/2023:00:13:02 +0200] "GET /robots.txt HTTP/1.1" 200 107 paginadeejemplo.com "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" \
66.249.64.0 - - [01/Apr/2023:00:13:04 +0200] "GET /wp-content/cache/wpfc-minified/1qij89fv/9nmup.css HTTP/1.1" 200 6645 paginadeejemplo.com "https://paginadeejemplo.com/" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" \
66.249.64.0 - - [01/Apr/2023:00:13:05 +0200] "GET /wp-content/cache/wpfc-minified/ei8498px/9nmup.js HTTP/1.1" 200 40270 paginadeejemplo.com "https://paginadeejemplo.com/" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" \
66.249.64.0 - - [01/Apr/2023:00:13:09 +0200] "GET /wp-content/cache/wpfc-minified/2oojiepa/9nmuo.css HTTP/1.1" 200 26986 paginadeejemplo.com "https://v/" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" \


deberás pasarle al programa un **USER-AGENT** (dentro de la lista de archivos que quieras inspeccionar), como puede ser por ejemplo: ```Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0```
