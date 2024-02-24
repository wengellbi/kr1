import lxml
import requests
from bs4 import BeautifulSoup

session = requests.session()
header = {"user-agent": "big_grid row form-row row-cols-1 row cols-sm-2 row-cols-xl-3 roq-cols-xxl-4"}

for j in range(1, 11):
    url = f"https://cash-backer.club/shops={j}"

    response = session.get(url,headers=header)
    soup = BeautifulSoup(response.text, "lxml")

    all_product = soup.find("div", class_="row col-lg-9 col-md-9 col-12")

    products = all_product.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

    for elem in products:
        price = elem.find("p", class_="card-text").text
        price = price[price.find(":")+1:price.find("₽")]
        title = elem.find("h3", class_="card-title").text.strip()
        with open("kups.txt", "a", encoding="utf-8") as file:
            file.write(f"{title} ---->>>>{price}\n")
            print(price)