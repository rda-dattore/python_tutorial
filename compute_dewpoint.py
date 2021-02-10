from mysci.read_data import read_data
from mysci.print import print_comparison
from mysci.computation import compute_dewpoint

# Column names and column indices to read
columns = {"date": 0, "time": 1, "tempout": 2, "humout": 5, "dewpt": 13}

#Data types for each column (only if non-string)
types = {"tempout": float, "humout": float, "dewpt": float}

# Read data from file
data = read_data(columns, types=types)

# compute dew point temperature
dewpoint_temp = [compute_dewpoint(temperature, humidity) for temperature, humidity in zip(data["tempout"], data["humout"])]

# Output comparison of data
print_comparison(" DEWPOINT", data["date"], data["time"], data["dewpt"], dewpoint_temp)
