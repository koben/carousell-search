import requests
import json



class CarousellSearch(object):
    def __init__(self, query_string=None, results=30):
        self.base_url = ("https://www.carousell.com.my/api-service/filter/search/3.3/products/")
        self.fields = {
            "count":results,
            "countryCode":"MY",
            "countryId":"1733045",
            "filters":[],
            "isFreeItems": False,
            "locale":"en",
            "prefill": {
                "prefill_sort_by":""
            },
            "query": query_string
        }
        self.query_fields = json.dumps(self.fields)

    def send_request(self):
        headers = {
           "Content-Type": "application/json",
        }
        r = requests.post( url=self.base_url, data=self.query_fields , headers=headers)
        data = json.loads(r.text)
        if 'results' in data['data']:
            return data['data']['results']
        return {}
