import requests
import os
import json
import time


class Crawling:
    bearer_token = ""
    search_url = ""
    query_params = {}

    def __init__(self):
        # To set your environment variables in your terminal run the following line:
        # export 'BEARER_TOKEN'='<your_bearer_token>'
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAMjyOwEAAAAAYm8zDZ9NMtvCd4K%2FTckEVsozHCA%3Daj3fsQ8Pgmka7tfdzLkeTFcY8jtvZW0hhDps7UFVnsiU1aJhnv"
        self.search_url = "https://api.twitter.com/2/tweets/search/all"

        # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
        # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
        self.query_params = {'query': 'baclofen', 'tweet.fields': 'created_at', 'start_time': '2020-01-01T00:00:00Z',
                        'end_time': '2021-01-01T00:00:00Z', 'max_results': '500'}

    def create_headers(self):
        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
        return headers

    def connect_to_endpoint(self, headers):
        response = requests.request("GET", self.search_url, headers=headers, params=self.query_params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main_act(self):
        headers = self.create_headers()
        json_response = self.connect_to_endpoint(headers)
        data = json.dumps(json_response, indent=4, sort_keys=True)
        print(data)
        self.query_params['next_token'] = json_response['meta']['next_token']
        time.sleep(2)
        self.main_act()

