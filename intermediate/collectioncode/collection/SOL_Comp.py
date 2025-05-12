#Then I will find the bad ones and label them on the list and then I will train the model on that
#and label the -1 

import requests
import json
import pandas as pd
import numpy as np
import io
import time
import os

def json_make():

    #Dont use, coordinates incorrect

    # solar_farms2 = {
    # "2W Permian Solar Project Hybrid": {"State": "Texas", "Coordinates": "31.243,-103.616", "Installed capacity (MW)": 420},
    # "Prospero Solar 1": {"State": "Texas", "Coordinates": "34.523,-101.216", "Installed capacity (MW)": 300},
    # "Titan (Texas) Solar Project": {"State": "Texas", "Coordinates": "30.680,-100.220", "Installed capacity (MW)": 260},
    # "Greasewood solar farm": {"State": "Arizona", "Coordinates": "32.491,-112.052", "Installed capacity (MW)": 255},
    # "Taygete Energy Project solar farm": {"State": "Texas", "Coordinates": "31.343,-101.437", "Installed capacity (MW)": 255},
    # "Av Solar Ranch One solar farm": {"State": "Colorado", "Coordinates": "37.213,-103.991", "Installed capacity (MW)": 253},
    # "Mount solar farm (United States)": {"State": "Utah", "Coordinates": "38.435,-112.704", "Installed capacity (MW)": 252},
    # "Copper Mountain Solar 5": {"State": "Nevada", "Coordinates": "35.840,-115.496", "Installed capacity (MW)": 252},
    # "Galloway 1 solar farm": {"State": "California", "Coordinates": "34.838,-118.227", "Installed capacity (MW)": 250},
    # "Moapa Southern Paiute solar farm": {"State": "Nevada", "Coordinates": "36.650,-114.773", "Installed capacity (MW)": 250},
    # "Phoebe Solar": {"State": "Texas", "Coordinates": "32.041,-102.225", "Installed capacity (MW)": 250},
    # "Westland solar farm Aquamarine": {"State": "California", "Coordinates": "36.257,-119.558", "Installed capacity (MW)": 250},
    # "Bighorn Solar 1": {"State": "California", "Coordinates": "35.029,-118.188", "Installed capacity (MW)": 240},
    # "Misae Solar 1": {"State": "Texas", "Coordinates": "32.222,-102.219", "Installed capacity (MW)": 240},
    # "Pleinmont Solar 2": {"State": "Indiana", "Coordinates": "39.666,-87.038", "Installed capacity (MW)": 240},
    # "Muscle Shoals solar farm": {"State": "Alabama", "Coordinates": "34.755,-87.618", "Installed capacity (MW)": 227},
    # "Azure Sky Solar": {"State": "Texas", "Coordinates": "29.858,-103.942", "Installed capacity (MW)": 225},
    # "Long Draw Solar": {"State": "Texas", "Coordinates": "29.858,-103.942", "Installed capacity (MW)": 225},
    # "Maplewood (Canadian Solar) solar farm 1": {"State": "Texas", "Coordinates": "28.508,-98.177", "Installed capacity (MW)": 222},
    # "Cool Springs Solar": {"State": "North Carolina", "Coordinates": "35.690,-79.652", "Installed capacity (MW)": 213},
    # "Tranquillity solar farm": {"State": "California", "Coordinates": "36.562,-120.197", "Installed capacity (MW)": 205},
    # "Twiggs Solar": {"State": "Georgia", "Coordinates": "32.753,-83.529", "Installed capacity (MW)": 204},
    # "ANSON Solar Center": {"State": "Texas", "Coordinates": "32.747,-99.850", "Installed capacity (MW)": 200},
    # "Athos solar farm 2": {"State": "Texas", "Coordinates": "30.806,-100.575", "Installed capacity (MW)": 200},
    # "Corazon Energy solar farm": {"State": "Texas", "Coordinates": "29.373,-101.387", "Installed capacity (MW)": 200},
    # "Dodge Flat solar farm": {"State": "Colorado", "Coordinates": "37.288,-105.671", "Installed capacity (MW)": 200},
    # "Hillcrest Solar": {"State": "Texas", "Coordinates": "31.573,-96.648", "Installed capacity (MW)": 200},
    # "Holstein 1 (Duke) solar farm": {"State": "Texas", "Coordinates": "34.939,-102.387", "Installed capacity (MW)": 200},
    # "Prairie Wolf Solar": {"State": "Illinois", "Coordinates": "39.990,-89.217", "Installed capacity (MW)": 200},
    # "Rambler solar farm": {"State": "Texas", "Coordinates": "31.650,-96.623", "Installed capacity (MW)": 200},
    # "Riverstart Solar Park": {"State": "Texas", "Coordinates": "28.862,-99.860", "Installed capacity (MW)": 200},
    # "Roadrunner (Enel) solar farm 1": {"State": "Texas", "Coordinates": "31.325,-102.631", "Installed capacity (MW)": 200},
    # "Sand Fork Solar": {"State": "Texas", "Coordinates": "31.903,-99.563", "Installed capacity (MW)": 200},
    # "Techren Solar 2": {"State": "Nevada", "Coordinates": "36.802,-115.600", "Installed capacity (MW)": 200},
    # "Wright Solar Park": {"State": "Texas", "Coordinates": "30.921,-99.244", "Installed capacity (MW)": 200},
    # "Impact Solar 1": {"State": "Texas", "Coordinates": "32.848,-101.891", "Installed capacity (MW)": 198},
    # "Golden Field Solar 3": {"State": "California", "Coordinates": "36.336,-119.205", "Installed capacity (MW)": 192},
    # "Garland solar farm 2": {"State": "Texas", "Coordinates": "33.009,-97.347", "Installed capacity (MW)": 185},
    # "Midway (174 Power Global) solar farm": {"State": "Georgia", "Coordinates": "32.547,-83.844", "Installed capacity (MW)": 182},
    # "Lily Solar Hybrid": {"State": "Texas", "Coordinates": "30.811,-100.238", "Installed capacity (MW)": 181},
    # "Aragorn Solar Project": {"State": "Texas", "Coordinates": "29.770,-99.902", "Installed capacity (MW)": 180},
    # "Castle Gap Solar Hybrid": {"State": "Texas", "Coordinates": "31.750,-101.450", "Installed capacity (MW)": 180},
    # "Townsite Solar Project Hybrid": {"State": "Texas", "Coordinates": "32.352,-100.963", "Installed capacity (MW)": 180},
    # "Camilla Solar Energy Project": {"State": "Georgia", "Coordinates": "31.201,-84.209", "Installed capacity (MW)": 171},
    # "Mesquite Solar 1": {"State": "Arizona", "Coordinates": "33.160,-112.605", "Installed capacity (MW)": 170},
    # "Highlander Solar Energy Station 1": {"State": "California", "Coordinates": "34.503,-118.917", "Installed capacity (MW)": 165},
    # "Rancho Seco Solar II": {"State": "California", "Coordinates": "38.330,-121.288", "Installed capacity (MW)": 160},
    # "Roserock solar farm": {"State": "Texas", "Coordinates": "32.313,-97.459", "Installed capacity (MW)": 160},
    # "Sun Streams solar farm": {"State": "Arizona", "Coordinates": "34.451,-112.720", "Installed capacity (MW)": 160},
    # "Juno Solar Project 1": {"State": "Texas", "Coordinates": "29.665,-95.482", "Installed capacity (MW)": 159},
    # "Springbok solar farm 2": {"State": "California", "Coordinates": "35.267,-118.274", "Installed capacity (MW)": 155},
    # "Buckthorn Westex solar farm": {"State": "Texas", "Coordinates": "30.344,-102.014", "Installed capacity (MW)": 154},
    # "North Rosamond Solar": {"State": "California", "Coordinates": "34.890,-118.217", "Installed capacity (MW)": 151},
    # "Topaz solar farm 2": {"State": "California", "Coordinates": "35.281,-120.179", "Installed capacity (MW)": 151},
    # "Badger Hollow solar farm 1": {"State": "Wisconsin", "Coordinates": "42.558,-89.891", "Installed capacity (MW)": 150},
    # "CA Flats Solar 2": {"State": "California", "Coordinates": "35.166,-120.675", "Installed capacity (MW)": 150},
    # "Crane Solar": {"State": "Texas", "Coordinates": "31.441,-102.340", "Installed capacity (MW)": 150},
    # "Elora Solar": {"State": "Tennessee", "Coordinates": "35.360,-86.722", "Installed capacity (MW)": 150},
    # "Fort Powhatan solar farm": {"State": "Virginia", "Coordinates": "37.265,-77.155", "Installed capacity (MW)": 150},
    # "Hardin Solar Energy 1": {"State": "Ohio", "Coordinates": "40.649,-84.163", "Installed capacity (MW)": 150},
    # "Mesquite Solar 3": {"State": "Arizona", "Coordinates": "33.160,-112.605", "Installed capacity (MW)": 150},
    # "Oberon (174 Power) solar farm 1": {"State": "Texas", "Coordinates": "30.620,-95.543", "Installed capacity (MW)": 150},
    # "Quitman Solar 1": {"State": "Texas", "Coordinates": "32.498,-95.396", "Installed capacity (MW)": 150},
    # "Sun Streams 2 solar farm": {"State": "Arizona", "Coordinates": "34.451,-112.720", "Installed capacity (MW)": 150},
    # "Two Creeks Solar": {"State": "Wisconsin", "Coordinates": "44.159,-87.361", "Installed capacity (MW)": 150},
    # "Upton County Solar": {"State": "Texas", "Coordinates": "31.117,-102.816", "Installed capacity (MW)": 150},
    # "Tenaska Imperial Solar Energy Center West": {"State": "California", "Coordinates": "32.744,-115.769", "Installed capacity (MW)": 149},
    # "Taylor County Solar": {"State": "Georgia", "Coordinates": "32.426,-84.255", "Installed capacity (MW)": 148},
    # "Campo Verde Solar": {"State": "California", "Coordinates": "35.564,-120.647", "Installed capacity (MW)": 147},
    # "East Blackland Solar Project 1": {"State": "Texas", "Coordinates": "31.380,-97.171", "Installed capacity (MW)": 144},
    # "Colonial Trail West solar farm": {"State": "Virginia", "Coordinates": "37.389,-76.924", "Installed capacity (MW)": 142},
    # "Edwards Sanborn solar farm 1B": {"State": "California", "Coordinates": "35.522,-118.835", "Installed capacity (MW)": 141},
    # "Juno Solar Project 2": {"State": "Texas", "Coordinates": "29.665,-95.482", "Installed capacity (MW)": 141},
    # "Maverick Solar 7": {"State": "Texas", "Coordinates": "27.799,-97.432", "Installed capacity (MW)": 132},
    # "CA Flats Solar 1": {"State": "California", "Coordinates": "35.169,-120.677", "Installed capacity (MW)": 130},
    # "Ivanpah Solar Electric Generating System 2": {"State": "California", "Coordinates": "35.557,-115.473", "Installed capacity (MW)": 130},
    # "Ivanpah Solar Electric Generating System 3": {"State": "California", "Coordinates": "35.557,-115.473", "Installed capacity (MW)": 130},
    # "Wilmot Energy Center solar farm": {"State": "Texas", "Coordinates": "30.976,-97.622", "Installed capacity (MW)": 130},
    # "Tenaska Imperial Solar Energy Center South": {"State": "California", "Coordinates": "32.744,-115.769", "Installed capacity (MW)": 129},
    # "American Kings Solar": {"State": "California", "Coordinates": "34.344,-117.404", "Installed capacity (MW)": 128},
    # "Big Beau Solar": {"State": "Texas", "Coordinates": "30.691,-96.823", "Installed capacity (MW)": 128},
    # "Robins Air Force Base Solar": {"State": "Georgia", "Coordinates": "32.621,-83.576", "Installed capacity (MW)": 128},
    # "Briar Creek Solar": {"State": "North Carolina", "Coordinates": "35.263,-79.617", "Installed capacity (MW)": 127},
    # "Genesis Solar Enegy Project 1": {"State": "California", "Coordinates": "34.021,-114.684", "Installed capacity (MW)": 125},
    # "Genesis Solar Enegy Project 2": {"State": "California", "Coordinates": "34.021,-114.684", "Installed capacity (MW)": 125},
    # "Solana Solar Generating Station 1": {"State": "Arizona", "Coordinates": "32.856,-112.781", "Installed capacity (MW)": 125},
    # "Solana Solar Generating Station 2": {"State": "Arizona", "Coordinates": "32.856,-112.781", "Installed capacity (MW)": 125},
    # "Coniglio Solar": {"State": "California", "Coordinates": "33.616,-116.336", "Installed capacity (MW)": 124},
    # "Indian Mesa Solar 1": {"State": "Texas", "Coordinates": "32.062,-101.300", "Installed capacity (MW)": 124},
    # "Milford Solar 1": {"State": "Utah", "Coordinates": "38.431,-113.198", "Installed capacity (MW)": 124},
    # "Redwood Solar": {"State": "Georgia", "Coordinates": "31.448,-83.508", "Installed capacity (MW)": 124},
    # "Royal Solar": {"State": "California", "Coordinates": "34.763,-118.844", "Installed capacity (MW)": 124},
    # "Tepco West Valley Solar": {"State": "Utah", "Coordinates": "40.400,-113.572", "Installed capacity (MW)": 124},
    # "Mesquite Solar 2": {"State": "Arizona", "Coordinates": "33.160,-112.605", "Installed capacity (MW)": 121},
    # "Montesol solar farm": {"State": "Texas", "Coordinates": "30.309,-97.336", "Installed capacity (MW)": 120},
    # "Plum Solar Energy Station": {"State": "Texas", "Coordinates": "28.911,-99.121", "Installed capacity (MW)": 120},
    # "Tepco West Valley Solar 1": {"State": "Utah", "Coordinates": "40.400,-113.572", "Installed capacity (MW)": 120},
    # "Tepco West Valley Solar 2": {"State": "Utah", "Coordinates": "40.400,-113.572", "Installed capacity (MW)": 120},
    # "Texas A&M Central Solar Plant": {"State": "Texas", "Coordinates": "30.608,-96.340", "Installed capacity (MW)": 120},
    # "Mount Signal Solar": {"State": "California", "Coordinates": "32.713,-115.481", "Installed capacity (MW)": 118},
    # "Briar Creek Solar 1": {"State": "North Carolina", "Coordinates": "35.263,-79.617", "Installed capacity (MW)": 116},
    # "Briar Creek Solar 2": {"State": "North Carolina", "Coordinates": "35.263,-79.617", "Installed capacity (MW)": 116},
    # "Green Power Solar": {"State": "Georgia", "Coordinates": "33.095,-83.658", "Installed capacity (MW)": 116},
    # "Rattlesnake Springs Solar": {"State": "Texas", "Coordinates": "30.999,-103.766", "Installed capacity (MW)": 116},
    # "South Santa Teresa Solar": {"State": "New Mexico", "Coordinates": "31.846,-106.689", "Installed capacity (MW)": 116},
    # "Arlington Valley Solar": {"State": "Arizona", "Coordinates": "32.721,-113.594", "Installed capacity (MW)": 112},
    # "Buckthorn solar farm": {"State": "Texas", "Coordinates": "30.229,-102.433", "Installed capacity (MW)": 110},
    # "Cienega Solar": {"State": "California", "Coordinates": "33.361,-116.859", "Installed capacity (MW)": 110},
    # "Duke Progress Columbus County solar farm": {"State": "North Carolina", "Coordinates": "34.172,-78.984", "Installed capacity (MW)": 110},
    # "Newberry solar farm": {"State": "South Carolina", "Coordinates": "34.306,-81.616", "Installed capacity (MW)": 110},
    # "Royal Solar 2": {"State": "California", "Coordinates": "34.763,-118.844", "Installed capacity (MW)": 110},
    # "South Santa Teresa Solar 3": {"State": "New Mexico", "Coordinates": "31.846,-106.689", "Installed capacity (MW)": 110},
    # "Seville solar farm": {"State": "California", "Coordinates": "33.803,-115.735", "Installed capacity (MW)": 109},
    # "Duke Notrees solar farm 2": {"State": "Texas", "Coordinates": "31.913,-102.866", "Installed capacity (MW)": 108},
    # "Grimmway Farms solar farm": {"State": "California", "Coordinates": "35.342,-119.207", "Installed capacity (MW)": 108},
    # "Ivanpah Solar Electric Generating System 1": {"State": "California", "Coordinates": "35.557,-115.473", "Installed capacity (MW)": 107},
    # "Hargray Leefield Solar": {"State": "Georgia", "Coordinates": "31.634,-82.135", "Installed capacity (MW)": 106},
    # "Spartan solar farm": {"State": "North Carolina", "Coordinates": "35.891,-80.003", "Installed capacity (MW)": 106},
    # "Wheeler Energy solar farm": {"State": "Georgia", "Coordinates": "31.185,-83.548", "Installed capacity (MW)": 106},
    # }

    def remove_duplicate_solar_farms(solar_farms):
        unique_solar_farms = {}
        
        for name, details in solar_farms.items():
            name_without_number = " ".join(name.split()[:-1])
            if name_without_number not in unique_solar_farms:
                unique_solar_farms[name_without_number] = details
                
        return unique_solar_farms



    
