

import random
import shapefile
import json

def load_contiguous_us_shapefile(shapefile_path):
    sf = shapefile.Reader(shapefile_path)
    return sf

def generate_contiguous_us_coordinates(shapefile_path, num_coordinates=100000):
    sf = load_contiguous_us_shapefile(shapefile_path)
    shapes = sf.shapes()

    coordinates_list = []
    while len(coordinates_list) < num_coordinates:
        # Generate random coordinates within the specified range
        latitude = random.uniform(24.396308, 49.384358)
        longitude = random.uniform(-125.000000, -66.934570)

        # Check if the generated coordinates fall within any shape's bounding box
        point = (longitude, latitude)
        for shape in shapes:
            if (shape.bbox[0] <= longitude <= shape.bbox[2]) and (shape.bbox[1] <= latitude <= shape.bbox[3]):
                coordinates_list.append({"lat": latitude, "lon": longitude})
                break

    return coordinates_list

if __name__ == "__main__":
    shapefile_path = "cb_2018_us_nation_5m.shp"
    with shapefile.Reader(shapefile_path) as w:
        coordinates_list = generate_contiguous_us_coordinates(shapefile_path, num_coordinates=50000)

dictionary = json.dumps(coordinates_list, indent=4)
with open("coordinates.json", "w") as outfile:
    outfile.write(dictionary)  
    
    
