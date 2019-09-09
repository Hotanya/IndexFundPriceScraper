#Hotanya Ragtah 2019

from botocore.vendored import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta
import json


def lambda_handler(event, context):

    initial_porfolio_price = float (2863.03)
    initial_date = date(2019, 9, 9) #set the initial date to a date where the fortnightly payment has gone
    num_of_shares_vanguard = float(1177.0900)
    num_of_shares_AMPNZShares = float(648.8300)
    num_of_shares_AMPAustralisianProperty = float(123.2400)
    fortnightly_contrib = float(100.00)
    current_value = initial_porfolio_price
    #print(initial_date)

    #sets a user-agent
    example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br'} #can make this better by having a list of random header


    #vanguard
    vanguard = requests.get("https://api.vanguard.com/rs/gre/gra/1.7.0/datasets/auw-retail-prices-data-mf.jsonp?vars=portId:8125&path=[portId=8125][0]",headers=example_headers).text #need to have headers to avoid being blocked
    nocallback = vanguard.replace('callback(','') #removed the callback( that it returns. we just need the json
    final = nocallback.replace(')','') #removes the ) at the end
    parsejson=json.loads(final) #parses it as json
    vanguard_price = parsejson["price"] #retrieves the price
    print("Vanguard Price:\n" + str(vanguard_price)+"AUD")

    #AMP Capital NZ Index
    ampnzshares = requests.get("https://www.ampcapital.com/nz/en/investments/funds/index-funds/nz-shares-index-fund",headers=example_headers) #need to have headers to avoid being blocked
    soup1 = BeautifulSoup(ampnzshares.content, 'html.parser')
    ampnzshares_price = soup1.find_all("div", class_ = 'ht-module_title ht-highlight_color')[1].get_text()
    #print("AMP Capital NZ Index Price:\n" + ampnzshares_price+"NZD")

    #AMP Capital Australisian Property Index Fund
    ampAustralisianProperty = requests.get("https://www.ampcapital.com/nz/en/investments/funds/index-funds/australasian-property-index-fund",headers=example_headers) #need to have headers to avoid being blocked
    soup2 = BeautifulSoup(ampAustralisianProperty.content, 'html.parser')
    ampAustralianProperty_price = soup2.find_all("div", class_ = 'ht-module_title ht-highlight_color')[1].get_text()
    #print("AMP Capital Australisian Property Index Fund:\n" + ampAustralianProperty_price+"NZD")

    #get day difference between today and initial date
    current_date = date.today()
    days_difference = (current_date - initial_date).days #.days shows just the number of days
    #print(days_difference)

    count = days_difference
    while count > 14: #while difference is less than 14 days i.e forntightly payment hasnt been made
        #current_value += initial_porfolio_price + (float(50) * float(vanguard_price)) + (float(50) * float(ampnzshares_price))
        num_of_shares_vanguard = num_of_shares_vanguard + (float(50)/float(vanguard_price))
        num_of_shares_AMPNZShares = num_of_shares_AMPNZShares + (float(50)/float(ampnzshares_price))
        count = count - 14
    print("Current Portfolio value is $" + str(current_value)+'AUD')
    return {
       "statusCode": 200,
       "body": json.dumps(current_value)}