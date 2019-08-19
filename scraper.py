#Hotanya Ragtah 2019

import requests
from bs4 import BeautifulSoup

#can make this better by having a list of random header
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

#vanguard
vanguard = requests.get("https://www.bloomberg.com/quote/VAN1579:AU",headers=example_headers) #need to have headers to avoid being blocked
soup = BeautifulSoup(vanguard.content, 'html.parser')
vanguard_price = soup.find_all("span", class_='priceText__1853e8a5')[0].get_text()
print("Vanguard Price:\n" + vanguard_price+"AUD")

#AMP Capital NZ Index 
ampnzshares = requests.get("https://www.ampcapital.com/nz/en/investments/funds/index-funds/nz-shares-index-fund",headers=example_headers) #need to have headers to avoid being blocked
soup1 = BeautifulSoup(ampnzshares.content, 'html.parser')
ampnzshares_price = soup1.find_all("div", class_='ht-align_center fund_detail_panels-panel-cell')[0].get_text()
print("AMP Capital NZ Index Price:\n" + ampnzshares_price+"NZD")

#AMP Capital Australisian Property Index Fund
ampAustralisianProperty = requests.get("https://www.ampcapital.com/nz/en/investments/funds/index-funds/australasian-property-index-fund",headers=example_headers) #need to have headers to avoid being blocked
soup2 = BeautifulSoup(ampAustralisianProperty.content, 'html.parser')
ampAustralianProperty_price = soup2.find_all("div", class_='ht-align_center fund_detail_panels-panel-cell')[0].get_text()
print("AMP Capital Australisian Property Index Fund:\n" + ampAustralianProperty_price+"NZD")




