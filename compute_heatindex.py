# Compute the heat index
def compute_heatindex(temperature, humidity):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = humidity / 100

    hi = (a + (b * temperature) + (c * rh) + (d * temperature * rh) +
          (e * temperature**2) + (f * rh**2) + (g * rh * temperature**2) +
          (rh * temperature * rh**2) + (i * temperature**2 * rh**2))

    return hi

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

#Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

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

# compute heat index
heatindex = []
for temperature, humidity in zip(data["tempout"], data["humout"]):
    heatindex.append(compute_heatindex(temperature, humidity))

# Output comparison of data
zip_data = zip(data["date"], data["time"], data["heatindex"], heatindex)
print("                ORIGINAL  COMPUTED           ")
print(" DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE")
print("------- ------ --------- --------- ----------")
for date, time, original_heatindex, computed_heatindex in zip_data:
    heatindex_diff = original_heatindex - computed_heatindex
    print(f'{date} {time:>6} {original_heatindex:9.6f} {computed_heatindex:9.6f} {heatindex:10.6f}')
