from geopy.geocoders import Nominatim
import json

city_dic = {
    "Alabama": ["Birmingham", "Montgomery", "Mobile", "Huntsville", "Tuscaloosa", "Hoover", "Dothan", "Auburn", "Decatur", "Madison", "Florence", "Gadsden", "Vestavia Hills", "Prattville", "Phenix City", "Alabaster", "Bessemer", "Enterprise", "Opelika", "Homewood"],
    "Alaska": ["Anchorage", "Fairbanks", "Juneau", "Sitka", "Ketchikan", "Wasilla", "Kenai", "Kodiak", "Bethel", "Palmer", "Homer", "Soldotna", "Valdez", "Nome", "Kotzebue", "Seward", "North Pole", "Dillingham", "Houston", "Craig"],
    "Arizona": ["Phoenix", "Tucson", "Mesa", "Chandler", "Glendale", "Scottsdale", "Gilbert", "Tempe", "Peoria", "Surprise", "Yuma", "Avondale", "Flagstaff", "Goodyear", "Lake Havasu City", "Buckeye", "Casa Grande", "Sierra Vista", "Maricopa", "Oro Valley"],
    "Arkansas": ["Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro", "North Little Rock", "Conway", "Rogers", "Bentonville", "Pine Bluff", "Hot Springs", "Benton", "Texarkana", "Sherwood", "Jacksonville", "Russellville", "Searcy", "Cabot", "Van Buren", "El Dorado"],
    "California": ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno", "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim", "Santa Ana", "Riverside", "Stockton", "Irvine", "Chula Vista", "Fremont", "San Bernardino", "Modesto", "Fontana", "Santa Clarita"],
    "Colorado": ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Thornton", "Arvada", "Westminster", "Pueblo", "Centennial", "Boulder", "Greeley", "Longmont", "Loveland", "Grand Junction", "Broomfield", "Castle Rock", "Commerce City", "Parker", "Littleton"],
    "Connecticut": ["Bridgeport", "New Haven", "Stamford", "Hartford", "Waterbury", "Norwalk", "Danbury", "New Britain", "Meriden", "Bristol", "West Haven", "Milford", "Middletown", "Norwich", "Shelton", "Torrington", "New London", "Ansonia", "Derby", "Groton"],
    "Delaware": ["Wilmington", "Dover", "Newark", "Middletown", "Smyrna", "Milford", "Seaford", "Elsmere", "Georgetown", "New Castle", "Millsboro", "Laurel", "Harrington", "Camden", "Clayton", "Lewes", "Milton", "Selbyville", "Bridgeville", "Ocean View"],
    "Florida": ["Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg", "Hialeah", "Tallahassee", "Fort Lauderdale", "Port St. Lucie", "Cape Coral", "Pembroke Pines", "Hollywood", "Miramar", "Gainesville", "Coral Springs", "Clearwater", "Palm Bay", "Miami Gardens", "Pompano Beach", "West Palm Beach"],
    "Georgia": ["Atlanta", "Augusta", "Columbus", "Macon", "Savannah", "Athens", "Sandy Springs", "Roswell", "Johns Creek", "Warner Robins", "Albany", "Alpharetta", "Marietta", "Valdosta", "Smyrna", "Dunwoody", "Rome", "East Point", "Milton", "Gainesville"],
    "Hawaii": ["Honolulu", "Pearl City", "Hilo", "Kailua", "Waipahu", "Kaneohe", "Mililani Town", "Kahului", "Ewa Gentry", "Kihei", "Makakilo City", "Wahiawa", "Schofield Barracks", "Wailuku", "Kapolei", "Ewa Beach", "Royal Kunia", "Halawa", "Waimalu", "Lahaina"],
    "Idaho": ["Boise", "Meridian", "Nampa", "Idaho Falls", "Pocatello", "Caldwell", "Coeur d'Alene", "Twin Falls", "Lewiston", "Post Falls", "Rexburg", "Moscow", "Eagle", "Ammon", "Kuna", "Hayden", "Mountain Home", "Chubbuck", "Garden City", "Blackfoot"],
    "Illinois": ["Chicago", "Aurora", "Rockford", "Joliet", "Naperville", "Springfield", "Peoria", "Elgin", "Waukegan", "Cicero", "Champaign", "Bloomington", "Decatur", "Arlington Heights", "Evanston", "Schaumburg", "Bolingbrook", "Palatine", "Skokie", "Des Plaines"],
    "Indiana": ["Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel", "Fishers", "Bloomington", "Hammond", "Gary", "Lafayette", "Muncie", "Terre Haute", "Kokomo", "Noblesville", "Anderson", "Greenwood", "Elkhart", "Mishawaka", "Lawrence", "Jeffersonville"],
    "Iowa": ["Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Iowa City", "Waterloo", "Ames", "West Des Moines", "Council Bluffs", "Dubuque", "Ankeny", "Urbandale", "Cedar Falls", "Marion", "Bettendorf", "Mason City", "Marshalltown", "Clinton", "Burlington", "Fort Dodge"],
    "Kansas": ["Wichita", "Overland Park", "Kansas City", "Olathe", "Topeka", "Lawrence", "Shawnee", "Manhattan", "Lenexa", "Salina", "Hutchinson", "Leavenworth", "Leawood", "Dodge City", "Garden City", "Emporia", "Junction City", "Derby", "Prairie Village", "Hays"],
    "Kentucky": ["Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington", "Hopkinsville", "Frankfort", "Henderson", "Richmond", "Jeffersontown", "Paducah", "Pleasure Ridge Park", "Florence", "Valley Station", "Elizabethtown", "Ashland", "Radcliff", "Newburg", "Nicholasville", "Madisonville"],
    "Louisiana": ["New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles", "Kenner", "Bossier City", "Monroe", "Alexandria", "Houma", "New Iberia", "Central", "Slidell", "Ruston", "Sulphur", "Hammond", "Natchitoches", "Gretna", "Opelousas", "Zachary"],
    "Maine": ["Portland", "Lewiston", "Bangor", "South Portland", "Auburn", "Biddeford", "Sanford", "Brunswick", "Scarborough", "Saco", "Westbrook", "Augusta", "Waterville", "Presque Isle", "Brewer", "Bath", "Caribou", "Old Town", "Rockland", "Ellsworth"],
    "Maryland": ["Baltimore", "Columbia", "Germantown", "Silver Spring", "Waldorf", "Glen Burnie", "Frederick", "Gaithersburg", "Rockville", "Bethesda", "Dundalk", "Bowie", "Aspen Hill", "Bel Air South", "North Bethesda", "Ellicott City", "Wheaton", "Germantown", "Towson", "South Bel Air"],
    "Massachusetts": ["Boston", "Worcester", "Springfield", "Lowell", "Cambridge", "New Bedford", "Brockton", "Quincy", "Lynn", "Fall River", "Newton", "Lawrence", "Somerville", "Framingham", "Haverhill", "Waltham", "Malden", "Brookline", "Plymouth", "Medford"],
    "Michigan": ["Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Lansing", "Ann Arbor", "Flint", "Dearborn", "Livonia", "Troy", "Westland", "Farmington Hills", "Kalamazoo", "Wyoming", "Southfield", "Rochester Hills", "Taylor", "Pontiac", "St. Clair Shores", "Royal Oak"],
    "Minnesota": ["Minneapolis", "St. Paul", "Rochester", "Bloomington", "Duluth", "Brooklyn Park", "Plymouth", "Maple Grove", "Woodbury", "St. Cloud", "Eagan", "Blaine", "Eden Prairie", "Coon Rapids", "Lakeville", "Burnsville", "Minnetonka", "Apple Valley", "Edina", "St. Louis Park"],
    "Mississippi": ["Jackson", "Gulfport", "Southaven", "Hattiesburg", "Biloxi", "Meridian", "Tupelo", "Olive Branch", "Greenville", "Horn Lake", "Pearl", "Clinton", "Madison", "Starkville", "Oxford", "Ridgeland", "Vicksburg", "Columbus", "Pascagoula", "Brandon"],
    "Missouri": ["Kansas City", "St. Louis", "Springfield", "Independence", "Columbia", "Lee's Summit", "O'Fallon", "St. Joseph", "St. Charles", "Blue Springs", "St. Peters", "Florissant", "Joplin", "Chesterfield", "Jefferson City", "Cape Girardeau", "Oakville", "Wildwood", "University City", "Ballwin"],
    "Montana": ["Billings", "Missoula", "Great Falls", "Bozeman", "Butte", "Helena", "Kalispell", "Havre", "Anaconda", "Miles City", "Belgrade", "Livingston", "Laurel", "Whitefish", "Lewistown", "Sidney", "Glendive", "Columbia Falls", "Polson", "Hamilton"],
    "Nebraska": ["Omaha", "Lincoln", "Bellevue", "Grand Island", "Kearney", "Fremont", "Hastings", "North Platte", "Norfolk", "Columbus", "Papillion", "La Vista", "Scottsbluff", "South Sioux City", "Beatrice", "Lexington", "Alliance", "Gering", "Blair", "York"],
    "Nevada": ["Las Vegas", "Henderson", "Reno", "North Las Vegas", "Sparks", "Carson City", "Elko", "Mesquite", "Boulder City", "Fernley", "Fallon", "Winnemucca", "West Wendover", "Ely", "Yerington", "Lovelock", "Wells", "Caliente", "Carlin", "Humboldt"],
    "New Hampshire": ["Manchester", "Nashua", "Concord", "Derry", "Dover", "Rochester", "Salem", "Merrimack", "Hudson", "Londonderry", "Keene", "Bedford", "Portsmouth", "Goffstown", "Laconia", "Hampton", "Milford", "Durham", "Exeter", "Windham"],
    "New Jersey": ["Newark", "Jersey City", "Paterson", "Elizabeth", "Edison", "Woodbridge", "Lakewood", "Toms River", "Hamilton", "Trenton", "Clifton", "Camden", "Brick", "Cherry Hill", "Passaic", "Middletown", "Union City", "Old Bridge", "Gloucester", "East Orange"],
    "New Mexico": ["Albuquerque", "Las Cruces", "Rio Rancho", "Santa Fe", "Roswell", "Farmington", "Clovis", "Hobbs", "Alamogordo", "Carlsbad", "Gallup", "Los Lunas", "Deming", "Sunland Park", "Las Vegas", "Portales", "Los Alamos", "Silver City", "Artesia", "Lovington"],
    "New York": ["New York", "Buffalo", "Rochester", "Yonkers", "Syracuse", "Albany", "New Rochelle", "Mount Vernon", "Schenectady", "Utica", "White Plains", "Hempstead", "Troy", "Niagara Falls", "Binghamton", "Freeport", "Valley Stream", "Long Beach", "Spring Valley", "Rome"],
    "North Carolina": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem", "Fayetteville", "Cary", "Wilmington", "High Point", "Greenville", "Asheville", "Concord", "Gastonia", "Jacksonville", "Chapel Hill", "Rocky Mount", "Burlington", "Wilson", "Huntersville", "Kannapolis"],
    "North Dakota": ["Fargo", "Bismarck", "Grand Forks", "Minot", "West Fargo", "Williston", "Dickinson", "Mandan", "Jamestown", "Wahpeton", "Devils Lake", "Valley City", "Grafton", "Beulah", "Rugby", "Horace", "Stanley", "New Town", "Lincoln", "Belcourt"],
    "Ohio": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton", "Parma", "Canton", "Youngstown", "Lorain", "Hamilton", "Springfield", "Kettering", "Elyria", "Lakewood", "Cuyahoga Falls", "Middletown", "Newark", "Euclid", "Mansfield"],
    "Oklahoma": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Lawton", "Edmond", "Moore", "Midwest City", "Enid", "Stillwater", "Muskogee", "Bartlesville", "Owasso", "Shawnee", "Yukon", "Bixby", "Ardmore", "Ponca City", "Jenks", "Duncan"],
    "Oregon": ["Portland", "Eugene", "Salem", "Gresham", "Hillsboro", "Beaverton", "Bend", "Medford", "Springfield", "Corvallis", "Albany", "Tigard", "Lake Oswego", "Keizer", "Grants Pass", "McMinnville", "Oregon City", "Redmond", "Tualatin", "West Linn"],
    "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster", "Harrisburg", "Altoona", "York", "State College", "Wilkes-Barre", "Norristown", "Chester", "Bethel Park", "Williamsport", "Monroeville", "Plum", "Easton"],
    "Rhode Island": ["Providence", "Warwick", "Cranston", "Pawtucket", "East Providence", "Woonsocket", "Coventry", "Cumberland", "North Providence", "South Kingstown", "West Warwick", "Johnston", "North Kingstown", "Newport", "Bristol", "Westerly", "Smithfield", "Central Falls", "Portsmouth", "Burrillville"],
    "South Carolina": ["Columbia", "Charleston", "North Charleston", "Mount Pleasant", "Rock Hill", "Greenville", "Summerville", "Goose Creek", "Sumter", "Hilton Head Island", "Florence", "Spartanburg", "Myrtle Beach", "Aiken", "Anderson", "Greer", "Greenwood", "Mauldin", "North Augusta", "Easley"],
    "South Dakota": ["Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "Watertown", "Mitchell", "Yankton", "Pierre", "Huron", "Spearfish", "Vermillion", "Brandon", "Box Elder", "Madison", "Sturgis", "Belle Fourche", "Tea", "Dell Rapids", "Mobridge", "Hot Springs"],
    "Tennessee": ["Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville", "Murfreesboro", "Franklin", "Jackson", "Johnson City", "Bartlett", "Hendersonville", "Kingsport", "Collierville", "Smyrna", "Cleveland", "Brentwood", "Germantown", "Spring Hill", "Columbia", "La Vergne"],
    "Texas": ["Houston", "San Antonio", "Dallas", "Austin", "Fort Worth", "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo", "Lubbock", "Garland", "Irving", "Amarillo", "Grand Prairie", "Brownsville", "Pasadena", "McKinney", "Mesquite", "Killeen"],
    "Utah": ["Salt Lake City", "West Valley City", "Provo", "West Jordan", "Orem", "Sandy", "Ogden", "St. George", "Layton", "Taylorsville", "South Jordan", "Logan", "Lehi", "Murray", "Bountiful", "Draper", "Riverton", "Roy", "Cottonwood Heights", "Pleasant Grove"],
    "Vermont": ["Burlington", "South Burlington", "Rutland", "Essex", "Colchester", "Bennington", "Brattleboro", "Hartford", "Milton", "Barre", "Williston", "Montpelier", "St. Johnsbury", "Winooski", "Shelburne", "St. Albans", "Swanton", "Northfield", "Lyndon", "Middlebury"],
    "Virginia": ["Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Newport News", "Alexandria", "Hampton", "Roanoke", "Portsmouth", "Suffolk", "Lynchburg", "Harrisonburg", "Leesburg", "Charlottesville", "Blacksburg", "Danville", "Manassas", "Petersburg", "Fredericksburg", "Winchester"],
    "Washington": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue", "Kent", "Everett", "Renton", "Yakima", "Spokane Valley", "Federal Way", "Bellingham", "Kennewick", "Auburn", "Pasco", "Marysville", "Lakewood", "Redmond", "Shoreline", "Richland"],
    "West Virginia": ["Charleston", "Huntington", "Morgantown", "Parkersburg", "Wheeling", "Weirton", "Fairmont", "Beckley", "Martinsburg", "Clarksburg", "South Charleston", "Vienna", "St. Albans", "Bluefield", "Moundsville", "Bridgeport", "Dunbar", "Oak Hill", "Elkins", "Nitro"],
    "Wisconsin": ["Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine", "Appleton", "Waukesha", "Eau Claire", "Oshkosh", "Janesville", "West Allis", "La Crosse", "Sheboygan", "Wauwatosa", "Fond du Lac", "New Berlin", "Wausau", "Brookfield", "Beloit", "Greenfield"],
    "Wyoming": ["Cheyenne", "Casper", "Laramie", "Gillette", "Rock Springs", "Sheridan", "Green River", "Evanston", "Riverton", "Cody", "Jackson", "Lander", "Rawlins", "Torrington", "Powell", "Douglas", "Worland", "Buffalo", "Mills", "Ranchettes"]
    
}





from geopy.geocoders import Nominatim
import time



geolocator = Nominatim(user_agent="city_coordinates")

coordinates_dict = {}

for state, cities in city_dic.items():
    coordinates_dict[state] = {}
    for city in cities:
        try:
            location = geolocator.geocode(city + ', ' + state, exactly_one=True, timeout=10)
            if location is not None:
                coordinates_dict[state][city] = (location.latitude, location.longitude)
                print(f"Coordinates for {city}, {state}: {location.latitude}, {location.longitude}")
                
            else:
                print(f"Coordinates not found for {city}, {state}")
        except Exception as e:
            print(f"Error fetching coordinates for {city}, {state}: {e}")
        time.sleep(1)  # To avoid overloading the geocoding service
    

print(coordinates_dict)

dictionary=json.dumps(coordinates_dict,indent=4)
with open("city_coords.json", "w") as outfile:
  outfile.write(dictionary)

