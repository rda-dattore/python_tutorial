from read_data import read_data

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

    heat_index = (a + (b * temperature) + (c * rh) + (d * temperature * rh) +
          (e * temperature**2) + (f * rh**2) + (g * rh * temperature**2) +
          (rh * temperature * rh**2) + (i * temperature**2 * rh**2))

    return heat_index


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
zip_data = zip(data["date"], data["time"], data["heatindex"], heatindex)
print("                ORIGINAL  COMPUTED           ")
print(" DATE    TIME  HEATINDEX HEATINDEX DIFFERENCE")
print("------- ------ --------- --------- ----------")
for date, time, original_heatindex, computed_heatindex in zip_data:
    heatindex_diff = original_heatindex - computed_heatindex
    print(f'{date} {time:>6} {original_heatindex:9.6f} {computed_heatindex:9.6f} {heatindex_diff:10.6f}')
