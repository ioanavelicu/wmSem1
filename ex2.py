### **Exercise 2: Web Scraping a Product Listings Page**
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# Fetch the webpage content
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract product names and prices
products = soup.find_all("div", class_="thumbnail")
products_list = []

print("Scraped Product Prices:\n")

for product in products[:10]:  # Limit to first 10 products
    name = product.find("a", class_="title").text.strip()
    price = product.find("h4", class_="price").text.strip()
    print(f"Product: {name}")
    print(f"Price: {price}\n")
    products_list.append(
        {"nume": name,
         "price": price}
    )


df_cleaned = pd.DataFrame(products_list)

df_cleaned.to_csv("scraped_products.csv", index=False)

# Obiectiv: Extrageți și structurați date de pe un site web public.
#
# Pași:
# Utilizați BeautifulSoup pentru a extrage numele produselor și prețurile de pe un site de testare e-commerce: Web Scraper Test Site.
# Extrageți numele produselor și prețurile de pe pagină.
# Stocați datele extrase într-un DataFrame Pandas.
# Eliminați eventualele produse duplicate.
# Rezultat așteptat: Un DataFrame cu coloanele Nume Produs și Preț, conținând cel puțin 10 produse.