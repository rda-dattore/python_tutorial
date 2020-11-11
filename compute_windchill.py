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
columns = {"date": 0, "time": 1, "tempout": 2, "windspeed": 7, "windchill": 12}

# Data types for each column (only if non-string)
types = {"tempout": float, "windspeed": float, "windchill": float}

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

# Output comparison of data
zip_data = zip(data["date"], data["time"], data["windchill"], windchill)
print("                ORIGINAL  COMPUTED           ")
print(" DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE")
print("------- ------ --------- --------- ----------")
for date, time, original_windchill, computed_windchill in zip_data:
    windchill_diff = original_windchill - computed_windchill
    print(f'{date} {time:>6} {original_windchill:9.6f} {computed_windchill:9.6f} {windchill_diff:10.6f}')
