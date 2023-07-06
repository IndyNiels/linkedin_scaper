



request1 = 'https://www.linkedin.com/voyager/api/feed/updatesV2?commentsCount=0&count=7&likesCount=0&moduleKey=home-feed%3Adesktop&paginationToken=973335724-1688565151364-2606fe14606cf434b08a99c808ce7d51&q=feed&sortOrder=MEMBER_SETTING&start=3'
request2 = 'https://www.linkedin.com/voyager/api/feed/updatesV2?commentsCount=0&count=9&likesCount=0&moduleKey=home-feed%3Adesktop&paginationToken=973335724-1688565151364-2606fe14606cf434b08a99c808ce7d51&q=feed&sortOrder=MEMBER_SETTING&start=10'
request3 = 'https://www.linkedin.com/voyager/api/feed/updatesV2?commentsCount=0&count=9&likesCount=0&moduleKey=home-feed%3Adesktop&paginationToken=973335724-1688565151364-2606fe14606cf434b08a99c808ce7d51&q=feed&sortOrder=MEMBER_SETTING&start=19'




import requests

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           }

import requests
import json

url = 'https://www.linkedin.com/voyager/api/feed/updatesV2'
headers = {
    'authority': 'www.linkedin.com',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'accept-language': 'en',
    'cookie': 'bcookie="v=2&e1a89a6b-3670-40ae-8ced-56c35bbef200"; bscookie="v=1&202209131036254dd4b17b-2b8e-43df-81de-005290ec582aAQERws24qXQmIvT-QawX9IAxHH2cZXtA"; li_alerts=e30=; li_gc=MTsyMTsxNjgxMjA2NTU4OzI7MDIxGly+r8OTJf+lJgDaGqAl8bW15ZLRpy3hEof2NKY9YPA=; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; li_theme=light; li_theme_set=app; _gcl_au=1.1.358883084.1681206567; visit=v=1&M; li_sugr=30114eda-2a8b-4fab-b181-4a2d3d8be309; timezone=Europe/Madrid; aam_uuid=02586308763051135951387022025500205715; li_rm=AQFd-_l3-TrG6QAAAYiU8mJz69hbVUowU_v8KH61kEbbdbgsxDuwpWYlf_96R-nYsiKNJ1DVg89F07MtfZlp3biGh2z7IWlwcEmqdrC1r-ONlbJfF0qxXMMKMFabJiK5coZ-r27QsxfJnPMS1U3KiSFyQj_Stv7WovJp_CqTR45Uwt3Brff0jJz0z9RSVfBR-9enRuKDxdxnVL7nqn3VoA3PBxVt99HsbLPGWVy6VbOM8Ykn6pHJA1H7ulzvnf9m7FLq06VsnbQP67ITms7yd28GaXEOBXWKW3vNGewY-D2HjJCaQ9HawYXrS17VOdkMPelxahzBBM2ikW8g7wg; g_state={"i_l":2,"i_p":1686705007520}; liap=true; JSESSIONID="ajax:4821431053429746946"; AnalyticsSyncHistory=AQLhCnovqJjMUQAAAYkbOoWxIOnzOmORvbWBN2oDxlt3ybkM5NPRT5U5wTIiBOWnqSMoc9cmv9B4eRezA2W9Cw; lms_ads=AQFEOvJMmgpEtgAAAYkbOoaHfNE90vUVCag4u8meYB3v9RVbOLmQ86B22-2EtjOLrc5sfg68Ilz88Don6goIrDp-jptwMQ9r; lms_analytics=AQFEOvJMmgpEtgAAAYkbOoaHfNE90vUVCag4u8meYB3v9RVbOLmQ86B22-2EtjOLrc5sfg68Ilz88Don6goIrDp-jptwMQ9r; PLAY_LANG=en; lang=v=2&lang=en-US; _guid=eb7e23ea-b8e5-42ab-8a41-a5494c2d4d4c; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiIxM2E2MGY0YS01NzgwLTRmYjYtOWFhOC0zNzEyZWVkYjA0YjR8MTY4ODQ4NjMxMSIsImFsbG93bGlzdCI6Int9IiwicmVjZW50bHktc2VhcmNoZWQiOiIiLCJyZWZlcnJhbC11cmwiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImFpZCI6IiIsInJlY2VudGx5LXZpZXdlZCI6IjUxMjQyOXw1NjQxMzR8MTM0MTc3OCIsIkNQVC1pZCI6IsOmw4ozwpgpw7JPwprCkTlcdTAwMDNNbMOtecKhIiwiZXhwZXJpZW5jZSI6ImVudGl0eSIsInRyayI6IiJ9LCJuYmYiOjE2ODg0OTEyMTksImlhdCI6MTY4ODQ5MTIxOX0.Z7qqSIvBtCY42bAde4OW7GUHOE53ZQ3-LaWjaNXjolI; li_at=AQEDAToD7KwApGWPAAABiLJNzdoAAAGJSdI9QE0AmvAjCLYGAiMT6envqeJGngiOEq7IrlPBvt-q85WkvonzKCjNM7okV1OrxbNB2IYelMQ21nI9eRsxvQ0h240xuf6e59FTLY3IOnFjgWU4g-VjbTeZ; ln_or=eyI0MzQ2MTM3IjoiZCJ9; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19544%7CMCMID%7C02414971026700826081436822082509328728%7CMCAAMLH-1689168098%7C6%7CMCAAMB-1689168098%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1688570498s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C419703489; li_mc=MTsyMTsxNjg4NTY1MTI4OzI7MDIx1YMalpnv2Q0xsyvw5I0Z30/Bl1w0o0hhmC7LaUoY31k=; UserMatchHistory=AQIw1-l0KlWeFAAAAYkmU3tb1xTo-n8pb4uphSxakgPrta2PMDrALu9WkvR1Rio62ZPOw6A3uuYtoETin22Z2euhEyjxUoqy50j1sdGWocpgNz6-NtHkQJUYA5vKJRGx9uxPoIfkoaPRVIggcQBLsElfRcO-pKlVPHo6RxaMSHVt9z5EQZ7r9UmWdrmy3F4ZV8O0ZLjPEwiIUOJurDxFMkJTsUx--QmV8FA915WqSujBNOJ12og9vDMSqfHd0LdDBtRZb87I5Xex-iyRKZTpv58LT1ot6JILYV25B8qJxxyMiFfyb14d11_mesJ1Bx152w3eUMHOGmFgeAJstETUyMbjdl66G0w; lidc="b=VB24:s=V:r=V:a=V:p=V:g=5057:u=69:x=1:i=1688565153:t=1688576104:v=2:sig=AQGDDqmINSdsFCA1xJd5IVyDCprN4KxM"',
    'csrf-token': 'ajax:4821431053429746946',
    'dnt': '1',
    'referer': 'https://www.linkedin.com/feed/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-li-lang': 'en_US',
    'x-li-page-instance': 'urn:li:page:d_flagship3_feed;o9ozvuycQwyIgdtEi0le0w==',
    'x-li-pem-metadata': 'Voyager - Feed=subsequent-feed-updates',
    'x-li-track': '{"clientVersion":"1.12.8893","mpVersion":"1.12.8893","osName":"web","timezoneOffset":2,"timezone":"Europe/Madrid","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":2880,"displayHeight":1800}',
    'x-restli-protocol-version': '2.0.0'
}
params = {
    'commentsCount': '0',
    'count': '9',
    'likesCount': '0',
    'moduleKey': 'home-feed:desktop',
    'paginationToken': '973335724-1688565151364-2606fe14606cf434b08a99c808ce7d51',
    'q': 'feed',
    'sortOrder': 'MEMBER_SETTING',
    'start': '10'
}

response = requests.get(url, headers=headers, params=params)
print(response.json())  # Process the response as needed

## save response to json file

with open('response.json', 'w') as f:
    json.dump(response.json(), f)

