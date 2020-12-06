# Data structure that stores stock market data for one timestamp
# @author: Ryan Bell


from decimal import Decimal

class DataNode:
    
    def __init__(self, ts, o, h, l, c, v):
        self.timestamp = int(ts)
        self.open = Decimal(o)
        self.high = Decimal(h)
        self.low = Decimal(l)
        self.close = Decimal(c)
        self.volume = int(v)
    
    # Parse comma separated string to DataNode
    def parse_str_to_node(str):
        ls = str.split(",")
        return DataNode(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])
    
    def to_string(self):
        return (
        str(self.timestamp) + ", " +
        str(self.open)  + ", " +
        str(self.high)  + ", " +
        str(self.low)  + ", " +
        str(self.close)  + ", " + 
        str(self.volume) + "\n")
        
    def merge_nodes(self, node):
        ts = self.timestamp
        o = self.open
        h = max(self.high, node.high)
        l = min(self.low, node.low)
        c = node.close
        v = self.volume + node.volume
        
        return DataNode(ts, o, h, l, c, v)