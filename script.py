import requests
from bs4 import BeautifulSoup

# URL del sitio exito.com
url_exito = 'https://www.exito.com/'
# Realiza una solicitud HTTP GET a la página de Exito
response_exito = requests.get(url_exito)

body_exito = []
"""
# Verifica que la solicitud fue exitosa
if response_exito.status_code == 200:
    # Parsea el contenido HTML de la página usando BeautifulSoup
    # response text tiene todo el dom de la página web, lo que uno ve en elementos al inspeccionar la página
    soup_exito = BeautifulSoup(response_exito.text, 'html')
    #print(soup_exito)

#que busque dentro de la variable soup las table de clase wikitable sortable
    #body = soup.find_all('table', class_="wikitable sortable")
else:
    print('Error al realizar la solicitud HTTP:', response_exito.status_code)
"""
# URL del sitio alkosto.com
url_alkosto = 'https://www.alkosto.com/'
# Realiza una solicitud HTTP GET a la página de Exito
response_alkosto = requests.get(url_alkosto)

body_alkosto = []
"""
# Verifica que la solicitud fue exitosa
if response_alkosto.status_code == 200:
    # Parsea el contenido HTML de la página usando BeautifulSoup
    # response text tiene todo el dom de la página web, lo que uno ve en elementos al inspeccionar la página
    soup_alkosto = BeautifulSoup(response_alkosto.text, 'html')
    print(soup_alkosto)

#que busque dentro de la variable soup las table de clase wikitable sortable
    #body = soup.find_all('table', class_="wikitable sortable")
else:
    print('Error al realizar la solicitud HTTP:', response_alkosto.status_code)
"""
def buscarProductosExito(producto):
    nombreProductos = []
    precioProductos = []
    URL_busqueda = f"{url_exito}s?q={producto}&sort=orders_desc&page="
    cantidadPaginas = 1
    for i in range(cantidadPaginas):
        URL_producto = f"{URL_busqueda}{i}"
        r = requests.get(URL_producto)
        soap = BeautifulSoup(r.text, "html.parser")
        productos = soap.find_all(class_ = "product-grid_fs-product-grid__SF25P")[0].ul
        productos = productos.find_all('li')
        
        print(len(productos))
        
        print(productos[0])
        
        
"""
        divs = soap.find_all('ul')[0].li.h3.text
        for div in divs:
            print(div.get_text(strip=True))
            if div.title != None:
                if producto in div.title:
                    print(div)
"""

buscarProductosExito("televisores")