class WordEntry(object):
    '''
    A class inheriting from Vehicle describing a bus

    ...

    Additional Attributes
    ----------
    from_station : str
        starting station of the bus
    
    to_station : str
        end station of the bus   
    '''
    
    def __init__(self, deutsch, type, englisch, stats):
        self.deutsch = deutsch
        self.type = type
        self.englisch = englisch
        self.stats = stats
    
    def vocab_entry(self):
        return str([str(self.deutsch), str(self.type), str(self.englisch), str(self.stats)])