#Hotanya Ragtah 2019

import requests
from bs4 import BeautifulSoup

#can make this better by having a list of random header
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

#page = requests.get("https://www.vanguardinvestments.com.au/adviser/adv/investments/product.html#/fundDetail/wholesale/portId=8122/?portfolio")
page = requests.get("https://www.bloomberg.com/quote/VAN1579:AU",headers=example_headers) #need to have headers to avoid being blocked
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
find = soup.find_all("span",class_='priceText__1853e8a5')[0].get_text()
print(find)


#print(list(soup.children)[3])
#print(soup.prettify())

