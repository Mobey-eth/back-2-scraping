import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1312&_nkw=airpods+pro&_sacat=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, "lxml")

with open("ebay_results2.txt", "w", encoding="utf-8") as file:
    # Write the prettified HTML content to the file
    file.write(html.text)

print("HTML content has been written to ebay_results.txt")
