# Compute the wind chill temperature
def compute_windchill(temperature, windspeed):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    windspeed16 = windspeed ** 0.16
    wind_chill_index = a + (b * temperature) - (c * windspeed16) + (d * temperature * windspeed16)
    return wind_chill_index


# Column names and column indices to read
columns = {"date": 0, "time": 1, "tempout": 2, "windspeed": 7}

# Data types for each column (only if non-string)
types = {"tempout": float, "windspeed": float}

# Initialize my data variable as an empty list
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, "r") as datafile:

    # read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            index = columns[column]
            # avoids key-not-found error
            type = types.get(column, str)
            value = type(split_line[index])
            data[column].append(value)

# compute wind chill index
windchill = []
for temperature, windspeed in zip(data["tempout"], data["windspeed"]):
    windchill.append(compute_windchill(temperature, windspeed))

