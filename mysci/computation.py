import math

def compute_windchill(temperature, windspeed):
    """
    Compute the wind chill factor given the temperature and wind speed

    NOTE: This computation is valid only for temperatures between -45F and +45F
          and for wind speeds between 3 mph and 60 mph

    Parameters:
        temperature: The temperature in units of F (float)
        windspeed: The wind speed in units of mph (float)
    """

    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    windspeed16 = windspeed ** 0.16
    wind_chill_index = a + (b * temperature) - (c * windspeed16) + (d * temperature * windspeed16)

    return wind_chill_index


def compute_heatindex(temperature, humidity):
    """
    Compute the heat index given the temperature and humidity

    Parameters:
        temperature: The temperature in units of F (float)
        humidity: The relative humidity in units of % (float)
    """

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
          (h * temperature * rh**2) + (i * temperature**2 * rh**2))

    return heat_index


def compute_dewpoint(temperature, humidity):
    """
    Compute the dew point temperature given the temperature and humidity

    Parameters:
        temperature: The temperature in units of F (float)
        humidity: The relative humidity in units of % (float)
    """

    temp_C = (temperature - 32) * 5 / 9 # Convert temperature from deg F to deg C
    rh = humidity / 100

    b = 18.678
    c = 257.14 # deg C

    gamma = math.log(rh) + (b * temp_C) / (c + temp_C)
    tdp = c * gamma / (b -gamma)

    tdp_F = 9 / 5 * tdp + 32 # Convert temperature from deg C to deg F
    return tdp_F;
