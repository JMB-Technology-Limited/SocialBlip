import requests

class Blipfoto:
    
    def __init__(self,  config,  data):
        self.config = config
        self.data = data

    def get_entries(self):
        url = 'https://api.blipfoto.com/4/entries/journal'
        headers = {'Authorization': 'Bearer ' + self.config.config['blipfoto']['access_token']}
        data = { "page_size": 30 }
        r = requests.get(url, headers=headers , params=data )
        return r.json()['data']['entries']
