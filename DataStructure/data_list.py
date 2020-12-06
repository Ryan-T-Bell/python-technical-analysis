# Data Structure List to store DataNodes by timestamp
# @author: Ryan Bell

from data_node import DataNode

class DataList:
    
    def __init__(self, symbol, data_list):
        self.symbol = symbol
        self.list = data_list

    def to_string(self):
        str = ""
        for node in self.list:
            str = str + node.to_string()
        return str
    
    def parse_str_to_list(str):
        i = 0
        new_list = str.split("\n")
        
        while i < len(new_list):
            new_list[i] = DataNode.parse_str_to_node(new_list[i])
            i += 1
        
        return new_list
    
    def get_node_by_timestamp(self, ts):
        for node in self.list:
            if node.timestamp == ts: 
                return node
        return -1
    
    def compress_list(self, factor):
        i = 0
        new_list = []
        
        while i < len(self.list):
            new_list.append(self.compress_next(i, factor))
            i += factor
        
        return new_list
    
    def compress_next(self, i, factor):
        node = self.list[i]
        limit = min(i + factor, len(self.list))
        
        while i < limit -1:
            i += 1
            node = node.merge_nodes(self.list[i])
        
        return node