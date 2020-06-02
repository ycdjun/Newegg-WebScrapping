from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100007709%20601194948%20601202919%20601203901%20601203927%20601205646%20601294835%20601295933%20601296377%20601301599%20601305993%20601321572%20601323902%20601326374%20601331379%20601341679&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2'

# opening up cconnection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

filename = "newegg.csv"
f = open(filename, 'w')
headers = "brand, product_name, price, shipping\n"
f.write(headers)

containers = page_soup.findAll("div", {"class": "item-container"})

for container in containers:

    brand = container.find("div", {"class": "item-branding"}).a.img['title']
    product_name = container.a.img["title"]
    price = container.find("li", {"class": "price-current"}).strong.text
    shipping = container.find('li', {"class": "price-ship"}).text.strip()
    print("Brand: " + brand)
    print("Product Name: " + product_name)
    print("Price: " + price)
    print("Shipping: " + shipping)
    f.write(brand + " , " + product_name.replace(",", " | ") +
            " , " + "$" + price.replace(",", "") + " , " + shipping + "\n")
f.close()
