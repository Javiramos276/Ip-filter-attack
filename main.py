import os
import gzip
from os import listdir
from os.path import isfile, join
import re


# Carpeta de directorio
path = "Elija su directorio"

# Obtenemos los archivos con extension .gz en formato de lista
onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".gz")] 


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

palabra = input("Ingrese el user-agent que desea rastrear: ")

def buscador_ips(file_content,palabra):
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') #Se crea el extractor de ips
    for line in file_content.split('\n'): 
        if palabra in line:
            match = pattern.search(line)
            if match:
                lista_total_ips.append(match[0])
    return lista_total_ips

def eliminar_duplicados(lista_total_ips):
    lista_ips_sin_repetir = [] #Se crea una lista vacia que contendra las ip sin repetir
    for ips in lista_total_ips: #Se recorre la lista de ips totales y si se encuentra alguna ip repetida se descarta
        if ips not in lista_ips_sin_repetir:
            lista_ips_sin_repetir.append(ips)
    return lista_ips_sin_repetir

def escribir_ips(lista_ips_sin_repetir):
    file = open(".htaccess", "w")
    file.writelines('<Limit GET POST>' '\n' 'order allow, deny' '\n' 'allow from all' '\n')
    for ip in lista_ips_sin_repetir:
        file.writelines('deny from'+ ' ' + ip +'\n')
    file.writelines('</Limit>')
    file.close()
        

lista_total_ips=[] #Se crea la lista vacia donde iran las ips


for archive in onlyfiles: #Para todos los archivos que se encuentren en la lista de archivos .gz se lee el contenido y se buscan las ips
    with gzip.open(archive, 'rb') as f:
        file_content = f.read().decode()
        ips = buscador_ips(file_content,palabra)
        lista_total_ips.extend(ips) #Se utiliza el metodo extend porque se manejan muchos elementos en una lista 

for file in os.listdir(path):
    if file.endswith(".py") or file.endswith(".gz"):
        continue

    file_path = join(path,file)
    with open(file_path, 'rb') as f:
        file_content = f.read().decode()
        ips = buscador_ips(file_content,palabra)
        lista_total_ips.extend(ips)

lista_sin_repetir = eliminar_duplicados(lista_total_ips)
print(lista_sin_repetir)
print(len(lista_sin_repetir))
escribir_ips(lista_sin_repetir)