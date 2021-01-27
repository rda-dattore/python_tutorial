from read_data import read_data
from print import print_comparison
from computation import compute_heatindex

# Column names and column indices to read
columns = {"date": 0, "time": 1, "tempout": 2, "humout": 5, "heatindex": 13}

#Data types for each column (only if non-string)
types = {"tempout": float, "humout": float, "heatindex": float}

# Read data from file
data = read_data(columns, types=types)

# compute heat index
heatindex = []
for temperature, humidity in zip(data["tempout"], data["humout"]):
    heatindex.append(compute_heatindex(temperature, humidity))

# Output comparison of data
print_comparison("HEATINDEX", data["date"], data["time"], data["heatindex"], heatindex)
