import subprocess
import os

#Agregar la consola de php de xampp al path
subprocess.run(["powershell.exe", '[Environment]::SetEnvironmentVariable("PATH", [Environment]::GetEnvironmentVariable("PATH", "User") + ";C:\\Xampp\\php", "User")'])
#Agregar laravel al path
subprocess.run(["powershell.exe", '[Environment]::SetEnvironmentVariable("PATH", [Environment]::GetEnvironmentVariable("PATH", "User") + ";$env:USERPROFILE\\AppData\\Roaming\\Composer\\vendor\\bin", "User")'])

#~ subprocess.run(["powershell.exe", "mkdir", "C:/Composer"], shell=True, capture_output=True)

#Instalar Composer
subprocess.run(["powershell.exe", "c:\\xampp\\php\\php.exe", '-r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"'])
subprocess.run(["powershell.exe", "c:\\xampp\\php\\php.exe", '-r "if (hash_file(\'sha384\', \'composer-setup.php\') === \'c5b9b6d368201a9db6f74e2611495f369991b72d9c8cbd3ffbc63edff210eb73d46ffbfce88669ad33695ef77dc76976\') { echo \'Installer verified\'; } else { echo \'Installer corrupt\'; unlink(\'composer-setup.php\'); } echo PHP_EOL;"'])
subprocess.run(["powershell.exe", "c:\\xampp\\php\\php.exe", "composer-setup.php", "--install-dir=C:/xampp/php"])
subprocess.run(["powershell.exe", "c:\\xampp\\php\\php.exe", '-r "unlink(\'composer-setup.php\');"'])

#Crear Archivo ejecutable de composer
file1= open("C:/xampp/php/composer.bat", "w")
file1.write('@echo OFF\n:: in case DelayedExpansion is on and a path contains ! \nsetlocal DISABLEDELAYEDEXPANSION\nphp "%~dp0composer.phar" %*\n')
file1.close()
