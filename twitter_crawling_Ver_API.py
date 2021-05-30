import requests
import json
import datetime
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
        self.query_params = {'query': '', 'tweet.fields': 'created_at', 'start_time': '2016-01-01T00:00:00Z',
                             'end_time': '2021-01-01T00:00:00Z', 'max_results': '500'}

    def create_headers(self):
        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
        return headers

    def connect_to_endpoint(self, headers):
        response = requests.request("GET", self.search_url, headers=headers, params=self.query_params)
        # print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main_act_months(self, brand_list, drug_name):
        self.query_params['tweet.fields'] = "lang"
        for year in range(2019, 2021):
            for month in range(6, 14):
                if month == 13:
                    self.query_params['end_time'] = str(year + 1) + "-" + str(1).zfill(2) + "-01T00:00:00Z"
                    self.query_params['start_time'] = str(year) + "-" + str(month - 1).zfill(2) + "-01T00:00:00Z"
                else:
                    self.query_params['end_time'] = str(year) + "-" + str(month).zfill(2) + "-01T00:00:00Z"
                    self.query_params['start_time'] = str(year) + "-" + str(month - 1).zfill(2) + "-01T00:00:00Z"
                fw = open(drug_name + " " + self.query_params['start_time'][0:10] + "~" + self.query_params['end_time'][
                                                                                          0:10] + ".txt", "w")
                for brand_name in brand_list:
                    self.query_params['query'] = brand_name
                    print(self.query_params)
                    self.crawling_part(fw)
                fw.close()

    def main_act_weeks(self, brand_list, drug_name):
        date = datetime.date(2020, 2, 1)
        self.query_params['start_time'] = str(date) + "T00:00:00Z"
        while True:
            date = date + datetime.timedelta(weeks=1)
            self.query_params['end_time'] = str(date) + "T00:00:00Z"
            dateforcheck = str(date)
            if dateforcheck[0:7] == "2020-03":
                break

            # main activity
            fw = open(drug_name + " " + self.query_params['start_time'][0:10] + "~" + self.query_params['end_time'][
                                                                                      0:10] + ".txt", "w")
            for brand_name in brand_list:
                self.query_params['query'] = brand_name
                print(self.query_params)
                self.crawling_part(fw)
            fw.close()

            self.query_params['start_time'] = str(date) + "T00:00:00Z"

    def main_act_indi(self, brand_list, drug_name):
        self.query_params['start_time'] = "2020-02-01T00:00:00Z"
        self.query_params['end_time'] = "2020-03-01T00:00:00Z"
        self.query_params['tweet.fields'] = "lang"
        # main activity
        fw = open(drug_name + " " + self.query_params['start_time'][0:10] + "~" + self.query_params['end_time'][
                                                                                  0:10] + ".txt", "w")
        for brand_name in brand_list:
            self.query_params['query'] = brand_name
            print(self.query_params)
            self.crawling_part(fw)
        fw.close()

    def crawling_part(self, fw):
        headers = self.create_headers()
        json_response = self.connect_to_endpoint(headers)
        data = json.dumps(json_response, indent=4, sort_keys=True)
        fw.write(data)
        try:
            self.query_params['next_token'] = json_response['meta']['next_token']
        except Exception as e:
            print(self.query_params['query'] + " done")
            self.query_params['next_token'] = "DUMMY"
            del self.query_params['next_token']
            # print(e)
            time.sleep(2)
            return
        time.sleep(2)
        self.crawling_part(fw)
