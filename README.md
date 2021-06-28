# twitter_crawling_Ver_API

## API Usage
### main_act_id(self, author_id_info, start_time, end_time)
#### input_values
author_id_info : (str) author's id ex) "1061602142"   
start_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2016-01-01T00:00:00Z"   
end_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2017-01-01T00:00:00Z"   

#### ex) main_act_id("1061602142", "2016-01-01T00:00:00Z", "2016-01-08T00:00:00Z")
#### output file name : 1061602142 2016-01-01~2016-01-08.txt
#### output data : 
~~~
{
    "data": [
        {
            "author_id": "1061602142",
            "created_at": "2016-01-03T03:39:44.000Z",
            "id": "683492913888768000",
            "lang": "en",
            "text": "Sometimes we end up in places we don't expect for reasons that aren't clear.   Tonight was one of those."
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-01T16:04:23.000Z",
            "id": "682955538561372164",
            "lang": "en",
            "text": "Station 84 run after shift from hell....... I feel better now.  Just finished a 6.32mi run with #EaseInto5K https://t.co/I3JRbxn63V"
        }
    ],
    "meta": {
        "newest_id": "683492913888768000",
        "oldest_id": "682955538561372164",
        "result_count": 2
    }
}
~~~

### main_act_months(self, brand_list, drug_name, start_year, end_year)
#### input_values
brand_list : (list) Keywords ex) ['Baclofen', 'Baclospas', 'Balgifen']   
drug_name : (str) output naming ex) Baclofen   
start_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2016-01-01T00:00:00Z"   
end_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2017-01-01T00:00:00Z"   

#### outputs (saved as .txt)
