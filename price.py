''' Gets the prices list from the CouchDB server '''
import json
import requests

d = {}
with open('creds.json') as f:
    d = json.loads(f.read())

USERNAME = d['username']
PASSWORD = d['password']
SHOP_NAME = d['shop_name']

BASE_URL = 'http://localhost:5984'

class PriceDict(object):
    ''' Makes request and holds data '''
    def __init__(self):
        j = {'name': USERNAME, 'password': PASSWORD}
        h = {'content-type': 'application/json'}
        r = requests.post(BASE_URL + '/_session', data=json.dumps(j), headers=h)
        a = 'AuthSession'
        self.cookie = a + '=' + r.cookies[a]
        h = {'set-cookie': self.cookie}
        r = requests.get(BASE_URL + '/shopkeeper/shops:' + USERNAME, headers=h)
        self.priceMap = {}
        try:
            self.priceMap = json.loads(r.text)['shops'][SHOP_NAME]
        except:
            pass
        print(self.priceMap)


if __name__ == '__main__':
    PriceDict()