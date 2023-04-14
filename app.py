# Web Scraping an Amazon product's data (Electronics => Computers and Accessories => Monitors) [From amazon.com]

from bs4 import BeautifulSoup
import requests
import json

# Read the index.html file
with open("index.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup to parse the html content
soup = BeautifulSoup(html_content, "html.parser")

# Find all div with class "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"
result_divs = soup.find_all("div", class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

# Data structure to store the results
data = []

# Loop through each div and extract required information
for div in result_divs:
    try:
        # Find img with class "s-image"
        img = div.find("img", class_="s-image")
        link = img["src"]
    except:
        link = ""

    try:
        # Find span with class "a-size-base-plus a-color-base a-text-normal"
        span = div.find("span", class_="a-size-base-plus a-color-base a-text-normal")
        title = span.text
    except:
        title = ""

    try:
        # Find span with class "a-icon-alt"
        span = div.find("span", class_="a-icon-alt")
        rating = span.text
    except:
        rating = ""

    try:
        # Find span with class "a-price-whole"
        span = div.find("span", class_="a-price-whole")
        price = span.text
    except:
        price = ""

    # Store the extracted information in data
    data.append({
        "link": link,
        "title": title,
        "rating": rating,
        "price": price
    })

# Open data.json and write the extracted data
with open("data.json", "w") as file:
    json.dump(data, file)

    
