import re, shutil
import numpy as np
import sys
from io import StringIO
import calendar
import time
from datetime import datetime

#Fonctions pour convertir un élément du tableau en liste
def Convert(string):
    li = list(string.split(","))
    return li

#Fonction principale permettant de récupérer les informations du fichier sql
def read_sql(sql_filename):
    sio = StringIO()
    #On ouvre le fichier entré en paramètre
    with open(sql_filename, 'r', encoding="UTF-16") as f:
        data_final = []
        #Boucle principale qui récupère les informations de chaque ligne du fichier
        for line in f:
            line = line.strip()
            #Récupération des données des INSERT INTO
            if line.lower().startswith('insert'):
                #Récupération du nom de la table
                match = re.search('INSERT INTO  `([0-9_a-zA-Z]+)`', line)
                if match:
                    tablename = match.group(1)
                else:
                    print(line)
                #Récupération des données produits
                data = re.findall('\([^\)]*\)', line)
                table_columns = data[0]
                res_data = get_data(data)
                for i in res_data:
                    data_final.append(i)
            else:
                continue
    #Récupération des colonnes (ean,prix,nom_produit,...)
    columns = Convert(table_columns)
    columns = [c.replace('(', '').replace(')', '').replace('`', '') for c in columns]
    for col in columns:
        sio.write(col.strip())
        sio.write(';')
    
    sio.write("\n")
    print("TABLENAME :", tablename)
    print("COLUMNS :", columns)

    #On met sous forme de tableau les données produit récupérées
    data_final = np.array(data_final, dtype=None)
    print("Data lines :")
    #Boucle permettant de formater les données du tableau pour le format CSV
    for i in range (len(data_final)):
        newline = data_final[i]
        newline = newline.strip(' ()')
        newline = newline.replace(',', ';') #Replace to format csv in Excel
        newline = newline.replace('`', '') #Delete comma 1
        newline = newline.replace("'", "") #Delete comma 2
        print(newline)
        sio.write(newline)
        sio.write("\n")
    sio.seek(0)
    #On créé le fichier .csv avec le nom de la table comme nom de fichier ainsi que la date du jour
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    date_time = datetime.fromtimestamp(ts)
    d = date_time.strftime("%m-%d-%Y")
    print("Current date : ", d)
    with open (tablename+'_'+d+'.csv', 'w') as fd:
        shutil.copyfileobj(sio, fd,-1)
    print("CSV filename :", tablename+'_'+d+'.csv')
    print("DONE")
    return sio

#Fonction nécessaire pour la récupéation des données produit
def get_data(data):
    datas = np.array(data, dtype=None)
    datan = datas[np.r_[1:len(datas)]]
    data_return = []
    for i in datan:
        data_return.append(i)
    return data_return

#Main
def main():
    try:
        fileName = input("Entrer le nom du fichier : ")
        print("Filename : ", fileName)
        donnees = read_sql(fileName)
    except KeyboardInterrupt:
        sys.exit(0)

main()