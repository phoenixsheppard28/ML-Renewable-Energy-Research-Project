import requests
import json
import pandas as pd
import numpy as np
import io
import time
import os
with open("city_coords.json") as w:
    coordinates = json.load(w)


# directory = '/Users/phoenixsheppard/Desktop/PSM_Data/New York/New York_0.csv'

# df=pd.read_csv(directory)

# print(df.head())
# frame_dic={
#     "Temperature":df['Latitude'][2:],
#     "Dew_Point":df['Clearsky DHI Units'][2:],
#     "GHI":df['DHI Units'][2:],
#     "Relative_Humidity":df['DNI Units'][2:],
#     "Solar_Zenith":df['GHI Units'][2:],
#     "Surface_Albedo":df["Solar Zenith Angle Units"][2:],
#     "Pressure":df["Temperature Units"][2:],
#     "Precipitable_Water":df["Pressure Units"][2:],
#     "Wind_Speed":df["Precipitable Water Units"][2:],
# }
# test=pd.DataFrame(frame_dic)
# test.to_csv("test3.csv",index=None)


frame_dic = {
    "State":pd.Series(),
    "City":pd.Series(),
    "Month":pd.Series(),
    "Day":pd.Series(),
    "Hour":pd.Series(),
    "Temperature": pd.Series(),
    "Dew_Point": pd.Series(),
    "GHI": pd.Series(),
    "Relative_Humidity": pd.Series(),
    "Solar_Zenith": pd.Series(),
    "Surface_Albedo": pd.Series(),
    "Pressure": pd.Series(),
    "Precipitable_Water": pd.Series(),
    "Wind_Speed": pd.Series()
}

key_list=list(frame_dic.keys())[2:]
print(key_list)
val_list=["Location ID","City","State","Latitude",'Clearsky DHI Units','DHI Units','DNI Units','GHI Units','Solar Zenith Angle Units','Temperature Units','Pressure Units','Precipitable Water Units']
count=0
temp_state=[]
temp_city=[]
for state,city in coordinates.items():
    for key in city:
        if(state!="Alaska"):
            
            dir_str=f'/Users/phoenixsheppard/Desktop/PSM_Data/{state}/{state}_{count}.csv'
            df=pd.read_csv(dir_str)
            for i in range(len(val_list)):
                frame_dic[key_list[i]]=pd.concat([frame_dic[key_list[i]],df[val_list[i]][2:]])
            

            s_df=pd.Series([df["State"][1]]*8760)
            c_df=pd.Series([df["City"][1]]*8760)

            s_df = s_df.reset_index(drop=True)
            c_df = c_df.reset_index(drop=True)

            frame_dic["State"]=pd.concat([frame_dic["State"],s_df])
            frame_dic["City"]=pd.concat([frame_dic["City"],c_df])

            count=count+1
            print(state)
            
    count=0

frame=pd.DataFrame(frame_dic)
frame.to_csv("Time_SeriesData.csv",index=False)



