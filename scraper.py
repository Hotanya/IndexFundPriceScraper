#Hotanya Ragtah 2019

import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime

def CurrentPortfolioValue():
    initial_porfolio_price = 100
    initial_date = date(2018, 8, 19)
    fortnightly_contrib = 50
    current_value = 0
    #print(initial_date)

    #get day difference between today and initial date
    current_date = date.today()
    days_difference = (current_date - initial_date).days #.days shows just the number of days
    #print(days_difference)

    count=days_difference
    while count > 14: #while difference is less than 14 days i.e forntightly payment hasnt been made
        current_value += initial_porfolio_price + fortnightly_contrib
        count = count - 14
    print("Current Portfolio value is $"+str(current_value))

CurrentPortfolioValue() #retrieves current portfolio value

#sets a user-agent    
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#can make this better by having a list of random header


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




