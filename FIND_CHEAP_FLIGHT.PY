import requests

url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"

idi = requests.get(url)
response = idi.json()
print (response)


#
# querystring = {
#     "market": "US",
#     "locale": "en-US",
#     "currency": "USD",
#     "QueryLegs": [
#         {
#             "originPlaceID": {
#                 "iata": "FAY"
#             },
#
#             "destinationPlaceId": {
#                 "iata": "EWR"
#             },
#
#             "date":{
#                 "year": "2025",
#                 "month": "01",
#                 "day": "20"
#             }
#         }
#
#     ],}
#
# get = requests.get(url, params=querystring)
# print (get.json())