# File management module
# @author: Ryan Bell

import os
import sys


###############################################################################
    

def get_current_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def get_delimiter():
    path = get_current_path()    
    if (path.find('\\') != -1):
        return '\\'
    else:
        return '/'
    
def get_download_path():
    d = get_delimiter()
    path = get_current_path()
    ls = path.split(d)
    return ls[0] + d + ls[1] + d + ls[2] + d + "Downloads" + d

def get_data_path():
    d = get_delimiter()
    return get_current_path() + d + "Data"


###############################################################################
    

def move_file_from_downloads_to_data(file_name):
    read_path = get_download_path() + file_name
    write_path = get_data_path() + file_name
    
    move_file(read_path, write_path)
     
def move_file(read_path, write_path):
    s = read_file(read_path)
    write_file(s, write_path)
    
    os.remove(read_path)
    
def read_file(read_path):
    file = open(read_path, "r")
    s = file.read()
    file.close()
    
    return s

def write_file(str, write_path):
    file = open(write_path, "w")
    file.write(str)
    file.close()


###############################################################################


def read_file_as_list(read_path):
    s = read_file(read_path)
    return s.split(',')