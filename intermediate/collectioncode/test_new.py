
import Renewable_Suitability_Predictor as rsp
coordinates_array = [
    [40.7128, -74.0060],    # New York City, NY
    [34.0522, -118.2437],   # Los Angeles, CA
    [41.8781, -87.6298],    # Chicago, IL
    [29.7604, -95.3698],    # Houston, TX
    [33.4484, -112.0740],   # Phoenix, AZ
    [39.9526, -75.1652],    # Philadelphia, PA
    [29.4241, -98.4936],    # San Antonio, TX
    [32.7157, -117.1611],   # San Diego, CA
    [37.7749, -122.4194],   # San Francisco, CA
    [47.6062, -122.3321],   # Seattle, WA
    [30.2672, -97.7431],    # Austin, TX
    [25.7617, -80.1918],    # Miami, FL
    [40.7128, -74.0060],    # New York City, NY (duplicate for more testing)
    [34.0522, -118.2437],   # Los Angeles, CA (duplicate for more testing)
    [38.9072, -77.0369],    # Washington, D.C.
    [42.3601, -71.0589],    # Boston, MA
    [34.7465, -92.2896],    # Little Rock, AR
    [35.1495, -90.0490],    # Memphis, TN
    [39.7684, -86.1581],    # Indianapolis, IN
    [32.7767, -96.7970],  # Los Angeles, CA
     # Dallas, TX
    # Add more test coordinates as needed
]
model_type = "wind"  # or "wind"

print(rsp.interface_multi_prediction(coordinates_array=coordinates_array, model_type=model_type, api_key="LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",email="phoenixducky@gmail.com", random_state=152))  # Adjust random_state as needed


# print(interface_single_prediction(api_key="LR4nu6g5mUZgN5oJqPOKFRj31bQCoHYcxdNKG2UU",email="phoenixducky@gmail.com", random_state=42))  # Adjust random_state as needed

#todo:
# change the package to reflect tmy , then do that for new solar or wind datasets, 980 cities and 120 good installations, then do new graphs
# update github and slideshow

# need to change how it indexes 
#github first 

#collect new data first

