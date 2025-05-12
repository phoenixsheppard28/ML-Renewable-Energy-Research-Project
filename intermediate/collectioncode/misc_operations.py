import requests
import json
import pandas as pd
import numpy as np
import io
import time
import os


def add_constant_column(data_frame, column_name, constant_value=1):
    """
    Add a new column with a constant value to a DataFrame.
    
    Parameters:
    data_frame (pd.DataFrame): DataFrame to which the column will be added.
    column_name (str): Name of the new column.
    constant_value: Value to fill the new column with (default is 1).
    
    Returns:
    pd.DataFrame: DataFrame with the new column added.
    """
    new_column = pd.Series([constant_value] * len(data_frame), name=column_name)
    new_data_frame = pd.concat([data_frame, new_column], axis=1)
    return new_data_frame

# df=pd.read_csv("temp.csv")
# df=add_constant_column(df,"Suitability",1)
# df.to_csv("temp.csv",index=False)

add_constant_column(pd.read_csv("All_labels_Wind_Updated.csv"), "Suitability", 1).to_csv("All_labels_Wind.csv", index=False)


#need to make the 


