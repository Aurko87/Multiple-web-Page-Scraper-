import requests
from bs4 import BeautifulSoup
import csv
final_data = []

# Extracting Raw Data From The Web
for page_num in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    # Converting The Raw Data to Soup
    soup = BeautifulSoup(response.text,"html.parser")
    
    # Filtering The Needed Data
    raw_data = soup.select("article.product_pod")
    for data in raw_data:
        name = data.select_one("h3 a")["title"] 
        price = data.select_one("p.price_color").text
        rating = data.select_one("p.star-rating")["class"][1]
        final_data.append([name,price,rating])

# Writing The Final Data in CSV
with open("Books_multiple_pages.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Name","Price","Ratings"])
    for name,price,rating in final_data:
        writer.writerow([name,price,rating])

# Reading The Final Data (CSV)
with open("Books_multiple_pages.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
