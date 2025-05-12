import requests 
import pandas as pd
import numpy as np
import matplotlib as plt
import json
import time
import asyncio
from shapely import Point 
from shapely.geometry import MultiPoint
from shapely import wkt


'''
response=requests.get("https://api.weather.gov/gridpoints/TOP/31,80/forecast")

data=response.json() #makes it a json not dict


print(response.status_code)

print(data["properties"]["periods"][0]["temperature"])#working 

test=pd.DataFrame(data["properties"]["periods"])  #csv test
print(test) 
test.to_csv("test.csv")
'''

with open("coordinates.json") as w:
    coordinates = json.load(w)

def wkt_make(latitude, longitude):
    # Create a Point object using the provided coordinates
    point = Point(longitude, latitude)
    
    # Return the WKT representation of the Point
    print(type(point.wkt))
    return point.wkt




paramaters={
    "api_key":"LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",
    "wkt":"",
    "names":2011,
    "email":"phoenixducky@gmail.com",
    "interval":60

}

r=requests.get("https://developer.nrel.gov/api/nsrdb/v2/solar/himawari7-download.json?",params=paramaters)
data=r.json()

dictionary=json.dumps(data,indent=4)

with open("solar.json", "w") as outfile:
    outfile.write(dictionary)



# async def request_data(params):
#     r = requests.get("https://developer.nrel.gov/api/solar/solar_resource/v1.json", params=params) 

# async def main():
#     for i in range(100):
#         params = {
#             "api_key": "LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",
#             "lat": coordinates[i]["lat"],   # this acecces the coordinates.json and takes the first dictionary and indexes it. In the real project 
#             "lon": coordinates[i]["lon"],   #you will replace 1 with i and loop through and somehow store the data in dataframe
#         }

#         print("starting task", i)
#         await asyncio.create_task(request_data(params))
#         print("ending task", i)


# asyncio.run(main())


# ghi_arr =np.array([])
# lat_arr =np.array([])
# lon_arr =np.array([])
# dni_arr =np.array([])
# tilt_arr=np.array([])

# i=0



# while i<len(coordinates): #will replace with len(coordinates)
#     params = {
#         "api_key": "LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",
#         "lat": coordinates[i]["lat"],   # this acecces the coordinates.json and takes the first dictionary and indexes it. In the real project 
#         "lon": coordinates[i]["lon"],   #you will replace 1 with i and loop through and somehow store the data in dataframe
#     }

#     r = requests.get("https://developer.nrel.gov/api/solar/solar_resource/v1.json", params=params) 
#     data = r.json()
#     print(r.status_code) 
#     # dictionary=json.dumps(data,indent=4)
    
    
    
#     if(data["outputs"]["avg_ghi"] == "no data"):
#         coordinates.pop(i)
#         i=i-1 #loop management
#     else:
#         ghi_arr=np.append(ghi_arr,data['outputs']["avg_ghi"]["annual"])  #works, now you must find a way to make it so that the array is mutable and i can expand it. Maybe series will work
#         lat_arr=np.append(lat_arr,data["inputs"]["lat"])
#         lon_arr=np.append(lon_arr,data["inputs"]["lon"])
#         dni_arr=np.append(dni_arr,data["outputs"]["avg_dni"]["annual"])
#         tilt_arr=np.append(tilt_arr,data["outputs"]["avg_lat_tilt"]["annual"])
#     i=i+1 #loop management
#     print(i)
    
# #print(ghi_arr,lat_arr,lon_arr,dni_arr,end="\n") #testing

# global_dic={
#     "ghi":ghi_arr,
#     "lat":lat_arr,
#     "lon":lon_arr,
#     "dni":dni_arr,
#     "tilt":tilt_arr
# }


# frame=pd.DataFrame(global_dic)
# #csv test
# frame.to_csv("solar.csv")




  




