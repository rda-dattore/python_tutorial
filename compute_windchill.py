from read_data import read_data

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

# Read data from file
data = read_data(columns, types=types)

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