with open("sol_list new.json") as w:
    data = json.load(w)

print(len(data))

def data_collect():
    def make_wkt(lat_lon_string):
        lat, lon = lat_lon_string.split(',')
        wkt = f'POINT({lon.strip()} {lat.strip()})'
        return wkt
        
    pramaters={
        "api_key":"LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",
        "email":"phoenixducky@gmail.com",
        "names":"tmy-2022"
    }
    count=0
    for solar_farm_name, solar_farm_data in data.items():
        state = solar_farm_data["State"]
        coordinates = solar_farm_data["Coordinates"]
        capacity = solar_farm_data["Installed capacity (MW)"]

        r=requests.get(f"http://developer.nrel.gov/api/nsrdb/v2/solar/psm3-2-2-tmy-download.csv?wkt={make_wkt(coordinates)}",params=pramaters)
        df=pd.read_csv(io.StringIO(r.content.decode('utf-8')))
        df.at[0,"State"]=state
        df.at[0,"City"]=solar_farm_name
        df.at[0,"Country"]="USA"
        dir_path=f"/Users/phoenixsheppard/Desktop/Solar_Labels/" 
        file_path=f"{dir_path}/{count}.csv" 
        df.to_csv(file_path,index=False)
        count+=1
        time.sleep(2)
        print("D0ne")


    
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
    print(len(data))
    while(count<len(data)):
        dir_str=f'/Users/phoenixsheppard/Desktop/Solar_Labels/{count}.csv'
        df=pd.read_csv(dir_str)
        for i in range(len(val_list)):
            frame_dic[key_list[i]]=pd.concat([frame_dic[key_list[i]],df[val_list[i]][2:]])
        
        count=count+1
        print(count)
                
       

    frame=pd.DataFrame(frame_dic)
    frame.to_csv("Solar_noloc.csv",index=False)


def take_average():


    def list_make():
        state_arr=[]
        name_arr=[]
        for solar_farm_name, solar_farm_data in data.items():
            state = solar_farm_data["State"]
            coordinates = solar_farm_data["Coordinates"]
            capacity = solar_farm_data["Installed capacity (MW)"]
            state_arr.append(state)
            name_arr.append(solar_farm_name)
        return [state_arr,name_arr]



    states=list_make()[0]
    name=list_make()[1] 

    AVG_dic = {
        "Temperature": None,
        "Dew_Point": None,
        "GHI": None,
        "Pressure":None,
        "Wind_Speed": None
    }

    key_list=list(AVG_dic.keys())
    print(key_list)

    df = pd.read_csv('Solar_noloc.csv')
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
    avg_frame.insert(0, 'Name', name)
    avg_frame.insert(0, 'State', states)
    avg_frame.to_csv("SOL_AVG new.csv",index=False)


# data_collect()
compile()
take_average()

#you have done it for suitable wind locations, and I think now you need to do it for non suitable wind locations 
# look into the documentation of supervised leaening to find out
    


