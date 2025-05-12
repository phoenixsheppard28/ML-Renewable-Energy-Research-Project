import requests 
import pandas as pd
import numpy as np
import matplotlib as plt
import json
from shapely import Point,Polygon
import time
import asyncio




with open("coordinates.json") as w:
    coordinates = json.load(w)

# def analyze():
#     if(data["cod"]!=200):
#         coordinates.pop(j)
#         j=j-1 #loop control 
#     else:
#         avg=0
        
#         avg=avg+data["result"]["wind"]["mean"]
        
#         wind_arr=np.append(wind_arr,avg)

#         avg=0
        
#         avg=avg+data["result"]["temp"]["mean"]
        
#         temp_arr=np.append(temp_arr,avg)

#         avg=0
        
#         avg=avg+data["result"]["pressure"]["mean"]
        
#         pressure_arr=np.append(pressure_arr,avg)

#         avg=0
        
#         avg=avg+data["result"]["humidity"]["mean"]
        
#         humid_arr=np.append(humid_arr,avg)
#         avg=data["result"]['clouds']["mean"]
#         cloud_arr=np.append(cloud_arr,avg)
#     j=j+1 #loop control
#     print(j)
        
# def collect():
#     global_dic={
#     "wind":wind_arr,
#     "temp":temp_arr,
#     "pressure":pressure_arr,
#     "humidity":humid_arr,
#     "clouds":cloud_arr
#     }

#     frame=pd.DataFrame(global_dic)
#     #csv test
#     frame.to_csv("test.csv")
#     print("done")




# async def request_data(params):
#     r=requests.get("https://history.openweathermap.org/data/2.5/aggregated/month",params=params)
#     data=r.json()
#     analyze()


# async def main():
#     j=0
#     while (j<10):
#         params={
#         "lat":coordinates[j]["lat"],
#         "lon": coordinates[j]["lon"],
#         "appid":"63d4e22f908754a94a8255c5107a2bfd",
#         "month":7

#     }

#         print("starting task", j)
#         await asyncio.create_task(request_data(params))
        
         
#         print("ending task", j)


# asyncio.run(main())
# collect()


wind_arr=np.array([])
temp_arr=np.array([])
pressure_arr=np.array([])
humid_arr=np.array([])
cloud_arr=np.array([])
precip_arr=np.array([])
lat_arr=np.array([])
lon_arr=np.array([])
sun_arr=np.array([])

j=0 #loop control
while(j<30000): #first 20000 of list IS DONE GO NEXT 
    paramaters={
        "lat":coordinates[j]["lat"],
        "lon": coordinates[j]["lon"],
        "appid":"63d4e22f908754a94a8255c5107a2bfd",
        "month":4

    }

    r=requests.get("https://history.openweathermap.org/data/2.5/aggregated/month",params=paramaters)

    data=r.json()
    
    # dictionary=json.dumps(data,indent=4)

    # with open("wind.json", "w") as outfile:
    #     outfile.write(dictionary)

    

    if(data["cod"]!=200):
        coordinates.pop(j)
        j=j-1 #loop control 
    else:
       
        
        wind_arr=np.append(wind_arr,data["result"]["wind"]["mean"])

        
        
        temp_arr=np.append(temp_arr,data["result"]["temp"]["mean"])

       
        
        pressure_arr=np.append(pressure_arr,data["result"]["pressure"]["mean"])

        
        
        humid_arr=np.append(humid_arr,data["result"]["humidity"]["mean"])

        
        cloud_arr=np.append(cloud_arr,data["result"]['clouds']["mean"])

        lat_arr=np.append(lat_arr,paramaters["lat"])
        lon_arr=np.append(lon_arr,paramaters["lon"])

        precip_arr=np.append(precip_arr,data["result"]["precipitation"]["mean"])
        sun_arr=np.append(sun_arr,data["result"]["sunshine_hours"])
    j=j+1 #loop control
    print(j)
        



global_dic={
    "wind":wind_arr,
    "temp":temp_arr,
    "pressure":pressure_arr,
    "humidity":humid_arr,
    "clouds":cloud_arr,
    "lat":lat_arr,
    "lon":lon_arr,
    "precipitation":precip_arr,
    "sunshine_hours":sun_arr
}

frame=pd.DataFrame(global_dic)

#csv test
frame.to_csv("wind2.csv")
print("done")

    



'''
def wkt_make(latitude, longitude):
    # Create a Point object using the provided coordinates
    point = Point(longitude, latitude)
    
    # Return the WKT representation of the Point
    print(type(point.wkt))
    return point.wkt


name="2011"
l=((40.772573, -74.303403),(38.808278, -79.021588),(40.245253, -83.795425),(42.949745, -77.675121))
def create_polygon_wkt(coordinates):

    
    polygon = Polygon(coordinates)
    polygon_wkt = polygon.wkt
    return polygon_wkt

paramaters={
    "api_key":"LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",
    "wkt":create_polygon_wkt(l),
    "names":name,
    "email":"phoenixducky@gmail.com",
    "interval":60

}

r= requests.get("http://developer.nrel.gov/api/nsrdb/v2/solar/himawari7-download.json",params=paramaters)

print(r.status_code)
data=r.json()

dictionary=json.dumps(data,indent=4)

with open("wind.json", "w") as outfile:
    outfile.write(dictionary)

'''
  

