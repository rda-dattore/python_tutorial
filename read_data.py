def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather STation data file

    Parameters:
        columns: A dictionary of column names mapping to column indices
        types: A dictionary of column names mapping to the types to which to
               convert each column of data
        filename: A string path pointing to the CU Boulder Weather Station data
                  file
    """
    # Initialize my data variable as an empty list
    data = {}
    for column in columns:
        data[column] = []

    # Read the data file

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

    return data
