@ECHO OFF
:: Installation des composants nécessaires à l'utilisation du script SQL_to_CSV.
TITLE Install Carnivor script components
ECHO Installation de python 3.10 en cours.
python-3.10.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
PAUSE
ECHO Installation de numpy en cours
pip install numpy
ECHO Installation de cx_Freeze en cours
python -m pip install --upgrade cx_Freeze
ECHO Installation de l'executable
python setup.py build