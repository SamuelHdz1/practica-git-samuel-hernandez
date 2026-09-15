# Creación y sincronización de repositorio con Git y GitHub

## Samuel Hernández Nava

## 2630016

## Nombre de la práctica

Creación y sincronización de un repositorio local con GitHub

## Objetivo de la práctica

Crear un repositorio local utilizando Git, vincularlo con un repositorio remoto en GitHub y comprobar cómo se sincronizan los cambios en ambos sentidos: desde el repositorio local hacia GitHub y desde GitHub hacia el repositorio local.

## Descripción del procedimiento

Primero se creó una carpeta, en mi caso dentro del escritorio, la cual era `practica-git-nombre-apellido` para trabajar en la práctica. Dentro de esta carpeta se inicializó un repositorio local utilizando Git y se estableció la rama principal con el nombre `main`.

Después se crearon los archivos `README.md` y `datos.txt`. El archivo `datos.txt` se utilizó para realizar diferentes modificaciones y comprobar la sincronización entre el repositorio local y GitHub.

Posteriormente se agregaron los archivos al área de preparación o Staging Area. Se verificaba el estado del repositorio en todo momento con el comando `git status` y se realizó el primer commit para guardar los cambios en el historial de Git.

Después se creó un repositorio público en GitHub y se vinculó con el repositorio local mediante HTTPS. Se enviaron los archivos del repositorio local a GitHub con `git push -u origin main` y se comprobó que aparecieran correctamente.

Finalmente, se realizó una modificación directamente desde GitHub y se descargó al repositorio local utilizando `git pull origin main`. Después se realizó otra modificación desde la computadora y se envió nuevamente a GitHub mediante `git push`. De esta manera se comprobó la sincronización en ambos sentidos.

## Comandos de Git utilizados

|Comando|Función|
|-|-|
|`git init`|Inicializa un nuevo repositorio de Git en la carpeta actual.|
|`git branch -M main`|Cambia el nombre de la rama principal a `main`.|
|`git status`|Muestra el estado actual del repositorio y los cambios realizados.|
|`git add .`|Agrega todos los archivos modificados al área de preparación (Staging Area).|
|`git commit -m "Primer commit"`|Guarda los cambios agregados al área de preparación en el historial del repositorio.|
|`git remote add origin URL`|Vincula el repositorio local con un repositorio remoto en GitHub.|
|`git remote -v`|Muestra la URL del repositorio remoto conectado.|
|`git push -u origin main`|Envía por primera vez los cambios del repositorio local hacia GitHub y establece la conexión con la rama remota.|
|`git pull origin main`|Descarga los cambios de GitHub y los incorpora al repositorio local.|
|`git push`|Envía los nuevos cambios del repositorio local hacia GitHub.|

## Creación del repositorio local

Para crear el repositorio local primero se creó una carpeta dentro del escritorio con el nombre `practica-git-nombre-apellido`. Después se abrió PowerShell dentro de esta carpeta y se utilizó el comando `git init` para inicializar el repositorio.

Posteriormente se utilizó el comando `git branch -M main` para establecer `main` como la rama principal. Después se crearon los archivos `README.md` y `datos.txt`, los cuales forman parte del contenido inicial del repositorio.

Finalmente, se utilizó `git add .` para agregar los archivos al área de preparación o Staging Area y `git commit -m "Primer commit"` para guardar los primeros cambios en el historial del repositorio.

## Vinculación del repositorio local con GitHub

Después de crear el repositorio local, se creó un repositorio público en GitHub con el mismo nombre. El repositorio de GitHub se dejó vacío para evitar problemas con los archivos del repositorio local.

Para conectar ambos repositorios se utilizó el comando `git remote add origin`, indicando la URL HTTPS del repositorio creado en GitHub. Después se utilizó `git remote -v` para comprobar que la conexión se hubiera realizado correctamente.

Finalmente, se utilizó el comando `git push -u origin main` para enviar por primera vez el contenido del repositorio local hacia GitHub.

## Sincronización Local → GitHub

Para comprobar la sincronización desde el repositorio local hacia GitHub, primero se realizaron cambios en el archivo `datos.txt` desde la computadora.

Después se utilizó `git status` para verificar que Git detectara los cambios realizados. Posteriormente, se utilizó `git add .` para agregar las modificaciones al área de preparación.

Se creó un nuevo commit utilizando `git commit -m "Actualización desde repositorio local"` para guardar los cambios en el historial. Finalmente, se utilizó `git push` para enviar los cambios desde el repositorio local hacia GitHub.

Al entrar nuevamente al repositorio en GitHub, se pudo comprobar que la modificación realizada desde la computadora también aparecía en el repositorio remoto.

## Sincronización GitHub → Local

Para comprobar la sincronización desde GitHub hacia el repositorio local, primero se modificó directamente el archivo `datos.txt` desde la página de GitHub. Se agregó una nueva línea indicando que el archivo fue modificado desde GitHub y se guardó el cambio realizando un commit.

Después se regresó al repositorio local utilizando PowerShell y se ejecutó el comando `git pull origin main`. Este comando permitió descargar los cambios realizados en GitHub y actualizar los archivos del repositorio local.

Finalmente, se abrió el archivo `datos.txt` desde la computadora y se comprobó que el cambio realizado desde GitHub también apareciera en el archivo local.

## Archivos contenidos en el repositorio

El repositorio contiene los siguientes archivos:

* `README.md`: contiene la información, objetivo, procedimiento, comandos utilizados y conclusión de la práctica.
* `datos.txt`: contiene el texto relacionado con la práctica y las modificaciones realizadas desde GitHub y desde el repositorio local.

## Conclusión personal

Con esta práctica aprendí cómo desde la terminal puedo manejar un repositorio local de manera más cómoda, además de vincularlo con un repositorio remoto en GitHub mediante diferentes comandos de Git. También pude entender mejor cómo se pueden enviar y recibir cambios entre ambos repositorios.

Además, pude comprobar que los cambios pueden sincronizarse en ambos sentidos. Con `git push` se pueden enviar los cambios del repositorio local a GitHub, mientras que con `git pull` se pueden descargar los cambios realizados en GitHub hacia la computadora.

Esta práctica me ayudó a comprender mejor el funcionamiento de Git y GitHub y la importancia de utilizar estas herramientas para llevar un control ordenado de los cambios realizados en un proyecto.

