import json
import requests


class Bitcoin:
    coindesk = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    def __init__(self):
        pass

    def get_current_price(self, url=coindesk):
        self.resp = requests.get(url)
        if self.resp.status_code == 200:
            return json.loads(self.resp.content.decode('utf-8'))
        else:
            return None
    
    def float_price(self, json_response):
        if json_response is not None:
            rate = json_response['bpi']['USD']['rate_float']
            try:
                return float(rate)
            except:
                return None
        else:
            return None
