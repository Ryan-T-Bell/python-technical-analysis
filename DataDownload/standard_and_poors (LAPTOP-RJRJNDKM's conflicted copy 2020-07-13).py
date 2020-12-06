import files

def convert_text_to_dictionary(file_name, index):
    
    data_list = get_file_as_list(file_name)
    str_return = ""
    
    for line in data_list:
        str_return = add_new_dictionary_line(str_return, line)
    
    return_path = files.get_current_path + file_name + "2"

    files.write_file(str_return, return_path)

def get_file_as_list(file_name):
    path = files.get_current_path() + "\\" + file_name
    s = str(files.read_file(path))
    return s.split(",")
    
def add_new_dictionary_line(str_return, line):
    
    
    