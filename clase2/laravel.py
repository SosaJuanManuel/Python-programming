import subprocess
import os

#Refrescar Variables de Entorno
#~ subprocess.run(["powershell.exe", '$env:Path = [System.Environment]::GetEnvironmentVariable("Path","User")'])
#~ subprocess.run(["powershell.exe", "echo", "$env:PATH"], shell=True)

#Instalar laravel
subprocess.run(["powershell.exe", "composer global require laravel/installer"], shell=True)

#~ #Refrescar Variables de Entorno
subprocess.run(["powershell.exe", '$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")'])

#Ejecutar new blog
subprocess.run(["powershell.exe", "laravel new blog"], shell=True)
