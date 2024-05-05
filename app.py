from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Función para hacer web scraping del precio del producto
def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Aquí debes inspeccionar el sitio web y encontrar el selector adecuado para el precio del producto
    price_element = soup.find('span', {'class': 'product-price'})  # Ejemplo hipotético del selector
    if price_element:
        return price_element.text.strip()
    else:
        return "Precio no encontrado"

# Ruta principal que muestra el precio del producto
@app.route('/')
def index():
    product_url = "https://example.com/product"  # URL del producto en el sitio web de comercio electrónico
    product_price = get_product_price(product_url)
    return render_template('index.html', product_price=product_price)

if __name__ == '__main__':
    app.run(debug=True)
