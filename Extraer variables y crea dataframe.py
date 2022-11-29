# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:02:31 2022

@author: nagge
"""

#import requests
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
# import required module
import os
import requests
import pandas as pd 
from bs4 import BeautifulSoup
#import htmldate
#from htmldate import find_date


# assign directory
economia = 'C:\\Users\\nagge\\Desktop\\webmining\\webmining\\noticias\\economia'
el_mundo = 'C:\\Users\\nagge\\Desktop\\webmining\\webmining\\noticias\\el-mundo'
el_pais = 'C:\\Users\\nagge\\Desktop\\webmining\\webmining\\noticias\\el-pais'
sociedad = 'C:\\Users\\nagge\\Desktop\\webmining\\webmining\\noticias\\sociedad'

savedirectory = 'C:\\Users\\nagge\\Desktop\\webmining\\webmining'
# iterate over files in that directory

df=pd.DataFrame(columns=["Sentence","label","Time"])

for filename in os.listdir(economia):
    f = os.path.join(economia, filename)
    date = ""
    # checking if it is a file
    if os.path.isfile(f):
        # Opening the html file
        HTMLFile = open(f, "r", encoding="utf8")
        # Reading the file
        index = HTMLFile.read()
        soup = BeautifulSoup(index, 'html.parser')
        data = ''
        b = ""
        noticia = soup.find("main", {"class": "article-text"})
        #print (noticia)
        os.chdir(savedirectory)
        os.getcwd()
        #TXTfile = open(f+".txt","w",encoding="utf8")
        try:
            for data in noticia.find_all("p"):
                b += data.get_text()
        except AttributeError:
            print("esta nota no se pudo:" + f )
        try:
            for data in soup.findAll('time'):
                if data.has_attr('datetime'):
                    date = data['datetime']
                    sep = "T"
                    date = date.split(sep,1)[0]
           
        except AttributeError:
            print("esta nota no saco fecha:" + f )

        noticia = f[52:60]
        nueva_fila = {'Sentence':b, 'label':noticia, 'Time':date}
        df = df.append(nueva_fila, ignore_index=True)
        #TXTfile.write(b+","+date+","+noticia)
        #TXTfile.close()
for filename in os.listdir(el_mundo):
    f = os.path.join(el_mundo, filename)
    date = ""
    # checking if it is a file
    if os.path.isfile(f):
        # Opening the html file
        HTMLFile = open(f, "r", encoding="utf8")
        # Reading the file
        index = HTMLFile.read()
        soup = BeautifulSoup(index, 'html.parser')
        data = ''
        b = ""
        noticia = soup.find("main", {"class": "article-text"})
        #print (noticia)
        os.chdir(savedirectory)
        os.getcwd()
        #TXTfile = open(f+".txt","w",encoding="utf8")
        try:
            for data in noticia.find_all("p"):
                b += data.get_text()
        except AttributeError:
            print("esta nota no se pudo:" + f )
        try:
            for data in soup.findAll('time'):
                if data.has_attr('datetime'):
                    date = data['datetime']
                    sep = "T"
                    date = date.split(sep,1)[0]
                                                 
        except AttributeError:
            print("esta nota no saco fecha:" + f )

        noticia = f[52:60]
        nueva_fila = {'Sentence':b, 'label':noticia, 'Time':date}
        df = df.append(nueva_fila, ignore_index=True)
        #TXTfile.write(b+","+date+","+noticia)
        #TXTfile.close()
        
for filename in os.listdir(el_pais):
    f = os.path.join(el_pais, filename)
    date = ""
    # checking if it is a file
    if os.path.isfile(f):
        # Opening the html file
        HTMLFile = open(f, "r", encoding="utf8")
        # Reading the file
        index = HTMLFile.read()
        soup = BeautifulSoup(index, 'html.parser')
        data = ''
        b = ""
        noticia = soup.find("main", {"class": "article-text"})
        #print (noticia)
        os.chdir(savedirectory)
        os.getcwd()
        #TXTfile = open(f+".txt","w",encoding="utf8")
        try:
            for data in noticia.find_all("p"):
                b += data.get_text()
        except AttributeError:
            print("esta nota no se pudo:" + f )
        try:
            for data in soup.findAll('time'):
                if data.has_attr('datetime'):
                    date = data['datetime']
                    sep = "T"
                    date = date.split(sep,1)[0]
                    
        except AttributeError:
            print("esta nota no saco fecha:" + f )

        noticia = f[52:59]
        nueva_fila = {'Sentence':b, 'label':noticia, 'Time':date}
        df = df.append(nueva_fila, ignore_index=True)
        #TXTfile.write(b+","+date+","+noticia)
        #TXTfile.close()
        
for filename in os.listdir(sociedad):
    f = os.path.join(sociedad, filename)
    date = ""
    # checking if it is a file
    if os.path.isfile(f):
        # Opening the html file
        HTMLFile = open(f, "r", encoding="utf8")
        # Reading the file
        index = HTMLFile.read()
        soup = BeautifulSoup(index, 'html.parser')
        data = ''
        b = ""
        noticia = soup.find("main", {"class": "article-text"})
        #print (noticia)
        os.chdir(savedirectory)
        os.getcwd()
        #TXTfile = open(f+".txt","w",encoding="utf8")
        try:
            for data in noticia.find_all("p"):
                b += data.get_text()
        except AttributeError:
            print("esta nota no se pudo:" + f )
        try:
            for data in soup.findAll('time'):
                if data.has_attr('datetime'):
                    date = data['datetime']
                    sep = "T"
                    date = date.split(sep,1)[0]
                    
        except AttributeError:
            print("esta nota no saco fecha:" + f )

        noticia = f[52:60]
        nueva_fila = {'Sentence':b, 'label':noticia, 'Time':date}
        df = df.append(nueva_fila, ignore_index=True)
        #TXTfile.write(b+","+date+","+noticia)
        #TXTfile.close()

df.to_csv('notas_completo.csv', header=True, index=False, encoding='utf-8')