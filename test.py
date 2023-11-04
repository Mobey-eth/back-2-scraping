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

# Find all product items on the page
listings = soup.find_all("div", class_="s-item__info clearfix")
images = soup.find_all("div", class_="s-item__wrapper clearfix")

for i in images:
    image = i.find("img")
    # print(image)
    print(image["src"])

# print(listings)


for listing in listings:
    title = listing.find("div", class_="s-item__title").text
    price = listing.find("span", class_="s-item__price").text

    if title and price:
        title_text = title.strip()
        price_text = price.strip()
        print(title_text, price_text)

        result_dict = {"title": title_text, "price": price_text}
        result_list.append(result_dict)
        item_name.append(title_text)
        prices.append(price_text)

    # print(listing.find("div", class_="s-item__title").text)
    # print(listing.find("span", class_="s-item__price").text)

# #for name in listing.find("div", attrs={"class": "s-item__title"}):
# for name in listing.select_one("div", attrs={"class": "s-item__title"}):
#     prod_name = name.select_one('"aria-level="3')
#     # title = prod_name.text.strip()
#     print(prod_name)
#     # print(title)
#     # item_name.append(prod_name)

print(item_name)
# title = item.find("h3", class_="s-item__title")
# price = item.find("span", class_="s-item__price")
# image = item.find("img", class_="s-item__image-img")

# if title and price and image:
#     title_text = title.text.strip()
#     price_text = price.text.strip()
#     image_src = image["src"]

#     result_dict = {"title": title_text, "price": price_text, "image": image_src}
#     result_list.append(result_dict)

# Print the result list
for result in result_list:
    print("Title:", result["title"])
    print("Price:", result["price"])
    print("\n")

print("Titles:", item_name)
print("Prices:", prices)
