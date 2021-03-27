import requests
import time
import json
import ast
import datetime
from shapely.geometry import Polygon
from Planet_py import *

ajax_url = "URL_TO_YOUR_DEPLOY_OF_WEBMAP_APPS/ajax.php"
planet_key = "YOUR_PLANET_KEY"
# go get last date from db
r = requests.post(ajax_url, data={'service': 'getLatestPlanet'})
print(r.status_code, r.reason)
print(r.text + '...')
robject = ast.literal_eval(r.text)
# Last date from db
latestdate = robject[0][0]

# add a day and go check planet from date to today
date_obj = datetime.datetime.strptime(latestdate, '%Y-%m-%d').date() + datetime.timedelta(1)

past = date_obj
present = datetime.datetime.now()
if past < present.date():
    print(str(past))
    while past < present.date():
        print("In time loop")
        print(past)
        api_key = planet_key
        layer_count = 2  # Include the n best layers
        start = str(past)
        end = str(past)  # None #'2019-01-30'  # Exclusive
        item_types = ['PSScene3Band', 'PSScene4Band']
        geometry = Polygon([[-91.2971270940011, 14.738967391807186],
          [-91.2971270940011, 14.608774531644963],
          [-91.1048663518136, 14.608774531644963],
          [-91.1048663518136, 14.738967391807186]])
        buffer = 0.5
        addsimilar = False
        myList = getMapID(api_key, geometry, start, end, layer_count, item_types, buffer, addsimilar)
        # here is where i would get info to add to db
        if len(myList) > 0 :
            theimage = myList[0]
            print(str(theimage))
            print(theimage["date"] +", " + theimage["LayerID"])

            # updatePlanetData
            idate = "'" + theimage["date"] + "'"
            url = "'" + theimage["url"][0] + "'"
            layerID = "'" + theimage["LayerID"] + "'"
            r2 = requests.post(ajax_url,
                              data={'service': 'updatePlanetData', 'date': idate, 'url': url, 'layerID': layerID})
            print(r2.status_code, r.reason)
            print(r2.text + '...')
            # updatePlanetData call sending theimage["date"] +", " + theimage["LayerID"]
        #add a day to past
        past = past + datetime.timedelta(1)
        time.sleep(1)
else:
    print("after today")

time.sleep(5)