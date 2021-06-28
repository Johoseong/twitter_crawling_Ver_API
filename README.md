# twitter_crawling_Ver_API

## API Usage
### main_act_id(self, author_id_info, start_time, end_time)
#### input_values
author_id_info : (str) author's id ex) "1061602142"   
start_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2016-01-01T00:00:00Z"   
end_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2017-01-01T00:00:00Z"   

#### outputs (saved as .txt)

~~~
{
    "data": [
        {
            "author_id": "1061602142",
            "created_at": "2016-01-30T12:42:03.000Z",
            "id": "693413865405681664",
            "lang": "en",
            "text": "Countdown to C2 is in the final days."
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-30T00:25:41.000Z",
            "id": "693228552871878656",
            "lang": "en",
            "text": "Chris jogs Salisbury https://t.co/YTSneqmV9N"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-29T18:11:35.000Z",
            "id": "693134409948647424",
            "lang": "en",
            "text": "What's not to like about a day like this. #sunshine https://t.co/nK2905EVMQ"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-28T16:00:42.000Z",
            "id": "692739082498281472",
            "lang": "en",
            "text": "Salisbury city run...Cool and cloudy, but it clears my head for the day Just finished a 4.31mi run with #EaseInto5K https://t.co/S3N6Es60WB"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T16:10:38.000Z",
            "id": "691654419742658560",
            "lang": "en",
            "text": "What if addiction isn't a spiritual or moral calamity to be overcome....but a chronic illness we don't understand. #baclofen_study #RadioLab"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T15:44:05.000Z",
            "id": "691647738807742466",
            "lang": "en",
            "text": "Enjoy every one..... Tomorrow's is not guaranteed.  #beautiful_day https://t.co/NDPSTK02n4"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T04:05:38.000Z",
            "id": "691471964997816320",
            "lang": "en",
            "text": "RT @DavidWhisenant: A police officer performs a selfless act of mercy and reminds everyone to check on shut ins. https://t.co/bfQIek107Q #g\u2026"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T04:05:28.000Z",
            "id": "691471926657728512",
            "lang": "en",
            "text": "RT @DavidWhisenant: Firefighters, EMS on scene of house fire, 613 Gold Hill Drive in Salisbury.  Pic from Rowan EMS"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T04:04:51.000Z",
            "id": "691471771623624705",
            "lang": "en",
            "text": "RT @DavidWhisenant: Woman burned Sunday in house fire is same woman cared for by police Lt, on Saturday. https://t.co/Cdfhwaq9pP"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T03:25:00.000Z",
            "id": "691461740811403265",
            "lang": "en",
            "text": "RT @DavidWhisenant: Woman burned, taken to hospital after fire on Gold Hill Dr in Salisbury. https://t.co/3uqCHN2BF2"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-22T15:51:02.000Z",
            "id": "690562322755117056",
            "lang": "in",
            "text": "@cnrichardson. Survival kit. #RowanJonas https://t.co/fj0M2iPk39"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-22T15:14:44.000Z",
            "id": "690553185895878656",
            "lang": "en",
            "text": "@cnrichardson exactly..... I too  wander the frozen tundra, all the while wondering did I not Espresso my wishes a Latte to these people."
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-19T17:59:47.000Z",
            "id": "689507558449639424",
            "lang": "en",
            "text": "Be the best version of you.... This has been in my wallet for the last 30 years.... It works. https://t.co/CXnbR2Rct9"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-17T01:25:10.000Z",
            "id": "688532482237566976",
            "lang": "en",
            "text": "RT @EMS12Lead: Should have gone to cath lab anyway but modified Sgarbossa removes all doubt @SmithECGBlog #FOAMed #MedEd #USMLE... https://\u2026"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-16T16:18:30.000Z",
            "id": "688394906860130304",
            "lang": "en",
            "text": "Station 85 loop around the hospital. Now off to get Stella for the day.  Just finished a 4.40mi run with #EaseInto5K https://t.co/4f9827fXRO"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-14T21:02:57.000Z",
            "id": "687741717827698689",
            "lang": "en",
            "text": "Stella Starbucks and Papa Starbucks @ Harris Teeter https://t.co/Df2tu0R6dE"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-13T19:21:40.000Z",
            "id": "687353841965264896",
            "lang": "en",
            "text": "Station,87 to Station 85 and back.  Crisp and cool day Just finished a 7.19mi run with #EaseInto5K https://t.co/63fDwWtJQ8"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-09T19:13:55.000Z",
            "id": "685902338427584514",
            "lang": "en",
            "text": "..... It's not just for burns anymore?\nhttps://t.co/AWttPGmHST"
        },
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
        "newest_id": "693413865405681664",
        "oldest_id": "682955538561372164",
        "result_count": 20
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
