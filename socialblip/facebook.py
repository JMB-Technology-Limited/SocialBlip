import urllib

class Facebook():
    
    def __init__(self,  config,  data):
        self.config = config
        self.data = data

    def get_url(self,  entry):
        url = 'https://www.blipfoto.com/entry/' +  str(entry['entry_id'])
        return 'https://www.facebook.com/sharer/sharer.php?u=' + urllib.parse.quote_plus(url)
        
