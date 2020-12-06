import files
import data_download

###############################################################################

def download_symbols_list():
    url = "https://www.slickcharts.com/sp500"
    data_str = data_download.download_url_as_str(url)
    
    return print(data_str)
    
def parse_list(data_str):
    parsed_list = []
    
    for line in data_str:
        symbol = line.split(",")
        parsed_list.append(symbol[0])
        
    return parsed_list


download_symbols_list()