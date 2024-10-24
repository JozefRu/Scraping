
import csv, json
from email import header
import string
import unicodedata
import pandas as pd
import requests

jsonFilePath = 'databaza.json'

CSV_URL = 'https://opendata.arcgis.com/api/v3/datasets/6b66219049674794b462b90512081220_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'


with requests.Session() as s:

    download = s.get(CSV_URL)



    decoded_content = download.content.decode('utf-8')



    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    my_list = list(cr)

    data = {}

###########################################################

# writing the data into the file

csvfile = open('g4g.csv', 'w+', encoding='utf-8', newline ='')


field = ['ObjectId','organizacia_ICO','organizacia_nazov', 'organizacia_adresa_ulica', 'organizacia_adresa_supisne_cisl', 'organizacia_adresa_orientacne_c', 'organizacia_adresa_PSC', 'organizacia_adresa_mesto', 'organizacia_adresa_krajina', 'organizacia_struktura', 'interne_cislo_zmluvy', 'externe_cislo_zmluvy', 'datum_podpisu', 'datum_ucinnosti', 'dátum_skoncenia_ucinnosti', 'typ', 'interne_cislo_suvisiacej_zmluvy', 'predmet', 'dodavatel_ICO', 'dodavatel_nazov', 'dodavatel_adresa_textovy_retaze', 'dodavatel_adresa_ulica', 'dodavatel_adresa_supisne_cislo', 'dodavatel_adresa_orientacne_cis', 'dodavatel_adresa_PSC', 'dodavatel_adresa_mesto', 'dodavatel_adresa_krajina', 'suma_zmluvy', 'mena', 'datum_zverejnenia', 'zverejnil', 'dokument', 'datum_aktualizacie']

#writerr = csv.writer(csvfile)
#writerr.writerow(header)

csvfile.write = csv.writer(csvfile, delimiter=',')

#new = data["Name"].str.split(" ", n = 1, expand = True)
#csvfile['Col'].str.split(',', expand=True)
csvfile.write.writerows(my_list)

