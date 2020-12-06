# Download market data from Yahoo Finance
# @author: Ryan Bell


import webbrowser
from lxml import html
import requests


###############################################################################
  

def download_yahoo_data(symbol):
    prefix = "https://query1.finance.yahoo.com/v7/finance/download/"
    suffix = "?period1=0&period2=9999999999&interval=1d&events=history&crumb=qx34YrEP5MY"
    
    open_url(prefix + symbol + suffix)

def open_url(url):
    webbrowser.open_new(url)
    

###############################################################################
    
    
def download_symbol_list():
    url = "https://www.slickcharts.com/sp500"
    html_tree = download_html_tree(url)
    return parse_html_tree(html_tree)
    
def download_html_tree(url):
    page = requests.get(url)
    return html.fromstring(page.content)

def parse_html_tree(html_tree):
    symbol = 'a'
    
    while symbol != 'zzzz':
        symbol = increment_string(symbol)
        html_tree.xpath('//a[@href="/symbol/' + symbol + '"]/text()')
    
# Increment string from "A" to "ZZZZ"
def increment_string(symbol):
    s = str(symbol)
    i = len(s) - 1
    
    increment_next = True
    
    while i > 0 and increment_next == True:
        c = increment_character(s[i])
        i = i - 1
        
        if c != "A": increment_next = False            
        
    
# Increment letter from "A" to "Z"
def increment_character(c):
    if c == "Z": return "A"
    
    ch = bytes(c, 'utf-8') 
    s = bytes([ch[0] + 1]) 
    s = str(s)
    return s[2];

    
###############################################################################
    
    
# download_symbol_list()

i = 0
l = "A"
while i < 50:
    i = i + 1
    l = increment_string(l)
    print(l)
    
    

#Unused code

#Yahoo page link to get directly to stock information
#prefix = https://finance.yahoo.com/quote/
#suffix = /history?period1=0&period2=9999999999&interval=1d&filter=history&frequency=1d

#Close Chrome window
#os.system("taskkill /im chrome.exe /f")