# Download market data from Yahoo Finance
# @author: Ryan Bell


import webbrowser
import urllib


###############################################################################
  

def download_url(url):
    webbrowser.open(url, new=0, autoraise=False)

def download_url_as_str(url):
    return str(urllib.request.urlopen(url).read())

def download_yahoo_data(symbol):
    prefix = "https://query1.finance.yahoo.com/v7/finance/download/"
    suffix = "?period1=0&period2=9999999999&interval=1d&events=history&crumb=qx34YrEP5MY"
    
    download_url(prefix + symbol + suffix)

def download_yahoo_data_list():
    symbol_list = get_s&p_list()
    for symbol in symbol_list:
        download_yahoo_data(symbol)

#Unused code

#Yahoo page link to get directly to stock information
#prefix = https://finance.yahoo.com/quote/
#suffix = /history?period1=0&period2=9999999999&interval=1d&filter=history&frequency=1d

#Close Chrome window
#os.system("taskkill /im chrome.exe /f")