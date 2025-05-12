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

def compile():
    frame_dic = {
    "Month":pd.Series(),
    "Day":pd.Series(),
    "Hour":pd.Series(),
    "Temperature": pd.Series(),
    "Dew_Point": pd.Series(),
    "GHI": pd.Series(),
    "Pressure": pd.Series(),
    "Wind_Speed": pd.Series()
    }

    key_list=list(frame_dic.keys())
    print(key_list)
    val_list=["Location ID","City","State","DHI Units","Latitude","Elevation","Dew Point Units","GHI Units"]
    count=0
    temp_state=[]
    temp_city=[]
    for state,city in coordinates.items():
        for key in city:
            if(state!="Alaska" and state!="Hawaii"):
                
                dir_str=f'/Users/phoenixsheppard/Desktop/PSM_Data/{state}/{state}_{count}.csv'
                df=pd.read_csv(dir_str)
                for i in range(len(val_list)):
                    frame_dic[key_list[i]]=pd.concat([frame_dic[key_list[i]],df[val_list[i]][2:]])
                
                count=count+1
                print(state)
                
        count=0

    frame=pd.DataFrame(frame_dic)
    frame.to_csv("Time_noloc_Data.csv",index=False)

def list_make():
    state_arr=[]
    city_arr=[]
    for state,city in coordinates.items():
        if state != "Alaska" and state != "Hawaii":
            state_arr.append(state)
            for key in city:
                city_arr.append(key)
    return[state_arr,city_arr]

# def add_col():
#     states=list_make()[0]
#     cities=list_make()[1]

#     csv_file_path = 'Time_noloc_Data copy.csv'  # Replace with your CSV file path
#     df = pd.read_csv(csv_file_path)


#     # Initialize counters
#     state_counter = 0
#     city_counter = 0
#     city_row_counter = 0
#     state_row_counter = 0

#     # Add "State" and "City" columns to the DataFrame
#     state_column = []
#     city_column = []

#     for index, row in df.iterrows():
#         state_column.append(states[state_counter])
#         city_column.append(cities[city_counter])
        
        
#         city_row_counter += 1
#         state_row_counter += 1
        
#         if  city_row_counter >= 8760:
#             city_counter+=1
#             city_row_counter = 0
#             print("2")
            
#         if  state_row_counter >= 175200:
#             state_counter+=1
#             state_row_counter = 0
#             print("1")

#     df.insert(0, 'City', city_column)
#     df.insert(0, 'State', state_column)

#     # Save the updated DataFrame to a new CSV file
#     output_csv_file = 'output_dataframe.csv'
#     df.to_csv(output_csv_file, index=False)

#     print("DataFrame with 'State' and 'City' columns added and saved to", output_csv_file)

def take_average():
    states=list_make()[0]
    cities=list_make()[1] 
    
    
    state_column = []
    city_column = []

    for c in cities:
        city_column.append(c)
    
    for s in states:
        for i in range(20):
            state_column.append(s)
    print(len(state_column))


    AVG_dic = {
        "Temperature": None,
        "Dew_Point": None,
        "GHI": None,
        "Pressure":None,
        "Wind_Speed": None
    }

    key_list=list(AVG_dic.keys())
    print(key_list)

    df = pd.read_csv('Time_noloc_Data.csv')
    def calculate_grouped_mean(data_frame, column_name, group_size):
        # Calculate the group indices based on rows
        group_indices = np.arange(len(data_frame)) // group_size
        
        # Group the DataFrame by the calculated indices and calculate the mean for the specified column
        grouped_mean_series = data_frame[column_name].groupby(group_indices).mean()
        

        return grouped_mean_series  #return a dataframe with the mean values for the specified column

    for i in range (len(key_list)):
        AVG_dic[key_list[i]]= calculate_grouped_mean(df,[key_list[i]],8760)[key_list[i]] #must do key_list[i] because it is the column name and calculate grouped mean returns a dataframe

    print(
        AVG_dic["Temperature"]
    )
    avg_frame = pd.DataFrame(AVG_dic)
    avg_frame.insert(0, 'City', city_column)
    avg_frame.insert(0, 'State', state_column)
    avg_frame.to_csv("AVG_Data.csv",index=False)

   
    
def clean(path):
    df = pd.read_csv(path)
    selected_columns = ['State', 'City', 'GHI', 'Wind_Speed', 'Temperature']
    filtered_df = df[selected_columns]
    filtered_df.to_csv(f"Clean_{path}",index=False)


# clean("wind+all.csv")
    

take_average()


   
#makes average data 

