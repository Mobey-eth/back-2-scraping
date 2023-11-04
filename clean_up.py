import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1312&_nkw=airpods+pro&_sacat=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

with open("ebay_results.txt", "r") as file:
    # Write the prettified HTML content to the file
    html = file.read()

# html = requests.get(url, headers=headers)
soup = BeautifulSoup(html, "lxml")

result_list = []
item_name = []
prices = []
product_images = []
links = []
description = []

# Find all product items on the page
listings = soup.find_all("div", class_="s-item__info clearfix")
images = soup.find_all("div", class_="s-item__wrapper clearfix")

for i in images:
    image = i.find("img")
    image_url = image["src"]
    product_images.append(image_url)

# print(product_images)


for listing in listings:
    title = listing.find("div", class_="s-item__title").text

    product_status_element = listing.find("div", class_="s-item__subtitle")
    product_status = (
        product_status_element.text
        if product_status_element is not None
        else "No status available"
    )

    price = listing.find("span", class_="s-item__price").text

    product_url = listing.find("a")
    link = product_url["href"]
    # print("Link:", link)
    # print("status:", product_status)

    if title and price and product_status:
        title_text = title.strip()
        price_text = price.strip()
        status = product_status.strip()

        result_dict = {
            "title": title_text,
            "price": price_text,
            "status": status,
            "link": link,
        }
        result_list.append(result_dict)

        # To get a list of the product names and their prices
        item_name.append(title_text)
        prices.append(price_text)


# Print the result list
for result in result_list:
    print("Title:", result["title"])
    print("Price:", result["price"])
    print("Status:", result["status"])
    print("Product Link:", result["link"])
    print("\n")
