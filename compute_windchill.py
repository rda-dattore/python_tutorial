from read_data import read_data
from print import print_comparison
from computation import compute_windchill

# Column names and column indices to read
columns = {"date": 0, "time": 1, "tempout": 2, "windspeed": 7, "windchill": 12}

# Data types for each column (only if non-string)
types = {"tempout": float, "windspeed": float, "windchill": float}

# Read data from file
data = read_data(columns, types=types)

# compute wind chill index
windchill = []
for temperature, windspeed in zip(data["tempout"], data["windspeed"]):
    windchill.append(compute_windchill(temperature, windspeed))

# Output comparison of data
print_comparison("WINDCHILL", data["date"], data["time"], data["windchill"], windchill)
