def print_comparison(variable_name, dates, times, original_data, computed_data):
    """
    Print a comparison of two time series (original and computed)

    Parameters:
        variable_name: A string name for the data being compared (limited to 9
                       characters in length)
        dates: A list of strings representing dates for each data
        times: A list of strings representing times for each data
        original_data: A list of original data (floats)
        computed_data: A list of computed data (floats)
    """
    # Output comparison of data
    print("                ORIGINAL  COMPUTED           ")
    print(f" DATE    TIME  {variable_name.upper():>9} {variable_name.upper():>9} DIFFERENCE")
    print("------- ------ --------- --------- ----------")
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, original, computed in zip_data:
        diff = original - computed
        print(f'{date} {time:>6} {original:9.6f} {computed:9.6f} {diff:10.6f}')
