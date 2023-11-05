import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1312&_nkw=airpods+pro&_sacat=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# with open("ebay_results.txt", "r") as file:
#     # Write the prettified HTML content to the file
#     html = file.read()

html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, "lxml")

result_list = []

# Find all product items on the page
listings = soup.find_all("div", class_="s-item__info clearfix")
images = soup.find_all("div", class_="s-item__wrapper clearfix")

for listing, image_container in zip(listings, images):
    title = listing.find("div", class_="s-item__title").text
    price = listing.find("span", class_="s-item__price").text

    if title and price:
        title_text = title.strip()
        price_text = price.strip()

        image = image_container.find("img")
        image_url = image["src"]

        result_dict = {"title": title_text, "price": price_text, "image_url": image_url}
        result_list.append(result_dict)

# Write the result_list to a CSV file
with open("ebay_results.csv", "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["title", "price", "image_url"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for result in result_list:
        writer.writerow(result)

# Print the result list
for result in result_list:
    print("Title:", result["title"])
    print("Price:", result["price"])
    print("Image URL:", result["image_url"])
    print("\n")
