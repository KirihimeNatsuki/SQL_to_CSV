@ECHO OFF
:: Installation des composants nécessaires à l'utilisation du script SQL_to_CSV.
TITLE Install SQL_to_CSV script components
SET /p InstallPython= "Voulez vous installer Python 3.10 ? (Y/N) "
IF %InstallPython% == "Y" (
    ECHO Installation de python 3.10 en cours.
    powershell -command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'C:/Tools/python-3.10.0-amd64.exe'); & c:\Tools\python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=c:\Tools\Python310; [Environment]::SetEnvironmentVariable('PATH', ${env:path} + ';C:\Tools\Python310', 'Machine')"
) ELSE (
    ECHO Python 3.10 ne sera pas installé
)
PAUSE
ECHO Installation de numpy en cours
pip install numpy
ECHO Installation de cx_Freeze en cours
python -m pip install --upgrade cx_Freeze
ECHO Installation de l'executable
python setup.py build