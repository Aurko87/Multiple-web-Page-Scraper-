import requests
from bs4 import BeautifulSoup
import csv

raw_data = []

# Extracting Raw data from the Web
for page_num in range(1,11):
    url = f"https://quotes.toscrape.com/page/{page_num}/"
    response = requests.get(url)
    # Soup
    soup = BeautifulSoup(response.text,"html.parser")

    # Filtering Needed Data
    needed_data = soup.select("div.quote")
    for data in needed_data:
        quotes = data.select_one("span.text")
        authors = data.select_one("small.author")
        tags = data.select("a.tag")
        tags_list = [tag.text for tag in tags]
        raw_data.append([quotes.text,authors.text,tags_list])

# CSV Writing
with open("Quotes,Authors,Tags.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes","Authors","Tags"])
    for quotes,authors,tags in raw_data:
        writer.writerow([quotes,authors,tags])

# CSV Reading
with open("Quotes,Authors,Tags.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
