from cgitb import html
from get_module import request_get
import requests
import json
from string import Template
import webbrowser
from validate import validate

url = 'https://aves.ninjas.cl/api/birds'

img_template = Template('<img src="$url" width="400" height="500">')
title_template = Template('<figcaption>$titulo</figcaption>')
html_template = Template('''
                        <!DOCTYPE html>
                        <html>
                        <head>
                        <title> Aves de Chile </title>
                        <center><h1> Aves de Chile </h1></center>
                        </head>
                        <body>
                        $body
                        </body>
                        </html>''')

#img_url = response[0]["images"]["full"]
#img_t = img_template.substitute(url = img_url)
#html_template.substitute(body = img_t)
if __name__ == "__main__":
    num_aves = input("Ingrese numero de aves: ")
    num_aves = validate(num_aves)
    response = request_get(url)[:num_aves]
    lista_imagenes_url = [elemento["images"]["full"] for elemento in response]
    lista_nombres_es = [elemento["name"]["spanish"] for elemento in response]
    lista_nombres_en = [elemento["name"]["english"] for elemento in response]
    images = ""

    for img,name_es,name_en in zip(lista_imagenes_url,lista_nombres_es,lista_nombres_en):
        images += img_template.substitute(url=img) +"\n"+ title_template.substitute(titulo=name_es+"/"+name_en) + "<p></p>"
    images = "<center>" + images + "</center>"
    html = html_template.substitute(body = images)

    with open("birds.html","w") as f:
        f.write(html)
    webbrowser.open_new_tab('birds.html')